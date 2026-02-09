from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Load model ONCE
predict_pipeline = PredictPipeline()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    try:
        if request.method == "GET":
            return render_template("home.html")

        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(request.form.get("reading_score", 0)),
            writing_score=float(request.form.get("writing_score", 0)),
        )

        pred_df = data.get_data_as_data_frame()
        results = predict_pipeline.predict(pred_df)

        return render_template("home.html", results=results[0])

    except Exception:
        import traceback
        traceback.print_exc()
        return render_template("home.html", error="Something went wrong during prediction")


if __name__ == "__main__":
    app.run()
