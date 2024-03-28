import networkx as nx
import matplotlib.pyplot as plt

def luo_kartta():
    kartta = {
        'koti': {'itä': 'hiekkatie'},
        'hiekkatie': {'itä': 'mummola', 'etelä': 'maantie', 'länsi': 'koti'},
        'maantie': {'länsi': 'kaatopaikka', 'itä': 'kyläpubi', 'pohjoinen': 'hiekkatie', 'etelä': 'moottoritie'},
        'moottoritie': {'pohjoinen': 'maantie', 'itä': 'armeija_alue', 'etelä': 'tampereen_keskustori'},
        'armeija_alue': {'länsi': 'sotilaskoti', 'itä': 'moottoritie'},
        'sotilaskoti': {'länsi': 'armeija_alue'},
        'tampereen_keskustori': {'pohjoinen': 'moottoritie', 'länsi': 'ratikka', 'itä': 'ylöjärven_keskusta'},
        'ratikka': {'itä': 'tampereen_keskustori', 'pohjoinen': 'kela'},
        'kela': {'etelä': 'ratikka'},
        'ylöjärven_keskusta': {'länsi': 'tampereen_keskustori', 'itä': 'kebab_ravintola', 'pohjoinen': 'takamaa'},
        'takamaa': {'etelä': 'ylöjärven_keskusta', 'pohjoinen': 'jarppa_setä'},
        'jarppa_setä': {'etelä': 'takamaa'},
        'kebab_ravintola': {'länsi': 'ylöjärven_keskusta', 'itä': 'parturi', 'pohjoinen': 'kirjasto'},
        'parturi': {'länsi': 'kebab_ravintola'},
        'kirjasto': {'etelä': 'kebab_ravintola', 'pohjoinen': 'täti'},
        'täti': {'etelä': 'kirjasto', 'pohjoinen': 'valintatalo'},
        'valintatalo': {'etelä': 'täti', 'länsi': 'mummola'},
        'mummola': {'länsi': 'hiekkatie', 'itä': 'valintatalo'}
    }
    return kartta

def visualisoi_kartta(kartta):
    G = nx.DiGraph()

    for paikka, suunnat in kartta.items():
        for suunta, kohde in suunnat.items():
            G.add_edge(paikka, kohde, label=suunta)

    pos = nx.spring_layout(G)
    edge_labels = {(u, v): d["label"] for u, v, d in G.edges(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)
    plt.title('Kartta')
    plt.axis('off')
    plt.show()

# Luo kartta ja visualisoi se
kartta = luo_kartta()
visualisoi_kartta(kartta)
