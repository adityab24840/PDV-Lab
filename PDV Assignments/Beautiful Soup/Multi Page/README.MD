# IMDb Top Movies Data Scraping Script

This is a Python script that allows you to scrape top movie data from IMDb for the year 2023. It fetches movie information including name, release year, IMDb rating, metascore, and votes, and stores it in a CSV file.

# Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Conclusion](#conclusion)

# Prerequisites

Before using the script, you need to have the following installed on your system:

- `Python` (3.6 or higher)
- `bs4` (Beautiful Soup) library
- `requests` library
- `pandas` library

You can install the required libraries using the following commands:

```bash
pip install beautifulsoup4 requests pandas
```

# Usage
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.0
3. Run the script using the following command:

```bash
python imdb_scraping_script.py
```
The script will start scraping movie data from IMDb. It will display progress as it scrapes, and it may take a while to complete.

4. Once the scraping is done, the script will create a CSV file named top_movies_2023.csv in the same directory. This file will contain the scraped movie data.

# Conclusion

The IMDb Top Movies Data Scraping Script is a versatile tool that simplifies the process of gathering movie information from IMDb for the year 2023. By fetching data such as movie names, release years, IMDb ratings, metascores, and votes, the script provides valuable insights into the top movies of the year.