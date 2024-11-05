from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        cont = toml.loads(content)
        name = cont["tool"]["poetry"]["name"]
        description = cont["tool"]["poetry"]["description"]
        dependencies = cont["tool"]["poetry"]["dependencies"]
        dev_depen = cont["tool"]["poetry"]["group"]["dev"]["dependencies"]

        license = cont["tool"]["poetry"]["license"]
        authors = cont["tool"]["poetry"]["authors"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_depen)
