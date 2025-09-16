from flask import Flask, render_template, request
import statistics as st

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    if request.method == "POST":
        try:
            data_str = request.form["angka"]
            data = [float(x) for x in data_str.split()]

            hasil = {
                "mean": round(st.mean(data), 2),
                "median": round(st.median(data), 2),
                "modus": round(st.mode(data), 2),
                "max": round(max(data), 2),
                "min": round(min(data), 2),
                "range": round(max(data) - min(data), 2),
                "stdev": round(st.stdev(data), 2)
            }
        except Exception as e:
            hasil = {"error": f"Terjadi kesalahan: {e}"}
    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
