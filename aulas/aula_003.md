# Treinamento web2py

## Aula 3 (03/04/14)

### 1. Processo de desenvolvimento de um sistema

O desenvolvimento de uma aplicação segue, usualmente, os seguintes pontos:

- 1.1. Especificações
- 1.2. Programação 
- 1.3. Testes
- 1.4. Produção

#### 1.1. Especificação

Definição das tarefas (quais são as ações que o sistema irá executar), informações (quais dados o sistema irá utilizar e gerar para gerar informação aos usuários), validações (regras de como os dados serão defnidos e inseridos) e usos (quem irá utilizar o sistema) que o sistema irá contemplar.

#### 1.2 Programação

- Definição dos dados
No caso do web2py, as definições dos dados estão na pasta ```models``` da aplicação.

- Definicão das regras
No caso do web2py, as definições dos dados estão na pasta ```controllers``` da aplicação.

- Elaboração das telas
No caso do web2py, as definições dos dados estão na pasta ```views``` da aplicação.

As definições acima seguem o modelo MVC (Modelo, Visão, Controle), comumente utilizado nos frameworks atuais.

#### 1.3. Testes

- Erros
- Regras
- Teste por usuário (usabilidade)

#### 1.4. Produção

- Assegurar que o servidor esteja de acordo com as necessidades de aplicação
- Atualização das aplicações em horários de menos demanda da aplicação
- Deploy de maneira rápida e preferencialmente automatizada.


### 2. Especificação

#### Cadastro de eventos turísticos

#### 2.1. Tipos de Usuários

- Responsável pelo evento: usuário que irá cadastrar os eventos no sistema
- Aprovador de eventos: usuário administrativo que irá validar (torná-los públicos) os eventos cadastrados



#### 2.2. Tarefas

- Ambos os usuários deverão fazer registro no sistema.

##### 2.2.1. Responsável pelo evento

- Realizar o cadastro dos eventos
- Visualizar os eventos cadastrados
- Destacar eventos recusados

##### 2.2.2. Aprovador de eventos

- Visualizar listagem de eventos não aprovados
- Visualizar listagem de eventos aprovados
- Aprovação do evento
	- Após a análise do evento, notificar o responsável pelo evento informando a situação da análise
- Gerar relatórios em PDF
- Definir eventos em destaque

#### 2.3. Dados necessários

##### 2.3.1. Cadastro de usuário

- Nome
- CPF
- Email
- Telefone
- Tipo de Organização (Circuito/Prefeitura)
- Perfil de Acesso

##### 2.3.1. Cadastro de eventos

- Responsável pelo evento
- Nome
- Data de Início
- Data do Fim
- Categoria (lista)
- Endereço
- Município (lista)
- Website (opcional)
- Página no Facebook (opcional)
- Email de contato
- Telefone (opcional)
- Descrição do evento
- Situação
- Destaque