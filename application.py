
from flask import json
from flask import Response
from flask_cors import CORS
from flask_api import FlaskAPI
import itertools
import pandas as pd
import re
import csv


app = Flask(__name__)

CORS(app)


@app.route('/matrix_item_logic/', methods=['GET'])
def extract():
values=[]
with open('Balloon.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}

        # print(mydict.values())
        col_list = ["description"]
        df = pd.read_csv("NDC.csv", usecols=col_list)
        found_word =0
        temp_lists = df.values.tolist()
        # print(temp_lists)
        for item in temp_lists:
            for j in item:
                print(j)
                for key,value in mydict.items():
                    val = value.split(",")
                    for v in val:
                        if re.findall(r"\b"+re.escape(v)+r"\b", j):
                            print(key,v)
    return jsonify()

if __name__ == '__main__':
   app.run(debug=True)
