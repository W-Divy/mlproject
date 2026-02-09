import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        try:
            # Base directory (project root)
            self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

            self.model_path = os.path.join(self.base_dir, "artifacts", "model.pkl")
            self.preprocessor_path = os.path.join(self.base_dir, "artifacts", "preprocessor.pkl")

            # Load ONCE
            self.model = load_object(self.model_path)
            self.preprocessor = load_object(self.preprocessor_path)

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):
        try:
            data_scaled = self.preprocessor.transform(features)
            preds = self.model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int,
    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            return pd.DataFrame({
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            })

        except Exception as e:
            raise CustomException(e, sys)
