# Hack4Sodertalje

## Problem statement
Climate change is **real**. There is not better way in saying this. These days, we witness the (some) effects of fast changing climates as rising sea levels, extreme winters, frequent heat waves across many cities in the world. Effect of the heat waves is adverse especially among vulnerable population groups living in urban settings. Mortality rates, in these groups, is on the rise due to **lack of awareness** and **prepardness** towards extreme weather occurances.

In Sweden, heat waves generally occured once in every 20 years. But, this new millenium has given us a new climate challenge where it has occured 4 times since 2000. As suggested by the Swedish researchers from Umea extended hot days of 27 degree - 30 degrees for 3 consecutive days will increase the mortality and cardiovascular health risk by 10 and 20 %, respectively[1]. Research suggests that effects of climate change will increase the occurance of heat waves and no. of consecutive hot days during summer. This in turn will affect the elderly and people with cardiovascular health conditions. 

## Our Hack - Sodertalje's Heat Wave Alert System
Our hack is a two-fold solution. 

To understand our hack, one should first have a clear idea on how temperatures are calculated in a city. National climate centers generally install a sophisticated thermometer unit at a select location, usually near airport in bigger cities, to gather daily mean temperature readings. These readings don't consider the influence of surrounding structures on the temperature at that location and it will be that much difficult to predict the actual temperature impact at a discrete street level. 

For example, in the picture below, one can see 3 different temperature readings in different locations in a city. This indicates that the problems needs to be tackled at a much more discrete/granular level, for which, we don't have the technological architecture at this moment. 

![Temperature changes are more granular](./photos-of-current-seats/UMD-heat+slide.png)


During the first stage of the hack, we propose to collect granular (street-level) temperature data using any of the following methods to identify hot-spots at a granular street level. 
1. Use satellite data to get granular (street-level) temperature data. 
2. Install temperature sensors at different streets (this solution might not be cost-effecient)
3. Distributed temperature collection using mobile phones (Some of current Mobile phones are equipped with temperature sensors)

Second half of our hack deals with identifying locations across Sodertalje municipality that could potentially serve as **cool-down** spots. Identifying these "cool-down" spots across a city without hugely modifying the current state infrastructure is the core idea of our solution. We identify and define **cool-down** spots in as:
1. Concrete-shaded regions 
2. Green-shaded regions 
3. Public air-conditioned or bath spaces

Finally, we bring everything together via:  
* An **alert** system to forecast severness of hot weather at a street-level granularity based on temperature data collected. 
* A location-based **messaging** system to suggest nearby "cool-down" spots.


## Data Sources
A multitude of data sources have been gathered for our hack. 
1. [Survey Results from Senior Population](./data/survey-results)
2. [Historical Temperature changes](./data/stockholm-historical-temps-monthly-3)
3. [Demographics of the City](./data/demographics-data)
4. [Bath places in the City](./data/bath-places)
5. [Green spaces in the City](./data/green-spaces-geojson-data)
6.  


## Workflow - The Data Pipeline


## What data says?



## Outcome of the Hack


## Reference
[1] https://doi.org/10.1016/j.maturitas.2011.03.008
[2] https://www.vox.com/22557563/how-to-redesign-cities-for-heat-waves-climate-change

