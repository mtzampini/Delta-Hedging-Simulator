import numpy as np
from scipy.stats import norm

class EuropeanCall:
    def __init__(self, S, K, T, r, sigma):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
    

    def d1_d2(self):
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return d1, d2
    
    def price(self):
        if self.T <= 0:
            return max(self.S - self.K, 0)
        d1, d2 = self.d1_d2()
        # Formula: S * N(d1) - K * e^(-rT) * N(d2)
        call_price = (self.S * norm.cdf(d1)) - (self.K * np.exp(-self.r * self.T)) * norm.cdf(d2)
        return call_price
    
    def delta(self):
        if self.T <= 0:
            return 1.0 if self.S > self.K else 0.0
        
        d1, _ = self.d1_d2()
        # Formula: delta(call) = N(d1)
        return norm.cdf(d1)
    
    def gamma(self):
        if self.T <= 0: return 0.0
        d1, _ = self.d1_d2()
        # Formula: N'(d1) / (S * sigma * sqrt(T))
        return norm.pdf(d1) / (self.S * self.sigma * np.sqrt(self.T))
    
    def theta(self):
        if self.T <= 0: return 0.0
        d1, d2 = self.d1_d2()
        
        term1 = - (self.S * self.sigma * norm.pdf(d1)) / (2 * np.sqrt(self.T))
        term2 = - self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        return term1 + term2