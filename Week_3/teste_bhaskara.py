import Bhaskara
import pytest

class TestBhaskara:
    
  
    '''
    def testa_uma_raiz(self):
        b == Bhaskara.Bhaskara()        
        assert b.calcula_raizes(1, 0, 0) == (1,0)      
       
    def testa_duas_raiz(self:
        b == Bhaskara.Bhaskara()
        assert b.calcula_raizes(1, -5, 6) == (2,3,2)
       
    def testa_zero_raiz(self, b):
        b == Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 10, 10) == 0

    def testa_raiz_negativa(self, b):
        b == Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
    '''

    '''
    @pytest.fixture
    def b(self):
        return Bhaskara.Bhaskara()
    
    def testa_uma_raiz(self, b):
        assert b.calcula_raizes(1, 0, 0) == (1,0)      
        
    def testa_duas_raiz(self, b):
        assert b.calcula_raizes(1, -5, 6) == (2,3,2)

    def testa_zero_raiz(self, b):
        assert b.calcula_raizes(10, 10, 10) == 0

    def testa_raiz_negativa(self, b):
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
    '''

#    '''
    @pytest.mark.parametrize("entrada","esperado", [
        (1,0,0),(1,0)
         ])
                             
    def teste_calcula_raizes(entrada, esperado):
        assert calcula_raizes(entrada) == esperado
#    '''
<<<<<<< HEAD:Week_three/teste_bhaskara.py
                        












        
        
=======


>>>>>>> 01012211f281246f0b4468d3d532bfdb38574893:Week_3/teste_bhaskara.py
