
def formattweets():
	request_body = {
		"settings" : { "number_of_shards" : 3, "number_of_replicas" : 1},
		'mappings' : {'tweets' : { 'properties' : {
		'coordinates' : {'properties' : {'coordinates' : {'type' : 'geo_point'},'type' : {'type' : 'text'}}},
		'created_at' : {'type' : 'date', 'format' : 'EEE MMM dd HH:mm:ss Z YYYY'},
		'id_str' : {'type' : 'keyword'},
		'lang' : {'type' : 'keyword'},
		'source' : {'type' : 'keyword'},
		'text' : {'type' : 'text'},
		'user' : {'properties' : {'created_at' : {'type' : 'date', 'format' : 'EEE MMM dd HH:mm:ss Z YYYY'},
		'description' : {'type' : 'text'},
		'name' : {'type' : 'text'},
		'screen_name' : {'type' : 'text'}}}}}}}
	return request_body
	
def formatusers():
	request_body = {
		"settings" : { "number_of_shards" : 3, "number_of_replicas": 1},
		'mappings' : {'userid' : { 'properties' : {
		'created_at' : {'type' : 'date', 'format' : 'EEE MMM dd HH:mm:ss Z YYYY'},
		'status_at' : {'type' : 'date', 'format' : 'EEE MMM dd HH:mm:ss Z YYYY'},
		'collected_at' : {'type' : 'date', 'format' : 'EEE MMM dd HH:mm:ss Z YYYY'},
		'coordinates' : {'properties' : {'coordinates' : {'type' : 'geo_point'},'type' : {'type' : 'text'}}},
		'id_str' : {'type' : 'keyword'},
		'lang' : {'type' : 'keyword'},
		'source' : {'type' : 'keyword'},
		'text' : {'type' : 'text'},
		'user' : {'properties' : {'created_at' : {'type' : 'date', 'format' : 'EEE MMM dd HH:mm:ss Z YYYY'},
		'description' : {'type' : 'text'},
		'name' :	{'type' : 'text'},
		'screen_name' : {'type' : 'text'}}}}}}}
	return request_body
