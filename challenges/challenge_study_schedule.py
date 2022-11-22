def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    time_counter = 0
    if target_time is None or isinstance(target_time, tuple):
        return None
    for entry, leave in permanence_period:
        if (entry is None or leave is None) or (
            not isinstance(entry, int) or not isinstance(leave, int)
        ):
            return None
        if entry <= target_time and target_time <= leave:
            time_counter += 1
    return time_counter