from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import torch
import pyperclip
import re
#pho_num = []

text = ""

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-large-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-large-NER")

def ner(text):
    # create a pipleine to get the output
    nlp = pipeline('ner', model=model, tokenizer=tokenizer)
    ner_list = nlp(text)

    # For Location - else replace the entites
    this_loc = []
    all_names_list_tmp = []

    for ner_dict in ner_list:
        if ner_dict['entity'] == 'B-LOC':
            if len(this_loc) == 0:
                this_loc.append(ner_dict['word'])
            else:
                all_names_list_tmp.append([this_loc])
                this_loc = []
                this_loc.append(ner_dict['word'])
        elif ner_dict['entity'] == 'I-LOC':
            this_loc.append(ner_dict['word'])

    all_names_list_tmp.append([this_loc])

    final_loc_list = []
    for name_list in all_names_list_tmp:
        full_name = ' '.join(name_list[0]).replace(' ##', '').replace(' .', '.')
        final_loc_list.append([full_name])


    # Person Name
    this_name = []
    all_names_list_tmp = []

    for ner_dict in ner_list:
        if ner_dict['entity'] == 'B-PER':
            if len(this_name) == 0:
                this_name.append(ner_dict['word'])
            else:
                all_names_list_tmp.append([this_name])
                this_name = []
                this_name.append(ner_dict['word'])
        elif ner_dict['entity'] == 'I-PER':
            this_name.append(ner_dict['word'])

    all_names_list_tmp.append([this_name])

    final_name_list = []
    for name_list in all_names_list_tmp:
        full_name = ' '.join(name_list[0]).replace(' ##', '').replace(' .', '.')
        final_name_list.append([full_name])


    # numbers removal if any important
    imp_num = []
    for z in text.split():
        if z.isdigit():
            imp_num.append(int(z))
            
    return final_name_list,final_loc_list




def get_phone_numbers(string):
    r = re.compile(
        r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    pho_num = [re.sub(r'\D', '', num) for num in phone_numbers]
    return pho_num

# email


def email(text):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    return(emails)


# call
get_phone_numbers(text)
email(text)


# list of outputs - LOC - NAME - Numbers
print(final_loc_list)
print(final_name_list)
print(imp_num)  # any imp numbers
print(emails)
print(pho_num)
