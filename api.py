from flask import Flask, render_template, request
import positional
import BST
import hashs
import inverted

app = Flask(__name__)


@app.route('/')  # อยากเอา direct ไว้ path ไหน
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST', 'GET'])  # POST = ส่งค่าผ่านทาง form
def result():
    # GET = ส่งค่ามาโดยตรง ผ่านทาง url
    if request.method == "POST":  # ส่งข้อมูลจากฟอร์มไปยัง Script โดยตรง
        re = {}
        re['Error'] = "Not Found"
        result = request.form['text']
        if(len(result) == 0):
            return render_template("layout.html", result=re)
        # return from geturl in positional.py
        Po = positional.Searching(result)
        Inv = inverted.search(result)
        bbst = BST.result(result)
        ha = hashs.result(result)
        return render_template("layout.html", po=Po, result=result, resultin=set(Inv), result2=bbst, result3=ha)


@app.route('/result/positional/', methods=['POST', 'GET'])
def invertedIndex(result):
    result = result
    results = inverted.search(result)
    print(result)
    return render_template('InvertedIndex.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
