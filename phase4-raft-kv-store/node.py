"""
A 3-node cluster that survives killing one process and still serves reads.

- node.py with a timer that "elections" every random 1-2 s.
- Broadcast "RequestVote" messages over local UDP sockets.
- Expand Raft nodes so the leader accepts SET key value and replicates it to followers.

"""

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
    
class Raft():
  def __init__(self, nodes):
    self.nodes = nodes
    self.current_term = 0
    self.voted_for = None

  def apply_vote(self):
    for node in self.nodes:
      if node.state == "follower": # you can vote
        voted = node.vote
        self.nodes[voted.get_id()].votes += 1

  def vote(self):
    pass

  def set_leader(self):
    votes = 0
    for node in self.nodes:
      # the leader is the node with highest votes
      if node.votes > votes:
        votes = node.votes
        self.leader = node

def main():

  return 0