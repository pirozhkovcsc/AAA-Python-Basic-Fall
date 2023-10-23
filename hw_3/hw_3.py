from typing import Iterable, List, Dict


class CountVectorizer:
    """Простая реализация класса CountVectorizer"""

    def __init__(self, lowercase: bool = True) -> None:
        self.lowercase = lowercase
        self.vocabulary: Dict[str, int] = {}

    def _tokenize(self, text: str) -> List[str]:
        """Токенизирует данный текст."""
        if self.lowercase:
            text = text.lower()
        # Разделяем текст по пробелам и убираем знаки препинания
        return [word.strip('.,!?()[]{}":;') for word in text.split()]

    def fit_transform(self, raw_documents: Iterable[str]) -> List[List[int]]:
        """Создает словарь и возвращает матрицу документ-терм."""
        # Поддерживаем счетчик, чтобы построить словарь
        counter = 0
        for row in raw_documents:
            for word in self._tokenize(row):
                if word not in self.vocabulary:
                    self.vocabulary[word] = counter
                    counter += 1

        matrix = [[0] * counter for _ in raw_documents]
        for row_ind, row in enumerate(raw_documents):
            for word in self._tokenize(row):
                if word in self.vocabulary:
                    matrix[row_ind][self.vocabulary[word]] += 1

        return matrix

    def get_feature_names(self) -> List[str]:
        """Возвращает имена признаков для преобразования."""
        return list(self.vocabulary.keys())


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
