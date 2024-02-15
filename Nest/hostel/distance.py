from geographiclib.geodesic import Geodesic



def calc_distance(hostel_lat, hostel_lng, school_latitude, school_longitude):
	'''
	using the central gps address of every school
	'''

	geod = Geodesic.WGS84

	
	res = geod.Inverse(school_latitude, school_longitude, hostel_lat, hostel_lng)
	'''
	assume an average person walks 80m in a minute
	'''

	dist = res['s12']
	average_walking_time = int(dist / 80)

	return f'{average_walking_time} mins'
