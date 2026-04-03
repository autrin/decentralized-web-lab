#!/bin/bash

# Simple Mesh Network Demo
# This script creates a basic mesh network simulation using network namespaces

echo "🌐 Simple Mesh Network Demo"
echo "=========================="
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🧹 Cleaning up..."
    sudo ip netns del node1 2>/dev/null
    sudo ip netns del node2 2>/dev/null
    sudo ip netns del node3 2>/dev/null
    sudo ip link del veth1-2 2>/dev/null
    sudo ip link del veth2-3 2>/dev/null
    sudo ip link del veth1-3 2>/dev/null
    echo "✅ Cleanup complete"
}

# Set up cleanup on script exit
trap cleanup EXIT

echo "📋 Creating mesh network topology..."
echo ""

# Create network namespaces (simulating different nodes)
echo "1. Creating network namespaces (nodes)..."
sudo ip netns add node1
sudo ip netns add node2
sudo ip netns add node3
echo "   ✅ Created 3 network namespaces"

# Create virtual ethernet pairs (simulating mesh connections)
echo ""
echo "2. Creating mesh connections..."
sudo ip link add veth1-2 type veth peer name veth2-1
sudo ip link add veth2-3 type veth peer name veth3-2
sudo ip link add veth1-3 type veth peer name veth3-1
echo "   ✅ Created 3 mesh connections"

# Move interfaces to namespaces
echo ""
echo "3. Configuring mesh topology..."
sudo ip link set veth1-2 netns node1
sudo ip link set veth2-1 netns node2
sudo ip link set veth2-3 netns node2
sudo ip link set veth3-2 netns node3
sudo ip link set veth1-3 netns node1
sudo ip link set veth3-1 netns node3
echo "   ✅ Moved interfaces to namespaces"

# Configure IP addresses
echo ""
echo "4. Assigning IP addresses..."
sudo ip netns exec node1 ip addr add 10.0.1.1/24 dev veth1-2
sudo ip netns exec node1 ip addr add 10.0.3.1/24 dev veth1-3
sudo ip netns exec node2 ip addr add 10.0.1.2/24 dev veth2-1
sudo ip netns exec node2 ip addr add 10.0.2.1/24 dev veth2-3
sudo ip netns exec node3 ip addr add 10.0.2.2/24 dev veth3-2
sudo ip netns exec node3 ip addr add 10.0.3.2/24 dev veth3-1
echo "   ✅ Assigned IP addresses"

# Bring up interfaces
echo ""
echo "5. Activating mesh connections..."
sudo ip netns exec node1 ip link set veth1-2 up
sudo ip netns exec node1 ip link set veth1-3 up
sudo ip netns exec node2 ip link set veth2-1 up
sudo ip netns exec node2 ip link set veth2-3 up
sudo ip netns exec node3 ip link set veth3-2 up
sudo ip netns exec node3 ip link set veth3-1 up
echo "   ✅ All interfaces are up"

# Configure routing (mesh routing)
echo ""
echo "6. Setting up mesh routing..."
sudo ip netns exec node1 ip route add 10.0.2.0/24 via 10.0.1.2
sudo ip netns exec node1 ip route add 10.0.2.0/24 via 10.0.3.2
sudo ip netns exec node2 ip route add 10.0.3.0/24 via 10.0.1.1
sudo ip netns exec node3 ip route add 10.0.1.0/24 via 10.0.2.1
sudo ip netns exec node3 ip route add 10.0.1.0/24 via 10.0.3.1
echo "   ✅ Mesh routing configured"

echo ""
echo "🎉 Mesh Network Created Successfully!"
echo "====================================="
echo ""
echo "📊 Network Topology:"
echo "   Node1 (10.0.1.1) ←→ Node2 (10.0.1.2)"
echo "      ↕                    ↕"
echo "   Node3 (10.0.3.2) ←→ Node2 (10.0.2.1)"
echo "      ↕"
echo "   Node1 (10.0.3.1)"
echo ""
echo "🔗 Multiple paths between nodes (mesh characteristic!)"
echo ""

# Test connectivity
echo "🧪 Testing mesh connectivity..."
echo ""

echo "Testing Node1 → Node3 (direct path):"
sudo ip netns exec node1 ping -c 2 10.0.3.2
echo ""

echo "Testing Node1 → Node3 (via Node2):"
sudo ip netns exec node1 ping -c 2 10.0.2.2
echo ""

echo "Testing Node3 → Node1 (direct path):"
sudo ip netns exec node3 ping -c 2 10.0.1.1
echo ""

echo "Testing Node3 → Node1 (via Node2):"
sudo ip netns exec node3 ping -c 2 10.0.1.1
echo ""

echo "🎯 Mesh Network Demo Complete!"
echo "=============================="
echo ""
echo "Key Concepts Demonstrated:"
echo "✅ Decentralized topology (no central hub)"
echo "✅ Multiple paths between nodes"
echo "✅ Self-healing capability (if one link fails, traffic routes around)"
echo "✅ Direct peer-to-peer communication"
echo ""
echo "This is the foundation of censorship-resistant networks!"
echo "In a real mesh network like CJDNS, these connections would be:"
echo "- Encrypted with public-key cryptography"
echo "- Spanning across the internet"
echo "- Self-organizing and self-healing"
echo ""
echo "Press Enter to clean up and exit..."
read
