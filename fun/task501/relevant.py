from shared.models import RelevantData


def precision(relevant, not_relevant):
    return relevant / float(relevant + not_relevant)


def count_relevant_data():
    relevants = ['google_relevant', 'bing_relevant', 'duckduckgo_relevant']

    results = {}
    for relevant_name in relevants:
        data = [int(x.is_relevant) for x in
                RelevantData.get_by_name(relevant_name)]
        true_positives = 0.
        _sum = 0.
        for nr, item in enumerate(data):
            if item and nr in range(len(data[:nr+1])):
                true_positives += 1.
                _sum += true_positives / nr if nr else _sum
        results[relevant_name] = _sum / len(data) if len(data) else 0.

    return results
