#coding=utf-8


from webBrowse import *
import urllib2,os

def save(url,name):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
	base_dir = '/home/fengbin/sda/python/phantomjs/walkface'
	req = urllib2.Request(url = url, headers = headers)
	binary_data = urllib2.urlopen(req).read()
	path = ('%s/%s')%(base_dir,name)
	temp_file = open(path, 'wb')
	temp_file.write(binary_data)
	temp_file.close()
	return
	
	
if __name__ == '__main__':
	br = webBrowse()
	br.zhihu_login()	
	
	url = "https://www.zhihu.com/people/skywind3000"
	dict_list = br.get_follower(url)
	for i in dict_list.keys():
		print i
		
	dict_list = br.get_following(url)
	repeat_list = {}
	for i in dict_list.keys():
		temp_url = ("%s%s") %('https://www.zhihu.com',dict_list[i]['href'].encode('ascii'))
		print temp_url
	
	
	repeat_list.update(br.repeat_get_following(url,1))
	
	
	for i in repeat_list.keys():
		print ('name %s')%repeat_list[i]['name']
		url = ('%s')%repeat_list[i]['image']
		file_name = ('%s.jpg')%repeat_list[i]['name']
		print file_name
		save(url,file_name)
		
