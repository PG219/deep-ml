import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """

    n = data.shape[0]
    s = np.random.default_rng(seed)

    shuffled_indices = s.permutation(n)

    train_end = int(n*train_frac)

    val = train_end + int(n*validation_frac)

    shuffled_data = data[shuffled_indices]

    train = shuffled_data[:train_end]

    validation = shuffled_data[train_end:val]

    test = shuffled_data[val:]


    return [train,validation,test]


    