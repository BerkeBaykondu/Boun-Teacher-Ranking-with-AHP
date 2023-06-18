Boun-Teacher-Ranking-with-AHP
This project is aimed at ranking teachers who offer courses for students to use during their course scheduling process.

# Project Description
This project encompasses various components such as web scraping, data visualization, rating comments using cosine similarity, and ranking using the Analytic Hierarchy Process (AHP) method on an Excel file.

# Web Scraping
The project collects student comments about Boğaziçi University courses and the courses offered in the current semester from the websites "https://www.bouncim.com/" and "https://kilicbaran.github.io/boun-course-planner/" using web scraping techniques.

# Data Visualization
The obtained data is visualized using various techniques to enhance understanding.

# Cosine Similarity
Based on the student comments from the "https://www.bouncim.com/" website, teachers who offer courses are rated using cosine similarity to evaluate the similarities of certain example sentences according to three main criteria: being student-friendly, being competent in their field, and their English proficiency.

# Data Preprocessing
Two separate datasets obtained through web scraping are merged after undergoing various preprocessing steps. This process results in a final dataset where only the ratings of available courses can be seen. The final dataset is obtained in the form of an Excel file.

# AHP Ranking
Courses and the teachers who offer them are ranked using the Analytic Hierarchy Process (AHP) method applied to the Excel file.


