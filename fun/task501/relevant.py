from shared.models import RelevantData


def precision(relevant, not_relevant):
    return relevant / float(relevant + not_relevant)


def count_relevant_data():
    relevants = ['google_relevant', 'bing_relevant', 'duckduckgo_relevant']

    results = {}
    for relevant_name in relevants:
        data = [int(x.is_relevant) for x in
                RelevantData.get_by_name(relevant_name)]

        batch = 0, 5
        _sum = 0.
        div = 0
        print data
        while True:
            div += 1
            true_p, total = 0, 0

            short_data = data[batch[0]:batch[1]]
            if not short_data:
                break

            res = range(len(short_data))
            m_j = [nr for nr, x in enumerate(short_data) if x]
            for nr, d in enumerate(res):
                if nr in m_j and nr in res[:nr+1]:
                    true_p += 1.
                    total += true_p

            _sum += total / len(m_j) if m_j else 0.
            batch = [x + 5 for x in batch]
        results[relevant_name] = _sum / div if div else _sum

    return results
