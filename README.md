# 9E0 Brain Tumor MRI Classification Competition

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ogoun09gerbad/Final_Repo_Brain_Cancer/blob/main/Brain_Tumor_Competition.ipynb)

## 4DD Description
This competition involves classifying brain MRI images into 4 categories: **Glioma, Meningioma, No Tumor, and Pituitary**. 

## 4C2 Repository Structure
- `train.csv`: Training data (Image paths and Labels).
- `test.csv`: Testing data for inference (Use these paths for your predictions).
- `solution.csv`: Ground truth labels (Private, used for evaluation).
- `sample_submission.csv`: Example format for your submission.
- `leaderboard.csv`: Current rankings based on Accuracy.
- `model.py`, `train.py`, `test.py`: Modular Python scripts for the pipeline.

## 680 Submission Guide (Step-by-Step)

### Step 1: Set up the Environment
Click the **Open in Colab** badge above to launch the notebook with all necessary libraries pre-installed.

### Step 2: Run Inference on Test Data
Load `test.csv` and use your trained model to predict the class for each image path listed.

### Step 3: Format the Submission File
Create a file named `submission.csv`. It must contain exactly two columns:
1. `ImageId`: The full path of the image (exactly as found in `test.csv`).
2. `Expected`: The predicted class name (e.g., `glioma`, `meningioma`).

### Step 4: Submit and Score
Upload your `submission.csv` to the repository. The leaderboard script will then calculate your **Accuracy** against the `solution.csv`.

## 4CA Evaluation
The evaluation metric is **Global Accuracy**.

---
Created by **OGOUNCHI G3raud Bad3l3** and **NDEYE Binta Ndiaye**
