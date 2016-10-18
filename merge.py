#-----------------------------------------------------------------------#
# Application: Grabs csvs from local directory, merges them, and export # 
#			   to out.csv.  											#
#																		#
# Versions:  Python 3.5													#
#			 Anaconda for Python 3.5									#
#																		#									
# Libraries: Pandas														#
#		     Glob														#
#																		#
# Functions: main() - Calls all other functions in order				#
#			 import_csv() - Grabs all files in our input directory that # 
#							ends in .csv 								#
#			 export_csv() - Export merged files to csv 					#
#			 merge_csvs() - Merges individual files into DataFrame		#
#																		#
#-----------------------------------------------------------------------#

import pandas as pd
import numpy as np
import glob


def main():
	# Grabs all files in our input directory that ends in .csv
	input_directory = import_csv()
	
	# Initialize a black DataFrame
	#columns = pd.Index(['Date','Time','Open','High','Low','Close','NA'])
	all_data = pd.DataFrame()

	# Appended all the individual files into the all_data Frame
	merged = merge_csvs(all_data, input_directory)

	export_csv(merged)

	return


def merge_csvs(all_data, input_directory):
	# Appended all the individual files into the all_data Frame

	for f in input_directory:
		df = pd.read_csv(f)
		all_data = all_data.append(df,ignore_index=True)
		print(f)

	return all_data


def import_csv():
	# Grabs all files in our input directory that ends in .csv
	return glob.glob("*.csv")

def export_csv(merged):
	#Export merged files to csv
	merged.to_csv('out.csv')
	return




if __name__ == "__main__":
	main();