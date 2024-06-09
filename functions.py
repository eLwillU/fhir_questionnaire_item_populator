import pandas as pd
import json


def create_question_title(link_id, prefix, question_text_de, question_text_fr, enable_when=False):
    if enable_when:
        template_question_title = {
            "linkId": link_id.strip(),
            "prefix": prefix.strip(),
            "text": question_text_de.strip(),
            "enableWhen": [
                {
                    "question": "3",
                    "operator": "=",
                    "answerCoding": {
                        "code": 0
                    }
                }
            ],
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
    else:
        template_question_title = {
            "linkId": link_id.strip(),
            "prefix": prefix.strip(),
            "text": question_text_de.strip(),
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
    return template_question_title


def create_answer_option(answer_text_de, answer_text_fr, code):
    answer_option = {
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
    return answer_option


def write_to_json(json_data, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        # Serialize the data and write it to the file
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def read_language_sheet(excel_file, sheet_name):
    data_frame = pd.read_excel(excel_file, sheet_name=sheet_name,
                               dtype={"linkid": str,
                                      "prefix": str,
                                      "numAnswers": int},
                               na_values=["NA"])

    return data_frame
