def get_statistics(input_list):
    sorted_input = sorted(input_list)
    input_length = len(input_list)

    mean = sum(sorted_input) / input_length

    middle_idx = (len(sorted_input) - 1) // 2
    median = sorted_input[middle_idx]

    if input_length % 2 == 0:
        middle_number_1 = sorted_input[middle_idx]
        middle_number_2 = sorted_input[middle_idx + 1]
        median = (middle_number_1 + middle_number_2) / 2

    number_counts = {x: sorted_input.count(x) for x in set(sorted_input)}
    mode = max(number_counts.keys(), key=lambda unique_number: number_counts[unique_number])

    sample_variance = sum([(number - mean) **2 / (input_length - 1) for number in sorted_input])

    sample_standard_deviation = sample_variance ** 0.5

    mean_standard_error = sample_standard_deviation / input_length ** 0.5
    z_score_standard_error = 1.96  * mean_standard_error
    mean_confidence_interval = [mean - z_score_standard_error, mean + z_score_standard_error]
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }
