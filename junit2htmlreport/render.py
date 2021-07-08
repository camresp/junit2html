"""
Render junit reports as HTML
"""
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape
from pathlib import Path

class HTMLReport(object):
    def __init__(self):
        self.title = ""
        self.report = None
        self.templates_path = None

    def load(self, report, title="JUnit2HTML Report", templates_path=None):
        self.report = report
        self.title = title

        if templates_path is not None:
            self.templates_path = Path(templates_path)

    def __iter__(self):
        return self.report.__iter__()


    def __str__(self) -> str:
        if self.templates_path and self.templates_path.resolve(strict=True):
            loader = FileSystemLoader(str(self.templates_path))
        else:
            loader = PackageLoader("junit2htmlreport", "templates")

        env = Environment(
            loader=loader,
            autoescape=select_autoescape(["html"])
        )

        template = env.get_template("report.html")
        return template.render(report=self, title=self.title)


class HTMLMatrix(object):
    def __init__(self, matrix):
        self.title = "JUnit Matrix"
        self.matrix = matrix

    def __str__(self) -> str:
        env = Environment(
            loader=PackageLoader("junit2htmlreport", "templates"),
            autoescape=select_autoescape(["html"])
        )

        template = env.get_template("matrix.html")
        return template.render(matrix=self.matrix, title=self.title)
