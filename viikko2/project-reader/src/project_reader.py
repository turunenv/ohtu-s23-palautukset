from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        file_dict = tomli.loads(content)
        project_info = file_dict['tool']['poetry']

        name = project_info['name']
        description = project_info['description']
        dependencies = project_info['dependencies'].keys()
        dev_dependencies = project_info['group']['dev']['dependencies'].keys()
        authors = project_info['authors']
        license = project_info['license']
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, authors, license)
