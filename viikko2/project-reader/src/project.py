class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _list(self, list):
        return "\n- ".join(list) if len(list) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nAuthors: \n- {self._list(self.authors)}\n"
            f"\nDependencies: \n- {self._list(self.dependencies)}\n"
            f"\nDevelopment dependencies: \n- {self._list(self.dev_dependencies)}"
        )
