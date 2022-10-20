import torch
import googletrans
from googletrans import Translator


from flask import Flask,render_template,url_for
from flask import request as req


def translate_hindi(url_content):
    translator = Translator()
    result = translator.translate(url_content, dest='hi')
    return (result.text)
def translate_english(url_content):
    translator = Translator()
    result = translator.translate(url_content, dest='en')
    return (result.text)
def translate_telegu(url_content):
    translator = Translator()
    result = translator.translate(url_content, dest='te')
    return (result.text)





app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    if req.method == "POST":
        url_content = req.form.get("url")       
        translate_text1=translate_hindi(url_content)
        translate_text2=translate_english(url_content)
        translate_text3=translate_telegu(url_content)      
        return render_template("index.html",value1=translate_text1,value2=translate_text2,value3=translate_text3)
        
    return render_template("main1.html")

if __name__ == "__main__":
    app.run(debug=True)