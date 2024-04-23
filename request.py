#for Link Route Request Procedure of LAPRP
import math


class Node:
    def __init__(self, node_id, x, y):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.Zi = None
        self.rhoi = None


class RLRQMessage:
    def __init__(self, Sid, Did, Pi, Bid, Fri, Vi):
        self.Sid = Sid
        self.Did = Did
        self.Pi = Pi
        self.Bid = Bid
        self.Fri = Fri
        self.Vi = Vi


def reliable_link_route_request(Sid, Did, theta_i, front_relative_nodes, Pi, Vi, Bid, routing_table):
    # Initialization
    Pi = Bid = Vi = 0

    # Request to send data packet
    if has_path_to(Sid, Did, routing_table):
        forward_data_packets()
    else:
        # Broadcast RLRQ packet
        broadcast_RLRQ_packet(Sid, Did, Pi, Bid, front_relative_nodes, Vi)

        for node in routing_table:
            if has_path_to(node, Did, routing_table):
                # Receiving node is destination node or it has path to destination
                #insert snippet to skip to line 52
            elif node in front_relative_nodes:
                # If receiving node is front relative node
                Si = calculate_Si(node, Did)
                if Si >= Ts:
                    VRi, GDi = compute_VRi_GDi(node, Did)
                    composite_metric = compute_composite_metric(VRi, GDi)
                    if tau_i_expired(tau_i, threshold):
                        # τi has expired
                        update_rhoi()
                        rebroadcast_RLRQ_message()
            else:
                discard_packet()

            if node == Did:
                # Destination node receives RLRQ packet
                update_Zi()
                unicast_reliable_link_route_reply()


def forward_data_packets():
    # Forward data packets using information in ρi


def has_path_to(source, destination, routing_table):
    # Check if source_node has a path to destination_node
    # Check if the destination is present in the routing table of the source node
    if source in routing_table and destination in routing_table[source]:
        return True
    return False


def broadcast_RLRQ_packet(Sid, Did, Pi, Bid, Fri, Vi):
    # Broadcast RLRQ packet
    rlrq_message = RLRQMessage(Sid, Did, Pi, Bid, Fri, Vi)
    print("Broadcasting RLRQ packet:", rlrq_message)



def calculate_Si(node, Did):
    # Calculate Si (Signal Strength)
    distance = calculate_geographic_distance(node.x, node.y, Did.x, Did.y)
    path_loss = calculate_path_loss(distance)
    signal_strength = calculate_transmit_power() - path_loss
    return signal_strength


def calculate_path_loss(distance):
    # Calculate path loss using the Friis free space model
    frequency = 2.4 * 10**9  # Carrier frequency in Hz (2.4 GHz)
    c = 3 * 10**8  # Speed of light in m/s
    wavelength = c / frequency
    gain_tx = calculate_transmit_antenna_gain()
    gain_rx = calculate_receive_antenna_gain()

    path_loss = (wavelength / (4 * math.pi * distance))**2 / (gain_tx * gain_rx)
    return path_loss


def calculate_geographic_distance(x1, y1, x2, y2):
    # Calculate geographic distance between two points
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def calculate_transmit_power():
    # Calculate transmit power in dBm


def calculate_transmit_antenna_gain():
    # Calculate transmit antenna gain in dBi


def calculate_receive_antenna_gain():
    # Calculate receive antenna gain in dBi


def compute_VRi_GDi(node, Did):
    # Compute VRi (Virtual Relative Distance) and GDi (Geographic Distance)
    VRi = compute_VRi(node)
    GDi = calculate_geographic_distance(node.x, node.y, Did.x, Did.y)
    return VRi, GDi


def compute_VRi(node):
    # Compute VRi (Virtual Relative Distance)
    VRi = math.sqrt(node.x**2 + node.y**2)
    return VRi


def compute_composite_metric(VRi, GDi):
    # Compute composite metric for node selection
    composite_metric = theta_i * VRi + (1 - theta_i) * GDi
    return composite_metric


def tau_i_expired(tau_i, threshold):
    # Check if τi has expired based on threshold
    if tau_i >= threshold:
        return True
    return False


def update_rhoi():
    # Update ρi


def rebroadcast_RLRQ_message():
    # Rebroadcast RLRQ message


def discard_packet():
    # Discard packet


def update_Zi():
    # Update Zi


def unicast_reliable_link_route_reply():
    # Unicast reliable link route reply


# Example usage
node1 = Node("node1", 0, 0)
node2 = Node("node2", 1, 0)
node3 = Node("node3", 0, 1)
node4 = Node("node4", 1, 1)
node5 = Node("node5", 2, 2)
N = [node1, node2, node3, node4, node5]  # List of nodes
routing_table = {
    node1: [node2, node3],
    node2: [node1, node4],
    node3: [node1, node4],
    node4: [node2, node3, node5],
    node5: [node4]
}
theta_i = 0.5
Ts = 0
tau_i = 0
threshold = 0


reliable_link_route_request(node1, node5, theta_i, [node2, node3], 0, 0, 0, routing_table)
