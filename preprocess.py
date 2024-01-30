import ast

import pandas as pd


def extract_columns(df):
    subject_word = []
    subject_start_idx = []
    subject_end_idx = []
    subject_type = []
    
    object_word = []
    object_start_idx = []
    object_end_idx = []
    object_type = []

    for subject, object in zip(df['subject_entity'], df['object_entity']):
        subject = ast.literal_eval(subject)
        object = ast.literal_eval(object)

        subject_word.append(subject['word'])
        subject_start_idx.append(subject['start_idx'])
        subject_end_idx.append(subject['end_idx'])
        subject_type.append(subject['type'])

        object_word.append(object['word'])
        object_start_idx.append(object['start_idx'])
        object_end_idx.append(object['end_idx'])
        object_type.append(object['type'])

    df['subject_word'] = subject_word
    df['subject_start_idx'] = subject_start_idx
    df['subject_end_idx'] = subject_end_idx
    df['subject_type'] = subject_type

    df['object_word'] = object_word
    df['object_start_idx'] = object_start_idx
    df['object_end_idx'] = object_end_idx
    df['object_type'] = object_type

    df.drop(columns=['subject_entity', 'object_entity'], inplace=True)

    return df


def data_cleaning(df):
    df.drop_duplicates(subset=['sentence', 'subject_word','object_word','label'], inplace=True)
    duplicates = df[df.duplicated(subset=['sentence', 'subject_word','object_word'], keep=False)]
    df.drop(duplicates[duplicates['label'] == 'no_relation'].index, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df['id'] = df.index

    return df


train, validation, test = pd.read_csv("./data/train.csv"), pd.read_csv("./data/validation.csv"), pd.read_csv("./data/test.csv")
train, validation, test = extract_columns(train), extract_columns(validation), extract_columns(test)
train = data_cleaning(train)
train.to_csv("./data/train_processed.csv", index=False)
validation.to_csv('./data/validation_processed.csv', index=False)
test.to_csv("./data/test_processed.csv", index=False)