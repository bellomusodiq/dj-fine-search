from .text_sims import TextSimilarity


def perform_search(model, search_text, fields=None):
    """
    word based filtering
    input: model, query_string, fields=None|fields to search from
    """
    if not search_text:
        return []
    if not isinstance(fields, list) and not isinstance(fields, tuple):
        raise ValueError('fields arguments should be a list or tuple')
    for field in fields:
        if not hasattr(model, field):
            raise AttributeError('{} does not have {} object'.format(model.__name__, field))
    queryset = model.objects.all()        
    filtered_list = []
    for query in queryset:
        query_list = []
        for field in fields:
            if field is not None:
                query_list.append(getattr(query, field))
        query_text = " ".join(query_list)
        score = TextSimilarity(query_text, search_text)
        score = score.evaluate()
        if score > 0:
            filtered_list.append((query, score))

    filtered_list = sorted(filtered_list, key=lambda query: query[1], reverse=True)
    filtered_list = [result[0] for result in filtered_list]
    return filtered_list
    
