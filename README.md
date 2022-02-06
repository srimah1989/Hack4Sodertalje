# Hack4Sodertalje

## Problem statement 
From elsewhere we know that extreme weather adversely affects vulnerable and excluded groups, while people with more available resources and better networks will do just fine. 

**Our focus here is the impact of heat waves on the vulnerable population**, though it can be applied to other extremes, such as extreme cold, extreme precipitation, extreme wind, smoke from forest fires and the like. 

The same groups are exposed: The sick, the elderly, the homeless, the poor. High energy prices this winter showed how, under wrong circumstances, the group of vulnerable people could grow larger than that. Södertälje is not a city characterised by extreme weather, nor will it be, but it is better prepared for some than for others. So let us turn up the heat.

This tool is designed for dual use, scenario planning and adverse weather information. Planners can correct weak spots ahead of time, while when the heat is here the affected (or their carers) can see how best to adapt. This goes for less extreme weather as well. Where others may feel a slight discomfort or even find it enjoyable, it will be a barrier for our groups from taking part in public life. This barrier can be reduced with some planning. 

It is an iterative tool, as it is used it will show which data sets are missing and motivate their owners to open these up. It is also intended to be used in other planning tools, for instance as an overlay. 



## Motivation


PREPAREDNESS (Visualisation and simulation)
* Based on this we should have analyse the improvements necessary to existing infrastructures in Sodertalje municipality to provide "cool-down" spots to it's residents. 
* Suggestions to increase resting spots under shades. 
* Public air conditioned spaces.
* Indoor activies on hot days to move from homes to air conditioned spaces. 
* Increasing public toilets and it's quality for people with difficutlies to feel welcomed on the city center (Instead of the current tin can in the middle of the city) 
* Temperature and details of bath places.

ALERT SYSTEM (Warning and information)
* Early warning systems from solid scientific basis to forecast severness of hot weather during summer. 
* Social media campigns to spread awareness of things to do on hot days.
* Mark places having heat island effects. 
* An info system on places to go on hots with temprature on bath places. (We have that data on open data) And systems to detect nearby "cool-down" spots.

## Our tool - Sodertalje's Heat Wave Alert System

(http://currents.plos.org/disasters/files/2013/10/Heatwave-levels-600x285.png)

Temperatures varies greatly in a city. For example, in the picture below, one can see 3 different temperature readings in different locations in a city. This indicates that the problems needs to be tackled at a much more discrete/granular level, for which, we don't have the technological architecture at this moment. 

![Temperature changes are more granular](./photos-of-current-seats/UMD-heat+slide.png)

During the first stage, we propose to collect granular (street-level) temperature data using any of the following methods to identify hot-spots at a granular street level. 
1. Use satellite data to get granular (street-level) temperature data. 
2. Install temperature sensors at different streets (this solution might not be cost-effecient)
3. Distributed temperature collection using mobile phones (Some of current Mobile phones are equipped with temperature sensors)

Second half of our hack deals with identifying locations across Sodertalje municipality that could potentially serve as **cool-down** spots. Identifying these "cool-down" spots across a city without hugely modifying the current state infrastructure is the core idea of our solution. We identify and define **cool-down** spots in as:
1. Concrete-shaded regions 
2. Green-shaded regions 
3. Public air-conditioned or bath spaces

[Eskilstuna 26 juli 2014](https://www.smhi.se/polopoly_fs/1.136268.1528803536!/image/str%C3%A5lningstemperatur_Eskilstuna.jpg_gen/derivatives/Original_542px/image/str%C3%A5lningstemperatur_Eskilstuna.jpg)

Finally, we bring everything together via:  
* An **alert** system to forecast severness of hot weather at a street-level granularity based on temperature data collected. 
* A location-based **messaging** system to suggest nearby "cool-down" spots.



## The Differential Engine (scenario simulation)
The tool will take both real time & predicted weather data, as well as simulated weather data. 

It can save snapshots of geographical data set to see urban climate of current environment compared with e.g. Södertälje 2022, or with proposed new features (e.g. turning a road into an allée, or the shades and reflections from a new building).

## The path of life
In addition to the location of cool-down spots and heat island, the tool can later evaluate available paths and their relative (dis)comfort, including for people with limited mobility. 

This includes distances between oases of rest, water, toilets, sheltered stops for public transport (we assume SL will in the future provide buses with air conditioning). 

## Building and population data
There is data on the buildings, their environmental classification, if not their heat resistance. Likewise we know where people are living, and within constraints of privacy their age and health status. Eventually the at-risk population can be simulated or contacted. 

## Useful data sets

* city map
* dynamic shade map: Solar studies based on Södertälje’s “virtual city” 3D map can show when and where public spaces will be in the sun and the solar intensity. This allows us to predict the ambient temperature at any public space at any time of day or year. When combined with heat photos and sensors (as described above) we will in addition to current temperatures, also be able to tell the causes of temperature differences. 
* weather forecast data
* map of vegetation
* public resting places
* public transport
* heat wave level 
* vulnerable population data
* building database
* accessible air conditioned public buildings
* public shelters, "ice boxes"


## Background and sources
Adverse effects of heat waves on mortality among vulnerable group of population are well known. Heat waves in Sweden used to occur once in every 20 years in the past century. But this new millenium has given us a new climate challenge where it has occured 4 times since 2000. As suggested by the Swedish researchers from Umea extended hot days of 27 degree - 30 degrees for 3 consecutive days will increase the mortality and cardiovascular health risk between 10 and 20% [1]. Research suggests that effects of climate change will increase the occurance of heat waves and consecutive hot days during summer. This in turn will affect the elderly and people with cardiovascular diseases. 


A multitude of data sources have been gathered for our hack. 
1. [Survey Results from Senior Population](./data/survey-results)
2. [Historical Temperature changes](./data/stockholm-historical-temps-monthly-3)
3. [Demographics of the City](./data/demographics-data)
4. [Bath places in the City](./data/bath-places)
5. [Green spaces in the City](./data/green-spaces-geojson-data)
6. [Svalkande miljöer viktiga när värmeböljor stressar svenska städer](https://www.smhi.se/forskning/forskningsnyheter/svalkande-miljoer-viktiga-nar-varmeboljor-stressar-svenska-stader-1.136119) 


## References
1. https://doi.org/10.1016/j.maturitas.2011.03.008
2. https://www.vox.com/22557563/how-to-redesign-cities-for-heat-waves-climate-change

