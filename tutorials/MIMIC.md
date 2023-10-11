# MIMIC-IV

This year, we're excited to have participating teams explore the **MIMIC-IV** dataset, a rich and complex dataset containing diverse datatypes ranging from EKGs, medical imaging studies, health records, and patient lab values and outcomes.

> This tutorial will walk through the basics of how to download the MIMIC-IV dataset to your local computer.

## Understanding the Dataset

MIMIC-IV is an healthcare dataset first published in January 2023 by Johnson AE et al. in Nature Scientific Data. You can read their study introducing the dataset [here](https://www.nature.com/articles/s41597-022-01899-x). Briefly, the dataset contains the de-identified medical information of over 500k patients admitted either to the ED or the ICU between 2008 and 2019 at [Beth Israel Deaconess Medical Center](https://www.bidmc.org). A detailed breakdown of patient demographic information can be found [here](https://www.nature.com/articles/s41597-022-01899-x/tables/2).

The official MIMIC-IV documentation from the research group is available [here](https://mimic.mit.edu/docs/iv/) and contains more detailed specifications on the different data modules, data structure, and relevant tutorials.

An example `Dataset` class has already been defined for you [here](../code/python_/database.py). If you are not yet familiar with Python, check out our **Introduction to Python** tutorial [here](../tutorials/INTRO_python.md).

## Downloading the Dataset

The MIMIC-IV dataset is available on PhysioNet [here](https://physionet.org/content/mimiciv/2.2/). Because the dataset contains sensitive patient data, it is important that your team completes the following steps to become a credentialed user and ultimately gain complete access to the dataset:

**Estimated Time for Completion: 30 min**

1. **Create a PhysioNet Account**: At least one of your team members will need to create an account on PhysioNet [here](https://physionet.org/register/).
2. **Sign Up as a Credentialed User**: Once you're logged in, you need to sign up for credentialed access [here](https://physionet.org/settings/credentialing/). The application for credentialed access is fairly straightforward and requires you to fill out basic information about yourself. You will also be asked for a reference: please include the following reference information:
  > - **Reference Category**: Supervisor (required for students and Postdocs)
  > - **Reference Name**: Michael Yao
  > - **Reference Email**: michael@mdplusplus.org
  > - **Reference Organization**: MDplus and University of Pennsylvania
  > - **Reference Job Title or Position**: MDplus Datathon Organizing Team

After submitting your team's application, you should be approved as a credentialed user in a few days (no more than a week).

3. **Complete CITI Training**: While waiting for approval as a credentialed user, please follow the instructions listed [here](https://physionet.org/about/citi-course/) to complete a short course on **Data or Specimens Only Research**. After completing the course, you can upload the training report (*not the certificate!*) to [this link](https://physionet.org/settings/training/).
4. **Sign the Data Use Agreement**: The data use agreement form can be found [here](https://physionet.org/content/mimiciv/view-dua/2.2/).

Congratulations! :partying_face: You should now have access to the complete MIMIC dataset at the bottom of [this page](https://physionet.org/content/mimiciv/2.2/).

## Downloading Dataset Modules

The total size of the MIMIC-IV dataset is a little over 7 GB, which is quite large and might contain extraneous information depending on your project. Furthermore, MIMIC-IV is further stratified into *modules*. The following modules are made available to you:

  > - [**`mimic-ed`**](https://physionet.org/content/mimic-iv-ed/2.2/): A dataset of over 400k ED admissions between 2011 and 2019. 
  > - [**`mimic-note`**](https://physionet.org/content/mimic-iv-note/2.2/): A dataset of over 300k de-identified free-text clinical notes.
  > - [**`mimic-ecg`**](https://physionet.org/content/mimic-iv-ecg/1.0/): A dataset of over 800k ECG waveforms.
  > - [**`mimic-pulseox`**](https://physionet.org/content/mit-critical-datathon-2023/1.0.0/): A dataset of approximately 80k pairs of SaO2 and SpO2 ICU measurements.
  > - [**`mimic-echo`**](https://physionet.org/content/mimic-iv-echo/0.1/): A dataset of over 500k echocardiograms.
  > - [**`mimic-cxr`**](https://physionet.org/content/mimic-cxr-jpg/2.0.0/): A dataset of over 350k CXRs as JPG images with corresponding clinical lables.

  Depending on your project, you are free to download any number of the above modules (or others!) for usage in this datathon.

## FAQs

### Can I use the older [MIMIC-III dataset](https://physionet.org/content/mimiciii/1.4/) and its associated modules instead?

Absolutely! You will not be penalized at all for using MIMIC-III in addition to/instead of MIMIC-IV and its modules.

### My computer is on the older side and won't be able to process such large datasets. What can I do?

If computational resources are a limiting barrier, please feel free to use the (much smaller) demo versions of the above datasets instead. You will not be penalized at all for using demo datasets instead of the full dataset. Here are a couple of links to the smaller demo datasets:

 - [**`mimic-iv-demo`**](https://physionet.org/content/mimic-iv-demo/2.2/)
 - [**`mimic-iv-ed-demo`**](https://physionet.org/content/mimic-iv-ed-demo/2.2/)
 - [**`mimic-iv-ecg-demo`**](https://physionet.org/content/mimic-iv-ecg-demo/0.1/)

If an official demo dataset is not available for your application of interest, feel free to use a subset of the full dataset for your actual project. Just make sure to clearly document your data pruning process and inclusion/exclusion criteria.

> **Tip**: Of note, **the demo versions do not require credential access and completing CITI training.** This means that the demo version is also helpful for exploring the dataset, prototyping ideas, and getting started on your project prior to credentialed access approval.

### I still have questions. What can I do?

Come to office hours scheduled throughout the datathon or email us! Feel free to also ask questions in the `#datathon2023` MDplus Slack channel - many folks might also have the same questions as you!