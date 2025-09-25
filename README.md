# 💖 Heart Disease Prediction Web App

## 👋 Introduction
Hi! I am **Jashandeep Kaur** 😊. This project is a **Heart Disease Prediction** web application built using **Python, Flask, and machine learning**. The app predicts the **10-year risk of coronary heart disease (CHD)** based on patient data.  

---

## 🏥 Project Overview
Heart disease is one of the leading causes of death worldwide. This project uses a **machine learning model** trained on patient data to predict whether someone is at risk of developing heart disease within the next 10 years.

The app allows users to input their personal and clinical details and get a **prediction along with the probability of risk**.

---

## 📊 Dataset Description
The dataset contains **3,794 patient records** with **15 columns**:

| Column | Description | Importance |
|--------|------------|------------|
| `Sex_male` | Gender (1 = Male, 0 = Female) | Men have higher heart disease risk |
| `age` | Age in years | Older age increases risk |
| `currentSmoker` | Smoker status (1 = Yes, 0 = No) | Smoking increases heart risk |
| `cigsPerDay` | Number of cigarettes smoked per day | Quantifies smoking intensity |
| `BPMeds` | Blood pressure medication (1 = Yes, 0 = No) | Indicates hypertension treatment |
| `prevalentStroke` | History of stroke (1 = Yes, 0 = No) | Previous stroke increases risk |
| `prevalentHyp` | History of hypertension (1 = Yes, 0 = No) | Hypertension is a major risk factor |
| `diabetes` | Diabetes status (1 = Yes, 0 = No) | Diabetes increases cardiovascular risk |
| `totChol` | Total cholesterol (mg/dL) | High cholesterol increases risk |
| `sysBP` | Systolic blood pressure | High blood pressure increases risk |
| `diaBP` | Diastolic blood pressure | Additional blood pressure measure |
| `BMI` | Body Mass Index | Overweight/obesity increases risk |
| `heartRate` | Heart rate (beats per minute) | Can indicate cardiovascular health |
| `glucose` | Blood glucose level | High glucose indicates diabetes risk |
| `TenYearCHD` | Target variable (1 = risk, 0 = no risk) | 10-year risk of heart disease |

---

## ⚡ Features Used in Prediction
Although the dataset has 15 columns, we used **9 key features** for prediction:  

`age`, `Sex_male`, `cigsPerDay`, `BPMeds`, `diabetes`, `BMI`, `totChol`, `sysBP`, `glucose`  

**Why only 9 features?**  
- Some features like `education` were dropped because they have minimal impact.  
- Others like `prevalentStroke` or `prevalentHyp` are either rare or redundant due to `BPMeds` and `sysBP`.  
- This selection improves model **accuracy and generalization**.  

---

## 🧠 Model
- **Algorithm:** Logistic Regression  
- **Target Variable:** `TenYearCHD` (1 = heart disease risk, 0 = no risk)  
- **How it works:** The model calculates the probability of heart disease risk based on weighted contributions from the 9 input features.  
- **Interpretation:**  
  - Probability > 0.5 → Predicts `Heart Disease Risk`  
  - Probability ≤ 0.5 → Predicts `No Heart Disease Risk`  

---

### 1. Clone the repository
```bash
git clone https://github.com/Jashan-hf-ai/heart-disease-prediction.git
cd heart-disease-prediction
---
title: Heart Disease Prediction
emoji: 🏃
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
