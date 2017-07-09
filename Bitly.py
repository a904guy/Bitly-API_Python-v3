import sys
from pprint import pformat as pf

import requests
from requests.auth import HTTPBasicAuth


class Bitly:
	url = 'https://api-ssl.bitly.com/%s'
	urls = {
		# Auth
		'_get_access_token': 'oauth/access_token',
		# Link
		'link_metadata': 'v3/link/info',
		'link_expand': 'v3/expand',
		'link_info': 'v3/info',
		'link_long': 'v3/link/lookup',
		'link_short': 'v3/shorten',
		'link_save': 'v3/user/link_save',
		'link_edit': 'v3/user/link_edit',
		'link_user_lookup': 'v3/user/link_lookup',
		'link_user_save_custom': 'v3/user/save_custom_domain_keyword',
		# Link Metrics
		'link_clicks': 'v3/link/clicks',
		'link_countries': 'v3/link/countries',
		'link_encoders': 'v3/link/encoders',
		'link_encoders_by_clicks': 'v3/link/encoders_by_count',
		'link_encoders_count': 'v3/link/encoders_by_count',
		'link_referrers': 'v3/link/referrers',
		'link_referrers_by_domain': 'v3/link/referrers_by_domain',
		'link_referring_domains': 'v3/link/referring_domains',
		# User Info / History
		'user_oauth': '/v3/oauth/app',  # oauth
		'user_info': '/v3/user/info',  # oauth
		'user_link': '/v3/user/link_history',  # oauth
		'user_tracking_domains': '/v3/user/tracking_domain_list',  # oauth
		# User Metrics
		'user_clicks': '/v3/user/clicks',  # oauth
		'user_countries': '/v3/user/countries',  # oauth
		'user_popular_earned_by_clicks': '/v3/user/popular_earned_by_clicks',  # oauth
		'user_popular_earned_by_shortens': '/v3/user/popular_earned_by_shortens',  # oauth
		'user_popular_links': '/v3/user/popular_links',  # oauth
		'user_popular_owned_by_clicks': '/v3/user/popular_owned_by_clicks',  # oauth
		'user_popular_owned_by_shortens': '/v3/user/popular_owned_by_shortens',  # oauth
		'user_referrers': '/v3/user/referrers',  # oauth
		'user_referring_domains': '/v3/user/referring_domains',  # oauth
		'user_shorten_counts': '/v3/user/shorten_counts',  # oauth
		# Organization Metrics
		# Domains
		# Campaigns
		# Deeplink Metrics
		# Data Streams
	}

	# Authentication
	username = None
	password = None
	client_id = None
	client_secret = None
	token = None

	def __init__(self, username: str = False, password: str = False, client_id: str = False, client_secret: str = False, access_token: str = False):

		assert (username is not None and password is not None and client_id is not None and client_secret is not None) or access_token is not None

		self.s = requests.Session()

		self.username = username
		self.password = password
		self.client_id = client_id
		self.client_secret = client_secret

		if False is access_token:
			self.token = self._get_access_token()
		elif isinstance(access_token, str) and access_token is not None:
			self.token = access_token

	def _get_access_token(self):
		return self.s.post(self.url % self.urls[sys._getframe().f_code.co_name], data={
			'grant_type': 'password',
			'username': self.username,
			'password': self.password,
		}, auth=HTTPBasicAuth(self.client_id, self.client_secret)).json()['access_token']

	# Link APIs http://dev.bitly.com/links.html

	def link_metadata(self, link: str):

		assert link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_expand(self, shortUrl: str = None, hash: str = None):

		assert shortUrl is not None or hash is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_info(self, shortUrl: str = None, hash: str = None, expand_user: bool = None):

		assert shortUrl is not None or hash is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_long(self, shortUrl: str):

		assert shortUrl is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_short(self, longUrl: str, domain: str = None):

		assert longUrl is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_save(self, longUrl: str, title: str = None, note: str = None, private: bool = None, user_ts: int = None, domain: str = None):

		assert longUrl is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_edit(self, longUrl: str, title: str = None, note: str = None, private: bool = None, user_ts: int = None, domain: str = None, archived: bool = None):

		assert longUrl is not None

		# Compile Edit fields list.
		edit = []
		for x in locals():
			if isinstance(locals()[x], None):
				continue
			if isinstance(locals()[x], str) and locals()[x] is not None:
				edit.append(x)
				continue
			if isinstance(locals()[x], bool):
				edit.append(x)
				continue
		edit = ",".join(edit)

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_user_lookup(self, url: list):

		assert len(url) > 0

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_user_save_custom(self, keyword_link: str, target_link: str, overwrite: bool = None):

		assert keyword_link is not None and target_link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	# Link Metrics API: http://dev.bitly.com/link_metrics.html

	def link_clicks(self, link: str, unit: str = 'day', units: int = -1, timezone='UTC', rollup: bool = False, limit: int = None, unit_reference_ts: int = None):

		assert link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_countries(self, link: str, unit: str = 'day', units: int = -1, timezone=None, rollup: bool = None, limit: int = None, unit_reference_ts: int = None):

		assert link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_encoders(self, link: str, subaccounts: bool = True, limit: int = None, expand_user: bool = None):

		assert link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_encoders_by_clicks(self, link: str, subaccounts: bool = False, limit: int = None, expand_user: bool = None):

		assert link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_encoders_count(self, link: str):

		assert link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_referrers(self, link: str, unit: str = 'day', units: int = -1, timezone='UTC', rollup: bool = False, limit: int = None, unit_reference_ts: int = None):

		assert link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_referrers_by_domain(self, link: str, unit: str = 'day', units: int = -1, timezone=None, rollup: bool = None, limit: int = None, unit_reference_ts: int = None):

		assert link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def link_referring_domains(self, link: str, unit: str = 'day', units: int = -1, timezone=None, rollup: bool = None, limit: int = None, unit_reference_ts: int = None):

		assert link is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	# User Info / History: https://dev.bitly.com/user_info.html

	def user_oauth(self, client_id: str):

		assert client_id is not None and isinstance(client_id, str)

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_info(self, login: str = None, full_name: str = None):

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_link(self, link: str = None, limit: int = None, offset: int = None, created_before: int = None, created_after: int = None, modified_after: int = None, expand_client_id: bool = None, archived: str = None, private: str = None, deeplinks: str = None, user: str = None, exact_domain: str = None, root_domain: str = None, keyword: str = None, query: str = None):

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_tracking_domains(self):

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	# User Metrics: https://dev.bitly.com/user_metrics.html

	def user_clicks(self, unit: str = 'day', timezone: str = 'America/New_York', rollup: bool = False, limit: int = 100, unit_reference_ts: str = 'now', format: str = 'json'):

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_countries(self, unit: str = 'day', timezone: str = 'America/New_York', rollup: bool = False, limit: int = 100, unit_reference_ts: str = 'now', format: str = 'json'):

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_popular_earned_by_clicks(self, domain: str = None, unit: str = 'day', units: int = None, timezone: str = 'America/New_York', limit: int = 100, unit_reference_ts: str = 'now'):

		assert domain is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_popular_earned_by_shortens(self, domain: str = None, unit: str = 'day', units: int = None, timezone: str = 'America/New_York', limit: int = 100, unit_reference_ts: str = 'now'):

		assert domain is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_popular_links(self, unit: str = 'day', units: int = None, timezone: str = 'America/New_York', limit: int = 100, unit_reference_ts: str = 'now'):

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_popular_earned_by_clicks(self, domain: str = None, unit: str = 'day', units: int = None, timezone: str = 'America/New_York', limit: int = 100, unit_reference_ts: str = 'now'):

		assert domain is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_popular_earned_by_shortens(self, domain: str = None, unit: str = 'day', units: int = None, timezone: str = 'America/New_York', limit: int = 100, unit_reference_ts: str = 'now'):

		assert domain is not None

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_referrers(self, unit: str = 'day', units: int = None, timezone: str = 'America/New_York', limit: int = 100, unit_reference_ts: str = 'now'):

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_referring_domains(self, unit: str = 'day', units: int = None, timezone: str = 'America/New_York', limit: int = 100, unit_reference_ts: str = 'now'):

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def user_shorten_counts(self, unit: str = 'day', units: int = None, timezone: str = 'America/New_York', limit: int = 100, unit_reference_ts: str = 'now'):

		return self._make_request(self.url % self.urls[sys._getframe().f_code.co_name], locals())

	def _make_request(self, api_url: str, additional_params: dict):

		params = {
			'access_token': self.token
		}
		for x in additional_params:
			if x == 'self':
				continue
			if isinstance(additional_params[x], bool):
				params[x] = str(additional_params[x]).lower()
				continue
			if isinstance(additional_params[x], int):
				params[x] = str(additional_params[x])
				continue
			if additional_params[x] is not None:
				params[x] = additional_params[x]
		res = self.s.get(api_url, params=params)
		# pp(res.request.__dict__)
		r = res.json()
		if r['status_code'] != 200:
			raise HTTPError(
				str(r['status_txt'] + ": %s\n" + pf(params)) % api_url)
		else:
			return r['data']
