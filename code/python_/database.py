"""
Python example source code for loading and analyzing the MIMIC-IV Dataset.

Author(s):
    [INSERT YOUR TEAM MEMBER NAMES AND EMAILS HERE]

Licensed under the MIT License. Copyright MDplus and the author(s) 2023.
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, NamedTuple, Optional, Sequence, Union


class PatientSample(NamedTuple):
    subject_id: int
    data: Dict[str, Union[pd.Series, pd.DataFrame]]


class MIMICDataset:
    def __init__(
        self,
        datapath: Union[Path, str],
        files: Union[str, Sequence[str]]
    ) -> None:
        """
        Args:
            datapath: path to the entire dataset.
            files: the specific file(s) that should be imported within the
                datapath.
        """
        self._datapath = datapath
        self._files = files
        if isinstance(self._files, str):
            self._files = [self._files]

        self._file_suffix = ".csv.gz"
        self._subject_id_key = "subject_id"

        self.prepare_data()

    def __len__(self) -> int:
        """
        Returns the length of the overall dataset as an integer.
        Input:
            None.
        Returns:
            The number of unique patients in the dataset.
        """
        return len(self._subject_ids)

    def __getitem__(self, idx: int) -> PatientSample:
        id_ = self._subject_ids[idx]
        item = {}
        for key, matrix in self.data.items():
            row_number = np.where(matrix[self._subject_id_key] == id_)[0]
            item[key] = matrix.iloc[row_number]
        return PatientSample(id_, item)

    def prepare_data(self) -> None:
        """
        Loads the specified data from the relevant CSV files.
        Input:
            None.
        Returns:
            None.
        """
        self.data = {}
        self._subject_ids = None

        for f in self._files:
            subject_ids = set([])
            key = f.replace(self._file_suffix, "")
            if not f.endswith(self._file_suffix):
                f = f + self._file_suffix
            self.data[key] = pd.read_csv(
                os.path.join(self._datapath, f), compression="gzip"
            )
            for _id in self.data[key][self._subject_id_key]:
                subject_ids.add(_id)

            if self._subject_ids is None:
                self._subject_ids = subject_ids
            else:
                self._subject_ids = self._subject_ids & subject_ids

        # Order the subject ids by number for deterministic behavior.
        self._subject_ids = sorted(list(self._subject_ids))

    def __repr__(self) -> str:
        """
        Represents the dataset object as a string with pertinent info.
        Input:
            None.
        Returns:
            A string representation of this dataset object.
        """
        info = ""
        for key in self.data:
            num_rows, num_features = self.data[key].shape
            info += key + ": "
            info += f"MIMIC Dataset with {num_rows} entries and "
            info += f"{num_features} features.\nFeatures:\n"
            for col, dtype in zip(
                self.data[key].columns, self.data[key].dtypes
            ):
                info += f"  `{col}` with {dtype} datatype\n"
        return info[:-1]

    def plot_distribution(
        self,
        key: str,
        column: str,
        savepath: Optional[Union[Path, str]] = None
    ) -> None:
        """
        Plots a specified variable from a DataFrame for the patient population
        in the dataset.
        Input:
            key: dataframe for which to find the column to plot.
            column: column value to plot. Must be a continuous variable.
            savepath: optional file path to save the resulting histogram to.
                Default not saved.
        Returns:
            None.
        """
        plt.figure(figsize=(10, 6))
        plt.hist(self.data[key][column], bins=100)
        plt.xlabel(column.title())
        plt.ylabel("Number of Patients")
        plt.xticks(rotation=45, ha="right")
        if savepath is not None:
            plt.savefig(
                savepath, dpi=600, transparent=True, bbox_inches="tight"
            )
        else:
            plt.show()
        plt.close()
        return


if __name__ == "__main__":
    datapath = os.path.join("./data", "mimic-iv-clinical-database-demo-2.2")
    dataset = MIMICDataset(
        datapath,
        files=[
        "hosp/admissions", "hosp/prescriptions", "hosp/procedures_icd"
        ]
    )
    dataset.plot_distribution("hosp/admissions", column="race")
