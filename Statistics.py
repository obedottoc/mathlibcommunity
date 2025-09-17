#Write your code here
import math
class Statistics:
    def z_test(sample_mean, population_mean, standard_deviation, sample_size):
        """
        One-sample Z-test statistic
        """
        return (sample_mean - population_mean) / (standard_deviation / math.sqrt(sample_size))

    def t_test(sample_mean, population_mean, sample_standard_deviation, sample_size):
        """
        One-sample T-test statistic
        """
        return (sample_mean - population_mean) / (sample_standard_deviation / math.sqrt(sample_size))

    def chi_square_test(observed, expected):
        """
        Chi-square statistic
        """
        return (observed - expected) ** 2 / expected

    def f_test(variance1, variance2):
        """
        F-test statistic
        """
        return variance1 / variance2
      
    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    @staticmethod
    def variance(data, sample=False):
        mean_val = Statistics.mean(data)
        squared_diffs = [(x - mean_val) ** 2 for x in data]

        if sample:
            return sum(squared_diffs) / (len(data) - 1)
        else:
            return sum(squared_diffs) / len(data)
    
    @staticmethod
    def std(data, sample=False):
        return math.sqrt(Statistics.variance(data, sample=sample))


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(Statistics.mean(data))
print(Statistics.median(data))
print(Statistics.variance(data))
print(Statistics.std(data))
print(Statistics.variance(data, sample=True))
print(Statistics.std(data, sample=True)) 

