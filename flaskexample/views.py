#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:43:38 2020

@author: yafen
"""

from flaskexample.color_Model import ColorID
from flask import render_template
from flask import request
from flaskexample import app
from sqlalchemy import create_engine
# from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import numpy as np
import time
from flaskexample.lip_bgr import lip_landmarks
# import psycopg2

# Python code to connect to Postgres
# You may need to modify this based on your OS,
# as detailed in the postgres dev setup materials.
user = 'yafen' #add your Postgres username here
host = 'localhost'
dbname = 'p_demo'
pswd = '112358'
db = create_engine('postgres://%s:%s@%s/%s'%(user,pswd,host,dbname))
# con = None
# con = psycopg2.connect(database = dbname, user = user)

# @app.route('/')
# @app.route('/index')
# def index():
#    return render_template("index.html",
#       title = 'Home', user = { 'nickname': 'Miguel' },
#       )

# @app.route('/db')
# def birth_page():
#    sql_query = """
#                SELECT * FROM birth_data_table WHERE delivery_method='Cesarean';
#                """
#    query_results = pd.read_sql_query(sql_query,db)
#    births = ""
#    for i in range(0,10):
#        births += query_results.iloc[i]['birth_month']
#        births += "<br>"
#    return births

# @app.route('/db_fancy')
# def cesareans_page_fancy():
#    # sql_query = """
#    #            SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean';
#    #             """
#    query_results=pd.read_csv('/home/yafen/insight_project/Week1Demo/ysl.csv')
#    births = []
#    for i in range(0,query_results.shape[0]):
#        births.append(dict(index=query_results.iloc[i]['brand'], attendant=query_results.iloc[i]['color_code'], birth_month=query_results.iloc[i]['color']))
#    return render_template('cesareans.html',births=births)

# @app.route('/input')
# def cesareans_input():
#    return render_template("input.html")

# @app.route('/output')
# def cesareans_output():
#      #pull 'birth_month' from input field and store it
#     patient = request.args.get('birth_month')
#    #just select the Cesareans  from the birth dtabase for the month that the user inputs
#     query = "SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean' AND birth_month='%s'" % patient
#     print(query)
#     query_results=pd.read_sql_query(query,db)
#     print(query_results)
#     births = []
#     for i in range(0,query_results.shape[0]):
#         births.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
#         the_result = ModelIt(patient, births)
#     return render_template("output.html",births = births, the_result = the_result)

# @app.route('/inputTest')
# def addition_input():
#    return render_template("inputTest.html")

# @app.route('/outputTest')
# def addition_output():
#    num_one = float(request.args.get('first_number'))
#    num_two = float(request.args.get('second_number'))
#    sumofnums = num_one + num_two
#    print(sumofnums)
#    return render_template("outputTest.html", sumofnums = sumofnums)

# @app.route('/ysl')
# def ysl_page():
#    sql_query = """
#                SELECT product_id,brand,looks,color_code,color FROM ysl_test_table;
#                """
#    query_results = pd.read_sql_query(sql_query,db)
#    colors = []
#    for i in range(query_results.shape[0]):
#        colors.append(dict(product_id=query_results.iloc[i]['product_id'],
#                           brand=query_results.iloc[i]['brand'],
#                           looks=query_results.iloc[i]['looks'],
#                           color_code=query_results.iloc[i]['color_code'],
#                           color=query_results.iloc[i]['color']))
#    return render_template("ysl.html",colors=colors)

# @app.route('/inputYsl')
# def ysl_input():
#    return render_template("inputYsl.html")

# @app.route('/outputYsl')
# def ysl_output():
#      #pull 'birth_month' from input field and store it
#     bgr_txt = request.args.get('bgr_mean')
#     bgr_vals = np.reshape(np.array([float(e) for e in bgr_txt.split(',')],dtype='float32'),(1,-1))
#    #just select the Cesareans  from the birth dtabase for the month that the user inputs
#     query = "SELECT product_id,brand,looks,color_code,color, rgb_mean FROM ysl_test_table;"
#     print(query)
#     query_results=pd.read_sql_query(query,db)
#     print(query_results)
#     df_ysl = ColorID(query_results, bgr_vals)
#     colors = []
#     for i in range(0,df_ysl.shape[0]):
#         colors.append(dict(product_id=df_ysl.iloc[i]['product_id'],
#                           brand=df_ysl.iloc[i]['brand'],
#                           looks=df_ysl.iloc[i]['looks'],
#                           color_code=df_ysl.iloc[i]['color_code'],
#                           color=df_ysl.iloc[i]['color']))        
#     return render_template("outputYsl.html",colors = colors, the_result = "As shown in the above table")

@app.route('/')
@app.route('/index')
# @app.route('/upload')
def upload_img():
    return render_template("file_upload.html")

# @app.route('/process',methods=['GET','POST'])
# def img_process():
#     # if request.method == 'POST':
#     f = request.files['file']
#     fname = f.filename
#     predictor_input = '/home/yafen/insight_project/Demos/shape_predictor_68_face_landmarks.dat'
#     bgr = lip_landmarks(predictor_input,fname)
#     return render_template("process.html", result = bgr, len_res = len(bgr))

@app.route('/match', methods=['GET','POST'])
def best_match():
     #pull 'birth_month' from input field and store it
    f = request.files['file']
    timestr = time.strftime("%Y%m%d-%H%M%S")
    fname = 'static/image/' + timestr
    f.save('flaskexample/'+fname)
    predictor_input = '/home/yafen/insight_project/Demos/shape_predictor_68_face_landmarks.dat'
    lip_detection = lip_landmarks(predictor_input,'/home/yafen/insight_project/Demos/flaskexample/'+fname)
    try:
        bgr_vals = np.reshape(np.array(lip_detection,dtype='float32'),(1,-1))
    # bgr_txt = request.args.get('result')
    # bgr_vals = np.reshape(np.array([float(e) for e in bgr_txt.split(',')],dtype='float32'),(1,-1))
   #just select the Cesareans  from the birth dtabase for the month that the user inputs
        query = "SELECT brand,price,looks,color_code,color_img_url,product_img_url,product_url,bgr_mean FROM lipsticks_bgr_table;"
        query_results=pd.read_sql_query(query,db)
    # print(query_results)
        df_sephora = ColorID(query_results, bgr_vals)
        results = []
        try:
            for i in range(0,df_sephora.shape[0]):
                results.append(dict(brand=df_sephora.iloc[i]['brand'],
                                  looks=df_sephora.iloc[i]['looks'],
                                  color_code=df_sephora.iloc[i]['color_code'],
                                  color_img=df_sephora.iloc[i]['color_img_url'],
                                  product_img=df_sephora.iloc[i]['product_img_url'],
                                  price=df_sephora.iloc[i]['price'],
                                  color_distance=df_sephora.iloc[i]['color_distance'],
                                  product = df_sephora.iloc[i]['product_url']))
        except:
            results = df_sephora
    except:
        results = lip_detection
    return render_template("match.html",results = results, len_res = len(results), filename=fname)