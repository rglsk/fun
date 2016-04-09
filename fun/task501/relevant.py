from shared.models import RelevantData


def save_relevant_data(data):
    for name, is_relevant in data.iteritems():
        RelevantData.create_or_update(name=name, is_relevant=is_relevant)


def precision(relevant, not_relevant):
    return relevant / float(relevant + not_relevant)

def recall(relevant, not_relevant):
    pass


def count_relevant_data():
    relevants = ['google_relevant', 'bing_relevant', 'duckduckgo_relevant']

    for relevant_name in relevants:
        relevant = RelevantData.get_by_name(relevant_name)

        relevant_count = relevant.relevant_count
        not_relevant_count = relevant.not_relevant_count
        Q = relevant_count + not_relevant_count

        _sum = 0
        for q in xrange(Q):
            _sum += 1 / relevant_count
