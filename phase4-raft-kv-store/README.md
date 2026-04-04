
So far a simple Raft implementation that randomly elects a leader every 1-2 seconds that is not distributed and does not handle failures.
TODO A 3-node cluster that survives killing one process and still serves reads.

- node.py with a timer that "elections" every random 1-2 s.
- TODO Broadcast "RequestVote" messages over local UDP sockets.
- TODO Expand Raft nodes so the leader accepts SET key value and replicates it to followers.
