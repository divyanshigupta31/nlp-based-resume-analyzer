import argparse
from utils import read_file, compute_score, missing_skills, generate_suggestions

def main():
    parser = argparse.ArgumentParser(description="Resume Analyzer")
    
    parser.add_argument("--resume", type=str, required=True)
    parser.add_argument("--jd", type=str, required=True)
    
    args = parser.parse_args()
    
    resume_text = read_file(args.resume)
    jd_text = read_file(args.jd)
    
    score = compute_score(resume_text, jd_text)
    missing = missing_skills(resume_text, jd_text)
    suggestions = generate_suggestions(missing)
    
    print("\n===== RESUME ANALYSIS =====\n")
    
    print(f"Match Score: {score}%\n")
    
    print("Missing Skills:")
    for skill in missing:
        print("-", skill)
    
    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)

if __name__ == "__main__":
    main()