import matplotlib.pyplot as plt
import copy
import networkx as nx
import math
import csv
import random as rand
import sys

_DEBUG_ = False

def buildG(G, file_, delimiter_):
    reader = csv.reader(open(file_), delimiter=delimiter_)
    for line in reader:
        if len(line) > 2:
            if float(line[2]) != 0.0:
                G.add_edge(int(line[0]),int(line[1]),weight=float(line[2]))
                G.add_edge(int(line[1]),int(line[0]),weight=float(line[2]))

        else:
            G.add_edge(int(line[0]),int(line[1]),weight=1.0)



def CmtyGirvanNewmanStep(G):
    # if _DEBUG_:
        # print("Running CmtyGirvanNewmanStep method ...")
    init_ncomp = nx.number_connected_components(G)    
    ncomp = init_ncomp
    k=None
    while ncomp <= init_ncomp:
        bw = nx.edge_betweenness_centrality(G, weight='weight')
        bh=bw 
        max_ = max(bw.values())
        for k, v in bw.items():
            if float(v) == max_:
                G.remove_edge(k[0],k[1])    
        ncomp = nx.number_connected_components(G) 
    # print("Betweeness : ",bh) 
    return bh




def _GirvanNewmanGetModularity(G, deg_, m_):
    New_A = nx.adj_matrix(G)
    New_deg = {}
    New_deg = UpdateDeg(New_A, G.nodes())
    comps = nx.connected_components(G)       
    # print('No of communities in decomposed G: {}'.format(nx.number_connected_components(G)))
    Mod = 0    
    for c in comps:
        EWC = 0   
        RE = 0    
        for u in c:
            EWC += New_deg[u]
            RE += deg_[u]       
        Mod += ( float(EWC) - float(RE*RE)/float(2*m_) )
    Mod = Mod/float(2*m_)
    if _DEBUG_:
        print("Modularity: {}".format(Mod))
    return Mod


def UpdateDeg(A, nodes):
    deg_dict = {}
    n = len(nodes)  
    B = A.sum(axis = 1)
    i = 0
    for node_id in list(nodes):
        deg_dict[node_id] = B[i, 0]
        i += 1
    return deg_dict


def runGirvanNewman(G, Orig_deg, m_):
    BestQ = 0.0
    Q = 0.0
    while True:    
        s=CmtyGirvanNewmanStep(G)
        Q = _GirvanNewmanGetModularity(G, Orig_deg, m_);
        print("Modularity of decomposed G: {}".format(Q))
        if Q > BestQ:
            BestQ = Q
            Bestcomps = list(nx.connected_components(G))    #Best Split
            # print("Identified components: {}".format(Bestcomps))
        if G.number_of_edges() == 0:
            break
    print("Betweeness :",s)
    if BestQ > 0.0:
        print("Max modularity found (Q): {} \nnumber of communities: {}".format(BestQ, len(Bestcomps)))
        print("Graph communities: ")
        for x in Bestcomps:
            print(x)
        return Bestcomps
    else:
        print("Max modularity (Q):", BestQ)


