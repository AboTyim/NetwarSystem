def squishtweet(y):
	print("SQUISHING")
	y._json.pop('coordinates', None)
	y._json.pop('contributors', None)
	y._json.pop('is_quote_status', None)
	y._json.pop('in_reply_to_status_id', None)
	y._json.pop('favorite_count', None)
	y._json.pop('in_reply_to_screen_name', None)
	y._json.pop('in_reply_to_user_id', None)
#	y._json.pop('retweet_count', None)
	y._json.pop('favorite', None)
	y._json.pop('favorited', None)
#	y._json.pop('favorite_count', None)
	y._json.pop('in_reply_to_user_id_str', None)
	y._json.pop('possibly_sensitive', None)
	y._json.pop('in_reply_to_status_id_str', None)
	y._json.pop('quoted_status', None)
	y._json.pop('quoted_status_id', None)
	y._json.pop('quoted_status_id_str', None)
	y._json.pop('timestamp_ms')
	y._json['user'].pop('translator_type')
	y._json['user'].pop('contributors_enabled')
	y._json['user'].pop('time_zone')
	y._json['user'].pop('utc_offset')
	y._json['user'].pop('geo_enabled')
	y._json['user'].pop('profile_background_color', None)
	y._json['user'].pop('profile_background_image_url', None)
	y._json['user'].pop('profile_background_image_url_https', None)
	y._json['user'].pop('profile_background_tile', None)
	y._json['user'].pop('profile_banner_url', None)
	y._json['user'].pop('profile_image_url_https', None)
	y._json['user'].pop('profile_link_color', None)
	y._json['user'].pop('profile_location', None)
	y._json['user'].pop('profile_sidebar_border_color', None)
	y._json['user'].pop('profile_sidebar_fill_color', None)
	y._json['user'].pop('profile_text_color', None)
	y._json['user'].pop('profile_use_background_image', None)

	y._json['user'].pop('default_profile_image', None)
	y._json['user'].pop('following', None)
	y._json['user'].pop('follow_request_sent', None)
	y._json['user'].pop('contributors', None)
	#which of these is flag?
	y._json.pop('retweeted', None)
	y._json.pop('retweets', None)
	y._json.pop('retweet', None)
	#nested retweet
#	try:
#		for thing in y._json['retweeted_status']['user']:
#			print("thing: " + str(thing))
#			y._json['retweeted_status'][0]['user'].pop(thing)
#		y._json['retweeted_status'].pop('coordinates', None)
#		y._json['retweeted_status'].pop('contributors', None)
#		y._json['retweeted_status'].pop('is_quote_status', None)
#		y._json['retweeted_status'].pop('in_reply_to_status_id', None)
#		y._json['retweeted_status'].pop('favorite_count', None)
#		y._json['retweeted_status'].pop('in_reply_to_screen_name', None)
#		y._json['retweeted_status'].pop('in_reply_to_user_id', None)
#		#y._json['retweeted_status'].pop('retweet_count', None)
#		y._json['retweeted_status'].pop('favorite', None)
#		y._json['retweeted_status'].pop('favorited', None)
#		#y._json['retweeted_status'].pop('favorite_count', None)
#		y._json['retweeted_status'].pop('in_reply_to_user_id_str', None)
#		y._json['retweeted_status'].pop('possibly_sensitive', None)
#		y._json['retweeted_status'].pop('in_reply_to_status_id_str', None)
#		y._json['retweeted_status'].pop('quoted_status', None)
#		y._json['retweeted_status'].pop('quoted_status_id', None)
#		y._json['retweeted_status'].pop('quoted_status_id_str', None)
#		y._json['retweeted_status'].pop('retweeted', None)
#		y._json['retweeted_status'].pop('retweets', None)
#		y._json['retweeted_status'].pop('retweet', None)
#		y._json['retweeted_status'].pop('timestamp_ms')
#		print("almost")
##		print(type(y._json['retweeted_status']['user']))
##		print(type(y._json['retweeted_status.user']))
#		y._json['retweeted_status'].pop('translator_type')
#		y._json['retweeted_status'].pop('contributors_enabled')
#		y._json['retweeted_status'].pop('time_zone')
#		y._json['retweeted_status'].pop('utc_offset')
#		y._json['retweeted_status'].pop('geo_enabled')
#		y._json['retweeted_status'].pop('profile_background_color', None)
#		y._json['retweeted_status'].pop('profile_background_image_url', None)
#		y._json['retweeted_status'].pop('profile_background_image_url_https', None)
#		y._json['retweeted_status'].pop('profile_background_tile', None)
#		y._json['retweeted_status'].pop('profile_banner_url', None)
#		y._json['retweeted_status'].pop('profile_image_url_https', None)
#		y._json['retweeted_status'].pop('profile_link_color', None)
#		y._json['retweeted_status'].pop('profile_location', None)
#		y._json['retweeted_status'].pop('profile_sidebar_border_color', None)
#		y._json['retweeted_status'].pop('profile_sidebar_fill_color', None)
#		y._json['retweeted_status'].pop('profile_text_color', None)
#		y._json['retweeted_status'].pop('profile_use_background_image', None)
#		y._json['retweeted_status'].pop('default_profile_image', None)
#		y._json['retweeted_status'].pop('following', None)
#		y._json['retweeted_status'].pop('follow_request_sent', None)
#		y._json['retweeted_status'].pop('contributors', None)
#	except:
#		print('derp')
	return(y)