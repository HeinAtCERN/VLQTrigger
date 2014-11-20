import os
import varial.tools as tools
tools.RootFilePlotter().run()
tools.WebCreator().run()
os.system('rm -r ~/www/RootFilePlotter')
os.system('mv RootFilePlotter ~/www')
