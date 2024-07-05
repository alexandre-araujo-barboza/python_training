import abc

class Veiculo(abc.ABC):
  def __new__(cls, *args):
    print('Veiculo novo com:')
    for i, arg in enumerate(args):
      print(f'\targumento({i + 1}): {arg}')
    instance = super().__new__(cls)
    return instance
  
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
      return results
    return inner
  
  def __repr__(self):
    class_name = type(self).__name__
    attrs = f'({self._cavalos!r}, {self._torque!r}, {self._marca!r}, {self._modelo!r})'
    return f'{class_name}{attrs}'
  
  def __enter__(self) -> None:
    print('Veículo iniciando')
  
  def __exit__(self, exc_type, exc_val, exc_tb) -> None:
    print('Veículo finalizando')
  
  def __del__(self) -> None:
    print('Destruindo veículo')

  @abc.abstractmethod
  def ligar(self) -> None:
    print('veículo ligando')
  
  @abc.abstractmethod
  def desligar(self) -> None:
    print('veículo desligando')
  
  @abc.abstractmethod
  def entrar(self, terrain) -> None:
    print(f'Veículo entrou na {terrain}')
  
  @abc.abstractmethod
  def sair(self, terrain) -> None:
    print(f'Veículo saiu da {terrain}')
  
  @abc.abstractmethod
  def acelerar(self, velocidade: int, rpm: int) -> None:
    print('veículo acelerando')
    print(f'\tvelocidade: {velocidade}') 
    print(f'\trpm: {rpm}')
  
  @abc.abstractmethod
  def freiar(self, velocidade: int, rpm: int) -> None:
    print('veículo freiando')
    print(f'\tvelocidade: {velocidade}') 
    print(f'\trpm: {rpm}')
    
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
  def ligar(self) -> None:
    super().ligar()
  
  def desligar(self) -> None:
    super().desligar()
  
  def entrar(self, terrain='terra') -> None:
    super().entrar(terrain)

  def sair(self, terrain='terra') -> None:
    super().sair(terrain)
  
  def acelerar(self, velocidade: int, rpm: int) -> None:
    super().acelerar(velocidade, rpm)
  
  def freiar(self, velocidade: int, rpm: int) -> None:
    super().freiar(velocidade, rpm)
   
class Barco(Veiculo) :
  def ligar(self) -> None:
    super().ligar()
  
  def desligar(self) -> None:
    super().desligar()
  
  def entrar(self, terrain='água') -> None:
    super().entrar(terrain)

  def sair(self, terrain='água') -> None:
    super().sair(terrain)
  
  def acelerar(self, velocidade: int, rpm: int) -> None:
    super().acelerar(velocidade, rpm)
  
  def freiar(self, velocidade: int, rpm: int) -> None:
    super().freiar(velocidade, rpm)
  
class Anfibio(Carro, Barco): 
  def ligar(self) -> None:
    super().ligar()
  
  def desligar(self) -> None:
    super().desligar()
  
  def entrar(self, terrain) -> None:
    super().entrar(terrain)

  def sair(self, terrain) -> None:
    super().sair(terrain)
  
  def acelerar(self, velocidade: int, rpm: int) -> None:
    super().acelerar(velocidade, rpm)
  
  def freiar(self, velocidade: int, rpm: int) -> None:
    super().freiar(velocidade, rpm)
  
# Carro
carro = Carro(200, 18.0, 'Mercedez', 'C-500')
carro(print('Veículo é um carro.'))
print(carro)
with carro as obj:
  carro.ligar()
  carro.entrar()
  carro.velocidade = 140
  carro.rpm = 4100
  carro.acelerar(carro.velocidade, carro.rpm)
  carro.velocidade = 64
  carro.rpm = 2180
  carro.freiar(carro.velocidade, carro.rpm)
  carro.sair()
  carro.desligar()
del carro
print()

# Barco
barco = Barco(160, 11.7, 'Volvo', 'V-30')
barco(print('Veículo é um barco.'))
print(barco)
with barco as obj:
  barco.ligar()
  barco.entrar()
  barco.velocidade = 80
  barco.rpm = 2200
  barco.acelerar(barco.velocidade, barco.rpm)
  barco.velocidade = 40
  barco.rpm = 1650
  barco.freiar(barco.velocidade, barco.rpm)
  barco.sair()
  barco.desligar()
del barco
print()

# Anfíbio
anfibio = Anfibio(185, 15.2, 'Toyota', 'Moby-Dick')
anfibio(print('Veículo é anfíbio.'))
print(anfibio)
with anfibio as obj:
  anfibio.ligar()
  anfibio.entrar('terra')
  anfibio.velocidade = 120
  anfibio.rpm = 4000
  anfibio.acelerar(anfibio.velocidade, anfibio.rpm)
  anfibio.velocidade = 80
  anfibio.rpm = 3200
  anfibio.freiar(anfibio.velocidade, anfibio.rpm)
  anfibio.sair('terra')
  anfibio.entrar('água')
  anfibio.velocidade = 60
  anfibio.rpm = 2760
  anfibio.freiar(anfibio.velocidade, anfibio.rpm)
  anfibio.velocidade = 70
  anfibio.rpm = 3000
  anfibio.acelerar(anfibio.velocidade, anfibio.rpm)
  anfibio.sair('água')
  anfibio.desligar()
del anfibio
print()
