from utils.mongo_helper import MongoHelper
import pandas as pd
from seed_api_project.settings import BASE_DIR

def initial_seed_collection():
    mongoHelper = MongoHelper()
    try:
        df = pd.read_csv("{app_path}/initial_data_files/seed_data.csv".format(app_path = BASE_DIR))
        data = []
        for index, row in df.iterrows():
            if(
                not pd.isnull(row["_id"]) and
                not pd.isnull(row["Seed_RepDate"]) and
                not pd.isnull(row["Seed_Year"]) and
                not pd.isnull(row["Seeds_YearWeek"]) and
                not pd.isnull(row["Seed_Varity"]) and
                not pd.isnull(row["Seed_RDCSD"]) and
                not pd.isnull(row["Seed_Stock2Sale"]) and
                not pd.isnull(row["Seed_Season"]) and
                not pd.isnull(row["Seed_Crop_Year"])
                ):

                data.append(
                    {
                        "_id": row["_id"],
                        "Seed_RepDate": row["Seed_RepDate"],
                        "Seed_Year": row["Seed_Year"],
                        "Seeds_YearWeek": row["Seeds_YearWeek"],
                        "Seed_Varity": row["Seed_Varity"],
                        "Seed_RDCSD": row["Seed_RDCSD"],
                        "Seed_Stock2Sale": int(row["Seed_Stock2Sale"].replace(',', '')),
                        "Seed_Season": row["Seed_Season"],
                        "Seed_Crop_Year": row["Seed_Crop_Year"]
                    }
                )
        result = mongoHelper.getCollection("seed").find()
        if len(list(result)) == 0:
            mongoHelper.getCollection("seed").insert_many(data)
            print("=============== initial_seed_collection.py ===============\n")
            print("initial_seed_collection.py : insert seed data successfully.\n")
            print("=============== initial_seed_collection.py ===============\n")
        mongoHelper.closeConnection()
        print("=============== initial_seed_collection.py ===============\n")
        print("initial_seed_collection.py : seed data already exists.\n")
        print("=============== initial_seed_collection.py ===============\n")
    except Exception as error:
        mongoHelper.closeConnection()
        raise error
    
    
    


