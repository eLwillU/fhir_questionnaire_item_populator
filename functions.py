import pandas as pd
import json
import pprint as pp


def createquetiontitle(linkid, prefix, question_text_de, question_text_fr):
    templatequestiontitle = {
        "linkId": linkid.strip(),
        "prefix": prefix.strip(),
        "text": question_text_de.strip(),
        "enableWhen": [],
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
                            "valueString": question_text_de.strip()
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
                            "valueString": question_text_fr.strip()
                        }
                    ]
                }
            ]
        },
        "type": "choice",
        "required": True,
        "answerOption": [

        ]
    }
    return templatequestiontitle


def createansweroption(answer_text_de, answer_text_fr, code):
    answeroption = {
        "valueCoding": {
            "code": code,
            "display": answer_text_de.strip(),
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
                                "valueString": answer_text_de.strip()
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
                                "valueString": answer_text_fr.strip()
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


def read_language_sheet(excel_file, sheet_name):
    data_frame = pd.read_excel(excel_file, sheet_name=sheet_name,
                               dtype={"linkid": str,
                                      "prefix": str,
                                      "numAnswers": int},
                               na_values=["NA"])

    return data_frame
