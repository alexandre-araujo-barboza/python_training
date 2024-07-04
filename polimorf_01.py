# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# S = Princípio da Responsabilidade Única (SRP - Single Responsibility Principle)
# O = Princípio do Aberto/Fechado (OCP - Open/Closed Principle)
# L = (*) Princípio da Substituição de Liskov (LSP - Liskov Substitution Principle)
# I = Princípio da Segregação de Interface (ISP - Interface Segregation Principle)
# D = Princípio da Inversão de Dependência (DIP - Dependency Inversion Principle)
# (*) Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload) 
# Sobreposição de métodos (override)

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)

'''
Princípio da Responsabilidade Única (SRP - Single Responsibility Principle)
É uma diretriz fundamental na construção de sistemas de software bem estruturados e de fácil manutenção. Porquanto, ao seguir esse princípio, os desenvolvedores se esforçam para garantir que cada classe tenha um propósito claramente definido e uma única responsabilidade no contexto do sistema. 

Embora, isso implica que uma classe deve ter uma única razão para mudar, o que significa que ela deve ser focada em realizar uma tarefa específica sem estar sobrecarregada com funcionalidades adicionais ou responsabilidades que pertençam a outras classes. 

Princípio do Aberto/Fechado (OCP - Open/Closed Principle)
Esse princípio é uma diretriz crucial na construção de sistemas de software flexíveis e adaptáveis. Ele promove a ideia de que as entidades de software devem ser abertas para extensão, permitindo a adição de novos comportamentos e recursos sem a necessidade de modificar o código existente. Essencialmente, isso significa que o software deve ser projetado de forma que novos requisitos possam ser atendidos sem que seja necessário alterar o código-fonte já implementado. 

Ademais, ao seguir o OCP, os desenvolvedores podem criar sistemas mais maleáveis e robustos, capazes de se adaptar a mudanças nos requisitos e de incorporar novas funcionalidades sem comprometer a estabilidade e a integridade do código existente.

Princípio da Substituição de Liskov (LSP - Liskov Substitution Principle)
Outrossim, esse princípio estabelece que objetos de um tipo base devem ser substituíveis por instâncias de um subtipo, sem que isso comprometa a funcionalidade do programa. 

Em suma, ele garante que as classes derivadas possam ser usadas de forma intercambiável com suas classes-base, sem alterar a corretude do sistema. Contudo, ao seguir o LSP, os desenvolvedores constroem hierarquias de classes mais robustas e coesas, resultando em um design de software mais flexível e adaptável. 

Princípio da Segregação de Interface (ISP - Interface Segregation Principle)
Desempenha um papel fundamental na garantia da coesão e da flexibilidade de interfaces em sistemas de software orientados a objetos. Primeiramente, esse princípio propõe que interfaces que reúnem muitas responsabilidades e funcionalidades não coesas devem ser divididas em interfaces menores e mais específicas, adaptadas às necessidades precisas dos clientes. Todavia, essa abordagem evita a imposição de implementações desnecessárias para as classes que não as necessitam, promovendo uma separação clara de funcionalidades e uma redução na complexidade do código. 

Ao seguir o ISP, os desenvolvedores podem criar interfaces mais enxutas e especializadas, resultando em um design de software mais flexível, adaptável e de fácil manutenção. 

Princípio da Inversão de Dependência (DIP - Dependency Inversion Principle)
Esse princípio, destaca a importância de depender de abstrações em vez de implementações concretas. Esse princípio fundamenta-se na premissa de que os módulos de software devem depender de interfaces, não de implementações específicas, promovendo uma estrutura mais flexível e adaptável. 

Todavia, ao adotar o DIP, os desenvolvedores são capacitados a criar sistemas mais maleáveis, onde as alterações em uma parte do código não resultam em efeitos colaterais indesejados em outras áreas.

Portanto, ao incorporar o SRP, OCP, LSP, ISP e DIP em suas práticas de desenvolvimento, os profissionais de software podem estabelecer uma base sólida para a construção de arquiteturas de software altamente escaláveis e sustentáveis.
'''