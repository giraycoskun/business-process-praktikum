# ============================================================================
# CUSTOM SIMPLICITY METRICS
# ============================================================================


def custom_simplicity_metric_1(petri_net):
    """
    Simplicity Metric 1: Structural Complexity Ratio

    Measures the ratio of (places + transitions) to the number of arcs.
    Lower values indicate higher complexity (more connections relative to nodes).

    Formula: (|P| + |T|) / |F|
    where P = places, T = transitions, F = arcs
    """
    places = len(petri_net.places)
    transitions = len(petri_net.transitions)
    arcs = len(petri_net.arcs)

    if arcs == 0:
        raise ValueError("The Petri net has no arcs; cannot compute complexity ratio.")

    # Normalize to 0-1 scale (higher is simpler)
    complexity_ratio = (places + transitions) / arcs
    # Typical Petri nets have ratio between 0.3-0.7, normalize accordingly
    normalized = min(1.0, complexity_ratio / 0.7)

    return {
        "metric_name": "Structural Complexity Ratio",
        "raw_value": complexity_ratio,
        "normalized_value": normalized,
        "places": places,
        "transitions": transitions,
        "arcs": arcs,
        "interpretation": "Higher values indicate simpler structure",
    }


def custom_simplicity_metric_2(petri_net):
    """
    Simplicity Metric 2: Average Node Degree

    Measures the average number of connections per node (place or transition).
    Lower average degree indicates simpler, more linear processes.

    Formula: 2 * |F| / (|P| + |T|)
    (Factor of 2 because each arc connects two nodes)
    """
    places = len(petri_net.places)
    transitions = len(petri_net.transitions)
    arcs = len(petri_net.arcs)

    total_nodes = places + transitions
    if total_nodes == 0:
        raise ValueError("The Petri net has no nodes; cannot compute average degree.")

    # Average degree
    avg_degree = (2 * arcs) / total_nodes

    # Normalize (typical values range from 2-6, invert so higher = simpler)
    normalized = max(0, 1 - (avg_degree - 2) / 4)

    return {
        "metric_name": "Average Node Degree",
        "raw_value": avg_degree,
        "normalized_value": normalized,
        "total_nodes": total_nodes,
        "interpretation": "Lower degree (higher normalized value) indicates simpler structure",
    }
