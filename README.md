# Resume Analyzer

## Overview

Resume Analyzer is a Python-based command-line tool that evaluates the relevance of a resume against a given job description. The tool leverages basic Natural Language Processing (NLP) techniques to compute a similarity score, identify missing skills, and provide actionable suggestions for improving resume alignment.

This project is designed to simulate how resumes are screened in real-world hiring workflows and to help users optimize their applications effectively.

---

## Features

* Computes a match score between resume and job description using TF-IDF and cosine similarity
* Identifies missing skills based on keyword comparison
* Generates suggestions to improve resume-job alignment
* Simple command-line interface for ease of use

---

## Technologies Used

* Python
* scikit-learn
* argparse

---

## Methodology

1. Accepts resume and job description as text inputs
2. Preprocesses text by normalizing and removing stop words
3. Converts text into numerical vectors using TF-IDF
4. Computes similarity score using cosine similarity
5. Extracts keywords to identify missing skills
6. Generates suggestions based on identified gaps

---

## Usage

### 1. Clone the repository

```bash id="w0gk6k"
git clone https://github.com/divyanshigupta31/nlp-based-resume-analyzer.git
cd resume-analyzer
```

### 2. Install dependencies

```bash id="52l5kv"
pip install scikit-learn
```

### 3. Run the program

```bash id="6md3ns"
python main.py --resume sample_resume.txt --jd sample_jd.txt
```

---

## Example Output

```text id="p7n6nt"
===== RESUME ANALYSIS =====

Match Score: 74.32%

Missing Skills:
- docker
- aws
- rest
- api

Suggestions:
- Consider adding 'docker' to your resume
- Consider adding 'aws' to your resume
```

---

## Project Scope

This project focuses on implementing a lightweight and interpretable approach to resume-job matching using basic NLP techniques. It is not intended to replace advanced Applicant Tracking Systems (ATS), but rather to demonstrate how text similarity and keyword analysis can be applied in a practical hiring context.

---

## Limitations

* Relies on simple keyword matching and TF-IDF representation
* Does not account for semantic similarity beyond basic vectorization
* Performance depends on quality of input text
* Limited to text-based inputs (no PDF parsing)

---

## Future Improvements

* Integration with PDF/DOCX parsing
* Advanced NLP techniques (word embeddings, transformers)
* Improved skill extraction using predefined taxonomies
* Web-based interface for better usability

---

## Author

Developed as part of practical exploration into NLP and real-world problem solving in recruitment workflows.
