import pandas as pd
from typing import NamedTuple


class PatientSample(NamedTuple):
    subject_id: int
    icd_code: str
    text: str


class MIMICDataset:

    def __init__(self):
        self.icd_codes = pd.read_csv("./data/diagnoses_icd_small.csv")
        self.notes = pd.read_csv("./data/discharge_small.csv")

        self.columns = ["subject_id", "hadm_id", "icd_code", "text"]

        # 1. Throw out information that we don't care about.
        self.icd_codes = self.icd_codes[["subject_id", "hadm_id", "icd_code"]]
        self.notes = self.notes[["subject_id", "hadm_id", "text"]]

        # 2. Find the intersection of the subject_ids between both tables.
        subject_ids_from_icd_table = self.icd_codes["subject_id"]
        subject_ids_from_notes_table = self.notes["subject_id"]
        self.subject_ids = sorted(
            list(
                set(subject_ids_from_icd_table) & set(
                    subject_ids_from_notes_table
                )
            )
        )

        # 2b. Throw out patient data that is not in self.subject_ids.
        self.icd_codes = self.icd_codes[
            self.icd_codes["subject_id"].isin(self.subject_ids)
        ]
        self.notes = self.notes[
            self.notes["subject_id"].isin(self.subject_ids)
        ]

        # 2c. Remove the duplicate rows from each of the tables.
        self.icd_codes = self.icd_codes.drop_duplicates(subset=["subject_id"])
        self.notes = self.notes.drop_duplicates(subset=["subject_id"])

    def __len__(self):
        # 3. How many patients do we have in this dataset?
        return len(self.subject_ids)

    def __getitem__(self, idx: int):
        # 4. Can we easily extract patient data from this dataset?
        patient_subject_id = self.subject_ids[idx]
        patient_icd_code = self.icd_codes[
            self.icd_codes["subject_id"] == patient_subject_id
        ]["icd_code"].item()
        patient_note = self.notes[
            self.notes["subject_id"] == patient_subject_id
        ]["text"].item()
        return PatientSample(
            patient_subject_id, patient_icd_code, patient_note
        )


if __name__ == "__main__":
    my_tiny_dataset = MIMICDataset()
    num_train = 14
    num_val = 2
    num_test = 4
    train_dataset = my_tiny_dataset[:num_train]
    val_dataset = my_tiny_dataset[num_train:(num_train+num_val)]
    test_dataset = my_tiny_dataset[(num_train+num_val):]
