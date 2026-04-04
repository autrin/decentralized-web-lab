
"""
A 3-node cluster that survives killing one process and still serves reads.

- node.py with a timer that "elections" every random 1-2 s.
- Broadcast "RequestVote" messages over local UDP sockets.
- Expand Raft nodes so the leader accepts SET key value and replicates it to followers.

"""
from enum import Enum
import random as rand

class State(Enum):
  FOLLOWER = "follower"
  CANDIDATE = "candidate"
  LEADER = "leader"

class Node:
  def __init__(self, id, state):
    self.id = id
    self.state = state
    self.vote = Node
    self.votes = 0
    self.peers = []
    self.leader = None

  def get_id(self):
    return self.id
  
  def get_state(self):
    return self.state
  
  def set_state(self, state):
    self.state = state

  def set_leader(self, leader):
    self.leader = leader

  def set_vote(self, vote):
    self.vote = vote
    
class Raft():
  def __init__(self, nodes):
    self.nodes = nodes
    self.current_term = 0

  def apply_vote(self):
    for node in self.nodes:
      if node.get_state() == State.FOLLOWER: # you can vote
        voted = node.vote
        self.nodes[voted.get_id()].votes += 1
    self.set_leader()

  def vote(self):
    # vote randomly
    for node in self.nodes:
      node.set_vote(rand.randint(0, 3))
      print(f"Node {node.get_id()} voted for {node.vote.get_id()}")
    self.apply_vote()

  def set_leader(self):
    votes = 0
    leader = Node(-1, State.LEADER)
    for node in self.nodes:
      # the leader is the node with highest votes
      if node.votes > votes:
        votes = node.votes
        leader = node
        node.set_state(State.LEADER)
    print(f"leader is {leader.get_id()}")
    for node in self.nodes:
      if node.get_state() != State.LEADER:
        node.set_leader(leader)

def main():
  try:
    nodes = [Node(0, State.FOLLOWER), Node(1, State.FOLLOWER), Node(2, State.FOLLOWER), Node(3, State.FOLLOWER)]
  except Exception as e:
    print("Error creating nodes: ", e)
    return -1
  try:
    raft = Raft(nodes)
    print("Starting voting...")
    raft.vote()
    return 0
  except Exception as e:
    print("Error running Raft: ", e)
    return -1

if __name__ == "__main__":
  main()