default_srcs = "*.exaltedcollection.com *.gstatic.com *.googleapis.com *.fontawesome.com"
base_domains="*.exaltedcollection.com"
media_srcs = f"{base_domains} *.gstatic.com *.googleapis.com"
font_srcs = "*.gstatic.com *.googleapis.com *.google-analytics.com *.cloudflare.com *.fontawesome.com"
scripts_srcs = "*.gstatic.com"

raw_str = f'''add_header Content-Security-Policy "
default-src {default_srcs}
script-src 'self' 'unsafe-inline' 'unsafe-eval' {scripts_srcs}; 
font-src 'self' data: blob: {font_srcs}; 
img-src 'self' data: blob: {media_srcs}; 
media-src 'self' data: blob: {media_srcs}; 
object-src 'self'; 
connect-src 'self' {base_domains};";'''

print(raw_str.replace('\n',' '))

'''
Working header for exaltedcollection.com

add_header Content-Security-Policy "script-src 'self' 'unsafe-inline' 'unsafe-eval' *.gstatic.com *.googleapis.com;  font-src data: blob: *.exaltedcollection.com *.gstatic.com *.googleapis.com *.google-analytics.com *.cloudflare.com *.fontawesome.com;  img-src data: blob: *.exaltedcollection.com *.gstatic.com *.googleapis.com https://cdn.pixabay.com 'self';  media-src 'self' data: blob: *.exaltedcollection.com *.gstatic.com *.googleapis.com;  object-src 'self';  connect-src 'self' *.exaltedcollection.com;";
'''
