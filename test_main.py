import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self):
        fighand = plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        mean = 0
        for i in range(1,len(this_x)) :
             mean = mean + this_x[i] - this_x[i-1]
        mean = mean / (len(this_x)-1)

        bar = np.sqrt(1/(lamd*lamd)/(len(this_x)-1))*st.norm.ppf( (0.99 + 1) / 2 )
        self.assertTrue( np.fabs( mean - 1/lamd )<bar, "the times between the events do not seem to be distributed correctly" )
        
    def test_yplot(self) :
        fighand = plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(1,len(this_x)) :
            self.assertTrue( np.fabs( this_y[i]-this_y[i-1]-1 )<1e-7, "the y-coordinates in your graph are not correct"  )
