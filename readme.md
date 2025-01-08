# Spam Email Classification

## Project Overview

This project classifies emails as spam or not using machine learning techniques. A user-friendly frontend built with **Streamlit** allows users to input email text and get predictions.

---

## Problem Statement

Spam emails are a major nuisance, wasting time and posing security threats. This project aims to develop an effective email classification model that can be used to automatically filter spam emails, ensuring a cleaner and more productive inbox experience.

---

## Objectives

- Build a machine learning model to classify emails as spam or not spam.
- Create an interactive application for spam detection.

---

## Dataset

- **Source:** [Kaggle Spam Mails Dataset](https://www.kaggle.com/datasets/venky73/spam-mails-dataset)
- **Description:**
  This dataset is collected from [here](https://www2.aueb.gr/users/ion/data/enron-spam/). I just used enron1 folder. It contains two folders of spam and ham. Each folder contains emails. I iterated to each text file of those folders and created a dataframe and written to a csv file. This can be helpful for others.

---

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:**
  - Pandas
  - Scikit-learn
  - Matplotlib
  - Seaborn
- **Deployment:**
  - **Frontend:** Streamlit for an interactive user interface to input email text.
  - **Backend:** FastAPI for managing API requests and serving the prediction model.

---

## Evaluation Metrics

The model's performance is evaluated using the following metrics:

- **Accuracy:** Proportion of correctly classified emails.
- **F1-Score:** Combines precision and recall to evaluate model performance.
- **Precision & Recall:** Measure how effectively the model identifies spam emails.

---

## NOTES

### Frontend Request URL Configuration

In `client/utils.py`, url = `http://fastapi:8080`

- **When running locally (outside Docker Compose)**:  
  Use the local URL:  
  `http://127.0.0.1:8080`

- **When running with Docker Compose**:  
  Update the frontend's request URL to:  
  `http://fastapi:8080`  
  This is the internal URL provided by Docker Compose for the FastAPI service within the shared Docker network.

> **Note**: The `fastapi` hostname works only when both FastAPI and Streamlit services are running within the same Docker Compose network.

---
