# 🏠 House Price Prediction - MLOps Project

Ce projet utilise le dataset [HouseData de Kaggle](https://www.kaggle.com/datasets/shree1992/housedata) pour prédire le prix des maisons.

## 🎯 Objectif

Mettre en place une solution MLOps complète incluant :

- Prétraitement et entraînement d’un modèle ML
- Déploiement via API REST (FastAPI)
- Dockerisation
- CI/CD avec GitHub Actions
- Logging structuré

## 🧱 Architecture du projet

house_price_mlops/
├── app/ # API FastAPI
├── data/ # Dataset
├── models/ # Modèle entraîné
├── notebooks/ # Analyse exploratoire
├── pipeline/ # Prétraitement et entraînement
├── tests/ # Tests unitaires
├── Dockerfile # Dockerisation
├── .github/workflows/ # CI/CD GitHub Actions

## 🚀 Lancer l’API

```bash
uvicorn app.main:app --reload
