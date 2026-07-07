def to_hms(total_seconds):
    hours = total_seconds // 3600
    leftover = total_seconds % 3600
    minutes = leftover // 60
    seconds = leftover % 60
    return (hours, minutes, seconds)
if __name__ == "__main__":
    print(to_hms(3660))
    print(to_hms(59))

