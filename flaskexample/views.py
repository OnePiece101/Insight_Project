#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:43:38 2020

@author: yafen
"""

from flask import render_template
from flaskexample import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

# Python code to connect to Postgres
# You may need to modify this based on your OS,
# as detailed in the postgres dev setup materials.
# user = 'postgres' #add your Postgres username here
# host = 'localhost'
# dbname = 'birth_db'
# pswd = '112358'
# db = create_engine('postgres://%s@%s/%s'%(user,host,dbname))
# con = None
# con = psycopg2.connect(database = dbname, user = user)

@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html",
      title = 'Home', user = { 'nickname': 'Miguel' },
      )

@app.route('/db')
def birth_page():
   # sql_query = """
   #             SELECT * FROM birth_data_table WHERE delivery_method='Cesarean';
   #             """
   query_results = pd.read_csv('/home/yafen/insight_project/Week1Demo/ysl.csv')
   colors = ""
   for i in range(0,10):
       colors += query_results.iloc[i]['color']
       colors += "<br>"
   return colors

@app.route('/db_fancy')
def cesareans_page_fancy():
   # sql_query = """
   #            SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean';
   #             """
   query_results=pd.read_csv('/home/yafen/insight_project/Week1Demo/ysl.csv')
   births = []
   for i in range(0,query_results.shape[0]):
       births.append(dict(index=query_results.iloc[i]['brand'], attendant=query_results.iloc[i]['color_code'], birth_month=query_results.iloc[i]['color']))
   return render_template('cesareans.html',births=births)
