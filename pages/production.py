import pickle
import pandas as pd


# MODEL
# ANN model

def predict_with_models(X_test, models):
    df_predictions = pd.DataFrame()

    for i in range(0, len(models)):
        predictions = models[i].predict(X_test)
        col_name = str(i)
        df_predictions[col_name] = predictions
    return df_predictions


def get_results(exercise_angina, oldpeak, chest_pain_type_asy, chest_pain_type_ata, st_slope_flat):
    # Oldpeak is a decimal number, the rest are 0 or 1.
    dataset = pd.DataFrame({
        'const': [1.0],
        'ExerciseAngina': [exercise_angina],
        'Oldpeak': [oldpeak],
        'ChestPainType_ASY': [chest_pain_type_asy],
        'ChestPainType_ATA': [chest_pain_type_ata],
        'ST_Slope_Flat': [st_slope_flat],
    })

    num_models = 6
    models = []

    for i in range(num_models):
        with open(f'models/model-{i}.pkl', 'rb') as file:
            model = pickle.load(file)
        models.append(model)

    df_predictions = predict_with_models(dataset, models)

    with open('models/model_stacked.pkl', 'rb') as file:
        model = pickle.load(file)

    predictions = model.predict(df_predictions)
    return predictions
