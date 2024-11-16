import spacy

nlp = spacy.load("en_core_web_sm")

target_names = {
    "Alan Hodgkin",
    "Andrew Huxley",
    "Kenneth Cole",
    "JZ Young",
    "L.W. Williams",
    "Enrico Sereni"
}

def extract_target_names(file_path, target_names):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    doc = nlp(text)
    
    extracted_names = {ent.text for ent in doc.ents if ent.label_ == "PERSON"}
    
    matched_names = extracted_names.intersection(target_names)
    
    return matched_names

txt_file_path = '/Users/yixiao/Desktop/outline.txt'

print("找到的人名:", names_found)


