from flask import Flask

app = Flask("SuperScrapper")

@app.route("/") #decorator : @--
def home(): 
  return "Hello Welcom to mi cassa!"
# decorator 밑에는 반드시 함수가 와야한다.

@app.route("/<username>")
def contact(username): #def의 이름은 contact이 아니어도 상관 없다.
  return f"Hello {username} how are you doing"

app.run(host = "0.0.0.0")