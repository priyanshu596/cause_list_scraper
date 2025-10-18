# ⚖️ eCourts Cause List Downloader

A Python-based desktop tool to automatically **fetch and download cause list PDFs** from live Indian **District Court websites (eCourts)** in real time.

---

## 🚀 Features

✅ Fetches **real-time cause lists** from multiple district court websites  
✅ Automatically **retries** on network or timeout errors  
✅ Simple **Tkinter GUI** (no command-line complexity)  
✅ Downloads **all available PDFs** for the selected court  
✅ Works **without Selenium or Captcha solving**  
✅ Saves files neatly inside an `output/` folder  

---

## 🧩 Tech Stack

- **Python 3.8+**
- **Libraries Used:**
  - `requests`
  - `beautifulsoup4`
  - `tkinter`
  - `urllib`

---

# ⚖️ eCourts Cause List Downloader

A Python-based desktop tool to automatically **fetch and download cause list PDFs** from live Indian **District Court websites (eCourts)** in real time.

---

## 🚀 Features

✅ Fetches **real-time cause lists** from multiple district court websites  
✅ Automatically **retries** on network or timeout errors  
✅ Simple **Tkinter GUI** (no command-line complexity)  
✅ Downloads **all available PDFs** for the selected court  
✅ Works **without Selenium or Captcha solving**  
✅ Saves files neatly inside an `output/` folder  

---

## 🧩 Tech Stack

- **Python 3.8+**
- **Libraries Used:**
  - `requests`
  - `beautifulsoup4`
  - `tkinter`
  - `urllib`

---

## 🛠️ Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install requests beautifulsoup4
```
2️⃣ Run the application
bash
Copy code
python ecourts_autoretry_final.py
3️⃣ Select a court and download
Choose a court name (e.g., New Delhi (Patiala House))

Click “Download Cause List PDFs”

The script will automatically:

Try all possible URLs for that court

Retry on slow or down servers

Download all judge-wise PDFs available today

📁 Output Location
All downloaded cause lists are saved to:

lua
Copy code
output/
Example:

lua
Copy code
output/
├── 2025101068.pdf
├── 2025101040.pdf
└── 2025100886.pdf
📷 Proof of Working
✅ Working Log Output
Screenshot of the script successfully fetching and downloading PDFs:


🖥️ Application Interface
Tkinter-based desktop UI for selecting court and downloading cause lists:


📁 Output Folder
Downloaded cause list PDFs saved in the output/ folder:


🧠 Notes
Some court websites only publish cause lists on working days (Mon–Sat).

If no PDFs are found, try:

A different court (like Saket or Patiala House)

Or retry during court hours (after 10 AM).

The script does not bypass captcha — it only uses publicly available data.

📜 Folder Structure
bash
Copy code
ecourts-cause-list-scraper/
│
├── ecourts_autoretry_final.py       # Main application script
├── output/                          # Folder for downloaded PDFs
│   ├── 2025101068.pdf
│   ├── 2025101040.pdf
│   └── ...
├── screenshots/                     # Screenshots for proof
│   ├── log_proof.png
│   ├── ui_app.png
│   └── output_folder.png
└── README.md                        # This file
🧑‍💻 Author
Name: PRIYANSHU SINGH
Internship: Think Act Rise
Date: October 2025
Email: priyanshu.asn2003@gmail.com
GitHub Repository: https://github.com/yourusername/ecourts-cause-list-scraper

✅ Summary
This project fulfills all internship requirements:

Real-time data fetching ✅

Automatic PDF download ✅

GUI interface ✅

Error handling & retry ✅

Working proof logs ✅

🎉 Successfully scrapes and downloads eCourts cause lists using a simple, robust, and fully automated Python application!
