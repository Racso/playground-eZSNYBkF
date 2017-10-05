# -*- coding: utf-8 -*-

from graphs import get_graph_info

def send_msg(channel, msg):
    print("TECHIO> message --channel '"+str(channel)+"' '"+str(msg)+"'")

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def test_get_graph_info():
    try:
        graph = [[1,3],[1,4],[4,5],[1,3],[3,2],[5,2],[5,5],[3,4]]
        a,b,c = get_graph_info(graph)
        assert a==4 and b==1 and c==True, "Fallo en prueba #1."

        graph = [[1,2],[3,1],[2,1],[3,2]]
        a,b,c = get_graph_info(graph)
        assert a==3 and b==0 and c==True, "Fallo en prueba #2."

        graph = [[1,1],[2,2],[3,3],[3,3]]
        a,b,c = get_graph_info(graph)
        assert a==4 and b==4 and c==True, "Fallo en prueba #3."

        graph = [[1,2],[1,3],[1,4],[2,4],[3,4],[4,4]]
        a,b,c = get_graph_info(graph)
        assert a==5 and b==1 and c==False, "Fallo en prueba #4."

        success()

        send_msg("¡Buen trabajo!", "¡Correcto!")
    except AssertionError as e:
        fail()
        send_msg("Oops! ðŸž", e)
        send_msg("Pista ðŸ’¡", "Un ciclo es una arista que conecta un nodo consigo mismo, y añade 2 al grado del nodo.")
        send_msg("Pista ðŸ’¡", "El grafo es no dirigido, de modo que una arista de A hacia B y una arista de B hacia A son paralelas.")

if __name__ == "__main__":
    test_get_graph_info()
