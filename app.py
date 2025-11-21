name: Deploy Diabetes Prediction App

on:
  push:
    branches:
      - main   

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"   

      - name: Deploy to Heroku (Diabetes App)
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
          heroku_app_name: "ml-will-i-get-diabetes2-app"   
          heroku_email: ${{ secrets.HEROKU_EMAIL }}
          usedocker: true   
          appdir: "C:/Users/Nanoo/OneDrive/Desktop/ANA-680/ml-diabetes-containerized-app"
