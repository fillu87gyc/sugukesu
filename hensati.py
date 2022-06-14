from math import sqrt


def calc_sum(data: list) -> int:
    """合計値を出すやつ

    Args:
        data: list<int>
        入力のデータ列. 配列で入れてね

    Return:
        result: int
        合計値
    """
    result: int = 0
    for d in data:
        result += d

    return result


def calc_standard_deviation(data_list: list, mean: float) -> float:
    """

    Args:
        data_list: list
        成績データ列
        mean: float
        平均値

    Returns: float
        標準偏差
    """
    squared_sum: int = 0  # 最後にルートするやつ
    N: int = len(data_list)  # データの数
    for data in data_list:
        squared_sum += (mean-data) * (mean-data)
    return sqrt((1/N)*(squared_sum))


def calc_HENSATI(data: int, mean: float, sd: float) -> float:
    """

    Args:
        data: その人の成績
        mean: 平均値
        sd: 標準偏差

    Returns: 偏差値
    """
    # 偏差値 = (点数 - 平均点) ÷ 標準偏差 × 10 + 50
    return ((data - mean) / sd) * 10 + 50


def main(args=None) -> None:
    N = int(input('データの個数を入力'))
    data = list()
    for i in range(N):
        tmp = int(input(str(i+1)+'個目のデータ'))
        data.append(tmp)
    print(data)
    sum: int = calc_sum(data)
    mean = sum / N
    sd: float = calc_standard_deviation(data, mean)
    print('Ans. '+str(calc_HENSATI(
        data=data[0],
        mean=mean,
        sd=sd)))


if __name__ == "__main__":
    main()
