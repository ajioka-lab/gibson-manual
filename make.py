#!/usr/bin/env python

from jinja2 import FileSystemLoader, Environment
import codecs 
import zipfile
import os

templateLoader = FileSystemLoader( searchpath="../_template" )

templateEnv = Environment( loader=templateLoader )

filelist = ['index', 'materials', 'workflow', 'print']

os.chdir( '_build' )

zf = zipfile.ZipFile( 'gibson-manual.zip', 'w' )

for f in filelist:
	template = templateEnv.get_template( f+'.html' )
	
	with codecs.open( f+'.html', 'wb', 'utf-8' ) as fh:
		fh.write( template.render(page=f) ) 
		zf.write( f+'.html' )

zf.write( 'css/' )
zf.write( 'css/bootstrap.min.css' )
zf.write( 'js/' )
zf.write( 'js/bootstrap.min.js' )
zf.write( 'js/jquery-1.9.1.min.js' )