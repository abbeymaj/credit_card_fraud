# Importing packages
from src.components.create_custom_data import CustomData
from src.pipelines.predict_pipeline import PredictPipeline
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin

# Instantiating the Flask application
app = Flask(__name__)
