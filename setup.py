from setuptools import find_packages,setup
from typing import List

def get_libraries(path:str)->List[str]:
     req = []

     with open(path) as file_obj:
          req = file_obj.readlines()
          
          [r.replace('\n','') for r in req]

          if('-e' in req):
               req.remove('-e')
               return req

        #   for r in req:
        #        r = r.replace('\n','')
        #        req.append(r)
        #        req.pop(0)

        #        if('\n' in req[0]):
        #              pass
        #        else:
        #              break




setup(name='MLPROJ',
      version='0.0.1',
      author='Kaushal',
      packages= find_packages(),
      install_requires = get_libraries('requirement.txt')
      )