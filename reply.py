# for Link Route Reply Procedure 

import math


class Node:
    def __init__(self, node_id, x, y):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.Zi = None


class RLRPMessage:
    def __init__(self, source_id, destination_id, bid):
        self.source_id = source_id
        self.destination_id = destination_id
        self.bid = bid


def reliable_link_route_reply(Sid, Did, Bid):
    for node in N:
        if node.node_id == Sid:
            forward_data_packets()
        else:
            # Update forward route entry
            update_Zi(node, Did)
            unicast_RLRP(node, Sid, Did, Bid)
            # Go to step 3


def forward_data_packets():
    # Forward data packets in the available path


def update_Zi(node, Did):
    # Update Zi (forward route entry)
    node.Zi = calculate_next_hop(node, Did)


def unicast_RLRP(sender, Sid, Did, Bid):
    # Perform unicast RLRP from sender to the next hop
    next_hop = sender.Zi
    rlrp_message = RLRPMessage(Sid, Did, Bid)
    print(f"Unicasting RLRP from {sender.node_id} to {next_hop.node_id}: {rlrp_message}")


def calculate_next_hop(source_node, destination_node):
    min_distance = float('inf')
    next_hop = None

    for node in N:
        if node.node_id != source_node.node_id:
            distance = calculate_distance(node.x, node.y, destination_node.x, destination_node.y)
            if distance < min_distance and distance <= max_transmission_range:
                min_distance = distance
                next_hop = node

    return next_hop


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# Create network nodes
node1 = Node(1, 0, 0)
node2 = Node(2, 100, 100)
node3 = Node(3, 200, 200)
node4 = Node(4, 300, 300)
node5 = Node(5, 400, 400)

N = [node1, node2, node3, node4, node5]
Sid = 1
Did = node5  
Bid = -64  # Assumed this reception threshold in dBm
max_transmission_range = 250  # Assumed maximum transmission range in meters

reliable_link_route_reply(Sid, Did, Bid)
