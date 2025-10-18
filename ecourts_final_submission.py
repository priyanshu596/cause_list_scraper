import tkinter as tk
from tkinter import ttk, messagebox
import requests, os, time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import date

# ---------------- Settings ----------------
OUTDIR = "output"

# 🏛️ Reliable Delhi District Court sites
COURT_SITES = {
    "South District (Saket)": "https://delhisouth.dcourts.gov.in/",
    "New Delhi (Patiala House)": "https://newdelhi.dcourts.gov.in/",
    "South-West District (Dwarka)": "https://dwarka.dcourts.gov.in/",
}

# Possible paths for PDFs
POSSIBLE_PATHS = [
    "daily-cause-list/",
    "cause-list/",
    "cause-list-daily-board/",
    "cause-list-%e2%81%84-daily-board/",
    "",
]

# -------------- Helpers ----------------
def find_pdfs(base_url):
    """Try multiple known paths and return PDF URLs"""
    for path in POSSIBLE_PATHS:
        full_url = urljoin(base_url, path)
        try:
            print(f"[TRY] {full_url}")
            r = requests.get(full_url, timeout=20)
            if r.status_code != 200:
                continue
            soup = BeautifulSoup(r.text, "html.parser")
            pdfs = [
                urljoin(full_url, a["href"])
                for a in soup.find_all("a", href=True)
                if a["href"].lower().endswith(".pdf")
            ]
            if pdfs:
                print(f"[OK] Found {len(pdfs)} PDFs at {full_url}")
                return pdfs, full_url
        except requests.exceptions.Timeout:
            print(f"[TIMEOUT] Retrying after 3s: {full_url}")
            time.sleep(3)
            continue
        except Exception as e:
            print(f"[WARN] {full_url} -> {e}")
            continue
    return [], None


def download_pdf(url):
    """Download and save a single PDF"""
    os.makedirs(OUTDIR, exist_ok=True)
    filename = os.path.join(OUTDIR, os.path.basename(url))
    try:
        with requests.get(url, stream=True, timeout=40) as r:
            r.raise_for_status()
            with open(filename, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
        return filename
    except Exception as e:
        print(f"[ERROR] {url}: {e}")
        return None


def start_download():
    """Main download flow"""
    court = court_var.get()
    if not court:
        messagebox.showerror("Error", "Please select a court.")
        return

    base_url = COURT_SITES[court]
    messagebox.showinfo("Fetching", f"Checking cause list for:\n{court}")

    # 🔁 Try 3 times automatically in case of slow server
    for attempt in range(3):
        pdfs, found_url = find_pdfs(base_url)
        if pdfs:
            break
        print(f"[RETRY] Attempt {attempt + 2}/3 for {court}...")
        time.sleep(2)

    if not pdfs:
        messagebox.showwarning("No PDFs Found", f"No cause lists found for {court}. Try another site.")
        return

    downloaded = 0
    for pdf in pdfs:
        path = download_pdf(pdf)
        if path:
            downloaded += 1
            print("  [DL]", path)

    messagebox.showinfo(
        "Done",
        f"✅ Downloaded {downloaded} PDFs from:\n{found_url}\n\nSaved to '{OUTDIR}' folder.",
    )

# -------------- UI ----------------
root = tk.Tk()
root.title("eCourts Cause List Downloader")
root.geometry("480x260")
root.resizable(False, False)

tk.Label(root, text="eCourts Cause List Downloader", font=("Segoe UI", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Select District Court:").grid(row=0, column=0, sticky="w", pady=5)
court_var = tk.StringVar()
ttk.Combobox(
    frame,
    textvariable=court_var,
    values=list(COURT_SITES.keys()),
    width=40,
    state="readonly"
).grid(row=0, column=1)

tk.Label(frame, text="Date (auto):").grid(row=1, column=0, sticky="w", pady=5)
tk.Label(frame, text=date.today().strftime("%d-%m-%Y")).grid(row=1, column=1, sticky="w")

tk.Button(
    root,
    text="Download Cause List PDFs",
    command=start_download,
    bg="#1976D2",
    fg="white",
    width=30
).pack(pady=20)

tk.Label(
    root,
    text="This version auto-retries & checks all known court URLs.\nCause lists saved in 'output' folder.",
    font=("Segoe UI", 9),
    justify="center"
).pack(pady=5)

root.mainloop()
