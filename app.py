from flask import Flask, render_template

app = Flask(__name__)

JOBS =[
  {
    'id':1,
    'title':'data analyst',
    'location':'bengaluru India',
    'salary':'Rs. 1,00,000'
    
  },
  {
  'id':2,
    'title':'data scientist',
    'location':'bengaluru India',
    'salary':'Rs. 15,00,000'
    
  },
  {
  'id':3,
    'title':'frontend engineer',
    'location':'remote',
    'salary':'Rs. 12,00,000'
  },
  {
    {
  'id':4,
    'title':'backend engineer',
    'location':'san francisco,USA',
    'salary':'$12,00,000'
    } 
  }
  
  
  
  
  
  
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
