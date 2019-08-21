def squishuser(y):
	y._json.pop('id', None)
	y._json.pop('default_profile', None)
	y._json.pop('default_profile_image', None)
	y._json.pop('geo_enabled', None)
	y._json.pop('has_extended_profile', None)
	y._json.pop('is_translation_enabled', None)
	y._json.pop('is_translator', None)
	y._json.pop('notifications', None)
	y._json.pop('profile_background_color', None)
	y._json.pop('profile_background_image_url', None)
	y._json.pop('profile_background_image_url_https', None)
	y._json.pop('profile_background_tile', None)
	y._json.pop('profile_banner_url', None)
	#y._json.pop('profile_image_url', None)
	y._json.pop('profile_image_url_https', None)
	y._json.pop('profile_link_color', None)
	y._json.pop('profile_location', None)
	y._json.pop('profile_location.bounding_box', None)
	y._json.pop('profile_location.contained_within', None)
	y._json.pop('profile_location.country', None)
	y._json.pop('profile_location.country_code', None)
	#y._json.pop('profile_location.full_name', None)
	#y._json.pop('profile_location.id', None)
	#y._json.pop('profile_location.name', None)
	#y._json.pop('profile_location.place_type', None)
	#y._json.pop('profile_location.url', None)
	y._json.pop('profile_sidebar_border_color', None)
	y._json.pop('profile_sidebar_fill_color', None)
	y._json.pop('profile_text_color', None)
	y._json.pop('profile_use_background_image', None)
	y._json.pop('contributors_enabled', None)
	y._json.pop('following', None)
	y._json.pop('follow_request_sent', None)
	y._json.pop('translator_type', None)
#	y._json.pop('time_zone')
#	y._json.pop('utc_offset')
	now = datetime.datetime.now()
	y._json['collected_at'] = now.strftime("%a %b %d %X +0000 %Y")
	try:
		status = y._json.pop('status', None)
		y._json['status_at'] = status['created_at']
	except:
		y._json['status_at'] = "Sun Jan 01 00:00:00 +0000 2006"
	return(y)

import datetime, platform, getpass
from .squishtweet import squishtweet
from .perflog import perflog
