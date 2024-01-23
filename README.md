# Web Scraping Wuzzuf Jobs

## Introduction
This project is a web scraping script written in Python using the BeautifulSoup library to extract job information from [Wuzzuf](https://wuzzuf.net/). The script targets jobs related to machine learning, data analysis, data science, and business intelligence. It gathers details such as job titles, companies, occupations, specifications, and links.

## Getting Started
To run the web scraping script, follow these steps:
1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Install the required libraries by running the following commands:
   ```
   !pip install requests
   !pip install bs4
   ```
4. Open the "Web Scraping 'Wuzzuf'.py" file in a Python environment or Jupyter Notebook.
5. Execute the cells in the notebook to run the web scraping script.

## Functions

### `number_of_pages(jobName)`
This function calculates the number of pages to scrape based on the total number of jobs related to the specified job name.

### `scrap(num_pages, url, job)`
This function performs the scraping of job information from multiple pages. It collects data such as job titles, companies, occupations, specifications, and links.

## Scraped Data
The script iterates through the specified job titles ('machine learning', 'data analysis', 'data science', 'business intelligence'), retrieves information from each job page, and creates a DataFrame. The combined DataFrame is then displayed and saved as a CSV file named "JobScraping.csv."

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## Acknowledgments
This project is a demonstration of web scraping techniques for educational purposes. Ensure that you comply with the terms of service of the websites you scrape. Modify and enhance the script as needed for your specific requirements.

Happy coding! 🚀🔍 #WebScraping #Python #DataCollection
