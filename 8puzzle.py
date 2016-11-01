#!/usr/bin/python
# AIML_Assignment 1: 8 Puzzle Problem.
# Author: Kavya(201301016) and SaiCharan(201311022).
# Date:26th January 2016. 
goal_state = [1,2,3,4,5,6,7,8,0]
array = [[] for i in range(100)]
k=0
import sys
def display_board( state ):
	print "-------------"
	print "| %i | %i | %i |" % (state[0], state[1], state[2])
	print "-------------"
	print "| %i | %i | %i |" % (state[3], state[4], state[5])
	print "-------------"
	print "| %i | %i | %i |" % (state[6], state[7], state[8])
	print "-------------"
	
def move_up( state ):

	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [0, 3, 6]:
		temp = new_state[index - 1]
		new_state[index - 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def move_down( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [2, 5, 8]:
		temp = new_state[index + 1]
		new_state[index + 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def move_left( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [0, 1, 2]:
		temp = new_state[index - 3]
		new_state[index - 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def move_right( state ):
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [6, 7, 8]:
		temp = new_state[index + 3]
		new_state[index + 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def create_node( state, parent, operator, depth, cost ):
	return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
	"""Returns a list of expanded nodes"""
	expanded_nodes = []
	expanded_nodes.append( create_node( move_up( node.state ), node, "left", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_down( node.state ), node, "right", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_left( node.state ), node, "up", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_right( node.state), node, "down", node.depth + 1, 0 ) )
	expanded_nodes = [node for node in expanded_nodes if node.state != None] 
	return expanded_nodes
def bfs( start, goal ):
	nodes = []
	nodes.append( create_node( start, None, None, 0, 0 ) )
	count=0
	while True:
		if len( nodes ) == 0: return None
		node = nodes.pop(0)
		if node.state == goal:
			moves = []
			temp = node
			k=0
			while True:
				array[k]=[]
				array[k].append(temp.state[0])
				array[k].append(temp.state[1])
				array[k].append(temp.state[2])
				array[k].append(temp.state[3])
				array[k].append(temp.state[4])
				array[k].append(temp.state[5])
				array[k].append(temp.state[6])
				array[k].append(temp.state[7])
				array[k].append(temp.state[8])
				k += 1
				moves.insert(0, temp.operator)
				if temp.depth == 1: break
				temp = temp.parent

			for i in reversed(range(k)):
				display_board(array[i])
			return moves
		nodes.extend( expand_node( node, nodes ) )

def dfs( start, goal, depth=10 ):
	depth_limit = depth
	nodes = []
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
		if len( nodes ) == 0: return None
		node = nodes.pop(0)
		if node.state == goal:
			moves = []
			temp = node
			while True:
				moves.insert(0, temp.operator)
				if temp.depth <= 1: break
				temp = temp.parent
			return moves				
		if node.depth < depth_limit:
			expanded_nodes = expand_node( node, nodes )
			expanded_nodes.extend( nodes )
			nodes = expanded_nodes

class Node:
	def __init__( self, state, parent, operator, depth, cost ):
		self.state = state
		self.parent = parent
		self.operator = operator
		self.depth = depth
		self.cost = cost

def readfile( filename ):
	f = open( filename )
	data = f.read()
	data = data.strip( "\n" )
	data = data.split( " " )
	state = [] 
	for element in data:
		state.append( int( element ) )
	return state

def main():
	starting_state = readfile( "input.txt" )
	display_board(starting_state)
	result = bfs( starting_state, goal_state )
	if result == None:
		print "No solution found"
	elif result == [None]:
		print "Start node was the goal!"
	else:
		print result
		print len(result), " moves"
	display_board(goal_state)

if __name__ == "__main__":
	main()
