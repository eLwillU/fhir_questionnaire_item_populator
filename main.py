import pandas as pd

from functions import create_answer_option, write_to_json, read_language_sheet, create_question_title

# reading the data
file = pd.ExcelFile('data/data.xlsx')
df_german = read_language_sheet(file, "german")
df_french = read_language_sheet(file, "french")

# Creating and saving the data
res = []
for index, row in df_german.iterrows():
    counter = 0
    german_value = df_german.loc[index, "question_text_de"]
    german_row = df_german.loc[index]

    french_value = df_french.loc[index, "question_text_fr"]
    french_row = df_french.loc[index]
    options = []

    title = create_question_title(link_id=row["linkid"], prefix=row["prefix"], question_text_de=german_value,
                                  question_text_fr=french_value, enable_when=row["enableWhenBlock?"])

    for i, element in german_row[5:].items():
        if pd.notna(element):
            german_answer = element
            french_answer = french_row[i]

            answerOption = create_answer_option(answer_text_de=german_answer, answer_text_fr=french_answer,
                                                code=counter)
            counter += 1
            options.append(answerOption)

    title["answerOption"].extend(options)
    res.append(title)

write_to_json(res, "data.json")