def main(argv):
    # if len(argv) < 2:
    #     sys.stderr.write("Usage: %s <input graph>\n" % (argv[0],))
    #     return 1
    x=int(input("Entre 1 to give input of the graph\nEntre 2 to give file input \n"))
    if x==2:
        # graph_fn = argv[1]
        graph_fn = input("Entre the file name ")
        G = nx.Graph()  
        buildG(G, graph_fn, ' ')
        copyGraph = copy.deepcopy(G)
        pos=nx.spring_layout(G)
        nx.draw(G,with_labels=True)
        # nx.draw_networkx_nodes(copyGraph,pos,nodelist=nlist,node_color=[colors[i] for x in range(len(nlist))],node_size=500,alpha=0.8)
        # nx.draw_networkx_edges(copyGraph,pos,alpha=0.1)
        plt.show()
        if _DEBUG_:
            print('G nodes: {} & G no of nodes: {}'.format(G.nodes(), G.number_of_nodes()))
        
        n = G.number_of_nodes()  
        A = nx.adj_matrix(G)   

        m_ = 0.0    
        for i in range(0,n):
            for j in range(0,n):
                m_ += A[i,j]
        m_ = m_/2.0
        if _DEBUG_:
            print("m: {}".format(m_))


        Orig_deg = {}
        Orig_deg = UpdateDeg(A, G.nodes())


        Bestcomps =runGirvanNewman(G, Orig_deg, m_)
        ng=Bestcomps
        pos=nx.spring_layout(copyGraph)
        number_of_colors = len(ng)
        colors = [(rand.random(),rand.random(),rand.random()) for i in range(number_of_colors)]
        for i in range(len(ng)):
            graph=ng[i]
            nlist = [node for node in graph]
            nx.draw_networkx_nodes(copyGraph,pos,nodelist=nlist,node_color=[colors[i] for x in range(len(nlist))],node_size=500,alpha=0.8)

        nx.draw_networkx_edges(copyGraph,pos,alpha=0.1)
        nx.draw_networkx_labels(copyGraph,pos,font_size=10)
        plt.axis('off')
        plt.show()
    else:
        x=int(input("Entre 1 to give input of the weighted graph\nEntre 2 to give  input of unweighted graph \n"))
        if x==1:
            G = nx.Graph()
            n=int(input("Enter the number of nodes "))
            e=int(input("Enter the number of edges \n"))
            for x in range(e):
                a=int(input("Entre the node one "))
                b=int(input("Entre the node two "))
                c=float(input("Entre the node weight \n"))
                G.add_edge(a,b,weight=c)
                G.add_edge(b,a,weight=c)
            copyGraph = copy.deepcopy(G)
            nx.draw(G,with_labels=True)
            plt.show()           
            n = G.number_of_nodes()  
            A = nx.adj_matrix(G)   

            m_ = 0.0    
            for i in range(0,n):
                for j in range(0,n):
                    m_ += A[i,j]
            m_ = m_/2.0
            if _DEBUG_:
                print("m: {}".format(m_))


            Orig_deg = {}
            Orig_deg = UpdateDeg(A, G.nodes())


            Bestcomps =runGirvanNewman(G, Orig_deg, m_)
            ng=Bestcomps
            pos=nx.spring_layout(copyGraph)
            number_of_colors = len(ng)
            colors = [(rand.random(),rand.random(),rand.random()) for i in range(number_of_colors)]
            for i in range(len(ng)):
                graph=ng[i]
                nlist = [node for node in graph]
                nx.draw_networkx_nodes(copyGraph,pos,nodelist=nlist,node_color=[colors[i] for x in range(len(nlist))],node_size=500,alpha=0.8)

            nx.draw_networkx_edges(copyGraph,pos,alpha=0.1)
            nx.draw_networkx_labels(copyGraph,pos,font_size=10)
            plt.axis('off')
            plt.show()
        else:
            G = nx.Graph()
            n=int(input("Enter the number of nodes "))
            e=int(input("Enter the number of edges "))
            print()
            for x in range(e):
                print("add edge ")
                a=int(input("Entre the node one "))
                b=int(input("Entre the node two "))
                print()
                G.add_edge(a,b,weight=1.0)
                G.add_edge(b,a,weight=1.0)
            copyGraph = copy.deepcopy(G)
            nx.draw(G,with_labels=True)
            plt.show()           
            n = G.number_of_nodes()  
            A = nx.adj_matrix(G)   

            m_ = 0.0    
            for i in range(0,n):
                for j in range(0,n):
                    m_ += A[i,j]
            m_ = m_/2.0
            if _DEBUG_:
                print("m: {}".format(m_))


            Orig_deg = {}
            Orig_deg = UpdateDeg(A, G.nodes())


            Bestcomps =runGirvanNewman(G, Orig_deg, m_)
            ng=Bestcomps
            pos=nx.spring_layout(copyGraph)
            number_of_colors = len(ng)
            colors = [(rand.random(),rand.random(),rand.random()) for i in range(number_of_colors)]
            for i in range(len(ng)):
                graph=ng[i]
                nlist = [node for node in graph]
                nx.draw_networkx_nodes(copyGraph,pos,nodelist=nlist,node_color=[colors[i] for x in range(len(nlist))],node_size=500,alpha=0.8)

            nx.draw_networkx_edges(copyGraph,pos,alpha=0.1)
            nx.draw_networkx_labels(copyGraph,pos,font_size=10)
            plt.axis('off')
            plt.show()



            


    
if __name__ == "__main__":
    sys.exit(main(sys.argv))
# main()