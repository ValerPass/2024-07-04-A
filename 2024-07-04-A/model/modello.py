import itertools

from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def getAvvistamenti(self):
        return DAO.get_all_sightings()

    def getAnniAvvistamenti(self):
        return DAO.get_years()

    def get_shape(self):
        return DAO.get_shapes()

    def buildGrafo(self, anno, forma):
        self.grafo.clear()

        # Filtra gli avvistamenti per anno e forma
        avv = [a for a in self.getAvvistamenti() if a.datetime.year == anno and a.shape == forma]

        # Aggiungi i nodi al grafo
        self.grafo.add_nodes_from(avv)

        # Aggiungi gli archi tra nodi con la stessa state e datetime coerente
        for n in self.grafo.nodes:
            for n2 in self.grafo.nodes:
                if not self.grafo.has_edge(n, n2) and n != n2:
                    if n.state == n2.state and n.datetime < n2.datetime:
                            self.grafo.add_edge(n, n2)

    def getDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)

    def getNumConnComp(self):
        return len(list(nx.weakly_connected_components(self.grafo)))


    #ordino per componente connessa maggiore
    def getBestConnComp(self):
        connectedComponents = list(nx.weakly_connected_components(self.grafo))
        connectedComponents.sort(key=lambda x: len(x), reverse=True)
        return connectedComponents[0], len(connectedComponents[0])