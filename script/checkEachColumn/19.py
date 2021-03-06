from __future__ import print_function

import sys
from pyspark import SparkContext
from csv import reader

if __name__ =="__main__":
	if len(sys.argv)!=2:
		print("Usage: <file>",file=sys.stderr)
		exit(-1)
	sc=SparkContext()
	crime=sc.textFile(sys.argv[1]).mapPartitions(lambda x:reader(x))
	#we would exclude header when checking data-quality for each column
	def has_header(first_line):
		has_header=True
		if first_line[0]=='CMPLNT_NUM':
			has_header=True
		else:
			has_header=False
		return has_header
	header=crime.first()
	if has_header(header):
		crime=crime.filter(lambda row: row!=header)
	#column at index 15 (starting from 0) is LOC_OF_OCCUR_DESC
	dev=crime.map(lambda row: row[18])
	housing_list=['1010 EAST 178TH STREET','104-14 TAPSCOTT STREET','1162-1176 WASHINGTON AVENUE',
 '131 SAINT NICHOLAS AVENUE',
 '1471 WATSON AVENUE',
 '154 WEST 84TH STREET',
 '303 VERNON AVENUE',
 '335 EAST 111TH STREET',
 '344 EAST 28TH STREET',
 '45 ALLEN STREET',
 '572 WARREN STREET',
 '830 AMSTERDAM AVENUE',
 'ADAMS',
 'ALBANY',
 'ALBANY II',
 'AMSTERDAM',
 'AMSTERDAM ADDITION',
 'ARMSTRONG I',
 'ARMSTRONG II',
 'FHA REPOSSESSED HOUSES (GROUP IV)',
 'ASTORIA',
 'ATLANTIC TERMINAL SITE 4B',
 'AUDUBON',
 'BAILEY AVENUE-WEST 193RD STREET',
 'BAISLEY PARK',
 'BARUCH',
 'BARUCH HOUSES ADDITION',
 'BAY VIEW',
 'BAYCHESTER',
 'BEACH 41ST STREET-BEACH CHANNEL DRIVE',
 'BEDFORD-STUYVESANT REHAB',
 'BELMONT-SUTTER AREA',
 'BERRY',
 'BERRY STREET-SOUTH 9TH STREET',
 'BETANCES I',
 'BETANCES II',
 'BETANCES II, 13',
 'BETANCES II, 18',
 'BETANCES II, 9A',
 'BETANCES III',
 'BETANCES III, 13',
 'BETANCES III, 18',
 'BETANCES III, 9A',
 'BETANCES IV',
 'BETANCES V',
 'BETANCES VI',
 'BETHUNE GARDENS',
 'BLAND',
 'BORINQUEN PLAZA I',
 'BORINQUEN PLAZA II',
 'BOSTON ROAD PLAZA',
 'BOSTON SECOR',
 'BOULEVARD',
 'BOYNTON AVENUE REHAB',
 'BRACETTI PLAZA',
 'BREUKELEN',
 'BREVOORT',
 'BRONX RIVER',
 'BRONX RIVER ADDITION',
 'BROWN',
 'BROWNSVILLE',
 'BRYANT AVENUE-EAST 174TH STREET',
 'BUSHWICK',
 'BUSHWICK II (GROUPS A & C)',
 'BUSHWICK II (GROUPS B & D)',
 'BUSHWICK II CDA (GROUP E)',
 'BUTLER',
 'CAMPOS PLAZA II',
 'CAREY GARDENS',
 'CARLETON MANOR',
 'CARVER',
 'CASSIDY-LAFAYETTE',
 'CASTLE HILL',
 'CHELSEA',
 'CHELSEA ADDITION',
 'CLAREMONT PARKWAY-FRANKLIN AVENUE',
 'CLAREMONT REHAB (GROUP 2)',
 'CLAREMONT REHAB (GROUP 3)',
 'CLAREMONT REHAB (GROUP 4)',
 'CLAREMONT REHAB (GROUP 5)',
 'CLASON POINT GARDENS',
 'CLINTON',
 'COLLEGE AVENUE-EAST 165TH STREET',
 'CONEY ISLAND',
 'CONEY ISLAND I (SITE 1B)',
 'CONEY ISLAND I (SITE 8)',
 'CONEY ISLAND I (SITES 4 & 5)',
 'CONLON LIHFE TOWER',
 'COOPER PARK',
 'CORSI HOUSES',
 'CROWN HEIGHTS',
 'CYPRESS HILLS',
 'DAVIDSON',
 'DE HOSTOS APARTMENTS',
 'DOUGLASS ADDITION',
 'DOUGLASS',
 'DOUGLASS I',
 'DOUGLASS II',
 'DREW-HAMILTON',
 'DYCKMAN',
 'EAGLE AVENUE-EAST 163RD STREET',
 'EAST 152ND STREET-COURTLANDT AVENUE',
 'EAST 165TH STREET-BRYANT AVENUE',
 'EAST 173RD STREET-VYSE AVENUE',
 'EAST 180TH STREET-MONTEREY AVENUE',
 'EAST NEW YORK CITY LINE',
 'EAST RIVER',
 'EASTCHESTER GARDENS',
 'EDENWALD',
 'ELLIOTT',
 'FARRAGUT',
 'FENIMORE-LEFFERTS',
 'FHA REPOSSESSED HOUSES (GROUP I)',
 'FHA REPOSSESSED HOUSES (GROUP II)',
 'FHA REPOSSESSED HOUSES (GROUP III)',
 'FHA REPOSSESSED HOUSES (GROUP V)',
 'FHA REPOSSESSED HOUSES (GROUP VI)',
 'FHA REPOSSESSED HOUSES (GROUP VII)',
 'FHA REPOSSESSED HOUSES (GROUP VIII)',
 'FHA REPOSSESSED HOUSES (GROUP IX)',
 'FHA REPOSSESSED HOUSES (GROUP X)',
 'FIORENTINO PLAZA',
 'FIRST HOUSES',
 'FOREST',
 'FOREST HILLS COOP (108TH STREET-62ND DRIVE)',
 'FORT INDEPENDENCE STREET-HEATH AVENUE',
 'FORT WASHINGTON AVENUE REHAB',
 'FRANKLIN AVENUE I CONVENTIONAL',
 'FRANKLIN AVENUE II CONVENTIONAL',
 'FRANKLIN AVENUE III CONVENTIONAL',
 'FULTON',
 'GARVEY (GROUP A)',
 'GLEBE AVENUE-WESTCHESTER AVENUE',
 'GLENMORE PLAZA',
 'GLENWOOD',
 'GOMPERS',
 'GOWANUS',
 'GRAMPION',
 'GRANT',
 'GRAVESEND',
 'GUN HILL',
 'HABER',
 'HAMMEL',
 'HARBORVIEW TERRACE',
 'HARLEM RIVER',
 'HARLEM RIVER II',
 'HARRISON AVENUE REHAB (GROUP A)',
 'HARRISON AVENUE REHAB (GROUP B)',
 'HERNANDEZ',
 'HIGHBRIDGE GARDENS',
 'HIGHBRIDGE REHABS (ANDERSON AVENUE)',
 'HIGHBRIDGE REHABS (NELSON AVENUE)',
 'HOE AVENUE-EAST 173RD STREET',
 'HOLMES TOWERS',
 'HOPE GARDENS',
 'HOWARD',
 'HOWARD AVENUE',
 'HOWARD AVENUE-PARK PLACE',
 'HUGHES APARTMENTS',
 'HUNTS POINT AVENUE REHAB',
 'HYLAN',
 'INDEPENDENCE',
 'INGERSOLL',
 'INTERNATIONAL TOWER',
 'ISAACS',
 'JACKSON',
 'JEFFERSON',
 'JOHNSON',
 'KING TOWERS',
 'KINGSBOROUGH',
 'KINGSBOROUGH EXTENSION',
 'LA GUARDIA',
 'LA GUARDIA ADDITION',
 'LAFAYETTE',
 'LATIMER GARDENS',
 'LAVANBURG HOMES',
 'LEAVITT STREET-34TH AVENUE',
 'LEHMAN VILLAGE',
 'LENOX ROAD-ROCKAWAY PARKWAY',
 'LEXINGTON',
 'LINCOLN',
 'LINDEN',
 'LONG ISLAND BAPTIST HOUSES',
 'LONGFELLOW AVENUE REHAB',
 'LOW HOUSES',
 'LOWER EAST SIDE I INFILL',
 'LOWER EAST SIDE II',
 'LOWER EAST SIDE III',
 'LOWER EAST SIDE REHAB (GROUP 5)',
 'MANHATTANVILLE',
 'MANHATTANVILLE REHAB (GROUP 2)',
 'MANHATTANVILLE REHAB (GROUP 3)',
 'MARBLE HILL',
 'MARCY',
 'MARCY AVENUE-GREENE AVENUE SITE A',
 'MARCY AVENUE-GREENE AVENUE SITE B',
 "MARINER'S HARBOR",
 'MARLBORO',
 'MARSHALL PLAZA',
 'MCKINLEY',
 'MELROSE',
 'MELTZER TOWER',
 'METRO NORTH PLAZA',
 'MIDDLETOWN PLAZA',
 'MILL BROOK',
 'MILL BROOK EXTENSION',
 'MITCHEL',
 'MONROE',
 'MOORE',
 'MORRIS I',
 'MORRIS II',
 'MORRIS PARK SENIOR CITIZENS HOME',
 'MORRISANIA',
 'MORRISANIA AIR RIGHTS',
 'MOTT HAVEN',
 'MURPHY',
 'NEW LANE AREA',
 'NOSTRAND',
 'OCEAN BAY APARTMENTS (BAYSIDE)',
 'OCEAN BAY APARTMENTS (OCEANSIDE)',
 'OCEAN HILL APARTMENTS',
 'OCEAN HILL-BROWNSVILLE',
 "O'DWYER GARDENS",
 'PALMETTO GARDENS',
 'PARK AVENUE-EAST 122ND, 123RD STREETS',
 'PARK ROCK REHAB',
 'PARKSIDE',
 'PATTERSON',
 'PELHAM PARKWAY',
 'PENNSYLVANIA AVENUE-WORTMAN AVENUE',
 'PINK',
 'POLO GROUNDS TOWERS',
 'POMONOK',
 'PSS GRANDPARENT FAMILY APARTMENTS',
 'PUBLIC SCHOOL 139 (CONVERSION)',
 'QUEENSBRIDGE NORTH',
 'QUEENSBRIDGE SOUTH',
 'RALPH AVENUE REHAB',
 'RANDALL AVENUE-BALCOM AVENUE',
 'RANDOLPH',
 'RANGEL',
 'RAVENSWOOD',
 'RED HOOK I',
 'RED HOOK II',
 'RED HOOK EAST',
 'RED HOOK WEST',
 'REDFERN',
 'REHAB PROGRAM (COLLEGE POINT)',
 'REHAB PROGRAM (DOUGLASS REHABS)',
 'REHAB PROGRAM (TAFT REHABS)',
 'REHAB PROGRAM (WISE REHAB)',
 'REID APARTMENTS',
 'RICHMOND TERRACE',
 'RIIS',
 'RIIS II',
 'ROBBINS PLAZA',
 'ROBINSON',
 'ROOSEVELT I',
 'ROOSEVELT II',
 'RUTGERS',
 'RUTLAND TOWERS',
 'SACK WERN',
 "SAINT MARY'S PARK",
 'SAINT NICHOLAS',
 'SAMUEL (CITY)',
 'SAMUEL (MHOP) I',
 'SAMUEL (MHOP) II',
 'SAMUEL (MHOP) III',
 'SARATOGA VILLAGE',
 'SEDGWICK',
 'SEWARD PARK EXTENSION',
 'SHEEPSHEAD BAY',
 'SHELTON HOUSE',
 'SMITH',
 'SOTOMAYOR HOUSES',
 'SOUNDVIEW',
 'SOUTH BEACH',
 'SOUTH BRONX AREA (SITE 402)',
 'SOUTH JAMAICA I',
 'SOUTH JAMAICA II',
 'STANTON STREET',
 'STAPLETON',
 'STEBBINS AVENUE-HEWITT PLACE',
 'STERLING PLACE REHABS (SAINT JOHNS-STERLING)',
 'STERLING PLACE REHABS (STERLING-BUFFALO)',
 'STRAUS',
 'STUYVESANT GARDENS I',
 'STUYVESANT GARDENS II',
 'SUMNER',
 'SURFSIDE GARDENS',
 'SUTTER AVENUE-UNION STREET',
 'TAFT',
 'TAPSCOTT STREET REHAB',
 'TAYLOR STREET-WYTHE AVENUE',
 'TELLER AVENUE-EAST 166TH STREET',
 'THOMAS APARTMENTS',
 'THROGGS NECK',
 'THROGGS NECK ADDITION',
 'TILDEN',
 'TODT HILL',
 'TOMPKINS',
 'TWIN PARKS EAST (SITE 9)',
 'TWIN PARKS WEST (SITES 1 & 2)',
 'TWO BRIDGES URA (SITE 7)',
 'UNION AVENUE-EAST 163RD STREET',
 'UNION AVENUE-EAST 166TH STREET',
 'UNITY PLAZA (SITES 17,24,25A)',
 'UNITY PLAZA (SITES 4-27)',
 'UNIVERSITY AVENUE REHAB',
 'UPACA (SITE 5)',
 'UPACA (SITE 6)',
 'VAN DYKE I',
 'VAN DYKE II',
 'VANDALIA AVENUE',
 'VLADECK',
 'VLADECK II',
 'WAGNER',
 'WALD',
 'WASHINGTON',
 'WASHINGTON HEIGHTS REHAB (GROUPS 1&2)',
 'WASHINGTON HEIGHTS REHAB PHASE III',
 'WASHINGTON HEIGHTS REHAB PHASE III',
 'WASHINGTON HEIGHTS REHAB PHASE III',
 'WASHINGTON HEIGHTS REHAB PHASE IV (C)',
 'WASHINGTON HEIGHTS REHAB PHASE IV (D)',
 'WEBSTER',
 'WEEKSVILLE GARDENS',
 'WEST BRIGHTON I',
 'WEST BRIGHTON II',
 'WEST FARMS ROAD REHAB',
 'WEST FARMS SQUARE CONVENTIONAL',
 'WEST TREMONT AVENUE-SEDGWICK AVENUE AREA',
 'WHITE',
 'WHITMAN',
 'WILLIAMS PLAZA',
 'WILLIAMSBURG',
 'WILSON',
 'WISE TOWERS',
 'WOODSIDE',
 'WOODSON',
 'WSUR (BROWNSTONES)',
 'WSUR (SITE A) 120 WEST 94TH STREET',
 'WSUR (SITE B) 74 WEST 92ND STREET',
 'WSUR (SITE C) 589 AMSTERDAM AVENUE',
 'WYCKOFF GARDENS']
	def is_valid(develop):
		is_valid=True
		if develop in housing_list:
			is_valid=True
		else:
			is_valid=False
		return is_valid
	dev=dev.map(lambda x:[x,'TEXT','name of NYCHA housing development of occurrence','NULL'] if len(x)==0 else ([x,'TEXT','name of NYCHA housing development of occurrence','VALID'] if is_valid(x) else [x,'TEXT','name of NYCHA housing development of occurrence','INVALID']))
	dev=dev.map(lambda x:' '.join(x))
	dev.saveAsTextFile("19.out")
	sc.stop()
