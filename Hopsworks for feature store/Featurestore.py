import pandas as pd
from hops import featurestore

# Connect to the feature store
featurestore.connect()

# Read the raw data
raw_data = pd.read_csv("air_quality_data_sa_2023_new.csv")

# Compute features and targets
# For example, let's say you want to use Temperature, Humidity, pm25, pm10, o3, no2 as features
features = raw_data[["Temperature", "Humidity", "pm25", "pm10", "o3", "no2"]]
targets = raw_data["AQI"]

# Define the name of the feature group
feature_group_name = "air_quality_features_2023"

# Define the schema for the feature group
schema = [
    ("Temperature", "float"),
    ("Humidity", "float"),
    ("pm25", "float"),
    ("pm10", "float"),
    ("o3", "float"),
    ("no2", "float"),
    ("AQI", "float")  # Assuming AQI is the target variable
]

# Create the feature group (if it doesn't already exist)
featurestore.create_featuregroup(
    feature_group_name,
    description="Feature group for air quality data and AQI targets in 2023",
    featuregroup_version=1,
    features_schema=schema
)

# Insert features into the feature group
featurestore.insert_into_featuregroup(
    features,
    feature_group_name,
    featurestore=featurestore.project_featurestore(),
    featuregroup_version=1
)

# Insert targets into the feature group
featurestore.insert_into_featuregroup(
    targets.to_frame(),  # Convert Series to DataFrame
    feature_group_name,
    featurestore=featurestore.project_featurestore(),
    featuregroup_version=1
)
