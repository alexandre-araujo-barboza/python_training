import abc

class Veiculo(abc.ABC):
  def __init__(self, cavalos: int, torque: float, marca: str, modelo: str) -> None:
    self._cavalos = cavalos
    self._torque = torque
    self._marca = marca
    self._modelo = modelo
    print('Veiculo criado com:')
    print(f'\tcavalos: {cavalos}')
    print(f'\ttorque: {torque}')
    print(f'\tMarca: {marca}')
    print(f'\tModelo: {modelo}')
  
  def __call__(self, func):
    def inner(*args, **kwargs):
      results = func(*args, **kwargs)
      print('Veiculo chamado com:')
      for i, arg in enumerate(args):
        print(f'\targ_{i}: {arg}')
      return results
    return inner
  
  def __new__(cls, *args, **kwargs):
    print('Veiculo novo com:')
    for i, arg in enumerate(args):
      print(f'\targ_{i}: {arg}')
    instance = super().__new__(cls)
    return instance
  
  def __repr__(self):
    class_name = type(self).__name__
    attrs = f'({self._cavalos!r}, {self._torque!r}, {self._marca!r}, {self._modelo!r})'
    print('Veículo representado como:')
    print('\t', attrs)
    return f'{class_name}{attrs}'
  
  def __enter__(self, terrain) -> None:
    print(f'Veículo entrou na: {terrain}')
  
  def __exit__(self, terrain) -> None:
    print(f'Veículo saiu da: {terrain}')
    
  @abc.abstractmethod
  def ligar(self) -> None:
    print('veículo ligando...')
  
  @abc.abstractmethod
  def acelerar(self, velocidade: int, rpm: int) -> None:
    print('veículo acelerando...')
    print(f'\tvelocidade: {velocidade}') 
    print(f'\trpm: {rpm}')
  
  @abc.abstractmethod
  def freiar(self, velocidade: int, rpm: int) -> None:
    print('veículo freiando...')
    print(f'\tvelocidade: {velocidade}') 
    print(f'\trpm: {rpm}')
  
  @abc.abstractmethod
  def desligar(self) -> None:
    print('veículo desligando...')
    
  @property
  def cavalos(self):
    return self._cavalos   
  
  @property
  def torque(self):
    return self._torque   
  
  @property
  def velocidade(self):
    return self._velocidade
  
  @property
  def rpm(self):
    return self._rpm

  @property
  def marca(self):
    return self._marca
  
  @property
  def modelo(self):
    return self._modelo

  @cavalos.setter
  def cavalos(self, cavalos: int):
    self._cavalos = cavalos
  
  @torque.setter
  def torque(self, torque: float):
    self._torque = torque

  @velocidade.setter
  def velocidade(self, velocidade: float):
    self._velocidade = velocidade
  
  @rpm.setter
  def rpm(self, rpm: float):
    self._rpm = rpm
  
  @marca.setter
  def marca(self, marca: str):
    self._marca = marca
  
  @modelo.setter
  def modelo(self, modelo: str):
    self._modelo = modelo

class Carro(Veiculo) :
  def __init__(self, cavalos: int, torque: float, marca: str, modelo: str) -> None:
    super().__init__(cavalos, torque, marca, modelo)

  def __call__(self, func):
    return super().__call__(func)
   
  def __new__(cls, *args, **kwargs):
    return super().__new__(cls, args, kwargs)
  
  def __repr__(self):
    return super().__repr__()
  
  def __enter__(self, terrain) -> None:
    super().__enter__(terrain)
  
  def __exit__(self, terrain) -> None:
    super().__exit__(terrain)
    
  def ligar(self) -> None:
    super().ligar()

  def acelerar(self, velocidade: int, rpm: int) -> None:
    super().acelerar(velocidade, rpm)
  
  def freiar(self, velocidade: int, rpm: int) -> None:
    super().freiar(velocidade, rpm)

  def desligar(self) -> None:
    super().desligar()

class Barco(Veiculo) :
  def __init__(self, cavalos: int, torque: float, marca: str, modelo: str) -> None:
    super().__init__(cavalos, torque, marca, modelo)

  def __call__(self, func):
    return super().__call__(func)
   
  def __new__(cls, *args, **kwargs):
    return super().__new__(cls, args, kwargs)
  
  def __repr__(self):
    return super().__repr__()
  
  def __enter__(self, terrain) -> None:
    super().__enter__(terrain)
  
  def __exit__(self, terrain) -> None:
    super().__exit__(terrain)
    
  def ligar(self) -> None:
    super().ligar()

  def acelerar(self, velocidade: int, rpm: int) -> None:
    super().acelerar(velocidade, rpm)
  
  def freiar(self, velocidade: int, rpm: int) -> None:
    super().freiar(velocidade, rpm)

  def desligar(self) -> None:
    super().desligar()

class Anfibio(Carro, Barco): 
  def __init__(self, cavalos: int, torque: float, marca: str, modelo: str) -> None:
    super().__init__(cavalos, torque, marca, modelo)
  def __call__(self, func):
    return super().__call__(func)
   
  def __new__(cls, *args, **kwargs):
    return super().__new__(cls, args, kwargs)
  
  def __repr__(self):
    return super().__repr__()
  
  def __enter__(self, terrain) -> None:
    super().__enter__(terrain)
  
  def __exit__(self, terrain) -> None:
    super().__exit__(terrain)
    
  def ligar(self) -> None:
    super().ligar()

  def acelerar(self, velocidade: int, rpm: int) -> None:
    super().acelerar(velocidade, rpm)
  
  def freiar(self, velocidade: int, rpm: int) -> None:
    super().freiar(velocidade, rpm)

  def desligar(self) -> None:
    super().desligar()

# carro = Carro(185, 15.2, 'TOYOTA', 'Mobile Flex')
# carro.__repr__()
# carro.__enter__('terra')
# carro.ligar()
# carro.velocidade = 100
# carro.rpm = 3000
# carro.acelerar(carro.velocidade, carro.rpm)
# carro.velocidade = 50
# carro.rpm = 2000
# carro.freiar(carro.velocidade, carro.rpm)
# carro.desligar()
# carro.__exit__('terra')

# barco = Barco(185, 15.2, 'TOYOTA', 'Mobile Flex')
# barco.__repr__()
# barco.__enter__('água')
# barco.ligar()
# barco.velocidade = 100
# barco.rpm = 3000
# barco.acelerar(carro.velocidade, carro.rpm)
# barco.velocidade = 50
# barco.rpm = 2000
# barco.freiar(carro.velocidade, carro.rpm)
# barco.desligar()
# barco.__exit__('água')

anfibio = Anfibio(185, 15.2, 'TOYOTA', 'Mobile Flex')
anfibio.__repr__()
anfibio.ligar()
anfibio.__enter__('terra')
anfibio.velocidade = 120
anfibio.rpm = 4000
anfibio.acelerar(anfibio.velocidade, anfibio.rpm)
anfibio.velocidade = 80
anfibio.rpm = 3200
anfibio.freiar(anfibio.velocidade, anfibio.rpm)
anfibio.__exit__('terra')
anfibio.__enter__('água')
anfibio.velocidade = 60
anfibio.rpm = 2760
anfibio.freiar(anfibio.velocidade, anfibio.rpm)
anfibio.velocidade = 70
anfibio.rpm = 3000
anfibio.acelerar(anfibio.velocidade, anfibio.rpm)
anfibio.__exit__('água')
anfibio.desligar()
