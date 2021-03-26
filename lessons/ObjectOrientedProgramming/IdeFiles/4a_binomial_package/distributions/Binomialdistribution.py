import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials

    """

    def __init__(self, prob=.5, size=20):
        self.p = prob
        self.n = size
        mean = self.calculate_mean()
        stdev = self.calculate_stdev()

        Distribution.__init__(self, mean, stdev)

    def calculate_mean(self):

        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """

        self.mean = self.n * self.p

        return self.mean



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))

        return self.stdev


    def replace_stats_with_data(self):

        """Function to calculate p and n from the data set

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        self.n = len(self.data)
        self.p = sum(self.data) / self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        ones = self.p * self.n
        plt.bar([0,1], [self.n - ones, ones], tick_label = ['Failure', 'Success'])
        plt.title('Histogram of Data')
		# plt.xlabel('Data')
		# plt.ylabel('Count')

    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        return (math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n-k)) * \
                (self.p**k) * (1 - self.p)**(self.n - k))

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        x = [x for x in range(self.n + 1)]
        y = [self.pdf(self, k) for k in x]

        plt.bar[x, y]
        plt.title['PDF of Binomial Distribution']
        plt.xlabel['Values of k']
        plt.ylabel['Probability']

    def __add__(self, other):

        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        return Binomial(prob  = self.p, size = self.n + other.n)


    def __repr__(self):

        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """
        return f'mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}'
