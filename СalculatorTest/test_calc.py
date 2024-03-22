from decimal import DivisionByZero
import pytest
import calc

class TestSum:
    @pytest.mark.parametrize("val_1, val_2, result", [(0, 1, 1),
                                                      (-1, -5, -6),
                                                      (-100, 100, 0)])
    def test_int(self, val_1, val_2, result):
        assert calc.sum(val_1, val_2) == result

    @pytest.mark.parametrize("val_1, val_2, result", [(0, 1.5, 1.5),
                                                      (-2, -1.2, -3.2),
                                                      (-100.2, 100.2, 0),
                                                      (1.4742678526459834, 2.1536543697542356, 3.627922222400219),
                                                      (1.474267852645983455, 2.153654369754235644, 3.6279222224002191)])    
    def test_single(self, val_1, val_2, result):
        assert calc.sum(val_1, val_2) == result

    @pytest.mark.parametrize("val_1, val_2", [('1', 1.5),
                                              (2, '1'),
                                               ('1', '1')]) 
    def test_isNotNumberException(self, val_1, val_2):
        with pytest.raises(TypeError):    
            calc.sum(val_1, val_2) #Is not a number
            
class TestMul:
    @pytest.mark.parametrize("val_1, val_2, result", [(0, 1, 0),
                                                      (-1, -5, 5),
                                                      (-100, 100, -10000)])
    def test_int(self, val_1, val_2, result):
        assert calc.mul(val_1, val_2) == result

    @pytest.mark.parametrize("val_1, val_2, result", [(4, 1.5, 6),
                                                      (-2, -1.2, 2.4),
                                                      (-3.2, 5.2, -16.64),
                                                      (1.4742678526459834, 2.1536543697542356, 3.1750634030392157)])    
    def test_single(self, val_1, val_2, result):
        assert calc.mul(val_1, val_2) == result

    @pytest.mark.parametrize("val_1, val_2", [('1', 1.5),
                                              (2, '1'),
                                               ('1', '1')]) 
    def test_isNotNumberException(self, val_1, val_2):
        with pytest.raises(TypeError):    
            calc.mul(val_1, val_2) #Is not a number
            
class TestDiv:
    @pytest.mark.parametrize("val_1, val_2, result", [(0, 1, 0),
                                                      (-1, -5, 0.2),
                                                      (-100, 100, -1)])
    def test_int(self, val_1, val_2, result):
        assert calc.div(val_1, val_2) == result

    @pytest.mark.parametrize("val_1, val_2, result", [(1, 1.5, 1.5),
                                                      (-2, -0.8, 2.5),
                                                      (-100.2, 100.2, -1),
                                                      (1.4742678526459834, 2.1536543697542356, 0.6845424564639959)])    
    def test_single(self, val_1, val_2, result):
        assert calc.div(val_1, val_2) == result

    @pytest.mark.parametrize("val_1, val_2", [('1', 1.5),
                                              (2, '1'),
                                               ('1', '1')]) 
    def test_isNotNumberException(self, val_1, val_2):
        with pytest.raises(TypeError):    
            calc.div(val_1, val_2) #Is not a number
     
    def test_divisionByZero(self):
        with pytest.raises(ZeroDivisionError):    
            calc.div(25, 0)

class TestSub:
    @pytest.mark.parametrize("val_1, val_2, result", [(0, 1, -1),
                                                      (-1, -5, 4),
                                                      (-100, 100, -200)])
    def test_int(self, val_1, val_2, result):
        assert calc.sub(val_1, val_2) == result

    @pytest.mark.parametrize("val_1, val_2, result", [(1, 1.5, -0.5),
                                                      (-2, -0.8, -1.2),
                                                      (-100.2, 100.2, -200.4),
                                                      (1.4742678526459834, 2.1536543697542356, -0.6793865171082522),
                                                      (1.474267852645983455, 2.153654369754235644, -0.6793865171082522)])    
    def test_single(self, val_1, val_2, result):
        assert calc.sub(val_1, val_2) == result

    @pytest.mark.parametrize("val_1, val_2", [('1', 1.5),
                                              (2, '1'),
                                               ('1', '1')]) 
    def test_isNotNumberException(self, val_1, val_2):
        with pytest.raises(TypeError):    
            calc.sub(val_1, val_2) #Is not a number       

        

    

