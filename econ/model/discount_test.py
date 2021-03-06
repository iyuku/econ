# Copyright (c) 2005, Rufus Pollock. All Rights Reserved
# Licensed under the GNU Public License (GPL) v2.0
# See the LICENSE file in the root of the distribution for details

from econ.model.discount import *
import econ.data

class TestDiscountRate:
    
    def testDiscountRateConstant(self):
        drc1 = DiscountRateConstant()
        # default rate is 1 so present value always 1
        assert drc1.getDiscount(5) == 1, "PV should be 1"
        drc1.setUnitDiscountRate(1/1.02)
        assert drc1.getUnitDiscountRate() == 1/1.02
        
        assert drc1.getDiscount(0) == 1, "PV when time elapsed is 0 should be 1"
        assert drc1.getDiscount(1) == 1/1.02
        
        assert drc1.getReturn(1) == 1.02
    
    def testGetSet(self):
        rate1 = 1.0/1.02
        rate2 = 1.0/1.05
        drc1 = DiscountRateConstant(1.0/1.02)
        out1 = drc1.getUnitDiscountRate()
        assert rate1 == out1
        
        drc1.setUnitDiscountRate(rate2)
        out2 = drc1.getUnitDiscountRate()
        assert rate2 == out2

class TestDiscountRateHistorical:
    
    @classmethod
    def setup_class(self):
        dataPoints = [(1850, 10.9), (1990,497.6), (2002, 695.1)]
        ts1 = econ.data.TimeSeries(dataPoints)
        self.discounter = DiscountRateHistorical(ts1)
    
    def test1(self):
        out1 = self.discounter.getReturn(1850, 2002)
        exp1 = 695.1 / 10.9
        assert round(out1-exp1, 6) == 0
