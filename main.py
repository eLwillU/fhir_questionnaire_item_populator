import pandas as pd
import json

def createquetiontitle(linkid, prefix, question_text_de, question_text_fr):
    templatequestiontitle = {
        "linkId": linkid,
        "prefix": prefix,
        "text": question_text_de,
        "_text": {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/translation",
                    "extension": [
                        {
                            "url": "lang",
                            "valueCode": "de"
                        },
                        {
                            "url": "content",
                            "valueString": question_text_de
                        }
                    ]
                },
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/translation",
                    "extension": [
                        {
                            "url": "lang",
                            "valueCode": "fr"
                        },
                        {
                            "url": "content",
                            "valueString": question_text_fr
                        }
                    ]
                }
            ]
        },
        "type": "choice",
        "required": True,
        "answerOption": []
    }
    return templatequestiontitle


def createansweroption(answer_text_de, answer_text_fr, code):
    answeroption = {
        "valueCoding": {
            "code": code,
            "display": answer_text_de,
            "_display": {
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/translation",
                        "extension": [
                            {
                                "url": "lang",
                                "valueCode": "de"
                            },
                            {
                                "url": "content",
                                "valueString": answer_text_de
                            }
                        ]
                    },
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/translation",
                        "extension": [
                            {
                                "url": "lang",
                                "valueCode": "fr"
                            },
                            {
                                "url": "content",
                                "valueString": answer_text_fr
                            }
                        ]
                    }
                ]
            }
        }
    }
    return answeroption


def writetojson(jsondata):
    with open('data.json', 'a', encoding='utf-8') as f:
        # Serialize the data and write it to the file
        json.dump(jsondata, f, ensure_ascii=False, indent=4)


df = pd.read_excel('data/data.xlsx',
                   dtype={"linkid": int,
                          "prefix": int,
                          "numAnswers": int},
                   na_values=["NA"])
res = []
options = []

for index, row in df.iterrows():
    juan = createquetiontitle(linkid=row["linkid"], prefix=row["prefix"], question_text_de=row["question_text_de"],
                              question_text_fr=row["question_text_fr"])

    german_value = ""
    french_value = ""
    counter = 0
    num_answers_value = row["numAnswers"]

    for i, (german, french) in enumerate(zip(row[6:], row.iloc[6 + num_answers_value:])):
        if i == num_answers_value:
            break
        if pd.notna(german):
            german_value = german
        if pd.notna(french):
            french_value = french
        juan_son = createansweroption(answer_text_de=german_value, answer_text_fr=french_value, code=counter)
        counter += 1
        options.append(juan_son)

    juan["answerOption"].extend(options)
    res.append(juan)

writetojson(res)
