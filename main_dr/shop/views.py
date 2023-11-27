from django.shortcuts import render

# Create your views here.
name: Deploy
on:
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.9]
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v3
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Tests
        run: |
          python manage.py test
      - name: executing remote ssh commands using password
        uses: appleboy/ssh-action@master
        with:
          host: 34.116.67.50
          username: ${{ secrets.USERNAME }}
          password: ${{ secrets.PASSWORD }}
          port: 22
          script: |
            cd main_dr
            source /home/kimd_22848/venv/bin/activate
            git pull
            python manage.py migrate
            python manage.py collectstatic --noinput
            sudo supervisorctl restart all

name: Deploy
on:
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.9]
    steps:
      - uses: actions/checkout@v3
      - name: executing remote ssh commands using password
        uses: appleboy/ssh-action@master
        with:
          host: 34.116.67.50
          username: ${{ secrets.USERNAME }}
          password: ${{ secrets.PASSWORD }}
          port: 22
          script: |
            cd main_dr
            source /home/kimd_22848/venv/bin/activate
            git pull
            python manage.py migrate
            python manage.py collectstatic --noinput
            sudo supervisorctl restart all