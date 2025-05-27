from src.data_loader import fetch_weather_data
from src.data_cleaner import clean_weather_data
from src.analyzer import plot_temperature
from src.data_loader import fetch_weather_data
from src.data_cleaner import clean_weather_data
from src.feature_engineering import engineer_features, select_features
from src.analyzer import plot_temperature
from src.data_loader import fetch_weather_data
from src.data_cleaner import clean_weather_data
from src.feature_engineering import engineer_features, select_features
from src.statistics import summarize_statistics, generate_insights, missing_data_report
from src.analyzer import plot_temperature
from src.data_loader import fetch_weather_data
from src.data_cleaner import clean_weather_data
from src.feature_engineering import engineer_features
from src.statistics import summarize_statistics, generate_insights
from src.pattern_analysis import detect_trends, detect_anomalies, identify_seasonal_patterns, plot_trend_and_anomalies
from src.analyzer import plot_temperature
from src.data_transformer import remove_outliers_iqr, log_transform, standardize

# Remove outliers
featured = remove_outliers_iqr(featured, column='tavg')

# Optional: log-transform and standardize
featured = log_transform(featured, column='tavg')
featured = standardize(featured, column='tavg')

# Load and process
raw_data = fetch_weather_data("New York", "2023-01-01", "2023-12-31")
cleaned = clean_weather_data(raw_data)
featured = engineer_features(cleaned)

# Statistics
summarize_statistics(featured)
generate_insights(featured)

# Trend & Pattern Analysis
featured = detect_trends(featured, column='tavg', window=30)
seasonal = identify_seasonal_patterns(featured)
featured = detect_anomalies(featured, column='tavg', threshold=2.0)

# Plot
plot_trend_and_anomalies(featured, column='tavg')


# Load data
raw_data = fetch_weather_data(location_name="New York", start="2023-01-01", end="2023-12-31")

# Clean
cleaned_data = clean_weather_data(raw_data)

# Feature Engineering
featured_data = engineer_features(cleaned_data)

# Summary & Insights
missing_data_report(featured_data)
summary = summarize_statistics(featured_data)
insights = generate_insights(featured_data)

# Visualization
plot_temperature(featured_data, location="New York")

# Load
raw_data = fetch_weather_data(location_name="New York", start="2023-01-01", end="2023-12-31")

# Clean
cleaned_data = clean_weather_data(raw_data)

# Engineer Features with integrity checks
featured_data = engineer_features(cleaned_data)

# Select subset of features
selected_data = select_features(featured_data, feature_list=[
    'time', 'tavg', 'tavg_rolling_7', 'temp_range', 'month', 'is_weekend'
])

# Visualize
plot_temperature(selected_data, location="New York")


# Step 1: Load raw data
raw_data = fetch_weather_data(location_name="New York", start="2023-01-01", end="2023-12-31")

# Step 2: Clean
cleaned_data = clean_weather_data(raw_data, method='interpolate')

# Step 3: Feature Engineering
featured_data = engineer_features(cleaned_data)

# Step 4: Feature Selection (optional)
selected_data = select_features(featured_data, feature_list=[
    'time', 'tavg', 'tavg_rolling_7', 'temp_range', 'month', 'dayofweek', 'is_weekend'
])

# Step 5: Plot
plot_temperature(selected_data, location="New York")


# Load raw data
raw_data = fetch_weather_data(location_name="New York", start="2023-01-01", end="2023-12-31")

# Clean using interpolation method
cleaned_data = clean_weather_data(raw_data, method='interpolate')

# Analyze
plot_temperature(cleaned_data, location="New York")

# Step 1: Load
raw_data = fetch_weather_data(location_name="New York", start="2023-01-01", end="2023-12-31")

# Step 2: Clean
cleaned_data = clean_weather_data(raw_data)

# Step 3: Analyze
plot_temperature(cleaned_data, location="New York")
summary.to_csv("data/statistics_summary.csv")
with open("data/insights.txt", "w") as f:
    for line in insights:
        f.write(line + "\n")

from src.initial_visuals import (
    plot_temperature_distribution,
    plot_monthly_avg_temperature,
    plot_temp_trend,
    plot_anomalies
)

# Initial Visualizations
plot_temperature_distribution(featured)
plot_monthly_avg_temperature(featured)
plot_temp_trend(featured)
plot_anomalies(featured)
