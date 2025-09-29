import pickle
import pandas as pd


def main():
    #load model
    with open("final_project.pkl", "rb") as f:
        saved_data = pickle.load(f)

    model=saved_data["model"]
    gender_encoder=saved_data["gender_encoder"]
    part_time_encoder=saved_data["part_time_encoder"]
    extra_encoder=saved_data["extra_encoder"]
    ord_diet=saved_data["ord_diet"]
    ord_parent=saved_data["ord_parent"]
    ord_internet=saved_data["ord_internet"]


    X_test=pd.read_csv("testdata.csv")
    print(model.predict(X_test))

if __name__ == "__main__":
    main()