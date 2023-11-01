"""
Python example source code for loading and analyzing the MIMIC-IV Dataset.

Author(s):
    [INSERT YOUR TEAM MEMBER NAMES AND EMAILS HERE]

Licensed under the MIT License. Copyright MDplus and the author(s) 2023.
"""
import os
import pandas as pd
import torch
from pathlib import Path
from torch.utils.data import Dataset
from typing import NamedTuple, Sequence, Union


class PatientSample(NamedTuple):
    subject_id: int
    hadm_id: int
    note_id: str
    icd_code: str
    icd_version: int
    text: str


class MIMICDataset(Dataset):
    def __init__(self, modules: Sequence[Union[Path, str]]):
        """
        Args:
            modules: a sequence of file paths to the relevant MIMIC-IV modules
                to import.
        """
        # Import the relevant modules as CSV files.
        self.modules = {}
        for mod in modules:
            self.modules[os.path.basename(mod)] = pd.read_csv(mod)

        # Find the intersection of the Subject IDs.
        self.subject_id = "subject_id"
        _ids = [
            set(df[self.subject_id].to_list())
            for _, df in self.modules.items()
        ]
        self._ids = _ids[0]
        for id_set in _ids:
            self._ids = self._ids & id_set
        self._ids = sorted(list(self._ids))

        for mod, df in self.modules.items():
            # Restrict our datasets to just the patients of interest.
            self.modules[mod] = df[df[self.subject_id].isin(self._ids)]
            # Remove duplicates to prevent data leakage.
            self.modules[mod] = self.modules[mod].drop_duplicates(
                self.subject_id
            )

        self._init_vocab()

    def __len__(self) -> int:
        """
        Returns the length of the dataset.
        Input:
            None.
        Returns:
            The length of the dataset.
        """
        return len(self._ids)

    def __getitem__(self, idx: int) -> PatientSample:
        """
        Returns the specified item from the dataset.
        Input:
            idx: index of the element to retrieve from the dataset.
        Returns:
            The specified item from the dataset.
        """
        patient = {}
        for mod, df in self.modules.items():
            for col in set(self.columns) & set(df.columns):
                patient[col] = df[df[self.subject_id] == self._ids[idx]][col]
                patient[col] = patient[col].item()
        return PatientSample(
            patient["subject_id"],
            patient["hadm_id"],
            patient["note_id"],
            patient["icd_code"],
            patient["icd_version"],
            patient["text"]
        )

    @property
    def columns(self) -> Sequence[str]:
        """
        Returns the properties of interest in constructing our dataset.
        Input:
            None.
        Returns:
            A list of the properties of interest to construct our dataset.
        """
        return [
            "subject_id",
            "hadm_id",
            "note_id",
            "icd_code",
            "icd_version",
            "text"
        ]

    def _init_vocab(self) -> None:
        """
        Creates the word vocabulary for the dataset.
        Input:
            None.
        Returns:
            None.
        """
        vocab = set([])
        for i in range(len(self)):
            note = self[i].text.split()
            if len(vocab) == 0:
                vocab = set(note)
            else:
                vocab = vocab | set(note)
        self.vocab = {
            word: idx for idx, word in enumerate(sorted(list(vocab)))
        }
        return

    def tokenize(self, note: str) -> torch.Tensor:
        """
        Encodes a note as a tensor of tokens.
        Input:
            note: a note.
        Returns:
            The corresponding token representation of the note.
        """
        return torch.tensor([self.vocab[word] for word in note.split()])


def main():
    _ = MIMICDataset(
        ["./data/diagnoses_icd_small.csv", "./data/discharge_small.csv"]
    )


if __name__ == "__main__":
    main()
