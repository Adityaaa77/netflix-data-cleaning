# Task 1: Data Cleaning and Preprocessing – Netflix Dataset

###  Dataset Used:
Netflix Movies and TV Shows – [Kaggle Link](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

###  Steps Performed:

- Loaded dataset using Pandas
- Identified and filled missing values:
  - `director`, `cast` → filled with "Unknown"
  - `country`, `rating` → filled with mode
  - `date_added` → stripped and parsed with `format='mixed'`, filled missing with earliest date
- Removed duplicate rows
- Standardized text fields (e.g. lowercased `type`, stripped spaces)
- Renamed all columns to lowercase and underscore-separated
- Converted `release_year` to integer and `date_added` to datetime
- Exported cleaned data to `netflix_cleaned.csv`

---

###  Files Included:
- `netflix_titles.csv` 
- `netflix_cleaned.csv` 
- `p1.py` – Python cleaning script
- `README.md` – Summary of what was done

---

###  Tools Used:
- Python 3.13
- Pandas
