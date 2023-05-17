from ting_file_management.file_process import create_file_out


def find_word(lines, word):
    occurrences = [{"linha": line_number} for line_number, 
                   line in enumerate(lines, start=1) if word.lower() in line.lower()]
    return occurrences


def exists_word(word, instance):
    all_occurrences = []
    for file_path in instance.list:
        file_info = create_file_out(file_path)
        occurrences = find_word(file_info["linhas_do_arquivo"], word)
        if occurrences:
            all_occurrences.append({
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return all_occurrences


def search_by_word(word, instance):
    results = []
    for file_path in instance.list:
        file_info = create_file_out(file_path)
        occurrences = find_word(file_info["linhas_do_arquivo"], word)
        if occurrences:
            file_results = {
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": [
                    {
                        "linha": occurrence["linha"],
                        "conteudo": file_info[
                            "linhas_do_arquivo"][occurrence["linha"] - 1].strip()
                    }
                    for occurrence in occurrences
                ]
            }
            results.append(file_results)
    return results

