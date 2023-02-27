from flask import Flask
from insurancepre.logger import logging
import sys
from insurancepre.exception import InsuranceException

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        insurance=InsuranceException(e,sys)
        logging.info(insurance.error_message)    
        logging.info("we are testing logging module")
    return "CI CD PIPELINE has been established"

if __name__ == '__main__':
    app.run(debug=True)