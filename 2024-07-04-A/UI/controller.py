import flet as ft
from UI.view import View
from model.modello import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_graph(self, e):
        self._view.txt_result1.controls.clear()
        anno = int(self._view.ddyear.value)
        forma = self._view.ddshape.value
        self._model.buildGrafo(anno, forma)
        self._view.txt_result1.controls.append(ft.Text("Grafo correttamente creato"))
        nNodes, nEdges = self._model.getDetails()
        self._view.txt_result1.controls.append(ft.Text(f"Il grafo ha {nNodes} nodi, {nEdges} archi"))
        numConnComp = self._model.getNumConnComp()
        self._view.txt_result1.controls.append(ft.Text(f"Il grafo ha: {numConnComp} componenti connesse."))

        bestConnComp, lenght = self._model.getBestConnComp()
        self._view.txt_result1.controls.append(
            ft.Text(f"La componente connessa più grande è costituita da {lenght} nodi."))
        for n in bestConnComp:
            self._view.txt_result1.controls.append(ft.Text(f"{n}"))

        self._view.update_page()

    def handle_path(self, e):
        pass

    def fillDDYear(self):
        anni = self._model.getAnniAvvistamenti()
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(anno))
        self._view.update_page()

    def fillDDshape(self):
        forme = self._model.get_shape()
        for f in forme:
            (self._view.ddshape.options.append(ft.dropdown.Option(f)))
        self._view.update_page()