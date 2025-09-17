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