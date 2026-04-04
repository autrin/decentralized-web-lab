
"""
So far a simple Raft implementation that randomly elects a leader every 1-2 seconds that is not distributed and does not handle failures.
TODO A 3-node cluster that survives killing one process and still serves reads.

- node.py with a timer that "elections" every random 1-2 s.
- TODO Broadcast "RequestVote" messages over local UDP sockets.
- TODO Expand Raft nodes so the leader accepts SET key value and replicates it to followers.

"""
from enum import Enum
import random as rand
import select
import sys
import termios
import time
import tty
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
    # reset votes from previous election
    for node in self.nodes:
      node.votes = 0
    # vote randomly
    for node in self.nodes:
      node.set_vote(self.nodes[rand.randint(0, 3)])
      print(f"Node {node.get_id()} voted for {node.vote.get_id()}")
    self.apply_vote()
  def set_leader(self):
    for node in self.nodes:
        if node.get_state() == State.LEADER:
          node.set_state(State.FOLLOWER)
        node.set_leader(None)
    max_votes = 0
    leader = Node(-1, State.LEADER)
    for node in self.nodes:
      # the leader is the node with highest votes
      if node.votes > max_votes:
        max_votes = node.votes
        leader = node
    leader.set_state(State.LEADER)
    print(f"leader is {leader.get_id()}")
    for node in self.nodes:
      if node.get_state() != State.LEADER:
        node.set_leader(leader)
def should_quit(timeout=0.1):
  ready, _, _ = select.select([sys.stdin], [], [], timeout)
  if not ready:
    return False
  return sys.stdin.read(1).lower() == 'q'
def main():
  print("Press 'q' to quit.")
  stdin_fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(stdin_fd)
  try:
    tty.setcbreak(stdin_fd)
    try:
      nodes = [Node(0, State.FOLLOWER), Node(1, State.FOLLOWER), Node(2, State.FOLLOWER), Node(3, State.FOLLOWER)]
    except Exception as e:
      print("Error creating nodes: ", e)
      raise e
    while(True):
      try:
        raft = Raft(nodes)
        print("Starting voting...")
        election_delay = rand.randint(1, 2)
        end_time = time.time() + election_delay
        while time.time() < end_time:
          if should_quit():
            return 0
        raft.vote()
      except Exception as e:
        print("Error running Raft: ", e)
        raise e
  finally:
    termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_settings)
if __name__ == "__main__":
  main()
  