class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _stringify_attr_list(self, attr_list):
        attr_list_with_hyphen = [f"- {item}" for item in attr_list]
        return "\n".join(attr_list_with_hyphen) if len(attr_list) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license or '-'}"
            f"\n\nAuthors:\n{self._stringify_attr_list(self.authors)}"
            f"\n\nDependencies:\n{self._stringify_attr_list(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n{self._stringify_attr_list(self.dev_dependencies)}"
        )
