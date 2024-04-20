from flask import Flask
app = Flask(__name__)
@app.route('/')
def welcome():
    return ("Welcome to long term internship in smartinternz in apsche")
@app.route('/longterm')
def second_fun():
    return("I am intresting to learn and improve my skills in ARTIFICIAL INTELLIGENCE & MACHINE LEARNING")
@app.route('/End')
def end():
    return("complete the internshi and gain a cerificate")
if __name__ == '__main__':
    app.run()




