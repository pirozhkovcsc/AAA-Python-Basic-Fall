from typing import Iterable, List
from math import log
from hw_3 import CountVectorizer


class TfidTransformer:
    """
    В этом классе реализация матрицы tf * idf.
    """

    @staticmethod
    def _tf_transform(matrix: List[List[int]]) -> List[List[float]]:
        """
        Для каждого слова в каждом документе
        считаем долю вхождения слова среди всех
        слов в документе.
        """
        result_matrix = [
            [round(col / sum(row), 3) for col in row]
            for row in matrix
        ]

        return result_matrix

    @staticmethod
    def _idf_transform(matrix: List[List[int]]) -> List[float]:
        """
        Для каждого слова считаем метрику:
            ln((Всего документов + 1) / (Документов со словом + 1)) + 1.
        """
        docs_cnt, words_cnt = len(matrix), len(matrix[0])
        # здесь будем хранить результат метрики для каждого слова
        result = []

        for word in range(words_cnt):
            # считаем количество документов, где есть данное слово
            docs_with_word = sum(map(lambda doc: doc[word] > 0, matrix))
            metric = log((docs_cnt + 1) / (docs_with_word + 1)) + 1
            result.append(round(metric, 3))

        return result

    def fit_transform(self, matrix: List[List[int]]) -> List[List[float]]:
        """
        Получаем матрицу tf * idf.
        """
        tf_matrix = self._tf_transform(matrix)
        idf_matrix = self._idf_transform(matrix)

        result = [
            list(
                map(
                    lambda tfidf: round(tfidf[0] * tfidf[1], 3),
                    zip(row, idf_matrix)
                )
            )
            for row in tf_matrix
        ]

        return result


class TfidfVectorizer(CountVectorizer):
    """Тривиальная реализация класса TfidfVectorizer."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # здесь используем композицию
        self.transformer = TfidTransformer()

    def fit_transform(self, raw_documents: Iterable[str]) -> List[List[float]]:
        """
        Из документов получаем tf * idf матрицу.
        """
        # получаем матрицу документ-терм.
        count_matrix = super().fit_transform(raw_documents)

        return self.transformer.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
