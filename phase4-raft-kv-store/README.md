A 3-node cluster that survives killing one process and still serves reads.

- node.py with a timer that "elections" every random 1-2 s.
- Broadcast "RequestVote" messages over local UDP sockets.
- Expand Raft nodes so the leader accepts SET key value and replicates it to followers.
