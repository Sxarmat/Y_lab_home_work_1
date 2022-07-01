from urllib.parse import urlparse


def domain_name(url):
	parse = urlparse(url)
	domain = (parse.path if not parse.netloc else parse.netloc).split('.')
	return domain[1] if domain[0] == 'www' else domain[0]
