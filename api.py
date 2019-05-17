from flask import Flask, render_template, request
import positional
import BST
import hashs
import inverted
import main
import time
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
            return render_template("notfound.html", error=re['Error'])
    Ranking = main.wildcard(result)
    return render_template("layout.html", result=result, Ranking=Ranking)


@app.route('/result/InvertedIndex/<result>', methods=['POST', 'GET'])
def InvertedIndex(result):
    start = time.time()
    result = result
    inv = inverted.search(result)
    print(result)
    totaltime = time.time()-start
    return render_template('InvertedIndex.html', result=result, inv=set(inv), time=totaltime)


@app.route('/result/positional/<result>', methods=['POST', 'GET'])
def positionalindex(result):
    start = time.time()
    result = result
    pos = positional.Searching(result)
    print(result)
    totaltime = time.time()-start
    return render_template('positional.html', result=result, positional=pos, time=totaltime)


@app.route('/result/hash/<result>', methods=['POST', 'GET'])
def geturlHash(result):
    start = time.time()
    result = result
    has = hashs.result(result)
    print(result)
    totaltime = time.time()-start
    return render_template('hash.html', result=result, has=has, time=totaltime)


@app.route('/result/binarysearchtree/<result>', methods=['POST', 'GET'])
def geturlTree(result):
    start = time.time()
    result = result
    bst = BST.result(result)
    print(result)
    totaltime = time.time()-start
    return render_template('binarysearchtree.html', result=result, bst=bst, time=totaltime)


if __name__ == "__main__":
    app.run(debug=True)
