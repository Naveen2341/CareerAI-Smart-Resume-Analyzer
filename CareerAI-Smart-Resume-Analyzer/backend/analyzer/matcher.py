import re
SKILL_BANK={
 "python":["python"],"django":["django"],"react":["react","react.js"],"javascript":["javascript","js"],
 "html":["html"],"css":["css"],"sql":["sql","sqlite","sqlite3","mysql","postgresql"],
 "rest api":["rest api","restful api"],"git":["git","github"],"docker":["docker"],
 "aws":["aws","amazon web services"],"machine learning":["machine learning","ml"],
 "pandas":["pandas"],"numpy":["numpy"],"java":["java"],"c++":["c++"],
 "communication":["communication"],"problem solving":["problem solving"]
}
def find_skills(text):
    source=text.lower()
    found=[]
    for skill,terms in SKILL_BANK.items():
        if any(re.search(r"(?<![a-z0-9+#])"+re.escape(term)+r"(?![a-z0-9+#])",source) for term in terms):
            found.append(skill)
    return found
def analyze(resume_text,job_text):
    resume=find_skills(resume_text); required=find_skills(job_text)
    if not required: required=["python","sql","communication"]
    matched=sorted(set(resume)&set(required)); missing=sorted(set(required)-set(resume))
    score=round((len(matched)/len(required))*100) if required else 0
    tips=[]
    if missing: tips.append("Build evidence for these job skills: "+", ".join(missing)+".")
    if not any(x in resume for x in ("django","react","rest api")): tips.append("Add a relevant web application project with clear technologies and outcomes.")
    if not re.search(r"\b(project|developed|built|created|implemented)\b",resume_text,re.I): tips.append("Add project experience using action verbs and measurable results.")
    if not tips: tips.append("Your detected skills align well. Tailor your summary and project bullets to this job.")
    return {"score":score,"matched_skills":matched,"missing_skills":missing,"recommendations":tips,"resume_skills":resume,"required_skills":required}
