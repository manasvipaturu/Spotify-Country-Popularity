# Music Preferences Analysis

This project aims to analyze and compare music preferences in different countries using a dataset of top Spotify songs in 73 countries. Comparing the top songs in different countries helps identify cultural music preferences. The dataset is sourced from Kaggle and contains information about daily top songs, their features, and the countries they are popular in.

I am using Kernel Density Estimation (KDE) plots to compare the popularity of top songs in different countries. 

1. X-Axis represenatnst poplarity of songs, which is a metric that quantifies how well-recieved or frequently the song is streamed, so higher values on the x-axis represent more popularity. 

2. Y-Axis represents the song distribution which means it shows how songs are typcally distributed across the different levels of popularity in the countries. In other words, the y-axis is indicating how many songs fall within a particular range of popularity on the x-axis. A higher point on the curve means more songs have that level of popularity. 

`Here's the relationship between the x and y axes:`

As you move from left to right along the x-axis (from lower to higher popularity values), the y-axis shows the density or concentration of songs in that popularity range.
High points on the curve indicate that many songs are popular within that range, while low points indicate fewer songs in that range.
By comparing the curves for different countries, you can identify differences in music preferences. For example, a country with a higher curve peak for songs of medium popularity might indicate a preference for moderately popular songs, while a country with a broader, flatter curve might have a diverse taste in popular songs.
The KDE plots allow you to visually compare the distribution of song popularity in different countries, helping you identify cultural music preferences.

## Dataset Information

- **Dataset Source**: [Kaggle Dataset]([link-to-kaggle-dataset](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated/))
- **File Name**: `universal_top_spotify_songs.csv`
- **Data Description**: The dataset provides detailed information about top songs, including their popularity, energy, valence, and more. It also includes the country where each song is popular.

## Project Files

- `music_analysis.py`: This Python script loads the dataset and analyzes the popularity of top songs in different countries, creating visualizations to identify cultural music preferences.
- `universal_top_spotify_songs.csv`: The dataset file sourced from Kaggle.

## More Project Specifics
More information on how it works: 
Kernel Density Estimation (KDE) is a data visualization technique used to estimate the probability density function of a continuous random variable. In simpler terms, it helps you visualize how data points are distributed along a continuous axis, such as time, distance, or, in your case, song popularity.

KDE plots allow you to visualize how songs are distributed across different levels of popularity in various countries.
Peaks in the curve indicate popular ranges of song popularity, and valleys indicate less popular ranges.
By comparing the KDE plots for different countries, you can identify differences in music preferences. Countries with distinct peaks or shapes in their curves may have unique preferences for popular songs.

I used KDE plots because they are a powerful tool for exploring an comparing data distributions and are often used in data analysis and visualization to gain insights into the underlying patters in the data. 

## Usage

To replicate the analysis, follow these steps:

1. **Prerequisites**: Ensure you have Python (3.6 or higher) installed on your system.

2. **Install Required Libraries**: Install the necessary Python libraries using pip:
   `pip install pandas matplotlib seaborn`


3. **Download the Dataset**: Download the 'universal_top_spotify_songs.csv' dataset from the [Kaggle Dataset](link-to-kaggle-dataset) and place it in the same directory as `music_analysis.py`.

4. **Run the Analysis**:

- Open a terminal or command prompt.
- Navigate to the directory containing `music_analysis.py` and the dataset file.
- Run the analysis script using the following command:

  ```
  python music_analysis.py
  ```

5. **View Results**: The script will generate visualizations comparing song popularity in different countries. Open the generated plots to identify music preferences.

## License

This project is licensed under the [MIT License](LICENSE).



