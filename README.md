![Alt Text](REFNOS_logo.png)

# REFNOS
Collection of python codes and scripts for processing miniseed files from SmartSolo IGU-16HR-3C. 

## First Steps:
For each service run, we extracted miniseed file using SoloLite. The format of the miniseed data is then adapted such that
the head id from the nodes is substituted by the station code, for instance, we moved from 45308192 to C001. Then, 
we add other variables like: Channel, year, month, day and julian day. 

The data is organized in directories with the next structure: [year/julian_day], as it is being prepared for Antelope databases. 
The conversion phase is handled by the python script: 0_convert_to_antelope.py. 

``python 0_convert_to_antelope.py -D [directory with data] -F [service run file] ``

![Daily Storage for Service Run 1 in Cartago, Costa Rica](Daily_Data_Storage.png)
