from flask import Flask, render_template,request
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(result):
    email = result["email"]
    subject = result["subject"]
    message = result["message"]
    with open('database.txt', mode='a') as file:
        file.write(f'\n{email},{subject},{message}')

def write_to_csvfile(result):
    email = result["email"]
    subject = result["subject"]
    message = result["message"]
    with open('database.csv', newline = '', mode='a') as csvfile:
        reader = csv.writer(csvfile, delimiter = ',', quotechar= '"')
        reader.writerow([email,subject,message])


@app.route('/submit_form',methods = ['POST', 'GET'])
def submit_form():
   if request.method == 'POST':
      result = request.form.to_dict()
      write_to_csvfile(result)
      return render_template("thankyou.html")
if __name__ == '__main__':
   app.run()