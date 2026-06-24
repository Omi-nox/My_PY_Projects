# 📚 Multi-Page Books Web Scraper & Analyzer

A Python-based automated web scraping application that extracts book details (Titles, Prices, and Star Ratings) from multiple pages of the popular sandbox website *Books to Scrape*. It parses the raw HTML, cleans up messy currency symbols, maps string ratings to integers, saves the structured data into a JSON file, and provides a breakdown analysis (highest-rated books, cheapest, and most expensive).

## 🚀 Features

- **Multi-Page Scraping:** Dynamically iterates through pagination to fetch books from multiple live web pages.
- **Smart HTML Parsing:** Uses `BeautifulSoup` to safely dig down into target tags and extract precise attributes.
- **Data Cleaning & Mapping:** Sanitizes broken currency artifacts (`Â£`) and converts text-based ratings (e.g., "Three") to clean integers (`3`) using a dictionary lookup strategy.
- **Data Persistence:** Exports the collected information into a beautifully formatted `books.json` file.
- **Built-in Analytics:** Automatically filters 4+ star ratings and computes statistical metrics (`min()` / `max()`) for prices.
- **Interactive CLI Menu:** User-friendly command-line terminal system to control the scraping, viewing, and saving pipelines separately.

## 🛠️ Tech Stack & Libraries Used

- **Python 3** (Core Logic)
- **Requests** (HTTP Requests to pull source HTML)
- **BeautifulSoup4** (HTML Parsing and Tree Navigation)
- **Pathlib** (Object-oriented filesystem path management)
- **JSON** (Data Serialization)

## 📁 Project Structure

```text
├── Intermediate/
│   └── web_scraper/
│       └── books.json          # Generated output file containing    structured data
        └── web_scraper_app.py          # Main executable script containing code logic
        └── README.md                   # Documentation file
```

## ⚙️ Installation & Setup

1. **Clone this repository to your local computer:**
   ```bash
   git clone https://github.com
   cd YOUR-REPO-NAME
   ```

2. **Install the required third-party libraries:**
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the script via your terminal:**
   ```bash
   python web_scraper_app.py
   ```

## 🖥️ How it Works & Visual Output

When executed, the program triggers an interactive menu inside your terminal:

1. **Step 1:** Pressing `1` targets the sandbox server, downloads page elements safely with built-in time delays (`time.sleep`) to respect server load, and renders formatted logs:
   ```text
   status code: 200
   Scraping page no. 1 with url: http://books.toscrape.com/
   Total no. Books scraped : 20
   Scraping done...showing books...
   ⭐  3 | £51.77 | A Light in the Attic
   ```

2. **Step 2:** Pressing `2` creates directory references dynamically using `Pathlib`, formats the arrays, and saves everything neatly into an external file. It concludes by calculating specific statistics:
   ```text
   THE OVERALL SUMMARY IS : .......
   Total no. Books scraped : 40
   ⭐ Highest rated books: ...
   1. Soumission
   2. Sharp Objects
   💰 Cheapest book: ...£10.0
   💰 Most expensive book: ...£59.99
   ```

## 🔑 Key Concepts Practiced

- **List Comprehensions:** Filtered highest-rated items gracefully inside the analytics segment using inline conditional loops.
- **Global States & Arrays:** Synchronized real-time scraping data across multiple discrete worker functions.
- **Dictionary Lookups (`.get()` Method):** Safely processed variable text tokens into absolute data parameters without allowing runtime system crashes.
