def exists_word(word, instance):
    result = []
    queue_length = len(instance)
    for queue_index in range(queue_length):
        data = instance.search(queue_index)
        if isinstance(data, dict):
            lines = data.get('linhas_do_arquivo', [])
            occurrences = []
            for line_idx, line_content in enumerate(lines, 1):
                if word.lower() in line_content.lower():
                    occurrences.append({"linha": line_idx})
            if occurrences:
                result.append({
                    "palavra": word,
                    "arquivo": data.get('nome_do_arquivo', ''),
                    "ocorrencias": occurrences
                })
    return result


def search_by_word(word, instance):
    result = []
    queue_length = len(instance)
    for queue_index in range(queue_length):
        data = instance.search(queue_index)
        if isinstance(data, dict):
            lines = data.get('linhas_do_arquivo', [])
            occurrences = []
            for line_idx, line_content in enumerate(lines, 1):
                if word.lower() in line_content.lower():
                    occurrences.append({
                        "linha": line_idx,
                        "conteudo": line_content
                    })
            if occurrences:
                result.append({
                    "palavra": word,
                    "arquivo": data.get('nome_do_arquivo', ''),
                    "ocorrencias": occurrences
                })
    return result
