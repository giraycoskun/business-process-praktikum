from collections import defaultdict, deque

# ============================================================================
# CUSTOM SIMPLICITY METRICS
# ============================================================================


def compute_reachability(petri_net):
    """
    Computes reachability for a Petri net using BFS on the bipartite graph.
    Returns: dict[node] = set(nodes reachable from node]
    """
    # Build adjacency list (graph of places + transitions)
    adj = defaultdict(set)

    # Add arcs both ways (Petri nets are bipartite but directed)
    for place in petri_net.places:
        for arc in place.out_arcs:
            adj[place].add(arc.target)
        for arc in place.in_arcs:
            adj[arc.source].add(place)

    for t in petri_net.transitions:
        for arc in t.out_arcs:
            adj[t].add(arc.target)
        for arc in t.in_arcs:
            adj[arc.source].add(t)

    # Compute reachability via BFS for each node
    reachability = {}
    for node in list(petri_net.places) + list(petri_net.transitions):
        visited = set()
        queue = deque([node])

        while queue:
            current = queue.popleft()
            for nxt in adj[current]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        reachability[node] = visited
    
    return reachability


def simplicity_metric_separability(petri_net):
    """
    Computes the Separability simplicity metric for a Petri net.
    Separability = (# node pairs with no path in either direction) / (total pairs)
    """
    nodes = list(petri_net.places) + list(petri_net.transitions)
    n = len(nodes)
    
    reach = compute_reachability(petri_net)

    separable_pairs = 0
    total_pairs = n * (n - 1) / 2

    # Count separable pairs
    for i in range(n):
        for j in range(i+1, n):
            a, b = nodes[i], nodes[j]

            # No path from a→b and no path from b→a
            if (b not in reach[a]) and (a not in reach[b]):
                separable_pairs += 1

    metric = separable_pairs / total_pairs
    normalized = metric  # already between 0-1

    return {
        "metric_name": "Separability",
        "raw_value": metric,
        "normalized_value": normalized,
        "interpretation": "Lower values indicate simpler structure",
    }


def simplicity_metric_node_degree(petri_net):
    """
    Computes the average node degree of a Petri net:
    (sum of all in/out arcs) / (number of nodes)

    Parameters
    ----------
    net : PetriNet
        The Petri net object from pm4py.

    Returns
    -------
    float
        The average degree of the net.
    """

    # Count nodes (places + transitions)
    places = petri_net.places
    transitions = petri_net.transitions
    num_nodes = len(places) + len(transitions)

    # Count incoming/outgoing arcs for each node
    total_degree = 0

    for place in places:
        total_degree += len(place.in_arcs) + len(place.out_arcs)

    for t in transitions:
        total_degree += len(t.in_arcs) + len(t.out_arcs)

    avg_degree= total_degree / num_nodes
    normalized = max(0, 1 - (avg_degree - 2) / 4)
    return {
        "metric_name": "Average Node Degree",
        "raw_value": avg_degree,
        "normalized_value": normalized,
        "total_nodes": num_nodes,
        "interpretation": "Lower degree (higher normalized value) indicates simpler structure",
    }
