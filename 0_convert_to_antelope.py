from obspy.core import read, UTCDateTime
from obspy.core.util.attribdict import AttribDict
import numpy as np 
import os
import glob
import datetime
import argparse


def format_file_name(var1, var2):

    if os.path.exists(var1) and os.path.exists(var2):
        print("The declared directory and input file exist....reading files and creating a list of data to be formated")
        
        node_code, head_id = np.loadtxt(var2, unpack=True, dtype='str', 
        			usecols=(0,1), skiprows=1)
        
        data_list = glob.glob(os.path.join(var1, "*miniseed"))
        
        if data_list:
            for i, waveform in enumerate(data_list):
            
                waveform_name = waveform.split("/")[1]
                head_id_field = waveform_name.split(".")[0]
                print(f"Working on: {waveform_name}")
                
                node_list = ['453027378', '453026348', '453027355', '453028059', '453027127', '453024936', '453025430', '453026874', '453026801']
                
                if head_id_field not in node_list:
                        lfn = np.nonzero(head_id == head_id_field)
                        node_field = node_code[lfn][0]
                        print(f"The head id: {head_id_field} corresponds with node id: {node_field}")
                        st = read(waveform)
                        tr = st[0]
                        tr.stats.station = node_field
                        tr.stats.network = "OV"
                        tr.stats.location = " "
                        if tr.stats.channel == "DPN":
                                tr.stats.channel = "HHN"
                        elif tr.stats.channel == "DPZ":
                                tr.stats.channel = "HHZ"
                        elif tr.stats.channel == "DPE":
                                tr.stats.channel = "HHE"
                        time  = tr.stats.starttime
                        year = time.year
                        month = str(time.month)
                        day = str(time.day)
                        day_of_year = time.julday
                        if len(month) == 1:
                                month = f"0{month}"
                        if len(day) == 1:
                                day = f"0{day}"
                        destino_final = f"{year}/{day_of_year}"
                        if not os.path.exists(destino_final):
                                os.makedirs(f"{destino_final}")
                        else:
                                print(f"destino final: {destino_final} already exists....saving files now!")
                        file_output_name = f"OV.{node_field}..{tr.stats.channel}.{year}.{month}.{day}.{day_of_year}.mseed"
                        print(f"The miniseed file: {waveform_name} ** is formatted with: {file_output_name}")
                        path_out = os.path.join(destino_final, file_output_name)
                        print(path_out)
                        tr.write(path_out, format='MSEED')
                

        else: 
            print("SmartSolo miniseed files not found....")

    else: 
        print("Please check data path, it does not exists in current directory....")
        

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Please add the input variables: -D for directory with miniseed data to be formated and -D with the service run node ids")
	parser.add_argument('-D', '--var1', type=str, required=True, help='Input directory where files are located')
	parser.add_argument('-F', '--var2', type=str, required=True, help='Input File with nodes Ids')
	
	args = parser.parse_args()
	format_file_name(args.var1, args.var2)
	

