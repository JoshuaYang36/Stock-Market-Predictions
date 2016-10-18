
import pandas as pd
import glob

def main():
	# Grabs all files in our input directory that ends in .csv
	input_directory = import_csv()
	
	# Initialize a black DataFrame
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