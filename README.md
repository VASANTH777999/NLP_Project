README - for JOB SELECTION BASED ON RESUMES-


This project allows users to match resumes with job positions based on extracted skills from resume texts. It also predicts the salary based on the relevance of the resume to the job position and whether the applicant is selected. The project uses Natural Language Processing (NLP) techniques to extract skills and match them with required skills for different job positions. The results are saved in a CSV file.
Through this project a user can able to select or deselect the person for the job based on their resume matching with the companys job description and job positions availability, once the code is runned it pops up with a GUI asking user to upload a Dataset or Resume once the Dataset is uploaded it performs the NLP techniques and operates the code and provides a Result file which is saved in File Manager.



# Features - 
Skill Extraction: Extracts relevant skills from resumes or job descriptions using regular expressions and NLP.
Job Position Matching: Matches the extracted skills from resumes to job positions in a company based on skill similarity.
Salary Prediction: Predicts the salary based on the match score of a resume with a job position.
Graphical User Interface (GUI): User-friendly interface for uploading CSV files, entering company skills and job positions, and viewing the results.
Dynamic Skill and Job Position Input: Users can input the skills required by the company and available job positions directly via the GUI.
Result Export: Saves the matching results and predictions in a CSV file, which includes the job position, relevance score, selection status, and predicted salary.


#Requirements -
Python 3.x
Libraries:pandas, spacy, sklearn, tkinter.


#Project Structure -
├── Job_Selection_based_on_Resume.py          # Main script to run the application
├── resumes_with_positions.csv  # Output CSV file with the matching results
├── README.md                  # Project documentation
├── Job_Selection_based_on_UpdatedResume.py   
├── resumes_with_positions_Updated.csv 
├── requirements.txt
├── Resume.csv                      #dataset for Job_selection_based_on_resume.py
└── UpdatedResumeDataSet.csv        #dataset for Job_selection_based_on_UpdatedResume.py


# HOW TO USE - 
1. Install the Required Dependencies: Ensure that Python 3.x and the required libraries are installed on your system. You can install the necessary dependencies by running:

pip install -r requirements.txt
If you don't have requirements.txt, you can install each package individually using pip:

pip install pandas spacy scikit-learn
Additionally, you will need the spaCy model:

python -m spacy download en_core_web_sm

2.Run the Application: Execute the main Python script to start the application:

python3 Job_Selection_based_on_Resume.py
python3 Job_Selection_based_on_UpdatedResume.py

3.Upload Resume Dataset:a file dialog will prompt you to select and upload your resume dataset.
The dataset should be in CSV format with a column named Resume_str containing the resume texts.

4. View and Save the Results:
After processing the resumes, the results will be saved in resumes_with_positions.csv.You can find this CSV file in the same directory as the script.

5.Open the Output CSV:
Open resumes_with_positions.csv in any text editor or spreadsheet software to view the results, including the matched job positions and predicted salaries for each resume.


# CONTRIBUTION - 
VASANTH - Generated a Working NLP model on Job_selection_based_on_Resumes, Collected the dataset (from Kaggle), worked on the coding parts of NLP model Training to reduce the processing time.


#Acknowledgments -
This project was developed as part of an academic initiative to optimize the resume matching process and enhance recruitment efficiency through automated skill extraction and job matching. Special thanks to our mentor for their guidance and invaluable support throughout the development process.
Note: Some assistance was taken from ChatGPT to generate and refine parts of the code used in this project, especially in handling Natural Language Processing tasks and building the user interface.

