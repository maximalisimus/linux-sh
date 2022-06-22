#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def main():
	'''
	G.add_edges_from([('A','B'),('A','C'),('C','B')])
	pos = nx.spring_layout(G)
	nx.draw_networkx_nodes(G,pos, node_size=500)
	nx.draw_networkx_edges(G,pos, edgelist=G.edges(),edge_color='blue')
	nx.draw_networkx_labels(G,pos)
	plt.show()
	'''
	# ese
	'''
	G.add_node(1)
	G.add_node(2)
	G.add_node(3)
	G.add_node(4)
	G.add_edge(1,2)
	G.add_edge(2,1)
	G.add_edge(1,3)
	G.add_edge(3,1)
	G.add_edge(2,4)
	G.add_edge(4,2)
	G.add_edge(3,4)
	G.add_edge(4,3)
	'''
	G = nx.DiGraph()
	'''
	G = nx.MultiDiGraph(format='png', directed=True)
	elist=[('1','2',1.0),('2','1',1.0),('1','3',1.0),('3','1',1.0),('2','4',1.0),('4','2',1.0),('3','4',1.0),('4','3',1.0)]
	elist=[('S1','S2',1.0),('S2','S1',1.0),('S2','S3',1.0),('S3','S2',1.0),('S3','S4',1.0),('S4','S3',1.0)]
	G.add_weighted_edges_from(elist)
	'''
	#G.add_nodes_from(['s1', 's2', 's3', 's4'])
	# G.add_edges_from([('s1', 's2'), ('s2', 's1'), ('s2', 's3'), ('s3', 's2'),('s3', 's4'),('s4', 's3')])
	# plt.figure(figsize=(8, 1))
	# G.add_edges_from([('s1', 's2'), ('s2', 's1'), ('s1', 's3'), ('s3', 's1'), ('s2', 's4'), ('s4', 's2'), ('s3', 's4'), ('s4', 's3')])
	#s = "s1,s2;s2,s1;s1,s3;s3,s1;s2,s4;s4,s2;s3,s4;s4,s3"
	#plt.figure(figsize=(8, 3))
	#s = "s1,s2;s2,s1;s2,s3;s3,s2;s3,s4;s4,s3"
	#plt.figure(figsize=(8, 2))
	G.add_nodes_from(['s0', 's1', 's2', 's3', 's4'])
	s = "s0,s1;s1,s0;s1,s2;s2,s1;s1,s3;s3,s1;s3,s4;s4,s3"
	plt.figure(figsize=(8, 3))
	lst = list(tuple(str(item).split(',')) for item in s.split(';'))
	G.add_edges_from(lst)
	plt.rcParams["figure.autolayout"] = True
	pos = nx.spring_layout(G)
	# drow alternate with size
	'''
	nx.draw_networkx_nodes(G,pos, node_size=300)
	nx.draw_networkx_edges(G,pos, edgelist=G.edges(),edge_color='blue')
	nx.draw_networkx_labels(G,pos)
	'''
	plt.gcf().canvas.set_window_title('My Graph')
	plt.legend(title='Si')
	nx.draw(G, with_labels=True, connectionstyle="arc3,rad = 0.15")
	plt.show()
	print(G.edges())
	G.remove_edges_from(list(G.edges()))
	print(G.edges())	

if __name__ == '__main__':
	main()
