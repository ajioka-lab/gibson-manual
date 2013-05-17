#!/usr/bin/env python

from jinja2 import FileSystemLoader, Environment
import codecs 
import zipfile
import os, shutil
from weasyprint import HTML, CSS

from subprocess import check_call
import shlex


shutil.rmtree( '_build' )

os.mkdir( '_build' )

os.chdir( '_build' )

os.mkdir( 'css' )
os.mkdir( 'js' )
os.mkdir( 'img' )

shutil.copyfile( os.path.join(os.path.dirname(__file__), '../_template/js/bootstrap.min.js'), os.path.join(os.path.dirname(__file__),'js/bootstrap.min.js' ))
shutil.copyfile( os.path.join(os.path.dirname(__file__), '../_template/js/jquery-1.9.1.min.js'), os.path.join(os.path.dirname(__file__),'js/jquery-1.9.1.min.js' ))
shutil.copyfile( os.path.join(os.path.dirname(__file__), '../_template/img/glyphicons-halflings.png'), os.path.join(os.path.dirname(__file__),'img/glyphicons-halflings.png' ))
shutil.copyfile( os.path.join(os.path.dirname(__file__), '../_template/img/glyphicons-halflings-white.png'), os.path.join(os.path.dirname(__file__),'img/glyphicons-halflings-white.png' ))

templateLoader = FileSystemLoader( searchpath="../_template" )

templateEnv = Environment( loader=templateLoader )

filelist = ['index', 'materials', 'workflow', 'print']


check_call( shlex.split('lessc -x --yui-compress ../_template/less/bootstrap.less css/bootstrap.min.css') )


zf = zipfile.ZipFile( 'GibsonManual.zip', 'w' )

for f in filelist:
	template = templateEnv.get_template( f+'.html' )
	
	with codecs.open( f+'.html', 'wb', 'utf-8' ) as fh:
		fh.write( template.render(page=f) ) 
		zf.write( f+'.html' )

#zf.write( 'css/' )
#zf.write( 'css/bootstrap.min.css' )
#zf.write( 'js/' )
#zf.write( 'js/bootstrap.min.js' )
#zf.write( 'js/jquery-1.9.1.min.js' )

#HTML('print.html').write_pdf('GibsonManual.pdf')

#zf.write( 'GibsonManual.pdf' )

