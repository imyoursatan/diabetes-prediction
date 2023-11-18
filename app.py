from flask import Flask, jsonify, request
import pickle
import joblib
import os
from flask_cors import CORS, cross_origin
import numpy as np
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

Scaler_Name = 'MinMaxScaler.save'
scaler = joblib.load(Scaler_Name)

Decision_Tree_Model = 'decision_tree_model_grid.save'
KNN_Model = 'knn_tuned.save'
Naive_Bayes_Model = 'naive_bayes_model_grid.save'

model_dt = joblib.load(Decision_Tree_Model)
model_knn = joblib.load(KNN_Model)
model_nb = joblib.load(Naive_Bayes_Model)

@app.route("/diabetes", methods=["GET"])
def predWine():

    if request.method == 'GET':

        a = float(request.args.get('Age'))
        b = float(request.args.get('BMI'))
        c = float(request.args.get('HighChol'))
        d = float(request.args.get('PhysHlth'))
        e = float(request.args.get('HighBP'))

        final_features = ([[a, b, c, d, e]])

        input_data_as_numpy_array = np.array(final_features)
        input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
        sample_scale = scaler.transform(input_data_reshape)
        print("final_features no scale: ", final_features)
        print("sample_scale : ", sample_scale)

        prediction_dt = model_dt.predict(sample_scale)
        prediction_knn = model_knn.predict(sample_scale)
        prediction_nb = model_nb.predict(sample_scale)

        proba_score_dt = model_dt.predict_proba(sample_scale)
        proba_score_knn = model_knn.predict_proba(sample_scale)
        proba_score_nb = model_nb.predict_proba(sample_scale)   

        print(prediction_dt[0])
        # prediction = model.predict(final_features)
    
        if prediction_dt[0] == 0:
            result_dt = str("Tidak Terkena Diabetes")
        if prediction_dt[0] == 1:
            result_dt = str("terkena Diabetes")

        if prediction_knn[0] == 0:
            result_knn = str("Tidak Terkena Diabetes")
        if prediction_knn[0] == 1:
            result_knn = str("terkena Diabetes")

        if prediction_nb[0] == 0:
            result_nb = str("Tidak Terkena Diabetes")
        if prediction_nb[0] == 1:
            result_nb = str("terkena Diabetes")

        response = {
            "prediction_result_dt": result_dt,
            "prediction_result_knn": result_knn,
            "prediction_result_nb": result_nb,

            "prediction_proba_dt": proba_score_dt.tolist(),  # Convert to list for JSON serialization
            "prediction_proba_knn": proba_score_knn.tolist(), 
            "prediction_proba_nb": proba_score_nb.tolist(), 

        }

        print("Hasil Prediksi Decision :", result_dt)
        print("Hasil Prediksi Decision :", result_knn)
        print("Hasil Prediksi Decision :", result_nb)

        return jsonify(response)


#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(debug=True)