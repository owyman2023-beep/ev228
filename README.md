# ev228
Individual Repository

“Generative AI was not used in this code"

Individual Group Project 
For this project I decided to look at snowfall data in Colorado to see how past years compared to modern data and historical averages. As an avid skier/snow sport enthusiast this was very interesting topic that I enjoyed looking into and creating a useful code that I can plug in any month I want to see how much snowfall it got at that time as it compares to the average for the location. 

Work flow: 
The main code used in this project is the snow_graphs.py code in this repository and fun_import.py and fun_plots.py are used aswell as refered functions. The code fun_import.py is used to import the gridded era5 land data set from my folder to the main code, snow_graph.py. The main code takes the imported era5 land data set of the snow depth (m) in Colorado from 1950 - 2025, it calculates the mean, standard deviation, and then z-score of the data from which ever month is selected by the user. The user can select which ever month they would like to see (1950-present and only months 01-03 for each year and only first day of each month). The code will display the z-score of the snow depth in the entire state of Colorado for the selected month ploting using the cartopy import package. The code will also print the mean z-score for that year and tell how that month compares to others generally. 














Practical 4 Work Flow to run code:
In data_imputs.py file, replace the inputs in the fpd.process_data function. Download the csv file to ev228_data folder and copy the file while in that location to get full file path. Rplace the first input as a string of the file path and confirm the output1 and output2 strings are acurate to the columns in the data. Save and run python data_imputs.py in terminal to see the graph of the weather data. 


