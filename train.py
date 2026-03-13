
import pandas as pd
from model import build_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def train_competition_model(train_df_path, valid_df_path):
    tr_df = pd.read_csv(train_df_path)
    # Logique simplifiée pour l'exemple script
    tr_gen = ImageDataGenerator(rescale=1/255).flow_from_dataframe(
        tr_df, x_col='Class Path', y_col='Class', target_size=(299, 299), batch_size=32)
    
    model = build_model()
    model.fit(tr_gen, epochs=3)
    model.save('brain_tumor_model.h5')
    return model
