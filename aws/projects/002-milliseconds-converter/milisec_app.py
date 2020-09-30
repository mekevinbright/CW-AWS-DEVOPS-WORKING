from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', developer_name = 'E2075 Fatih Metin')

@app.route('/', methods=['GET', 'POST'])
def convertmili():
    if request.method == 'POST':
        ms = request.form['number']
        if not ms.isdigit():
            return render_template('index.html', developer_name = 'E2075 Fatih Metin', not_valid = True)
        elif ms.isdigit():
            ms = int(request.form['number'])
            result = ""
            saat = ms // 3600000
            if saat != 0:
                result += str(saat) + " hour/s " 
            dakika = (ms // 60000) % 60
            if dakika != 0:
                result += str(dakika) + " minute/s " 
            saniye = (ms // 1000) % 60
            if saniye != 0:
                result += str(saniye) + " second/s " 
            if result == "":
                result = "Just " + str(ms) + " miliseconds"
            return render_template('result.html', developer_name = 'E2075 Fatih Metin', milliseconds = ms, result = result)

      
    
if __name__ == "__main__":
    # app.run(debug = True)

    app.run(host='0.0.0.0', port=80)