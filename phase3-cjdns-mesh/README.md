# Phase 3: Simple Mesh Simulation (No CJDNS)

This folder contains a **safe mesh-network simulation** that demonstrates the
core ideas behind censorship-resistant mesh networks without running CJDNS or
Docker images.

## What this simulation does

The script `simple-mesh-demo.sh`:
- Creates **three isolated network namespaces** (`node1`, `node2`, `node3`)
- Connects them with **virtual Ethernet links** (veth pairs)
- Assigns **private IPs** on three subnets:
  - `10.0.1.0/24` (node1 ↔ node2)
  - `10.0.2.0/24` (node2 ↔ node3)
  - `10.0.3.0/24` (node1 ↔ node3)
- Adds **multiple routes** so there is more than one path between nodes
- Runs **ping tests** to show connectivity over different paths
- **Cleans up** all namespaces and links on exit

This demonstrates:
- Decentralized topology (no central hub)
- Multiple paths between nodes
- Self-healing behavior (alternate paths)
- Peer-to-peer connectivity

## Run the demo

```bash
cd /home/autrin/decentralized-web-lab/phase3-cjdns-mesh
./simple-mesh-demo.sh
```

Press **Enter** when prompted to clean up and exit.

## Notes

- This is **not CJDNS**. It is a controlled, local simulation of mesh concepts.
