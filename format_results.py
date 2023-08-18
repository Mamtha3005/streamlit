import json
import pandas as pd

def format_merged_cell(value1, value2):
    merged_cell = f'<div style="display: flex; flex-direction: row;"><div style="width: 50%;">{value1}</div><div style="width: 50%;">{value2}</div></div>'
    return merged_cell

def format_to_json(prediction):
    f = open('sampleResults.json')
    json_data = json.load(f)
    print("data: ", json_data)

    df = pd.DataFrame(columns=['Index'], data={'Index': ['Nucleotide','hAm','hCm','hGm','hTm','hm1A',
                                                         'hm5C','hm5U','hm6A','hm6Am','hm7G','hPsi','Atol']})
    print(df)

    dataWithProbabilities = json_data['POSITION_WITH_PROBABILITIES']
    for data in dataWithProbabilities:
        index = data['RNA_MODIFIED_INDEX']
        column = getBinaryColumn(data)
        df[index] = column

    print(df)
    return df

def getBinaryColumn(jsonObject):
    print('jsonObject: ', jsonObject)
    nucleotide = jsonObject['PARENT_MODIFIED_NUCLEOTIDE']
    probabilities = jsonObject['BINARY_MODIFICATION_PROBABILITIES']
    hAm = ''
    hCm = ''
    hGm = ''
    hTm = ''
    hm1A = ''
    hm5C = ''
    hm5U = ''
    hm6A = ''
    hm6Am = ''
    hm7G = ''
    hPsi = ''
    Atol = ''
    print("probabilities: ", probabilities)
    for p in probabilities:
        if "hAm" in p:
            hAm = p['hAm']
        if "hCm" in p:
            hCm = p['hCm']
        if "hGm" in p:
            hGm = p['hGm']
        if "hTm" in p:
            hTm = p['hTm']
        if "hm1A" in p:
            hm1A = p['hm1A']
        if "hm5C" in p:
            hm5C = p['hm5C']
        if "hm5U" in p:
            hm5U = p['hm5U']
        if "hm6A" in p:
            hm6A = p['hm6A']
        if "hm6Am" in p:
            hm6Am = p['hm6Am']
        if "hm7G" in p:
            hm7G = p['hm7G']
        if "hPsi" in p:
            hPsi = p['hPsi']
        if "Atol" in p:
            Atol = p['Atol']

    column = [nucleotide, hAm, hCm, hGm, hTm, hm1A, hm5C, hm5U, hm6A, hm6Am, hm7G, hPsi, Atol]

    print("column: ", column)
    return column

def save_json_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
