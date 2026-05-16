from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Vịt quay Lạng Sơn",
        "price": "350.000đ",
        "image": "/static/image/1.jfif",
        "desc": "Vịt quay lá móc mật thơm ngon đặc trưng, lớp da giòn rụm, thịt mềm ngọt thấm đẫm gia vị núi rừng."
    },
    {
        "id": 2,
        "name": "Na Chi Lăng",
        "price": "80.000đ/kg",
        "image": "/static/image/2.jfif",
        "desc": "Na Chi Lăng nổi tiếng với vị ngọt thanh, thơm đặc trưng, quả to đều, cùi dày và ít hạt."
    },
    {
        "id": 3,
        "name": "Măng ớt Lạng Sơn",
        "price": "50.000đ/hũ",
        "image": "/static/image/3.jfif",
        "desc": "Măng cay giòn, thơm mùi quả móc mật, ăn kèm với phở hoặc bún cực kỳ bắt cơm."
    }
]

news = [
    {
        "id": 1,
        "title": "Na Chi Lăng vào mùa thu hoạch",
        "image": "/static/image/4.jfif",
        "content": "Năm nay na Chi Lăng được mùa, chất lượng cao, thu hút đông đảo thương lái và khách du lịch. Đặc biệt, na năm nay có độ ngọt đậm, quả đều và đẹp hơn mọi năm. Chính quyền địa phương đang đẩy mạnh xúc tiến thương mại để đưa sản phẩm vươn xa hơn.",
        "date": "15/05/2024"
    },
    {
        "id": 2,
        "title": "Đặc sản Lạng Sơn hút khách",
        "image": "/static/image/5.jfif",
        "content": "Nhiều đặc sản vùng cao như vịt quay, phở vịt đang trở thành thương hiệu nổi tiếng cả nước. Lượng khách du lịch đến với Lạng Sơn tăng mạnh trong dịp hè này, phần lớn là để thưởng thức những món ăn đặc trưng của vùng đất Xứ Lạng.",
        "date": "10/05/2024"
    }
]

@app.route("/")
def home():
    return render_template("index.html", products=products, news=news)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template("product_detail.html", product=product)
    return "Sản phẩm không tồn tại", 404

@app.route("/news/<int:news_id>")
def news_detail(news_id):
    item = next((n for n in news if n["id"] == news_id), None)
    if item:
        return render_template("news_detail.html", news=item)
    return "Bài viết không tồn tại", 404

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        new_id = max(p["id"] for p in products) + 1 if products else 1
        new_product = {
            "id": new_id,
            "name": request.form.get("name"),
            "price": request.form.get("price"),
            "image": request.form.get("image"),
            "desc": request.form.get("desc")
        }
        products.append(new_product)
        return redirect(url_for("home"))
    return render_template("add_product.html")

if __name__ == "__main__":
    app.run(debug=True)