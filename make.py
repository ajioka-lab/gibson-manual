#!/usr/bin/env python

from jinja2 import FileSystemLoader, Environment
import codecs 
import zipfile
import os, shutil, shlex
from weasyprint import HTML, CSS
from subprocess import check_call 
from datetime import date

# generate version number
VERSION = '0.1'
DATE_STRING = date.today().strftime('%Y%m%d')
version_string = '%s-%s' % (VERSION, DATE_STRING)

# clean build directory
shutil.rmtree( '_build' )
os.mkdir( '_build' )
os.chdir( '_build' )
os.mkdir( 'css' )

# copy in javascript and image resources
shutil.copytree( os.path.join(os.path.dirname(__file__), '../_template/js/' ), os.path.join( os.path.dirname(__file__), 'js' ) )
shutil.copytree( os.path.join(os.path.dirname(__file__), '../_template/img/' ), os.path.join( os.path.dirname(__file__), 'img' ) )

# generate CSS
check_call( shlex.split('lessc -x --yui-compress ../_template/less/bootstrap.less css/bootstrap.min.css') )

# load templates
templateLoader = FileSystemLoader( searchpath="../_template" )
templateEnv = Environment( loader=templateLoader )



filelist = ['index', 'materials', 'workflow', 'print']
#zf = zipfile.ZipFile( 'GibsonManual.zip', 'w' )

# create the four html files
for f in filelist:
	template = templateEnv.get_template( f+'.html' )
	with codecs.open( f+'.html', 'wb', 'utf-8' ) as fh:
		fh.write( template.render(page=f, version=version_string) ) 
		#zf.write( f+'.html' )

#zf.write( 'css/' )
#zf.write( 'css/bootstrap.min.css' )
#zf.write( 'js/' )
#zf.write( 'js/bootstrap.min.js' )
#zf.write( 'js/jquery-1.9.1.min.js' )

# create the PDF
HTML('print.html').write_pdf('GibsonManual.pdf')
# and delete the html file
os.remove('print.html')

#zf.write( 'GibsonManual.pdf' )

