from flask import Flask, render_template

app = Flask(__name__)

products = [
    {
        "name": "Vịt quay Lạng Sơn",
        "price": "350.000đ",
        "image": "/static/image/1.jfif",
        "desc": "Vịt quay lá móc mật thơm ngon đặc trưng"
    },
    {
        "name": "Na Chi Lăng",
        "price": "80.000đ/kg",
        "image": "/static/image/2.jfif",
        "desc": "Na ngọt, thơm, đặc sản nổi tiếng"
    },
    {
        "name": "Măng ớt Lạng Sơn",
        "price": "50.000đ/hũ",
        "image": "/static/image/3.jfif",
        "desc": "Măng cay giòn, ăn cực bắt cơm"
    }
]

news = [
    {
        "title": "Na Chi Lăng vào mùa thu hoạch",
        "image": "/static/image/4.jfif",
        "content": "Năm nay na Chi Lăng được mùa, chất lượng cao..."
    },
    {
        "title": "Đặc sản Lạng Sơn hút khách",
        "image": "/static/image/5.jfif",
        "content": "Nhiều đặc sản vùng cao đang được ưa chuộng..."
    }
]

@app.route("/")
def home():
    return render_template("index.html", products=products, news=news)

if __name__ == "__main__":
    app.run(debug=True)