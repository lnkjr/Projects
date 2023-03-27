ETL Script Using Python and Prefect
=================================================

[Description]
=================================================
*Disclaimer: This project is from Datatalks Club Youtube channel.

- web_to_gcs.py allows users to download datasets from New York Taxi and Limousine Commission Website. The script is mainly for gathering Taxi Trips only. Users are required to specify the color of the taxi('yellow' or 'green'), month, and year of the data they want to access.

Here's the flow of the script: 

- Reads the file using pandas and store it as a pandas DataFrame;
- Cleans the data by changing the data type of the 'lpep_dropoff_datetime' & 'lpep_pickup_datetime' columns into pandas datetime format and displays the data type of columns for checking;
- Writes the data frame locally into a folder as a parquet file;
- Stores the parquet file into Google Cloud Storage / Bucket



[Getting Started]
=================================================

- To use this script, you'll need to make sure that the required libraries are installed on your system. You can do this by running the following command in your terminal:

			`pip install -r requirements.txt`

- Before running the script, you need to start a local instance of the Prefect flow orchestration server called Orion. This will provide you with a URL that redirects to the Prefect dashboard. To start the instance, run the following command:

			`prefect orion start`

- You also need to create a folder named 'data' within the same directory as the script. Inside the data folder create a folder named either 'green' or 'yellow'



[Usage]
=================================================

- Clone or download the project
- Open your terminal and navigate to the directory containing web_to_gcs.py
- Make sure that the required libraries are installed
- You need to create a Prefect Block on the Prefect dashboard through the URL provided
- Modify the values of the parameters 'color', 'months', and 'year' to the specifications of the file you wish to download.
- Run the web_to_gcs.py script by following the command:

			`python web_to_gcs.py`

- After running the script, you may check your Google Cloud Storage if the script successfuly loaded the file.



[Limitations and Possible Future Improvements]
=================================================

- The script is currently designed to work only with the New York Taxi and Limousine Commission website. It may not work with other similar websites or sources of data.
- The script only allows users to download data for a specific taxi color, month, and year. Users may not be able to download other data from the website using the script
- The script assumes that the user has access to a Google Cloud Storage account and has set up the necessary credentials and configurations.

- Use argparse or click to create a command-line interface that allows users to input the parameters (color, month, and year) without modifying the code. This makes it more user-friendly and easier to automate.
- Add error handling
- ETC

