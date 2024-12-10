import pandas as pd
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import filedialog, messagebox

nlp = spacy.load("en_core_web_sm")

skills_list = [
    'Python', 'Java', 'AWS', 'Machine Learning', 'Data Science', 'SQL', 'C++', 
    'Cloud Computing', 'Docker', 'Kubernetes', 'Linux', 'DevOps', 'React', 'Node.js',
    'NLP', 'Deep Learning', 'HTML', 'CSS', 'JavaScript', 'Communication', 'Teamwork'
]

job_positions = {
    "Software Developer": ['Python', 'Java', 'AWS', 'Cloud Computing', 'SQL'],
    "Data Scientist": ['Machine Learning', 'Data Science', 'Python', 'SQL', 'Deep Learning'],
    "DevOps Engineer": ['AWS', 'Docker', 'Kubernetes', 'Linux', 'DevOps'],
    "Web Developer": ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js'],
    "NLP Engineer": ['NLP', 'Machine Learning', 'Python', 'Deep Learning'],
    "Project Manager": ['Communication', 'Teamwork', 'Leadership']
}

def extract_skills_from_text(text):
    extracted_skills = []
    text_lower = text.lower()
    for skill in skills_list:
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text_lower):
            extracted_skills.append(skill)
    return extracted_skills

def calculate_position_similarity(resume_skills, job_skills):
    resume_skills_str = ' '.join(resume_skills)
    job_skills_str = ' '.join(job_skills)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_skills_str, job_skills_str])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return cosine_sim[0][0]

def match_position(extracted_skills):
    best_match = None
    highest_similarity = 0
    
    for position, required_skills in job_positions.items():
        similarity = calculate_position_similarity(extracted_skills, required_skills)
        
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = position
            
    return best_match, highest_similarity

def predict_salary(position, relevance_score, selected):
    # Base salary of 150,000 INR and max salary of 500,000 INR
    base_salary = 150000
    max_salary = 500000
    if selected:
        salary = base_salary + (max_salary - base_salary) * relevance_score
    else:
        salary = base_salary + (max_salary - base_salary) * (relevance_score * 0.5)  # Reduced salary scale
    return round(salary, 0)  # Round salary to the nearest whole number

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        process_file(file_path)

def process_file(file_path):
    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        if 'Resume_html' in df.columns:
            df = df.drop(columns=['Resume_html'])

        df['Extracted_skills'] = df['Resume_str'].apply(extract_skills_from_text)

        df['MatchedPosition_in_company'] = df['Extracted_skills'].apply(lambda x: match_position(x)[0])
        df['Position_relevance_score'] = df['Extracted_skills'].apply(lambda x: match_position(x)[1])

        df['Selected/Notselected_for_company'] = df['Position_relevance_score'].apply(
            lambda x: 'Selected' if x > 0.65 else 'Not Selected')

        df['PredictedSalary_to_be_given'] = df.apply(
            lambda row: predict_salary(row['MatchedPosition_in_company'], row['Position_relevance_score'], row['Selected/Notselected_for_company'] == 'Selected'), 
            axis=1
        )

        df.to_csv('resumes_with_positions.csv', index=False)

        messagebox.showinfo("Success", "Your results have been saved to 'resumes_with_positions.csv'")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Resume Job Matching")

label = tk.Label(root, text="Select a resume dataset to process:")
label.pack(pady=20)

load_button = tk.Button(root, text="Load CSV File", command=load_file)
load_button.pack(pady=20)

root.mainloop()