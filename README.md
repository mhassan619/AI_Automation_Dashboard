<div align="center">

# ⚙️ AI AUTOMATION DASHBOARD
### 🚀 Production-Ready Web Scrapers, Profiles Analyzers & Live Automation Tools

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/BeautifulSoup-3478F6?style=for-the-badge&logo=python&logoColor=white" alt="BeautifulSoup" />
  <img src="https://img.shields.io/badge/GitHub%20API-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub API" />
</p>

---

[🌐 Launch Live Automation Suite](https://aiautomationdashboard-cyaeoww9sgapjwm7zlsxg6.streamlit.app/) • [💼 LinkedIn Profile](https://www.linkedin.com/in/muhammad-hassan-python) • [💻 Main Portfolio](https://github.com/mhassan619)

</div>

---

## 📋 Project Overview

This repository hosts a centralized, multipage **AI Automation & Web Scraping Portal** built using Streamlit. It consolidates independent enterprise automation scripts, modular utilities, and high-throughput data extraction scrapers into a single interactive user interface. 

Instead of executing scattered Python scripts via CLI, recruiters and users can experience, monitor, and trigger real-time automations directly from their web browsers.

---

## 🛠️ Key Features & Modular Architecture

### 🚀 Integrated Automation Tools
* **📊 Deep GitHub Profile Analyzer (`1_GitHub.py`):** Integrates directly with the GitHub REST API to fetch comprehensive user analytics, repository statistics, tracking patterns, and contribution frequencies.
* **🌤️ Real-Time Weather Forecaster (`2_Weather.py`):** Connects with global atmospheric APIs to extract live weather conditions, wind speeds, and predictive forecasts for any global coordinate.
* **📚 High-Throughput E-Commerce Scraper (`3_Books.py`):** Uses BeautifulSoup to programmatically crawl e-commerce structures, parse raw HTML DOM elements, and package product details into download-ready CSV structures.

---

## 📂 Repository File Structure

The project strictly follows modular programming paradigms to separate frontend UI rendering from underlying backend automation engines:

```text
AI_Automation_Dashboard/
│
├── main.py                  # Main landing page & core application config
├── requirements.txt         # Production dependencies & tracking packages
│
├── pages/                   # Streamlit Multipage Frontend Architecture
│   ├── 1_GitHub.py          # GitHub API interaction & rendering dashboard
│   ├── 2_Weather.py         # Live Weather rendering and dashboard UI
│   └── 3_Books.py           # E-Commerce parser interface & CSV exporter
│
└── utils/                   # Pure Python Backend Automation Engines
    ├── __init__.py          # Python package initializer
    ├── github.py            # API queries, authorization & token logic
    └── weather.py           # Endpoint handling and raw JSON parsers

```
## 🛠️ Technologies & Packages Used
 * **Frontend Framework:** Streamlit (Dynamic multi-page UI mapping)
 * **Data Extraction & Scraping:** BeautifulSoup4 (HTML tree parsing & DOM traversing)
 * **HTTP & API Engines:** Requests (Asynchronous endpoint communication)
 * **Data Operations:** Pandas & NumPy (Exporting to structured matrix & CSV engines)
## 💻 Local Installation & Setup
Want to run this Automation Suite locally? Follow these steps:
 1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/mhassan619/AI_Automation_Dashboard.git](https://github.com/mhassan619/AI_Automation_Dashboard.git)
   cd AI_Automation_Dashboard
   
   ```
 2. **Configure Virtual Environment (Recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   
   ```
 3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   
   ```
 4. **Launch the Dashboard:**
   ```bash
   streamlit run main.py
   
   ```
## 📈 System Mindset & Standards
 * **Error Handling:** Every API call and scraper is wrapped inside strict try-except protocols to prevent UI breaking during connection timeouts.
 * **Modular Logic:** Separate routing ensures that changing the API source or scraper tags inside utils/ will never disrupt the pages/ frontend rendering.
<div align="center">
### 🌱 "Consistency beats motivation, every single day."
📩 Connect via Email • 🌐 Let's Network on LinkedIn
</div>
```
