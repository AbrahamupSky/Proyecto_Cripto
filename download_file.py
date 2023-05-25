import urllib.request

def download_file(file_url):
  file_name = file_url.split("/")[-1]
  urllib.request.urlretrieve(file_url, file_name)
  return file_name
