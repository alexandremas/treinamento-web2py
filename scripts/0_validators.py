# coding: utf8

def advanced_editor(field, value):
    return TEXTAREA(_id=str(field).replace('.', '_'),
                    _name=field.name, _class='text ckeditor', value=value, _cols=80, _rows=10)


def to_decimal(value):
    value = value.replace('R$', '')
    without_dot = value.replace('.', '')
    decimal = without_dot.replace(',', '.')
    return decimal


class IS_CPF_OR_CNPJ(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, value):
        try:
            #return (value, 'cpf incorreto'+str(value))
            #return (value, 'cpf incorreto'+str(cl))
            c = []
            for d in value:
                if d.isdigit():
                    c.append(d)
            cl = str(''.join(c))
            #return (value, 'cpf incorreto'+str(cl))
            if len(cl) == 11:
                cpf = cl
                cnpj = None
            elif len(cl) == 14:
                cpf = None
                cnpj = cl
            else:
                return (value, 'Número de dígitos incorreto para CPF ou CNPJ')

            #return(cpf,'aquiok'+str(len(cpf)==11))
            if cpf:

                def valida(value):

                    def calcdv(numb):
                        result = int()
                        seq = reversed(((range(9, id_type[1], -1) * 2)[:len(numb)]))
                        #return (value,'to fundo1')
                        for digit, base in zip(numb, seq):
                            result += int(digit) * int(base)

                        dv = result % 11
                        #return (value,'to fundo1'+str(dv))
                        return (dv - 10) and dv or 0

                    id_type = ['CPF', -1]

                    numb, xdv = value[:-2], value[-2:]

                    dv1 = calcdv(numb)
                    #return (value,'entrei'+str(dv1))
                    dv2 = calcdv(numb + str(dv1))
                    return (('%d%d' % (dv1, dv2) == xdv and True or False), id_type[0])


                try:
                    cpf = str(value)
                    #return(cpf,'aquiok'+str(len(cpf)==11))
                    if len(cpf) >= 11:

                        #return (value, 'cpf acima de 11')
                        c = []
                        for d in cpf:
                            if d.isdigit():
                                c.append(d)
                        cl = str(''.join(c))
                        #return (value, 'cpf incorreto'+str(cl))
                        if len(cl) == 11:
                            if valida(cl)[0] == True:
                                return (value, None)
                            else:
                                return (value, 'cpf inválido')
                        elif len(cl) < 11:
                            return (value, 'cpf incompleto')
                        else:
                            return (value, 'cpf tem mais de 11 dígitos')
                        if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
                            return (value, 'cpf deve estar no formato 000.000.000-00' + cpf[11])
                    else:
                        return (value, 'cpf deve estar no formato 000.000.000-00')
                        #return(cpf,'aquiok'+str(len(cpf)==11))
                except:
                    return (value, 'algum erro' + str(value))
            elif cnpj:

                """ Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam """
                inteiros = map(int, cnpj)
                novoCnpj = inteiros[:12]

                prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                while len(novoCnpj) < 14:
                    r = sum([x * y for (x, y) in zip(novoCnpj, prod)]) % 11
                    if r > 1:
                        f = 11 - r
                    else:
                        f = 0
                    novoCnpj.append(f)
                    prod.insert(0, 6)
                    #return(str(novoCnpj),'aquiok')
                """ Se o número gerado coincidir com o número original, é válido """
                if novoCnpj == inteiros:
                    #cnpj = ''.join(novoCnpj)

                    return (str(cnpj), None)

                else:
                    return (value, 'CNPJ não é válido')



        except:
            return (value, 'algum erro' + str(value))

    def formatter(self, value):
        if len(value) == 11:
            formatado = value[0:3] + '.' + value[3:6] + '.' + value[6:9] + '-' + value[9:11]
        elif len(value) == 14:
            formatado = value[0:2] + '.' + value[2:5] + '.' + value[5:8] + '/' + value[8:12] + '-' + value[12:14]
        else:
            formatado = value
        return formatado


class IS_CNPJ(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, value):
        try:
            #return (value, 'cpf incorreto'+str(value))
            #return (value, 'cpf incorreto'+str(cl))
            c = []
            for d in value:
                if d.isdigit():
                    c.append(d)
            cl = str(''.join(c))
            #return (value, 'cpf incorreto'+str(cl))
            if len(cl) == 14:
                cnpj = cl
            else:
                return (value, 'Número de dígitos incorreto para CNPJ')

            if cnpj:

                """ Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam """
                inteiros = map(int, cnpj)
                novoCnpj = inteiros[:12]

                prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                while len(novoCnpj) < 14:
                    r = sum([x * y for (x, y) in zip(novoCnpj, prod)]) % 11
                    if r > 1:
                        f = 11 - r
                    else:
                        f = 0
                    novoCnpj.append(f)
                    prod.insert(0, 6)
                    #return(str(novoCnpj),'aquiok')
                """ Se o número gerado coincidir com o número original, é válido """
                if novoCnpj == inteiros:
                    #cnpj = ''.join(novoCnpj)

                    return (str(cnpj), None)

                else:
                    return (value, 'CNPJ não é válido')



        except:
            return (value, 'algum erro' + str(value))

    def formatter(self, value):
        formatado = value[0:2] + '.' + value[2:5] + '.' + value[5:8] + '/ ' + value[8:12] + '-' + value[12:14]
        return formatado


class IS_CEP(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, value):
        try:
            #return (value, 'cpf incorreto'+str(value))
            #return (value, 'cpf incorreto'+str(cl))
            c = []
            for d in value:
                if d.isdigit():
                    c.append(d)
            cl = str(''.join(c))
            #return (value, 'cpf incorreto'+str(cl))
            if len(cl) == 8:
                cep = cl
                return (str(cep), None)
            else:
                return (value, 'Número de dígitos incorreto para CEP')



        except:
            return (value, 'algum erro' + str(value))

    def formatter(self, value):
        formatado = value[0:2] + '.' + value[2:5] + '-' + value[5:8]
        return formatado


class IS_TELEFONE(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, value):
        try:
            telefone = str(value)
            #return(cpf,'aquiok'+str(len(cpf)==11))
            if len(telefone) >= 10:
                #return (value, 'cpf acima de 11')
                c = []
                for d in telefone:
                    if d.isdigit():
                        c.append(d)
                cl = str(''.join(c))
                #return (value, 'cpf incorreto'+str(cl))
                if len(cl) == 10:
                    return (str(cl), None)
                elif len(cl) < 10:
                    return (value, 'telefone incompleto')
                else:
                    return (value, 'o telefone tem mais de 10 dígitos')
            else:
                return (value, 'O telefone deve estar no formato 00-0000-0000')
                #return(cpf,'aquiok'+str(len(cpf)==11))
        except:
            return (value, 'algum erro' + str(value))

    def formatter(self, value):
        if value and len(value) == 10:
            formatado = value[0:2] + '-' + value[2:6] + '-' + value[6:10]
        else:
            formatado = value
        return formatado


def to_telefone(value):
    if value and len(value) == 10:
        formatado = value[0:2] + '-' + value[2:6] + '-' + value[6:10]
    else:
        formatado = value
    return formatado


class IS_CPF(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, value):

        def valida(value):

            def calcdv(numb):
                result = int()
                seq = reversed(((range(9, id_type[1], -1) * 2)[:len(numb)]))
                #return (value,'to fundo1')
                for digit, base in zip(numb, seq):
                    result += int(digit) * int(base)

                dv = result % 11
                #return (value,'to fundo1'+str(dv))
                return (dv - 10) and dv or 0

            id_type = ['CPF', -1]

            numb, xdv = value[:-2], value[-2:]

            dv1 = calcdv(numb)
            #return (value,'entrei'+str(dv1))
            dv2 = calcdv(numb + str(dv1))
            return (('%d%d' % (dv1, dv2) == xdv and True or False), id_type[0])


        try:
            cpf = str(value)
            #return(cpf,'aquiok'+str(len(cpf)==11))
            if len(cpf) >= 11:

                #return (value, 'cpf acima de 11')
                c = []
                for d in cpf:
                    if d.isdigit():
                        c.append(d)
                cl = str(''.join(c))
                #return (value, 'cpf incorreto'+str(cl))
                if len(cl) == 11:
                    if valida(cl)[0] == True:
                        return (cl, None)
                    else:
                        return (cl, 'cpf inválido')
                elif len(cl) < 11:
                    return (cl, 'cpf incompleto')
                else:
                    return (cl, 'cpf tem mais de 11 dígitos')
            else:
                return (value, 'cpf deve estar no formato 000.000.000-00')
                #return(cpf,'aquiok'+str(len(cpf)==11))


        except:
            return (value, 'algum erro' + str(value))

    def formatter(self, value):
        #if value ==11:
        formatado = value[0:3] + '.' + value[3:6] + '.' + value[6:9] + '-' + value[9:11]
        #else:
        #    formatado=value
        #formatado = value
        return formatado


class E_DINHEIRO(object):
    def __init__(self, format=True, error_message='Digite o valor!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, value):

        d = str(value)
        if len(d) < 1:
            return (d, 'É obrigatório o preenchimento deste campo')
        d = d.replace('R$', '')
        d = d.replace('.', '')
        d = d.replace(',', '.')
        #return (value, valor[-3:-2])
        try:
            return (d, None)
        except:
            return (d, str(d) + 'o valor digitado não é um número válido')

    def formatter(self, value):
        if value < 0:
            value = 0
        import locale

        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        value = locale.currency(value, grouping=True)
        return value


def to_money(value):
    if value < 0:
        value = 0
    import locale

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    value = locale.currency(value, grouping=True)
    return value


def money(value):
    d = str(value)
    d = d.split('.')
    try:
        centavos = d[1][0:2]
    except:
        centavos = '00'
    if len(centavos) == 1:
        centavos = centavos + '0'

    inteiros = d[0]
    l = len(inteiros)
    i = 0
    if l > 3:
        r = l % 3
        reais = inteiros[0:r]
        while (i + 1) < (l - r):
            s = r + i
            if len(reais) > 0:
                reais = reais + '.' + inteiros[s:s + 3]
            else:
                reais = inteiros[s:s + 3]
            i = i + 3
    elif l > 0:
        reais = inteiros
    else:
        reais = 0
    return 'R$ %s,%s' % (reais, centavos)


def valor(value):
    d = str(value)
    d = d.split('.')
    try:
        centavos = d[1][0:2]
    except:
        centavos = '00'
    if len(centavos) == 1:
        centavos = centavos + '0'

    inteiros = d[0]
    l = len(inteiros)
    i = 0
    if l > 3:
        r = l % 3
        reais = inteiros[0:r]
        while (i + 1) < (l - r):
            s = r + i
            if len(reais) > 0:
                reais = reais + '.' + inteiros[s:s + 3]
            else:
                reais = inteiros[s:s + 3]
            i = i + 3
    elif l > 0:
        reais = inteiros
    else:
        reais = 0
    return '%s,%s' % (reais, centavos)


class VALOR_PAGO(object):
    def __init__(self, format=True, error_message=''):
        #self.format = format
        self.error_message = error_message

    def __call__(self, value):
        return (0, None)

    def formatter(self, value):
        #return value
        soma = db.pagamento_realizado.valor_total.sum()
        pago = db(db.pagamento_realizado.convenio_id == self.convenio.id
        ).select(soma).first()[soma]
        if not pago:
            pago = 0
        return to_money(pago)


#db.convenio.virtualfields.append(ConveniosVirtualFields())


def lt(s):
    try:
        s = unicode(s, 'utf-8').encode('latin-1')
    except:
        s = str(s)
    return s


def tl(s):
    try:
        data = s
        udata = data.decode("utf-8")
        return udata.encode("latin-1", "ignore")
    except:
        return ''


def make_time(value):
    if value:
        return value[6:10] + '-' + value[3:5] + '-' + value[0:2]
    else:
        return None


data = IS_NULL_OR(IS_DATE(format=T('%d-%m-%Y')))


def make_data(field):
    if type(field) is datetime.date:
        return field.strftime("%d/%m/%Y")
    else:
        return ''


def make_year(field):
    if type(field) is datetime.date:
        return field.strftime("%Y")
    else:
        return ''


status_analise = ['Início Cadastro', 'Protocolo', 'Diligência Protocolo', 'Retorno de Diligência Protocolo',
                  'Em análise parecer técnico',
                  'Diligência Parecer Técnico', 'Retorno de Diligência Parecer Técnico', 'Agendado',
                  'Diligência Comitê',
                  'Retorno de Diligência Comitê', 'Reprovado']
status_aprovados = ['Aprovado', 'Certidão de Aprovação assinada', 'Publicação', 'Prorrogado',
                    'Em reajuste', 'Protocolo Reajuste', 'Diligência Reajuste', 'Reajuste Aprovado',
                    'Reajuste Reprovado', 'Solicitação de Início de Execução']


def check_limite_projetos(projeto):
    status_limite = status_analise[1:-1]

    status_limite.extend(status_aprovados)
    projetos = db(
        (db.projeto.empreendedor == projeto.empreendedor) & (db.projeto.status_analise.belongs(status_limite))).select()

    return len(projetos)


def checklist(projeto_id, short=False):
    projeto = db(db.projeto.id == projeto_id).select().first()
    c = [i for i in range(12)]

    limite = check_limite_projetos(projeto)

    c[2] = 'red' if (projeto.status_analise == 'Início Cadastro' and limite > 2) else 'green'
    despesas = db((db.despesa.projeto == projeto.id)).select()
    total_incentivado = 0.00
    total_despesas = 0.00
    total_terceiro = 0.00
    total_outros = 0.00
    dsqt = ''
    dso = ''
    for despesa in despesas:
        if despesa.fonte_recurso == "Incentivo":
            total_incentivado += float(despesa.total)
        if despesa.fonte_recurso == "Outros":
            total_outros += float(despesa.total)
        if despesa.fonte_recurso == "Pagamento a Terceiros":
            total_terceiro += float(despesa.total)
        if int(despesa.quantidade) < 1:
            dsqt += '<a href="%s" target="_blank" >%s</a>' % (
                URL(r=request, c='default', f='despesas', args=[despesa.projeto, despesa.id]), despesa.nome)
        if despesa.fonte_recurso == 'Incentivo' and len(despesa.orcamento1) < 1:
            dso += '<a href="%s" target="_blank" >%s</a>' % (
                URL(r=request, c='default', f='despesas', args=[despesa.projeto, despesa.id]), despesa.nome)
        total_despesas += float(despesa.total)
    if total_terceiro > 0.00:
        total_incentivado = total_incentivado + total_terceiro

    c[6] = 'green' if len(dsqt) == 0 else 'red'
    c[1] = 'red' if len(dso) > 1 else 'green'
    #c[2] = 'red' if total_despesas < 1 else 'green'
    c[3] = 'red' if total_incentivado < 1 else 'green'

    m = []
    try:
        for modalidade in projeto.modalidades:
            m.append(db.modalidade[modalidade].modalidade)

        modalidades = ', '.join(m)
    except:
        modalidades = ''

    c[4] = 'red'
    if len(modalidades) > 0:
        c[4] = 'green'

    metas = db(db.meta.projeto == projeto.id).select()
    msq = ''
    for meta in metas:
        if int(meta.quantidade or 0) < 1:
            msq += ' <a href="%s" target="_blank" >%s</a>' % (
                URL(r=request, c='default', f='metas', args=[meta.projeto, meta.id]), meta.meta)
    c[5] = 'red' if len(msq) > 0 else 'green'

    try:
        percentualt = total_terceiro / (total_incentivado / 0.9) * 100
    except:
        percentualt = 0.00

    c[11] = "red" if percentualt > 10.0 else "green"
    documentos = db((db.documento.projeto == projeto.id)).select()

    #documentos
    tipos = ['COMPROVAÇÃO DE CAPACIDADE TÉCNICA',
             'PLANO DE DIVULGAÇÃO DE LOGOMARCA', 'ESTATUTO SOCIAL']
    o = []
    for documento in documentos:
        if not documento.tipo in o:
            o.append(documento.tipo)
    d = set(tipos) - set(o)
    if len(d) > 0:
        c[7] = 'red'
        msgd = "<a href='%s' >Não foram cadastrados os seguintes \
         documentos exigidos: " % (URL(r=request, f='projeto', args=[projeto.id, 'documentos']))
        msgd += ', '.join(d)
        msgd += '</a>'
    else:
        c[7] = 'green'
        msgd = len(documentos)
    beneficiados = projeto.beneficiados
    c[8] = 'red' if beneficiados < 1 else 'green'
    c[9] = 'green' if total_incentivado < 360000.00 else 'red'

    metas = db(db.meta.projeto == projeto_id).select()

    c[10] = 'red' if len(metas) < 1 else 'green'
    c[0] = 'green'

    if 'red' in c:
        message = "A emissão da declaração de veracidade e o encaminhamento do projeto para protocolo somente serão liberadas após resolvidas as pendências EM VERMELHO acima"
        if short == True:
            return 'Incompleto'
    else:

        if request.now.date() <= projeto.edital.data_termino or projeto.status_analise in ['Diligência Protocolo',
                                                                                           'Diligência Parecer Técnico',
                                                                                           'Diligência Comitê',
                                                                                           'Em reajuste',
                                                                                           'Em readequação']:
            message = XML(''' <a href='../declaracao/%s' target='_blank' > Gerar Prévia do Projeto</a><br><br>
    <p style='color:red'>Clique no botão acima para gerar uma prévia do Projeto em PDF. <br>
        Confira todas as informações.<br>
        Após tudo conferido, clique em 'Finalizar' no menu acima. <br>
        A nova tela irá gerar uma versão final em PDF para armazenamento no sistema <br>
        e encaminhamento da DECLARAÇÃO DE VERACIDADE,a realização do protocolo do projeto, <br>
        e NÃO PERMITIRÁ QUE O PROJETO SEJA MAIS EDITADO.
    </p>
        ''' % (projeto.id))
            if short == True:
                return 'Pronto para Protocolo'
        else:
            message = '<font color=red>O prazo para protocolo no edital "' + projeto.edital.nome + '" expirou em ' + make_data(
                projeto.edital.data_termino) + '</font>'
        if short == True:
            return 'Edital encerrado'

    return DIV(XML("""
    <table>
<tr  class='gray'><td>Modalidades</td><td class='%s'> %s </td></tr>
<tr class='gray'><td>Nº de Beneficiados: </td><td class='green'>%s </td></tr></table>
<table>
<tr class='gray'><td>Nº de Metas: </td><td class='%s'>%s </td></tr>
<tr  class='gray'><td>Metas com pendência de quantidade</td><td class='%s'> %s </td></tr>
</table>
<table>
<tr  class='gray'><td>Número de despesas</td><td class='green'> %s </td></tr>
<tr  class='gray'><td>Despesas com pendência de quantidade mensal</td><td class='%s'> %s </td></tr>
<tr  class='gray'><td>Despesas com pendẽncia de orçamento:</td><td class='%s'> %s </td></tr>
<tr  class='gray'><td>Despesas com outra fonte de recurso:</td><td class='%s'> %s </td></tr>
</table>
<table>
<tr  class='gray'><td>Valor Total a ser captado:</td><td class='%s'> %s </td></tr>
<tr  class='gray'><td>Percentual destinado a Pagamento de Terceiros:</td><td class='%s'> %s </td></tr>
<tr  class='gray'><td>Valor destinado ao projeto esportivo:</td><td class='%s'> %s </td></tr>
<tr  class='gray'><td>Valor destinado pelo apoiador à SETES:</td><td class='green'> %s </td></tr>
<tr  class='gray'><td>Número de projetos em análise ou captação:</td><td class='%s'> %s </td></tr>


</table>
    %s
    """ % (c[4], modalidades or 'nenhuma',
           projeto.beneficiados,

           c[10], len(metas),
           c[5], msq or 'nenhuma',

           len(despesas),
           c[6], dsqt or 'nenhuma',
           c[1], dso or 'nenhuma',
           c[0], money(total_outros),

           c[9], money(total_incentivado / 0.9),
           c[11], "{0:.2f}".format(percentualt) + '%',
           c[3], money(total_incentivado),
           money(total_incentivado / 9),
           c[2], limite,


           message)
    ))


def max_meses(projeto, mes_inicio, meses):
    max = db.projeto[projeto].meses
    row = db.despesa[request.args(2)]

    if int(meses) < 1:
        meses = 1
        session.flash = 'A duração não pode ser menor que 1'
        row.update_record(meses=meses)
    session.flash = ''
    if int(mes_inicio) > max:
        mes_inicio = max - int(meses) + 1
        row.update_record(mes_inicio=mes_inicio)
        session.flash += "O mes de início foi ajustado para que termine com o projeto. "
    if int(mes_inicio) < 1:
        mes_inicio = 1
        row.update_record(mes_inicio=mes_inicio)
        session.flash += "O mes de início não pode ser menor que 1. "
    duracao = int(mes_inicio) + int(meses) - 1

    if duracao > max:
        duracao = max - int(mes_inicio) + 1
        row.update_record(meses=duracao, total=row.valor_unitario * duracao)
        session.flash += "A duração da despesa é maior que a duração do projeto. O número de meses foi corrigido automaticamente"
        return max


def checa_duracao(projeto_id, meses):
    r = db.executesql("select max(meses+mes_inicio) as termino from despesa\
     where projeto = %s" % projeto_id)
    if r[0][0] is not None:
        maxduracao = r[0][0] - 1
        if int(maxduracao) > int(meses):
            db.executesql('update projeto set meses = %s where id = %s' % (
                maxduracao, projeto_id))
            session.flash = " O número de meses do projeto foi ajustado para o término das despesas cadastradas"


def invert_bool(bool):
    if bool is True:
        return False
    else:
        return True


def tl_bool(bool):
    if bool is True:
        return "Sim"
    else:
        return "Não"


def money_to_double(value):
    if not value:
        raise Error
    d = str(value)
    d = d.replace('R$', '')
    d = d.replace('.', '')
    d = d.replace(',', '.')
    if d.find('.') == -1:
        d = d + '.00'

    #return (value, valor[-3:-2])
    return d


def admin(f=None):
    if auth.user_id == 1 or auth.user.subordinado == 1:
        return f
    else:
        response.flash = "Você não tem permissão para acessar o conteúdo"
        redirect('default/index')


def is_admin():
    if auth.user.subordinado == administrator:
        return True
    else:
        return False


def is_executor():
    if auth.user_id > 1 and auth.user.subordinado is None:
        return True
    else:
        return False


def get_empreendedor():
    if auth.user.subordinado < 4:
        return auth.user_id
    else:
        return auth.user.subordinado


def executor_or_admin(id):
    if auth.user_id == 1 or auth.user.subordinado == 1:
        pass
    elif auth.user_id == id or auth.user.subordinado is id:
        pass
    elif auth.user.subordinado == 3:
        pass
    else:
        response.flash = "Você não tem permissão para acessar o conteúdo"
        redirect(URL(r=request, c='default', f='index'))


def check_status(id):
    try:
        hist = db(db.historico.projeto == id).select(orderby=~db.historico.id).first()
        return '%s em %s' % (hist.ocorrencia, make_data(hist.quando))

    except:
        projeto = db.projeto[id]
        return 'Início do cadastro em %s' % (make_data(projeto.criado_em))


def check_status_tc(id):
    try:
        hist = db(db.historico_tc.tc == id).select(orderby=~db.historico.id).first()
        return '%s em %s' % (hist.ocorrencia, make_data(hist.quando))

    except:
        projeto = db.projeto[id]
        return 'Início do cadastro em %s' % (make_data(projeto.criado_em))


def check_edicao(id):
    hist = db(db.historico.projeto == id).select(orderby=~db.historico.id).first()

    try:
        if hist.id:
            projeto = db.projeto[id]
            if projeto.readonly == False:
                return A('Adequar Projeto', _href=URL(r=request, c='default', f='projeto', args=[id]), _target='_blank')
            elif projeto.readonly == True:
                return A('Ver Projeto', _href=URL(r=request, c='default', f='detalhes', args=[id]), _target='_blank')
    except:
        return A('Continuar Cadastro', _href=URL(r=request, c='default', f='projeto', args=[id]), _target='_blank')


def check_locais(id):
    locais = db(db.local.projeto == id).select(orderby=db.local.id)
    n = len(locais)
    return n


def check_metas(id):
    metas = db(db.meta.projeto == id).select(orderby=db.meta.id)
    n = len(metas)
    return n


def check_despesas(id):
    rows = db(db.despesa.projeto == id).select(orderby=db.despesa.id)
    n = len(rows)
    return n


def check_documentos(id):
    documentos = db(db.documento.projeto == id).select(orderby=db.documento.id)
    n = len(documentos)


    #documentos
    tipos = ['COMPROVAÇÃO DE CAPACIDADE TÉCNICA',
             'PLANO DE DIVULGAÇÃO DE LOGOMARCA', 'ESTATUTO SOCIAL']
    o = []
    for documento in documentos:
        if not documento.tipo in o:
            o.append(documento.tipo)
    d = set(tipos) - set(o)
    if len(d) > 0:
        valido = False
    else:
        valido = True
    return dict(n=n, valido=valido)


def menu_inteligente(id):
    menu = '<table><tr>'
    if id == None:
        bbasic = '#007fff'

        menu += '<td style="background-color:%s;"><a href=%s style="color:white;" >1. Informações Básicas </a><td>' % (
            bbasic, URL(r=request,
                        f='projeto', user_signature=True))
        menu += '</tr></table>'

    else:
        bbasic = '#007fff'
        bmetas = '#766b6b'
        bdespesas = '#766b6b'
        blocais = '#766b6b'
        bdocumentos = '#766b6b'
        bfinalizar = '#766b6b'
        if db.projeto[id].readonly == True:
            redirect(URL(r=request, f='detalhes', args=[id]))
        menu += '<td style="background-color:%s;"><a href=%s style="color:white;" >1. Informações Básicas </a><td>' % (
            bbasic, URL(r=request,
                        f='projeto', args=[request.args(0)], user_signature=True))

        nmetas = check_metas(id)
        if nmetas > 0:
            bmetas = '#007fff'

        menu += '<td style="background:%s; "><a href=%s style="color:white;" >2. Metas  </a><td> ' % (
            bmetas, URL(r=request, f='metas',
                        args=[request.args(0)], user_signature=True))

        ndespesas = check_despesas(id)
        if ndespesas > 0:
            bdespesas = '#007fff'
        if nmetas > 0:
            menu += '<td style="background:%s;"><a href=%s style="color:white;" >3.Despesas  </a><td>' % (
                bdespesas, URL(r=request, f='despesas', args=[request.args(0)], user_signature=True))

        nlocais = check_locais(id)
        if nlocais > 0:
            blocais = '#007fff'
        if ndespesas > 0 and nmetas > 0:
            menu += '<td style="background:%s;"><a href=%s style="color:white;" >4. Locais  </a><td>' % (
                blocais, URL(r=request, f='local', args=[request.args(0)], user_signature=True),)

        doc = check_documentos(id)
        if doc['valido'] == True:
            bdocumentos = '#007fff'
        if nlocais > 0 and ndespesas > 0 and nmetas > 0:
            menu += '<td style="background:%s; "><a href=%s style="color:white;" >5. Documentos  </a><td>' % (
                bdocumentos, URL(r=request, f='documentos', args=[request.args(0)], user_signature=True))
        if doc['valido'] == True and nlocais > 0 and ndespesas > 0 and nmetas > 0:
            menu += '<td style="background:%s;"><a href=%s style="color:white;" >6. Verificar </a><td>' % (
                bfinalizar, URL(r=request, f='status', args=[request.args(0)]))

        if checklist(id, short=True) == 'Pronto para Protocolo':
            menu += '<td style="background:%s;"><a href=%s style="color:white;" >7. Finalizar </a><td>' % (
                bfinalizar, URL(r=request, f='protocolo', args=[request.args(0)]))

        historico = db(db.historico.projeto == id).select(orderby=~db.historico.id).first()
        link = ''
        if historico:
            if historico.ocorrencia == 'Em reajuste' or historico.ocorrencia[:11] == "Diligência":
                menu += '<td style="background:%s;"><a href=%s style="color:white;" >8. Histórico de Tramitação </a></td>' % (
                    bfinalizar, URL(r=request, f='detalhes', args=[request.args(0)]))
                menu += '</tr></table>'
                if historico.arquivo and len(historico.arquivo) > 0:
                    link = "<a href=" + URL(r=request, f='download', args=[
                        historico.arquivo]) + " style='color:white;'>Arquivo com informações adicionais</a>"
                if historico.detalhamento:
                    d = historico.detalhamento
                else:
                    d = ''
                menu += "<p style='background:red;color:white'>%s:<br>%s <br>%s </p>" % (historico.ocorrencia, d, link)
            else:
                menu += '</tr></table>'
        else:
            menu += '</tr></table>'
    return XML(menu)


def menu_tc(id):
    menu = '<table><tr>'
    if id == None:
        bbasic = '#007fff'

        menu += '<td style="background-color:%s;"><a href=%s style="color:white;" >1. Dados do Apoio </a><td>' % (
            bbasic, URL(r=request, f='tc', args=[request.args(0)], user_signature=True))

    else:
        tc = db.tc[request.args(1)]
        if tc.readonly == True:
            redirect(URL(r=request, f='detalhes_tc', args=[request.args(0), request.args(1)]))
        bbasic = '#007fff'
        bmetas = '#766b6b'
        bdespesas = '#766b6b'

        menu += '<td style="background-color:%s;"><a href=%s style="color:white;" >1. Dados do Apoio </a><td>' % (
            bbasic, URL(r=request, f='tc', args=[request.args(0), request.args(1)], user_signature=True))

        menu += '<td style="background-color:%s;"><a href=%s style="color:white;" >2. Repasses </a><td>' % (
            bbasic, URL(r=request,
                        f='repasses', args=[request.args(0), request.args(1)], user_signature=True))

        nrepasses = check_repasses(id)
        if nrepasses > 0:
            bmetas = '#007fff'
            menu += '<td id="m3" style="background:%s; "><a href=%s style="color:white;" >3. Verificar</a><td> ' % (
                bmetas, URL(r=request, f='resumo_tc', args=[request.args(0), request.args(1)], user_signature=True))
            menu += '<td id="m4" style="background:%s;"> <a href=%s style="color:white;" >4. Finalizar</a></ td> ' % (
                bdespesas, URL(r=request, f='finalizar', args=[request.args(0), request.args(1)], user_signature=True))
    menu += '</tr></table>'

    return XML(menu)


def check_repasses(id):
    rows = db(db.repasse.tc == id).select()
    n = len(rows)
    total = 0.00
    for row in rows:
        total += row.valor
    return dict(n=n, total=total)


def check_file(file):
    if len(file) > 0:
        #return len(file)
        return A('Arquivo', _href=URL(r=request, f='download', args=[file]))
    else:
        return ''
    pass


def count_orcamento(despesa):
    n = 0
    if len(despesa.orcamento1) > 0:
        n += 1
    if len(despesa.orcamento2) > 0:
        n += 1
    if len(despesa.orcamento3) > 0:
        n += 1
    return str(n)


def get_file_path(file):
    a = file.split('.')
    path = './applications/' + request.application + '/uploads/' + a[0] + '.' + a[1] + '/' + a[2][:2] + '/'
    return path + file


def gerapdf(output=None):
    url = URL('download')

    if request.vars.projeto or request.args(0):
        from gluon.contrib.pyfpdf import FPDF
        from datetime import timedelta, date

        p = request.vars.projeto or request.args(0)
        projeto = db.projeto[p]
        executor_or_admin(projeto.empreendedor)

        def repmod(values):
            r = []
            for value in values:
                r.append(db.modalidade[value].modalidade)
            return ','.join(r)

        class PDF(FPDF):
            def __init__(self):
                FPDF.__init__(self)

            def header(self):
                #print "header"
                #Logo
                #self.Image('logo_pb.png',10,8,33)

                #Arial bold 15
                self.set_font('Arial', 'B', 10)

                #self.cell(80)
                if self.cur_orientation == 'P':
                    cs = 95
                    s = 190
                else:
                    cs = 135
                    s = 270
                self.cell(cs, 5, 'Governo do Estado de Minas Gerais', 1, 0)
                self.cell(cs, 5, tl('Secretaria de Estado de Turismo e Esportes'), 1, 0)
                self.cell(0, 5, '', 0, 1)
                ano = make_year(projeto.criado_em)
                if request.vars.projeto:
                    caput = "Dados do Projeto"
                elif request.args(0):
                    caput = "Prévia do Projeto"
                self.multi_cell(s, 5, tl('%s nº %s/%s - %s \n apresentado por %s' % (
                    caput, projeto.id, ano, projeto.nome, auth.user.first_name)), 1, align='C')

                return

            def footer(self):
                #print "footer"
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                self.cell(0, 10, tl('Página ' + str(self.page_no())), 0, 0, 'C')
                return

            def First_Page(self):
                data_limite = date.today() + timedelta(days=7)
                self.add_page()
                self.set_font('Arial', '', 8)
                from datetime import datetime

                text0 = 'Versão  emitida em ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                despesas = db(db.despesa.projeto == projeto.id).select()
                total_incentivado = 0.0
                total = 0.0
                total_atividade_fim = 0.0
                total_atividade_meio = 0.0
                total_despesas = 0.0
                total_terceiro = 0.0
                for despesa in despesas:
                    total_despesas += float(despesa.total)
                    if despesa.fonte_recurso == "Incentivo":
                        total_incentivado += float(despesa.total)
                    if despesa.fonte_recurso == "Pagamento a Terceiros":
                        total_terceiro += float(despesa.total)
                if total_terceiro > 0.00:
                    total_incentivado = total_incentivado + total_terceiro

                try:
                    percentualt = total_terceiro / (total_incentivado / 0.9) * 100
                except:
                    percentualt = 0.00

                text = '''
GOVERNO DO ESTADO DE MINAS GERAIS. 
Secretaria de Estado de Turismo e Esportes.
Subsecretaria de Esportes.
Superintendência de Fomento e Incentivo ao Esporte.
Diretoria de Gestão de Lei de Incentivo ao Esporte.
Rod. Prefeito Américo Gianetti, s/n – Prédio Gerais – 11 º andar. Bairro Serra Verde – CEP: 31.630-901 – CA/BH/MG


Formulário de inscrição do Projeto nº %s/%s – %s apresentado por %s


Eu, %s, CPF %s, solicito que o projeto %s seja analisado e aprovado nos termos do Edital Nº%s/%s, para efeito dos benefícios de que tratam a Lei Nº 20.824/2013, o Decreto nº 46.308/2013.

DECLARAÇÃO

Declaro que o Executor %s, CNPJ %s está regularmente inscrito no Cadastro Geral de Convenentes do Estado de Minas Gerais –CAGEC, não está bloqueado no Sistema Integrado de Administração Financeira- SIAFI, e não está inscrito como devedor no Cadastro Informativo de Inadimplência em Relação à Administração Pública do Estado de Minas Gerais - CADIN/MG.

Declaro ainda que as informações cadastradas no Sistema de Informação Minas Olímpica Incentivo ao Esporte - relativas ao projeto esportivo são verdadeiras, conforme este Formulário.

Estou ciente que o projeto poderá sofrer alterações em qualquer dos seus aspectos, por meio de diligências ou readequação, e que me comprometo em desenvolvê-lo conforme a última versão aprovada pelo Comitê de Avaliação, disponível pelo sistema.

Valor Total a ser captado: R$ %s
Percentual a ser pago a terceiros: %s
Valor destinado ao Projeto Esportivo: R$ %s
Valor destinado pelo apoiador à SETES: R$ %s







    %s, %s

     ________________________________________________________
      Carimbo e Assinatura do representante legal da entidade


      ''' % (projeto.id, projeto.criado_em.strftime('%Y'), projeto.nome, projeto.empreendedor.first_name,
             projeto.empreendedor.responsavel_legal, projeto.empreendedor.cpf, projeto.nome,
             projeto.edital, projeto.edital.data_inicio.strftime('%Y'),
             projeto.empreendedor.first_name, projeto.empreendedor.cnpj,
             money(total_incentivado / 0.9), "{0:.2f}".format(percentualt) + '%', money(total_incentivado),
             money(total_incentivado / 9),
             projeto.empreendedor.municipio.municipio, request.now.strftime('%d de %B de %Y')   )

                self.multi_cell(190, 5, tl(text0 + text), 1, 0)

                pdf.add_page()
                self.multi_cell(190, 5, tl('Objeto: %s' % projeto.objeto), 1, 0)
                self.multi_cell(190, 5, tl('Manifestação Esportiva: %s' % projeto.manifestacao), 1, 0)
                self.multi_cell(190, 5, tl('Modalidades: %s' % repmod(projeto.modalidades)), 1, 0)
                self.multi_cell(190, 5, tl('Objetivos: %s' % projeto.objetivos), 1, 0)
                self.multi_cell(190, 5, tl('Metodologia: %s' % projeto.metodologia), 1, 0)
                self.multi_cell(190, 5, tl('Justificativa: %s' % projeto.justificativa), 1, 0)
                self.multi_cell(190, 5, tl('Duração em meses: %s' % projeto.meses), 1, 0)
                self.multi_cell(190, 5, tl('Público-Alvo: %s' % projeto.publico_alvo), 1, 0)
                self.multi_cell(190, 5, tl('Total de Beneficiados: %s' % projeto.beneficiados), 1, 0)
                self.multi_cell(190, 5, tl('Valor Total a ser captado: %s' % money(total_incentivado / 0.9)), 1, 0)
                self.multi_cell(190, 5, tl(
                    'Percentual destinado a Pagamento de Terceiros:' + "{0:.2f}".format(percentualt) + '%'), 1, 0)
                self.multi_cell(190, 5, tl('Valor Destinado ao Projeto Esportivo: %s' % money(total_incentivado)), 1, 0)
                self.multi_cell(190, 5,
                                tl('Valor destinado pelo apoiador à SETES:  %s ' % (money(total_incentivado / 9))), 1,
                                0)


            def metas(self):
                pdf.add_page('L')
                y0 = self.y
                metas = db(db.meta.projeto == projeto.id).select()
                self.ln()
                self.cell(270, 8, tl('Resumo de Metas e Despesas'), 1, 1, 'L')
                self.cell(30, 8, 'Quantidade total', 1, 0, 'L')
                self.cell(140, 8, tl('Descrição da Meta'), 1, 0, 'L')
                self.cell(100, 8, tl('Documentos comprobatórios'), 1, 1, 'L')

                for meta in metas:
                    p1 = self.page_no
                    y1 = self.y
                    s1 = self.get_string_width(meta.meta)
                    s2 = self.get_string_width(meta.documentos_comprobatorios.rstrip())
                    if y1 > 150 and (s1 > 138 or s2 > 100):
                        self.add_page('L')
                    self.cell(30, 8, str(meta.quantidade), 1, 0, 'L')
                    x = self.x

                    self.multi_cell(140, 8, tl(meta.meta), 1, 0, 'L')
                    self.x = x + 140
                    y2 = self.y
                    p2 = self.page_no
                    if y2 < y1:
                        self.y = y0
                    else:
                        self.y = y1
                    self.multi_cell(100, 8, tl(meta.documentos_comprobatorios.rstrip()), 1, 1, 'L')
                    y3 = self.y
                    if y2 > y3:
                        self.y = y2
                    else:
                        self.y = y3

                despesasincentivo = db((db.despesa.projeto == projeto.id) &
                                       (db.despesa.fonte_recurso == "Incentivo")).select(orderby=db.despesa.nome)
                outrasdespesas = db((db.despesa.projeto == projeto.id) &
                                    (db.despesa.fonte_recurso == "Outros")).select(orderby=db.despesa.nome)
                terceiros = db((db.despesa.projeto == projeto.id) &
                               (db.despesa.fonte_recurso == "Pagamento a Terceiros")).select(orderby=db.despesa.nome)
                self.set_font('Arial', '', 7)
                self.ln()
                self.cell(270, 8, 'Resumo de Despesas Incentivadas', 1, 1, 'L')
                self.cell(16, 8, tl('Orçamentos'), 1, 0, 'L')
                self.cell(190, 8, tl('Nome da Despesa'), 1, 0, 'L')

                self.cell(16, 8, 'Quantidade', 1, 0, 'L')
                self.cell(16, 8, tl('Unidade'), 1, 0, 'L')
                self.cell(16, 8, tl('Valor unitário'), 1, 0, 'L')
                self.cell(16, 8, tl('Total'), 1, 1, 'L')
                totalano = 0.00
                total = 0.00
                for despesa in despesasincentivo:

                    self.cell(16, 8, count_orcamento(despesa), 1, 0, 'L')
                    x = self.x
                    y1 = self.y
                    self.multi_cell(190, 8, tl(despesa.nome), 1, 0, 'L')
                    self.x = x + 190
                    y2 = self.y
                    self.y = y1
                    self.cell(16, 8, str(despesa.quantidade), 1, 0, 'L')

                    self.cell(16, 8, tl(despesa.unidade), 1, 0, 'L')
                    self.cell(16, 8, valor(despesa.valor_unitario), 1, 0, 'L')

                    d = float(despesa.quantidade) * despesa.valor_unitario
                    total = total + d

                    self.cell(16, 8, valor(total), 1, 1, 'L')
                    y3 = self.y
                    if y2 > y3:
                        self.y = y2
                    else:
                        self.y = y3
                self.cell(254, 8, tl('Total'), 1, 0, 'L')
                self.cell(16, 8, valor(total), 1, 1, 'L')

                p = 1
                self.ln()
                totaldespesa = [0.00] * (projeto.meses + 1)
                self.cell(270, 8, 'Resumo de Outras Despesas', 1, 1, 'L')
                self.cell(16, 8, tl('Orçamentos'), 1, 0, 'L')
                self.cell(190, 8, tl('Nome da Despesa'), 1, 0, 'L')

                self.cell(16, 8, 'Quantidade', 1, 0, 'L')
                self.cell(16, 8, tl('Unidade'), 1, 0, 'L')
                self.cell(16, 8, tl('Valor unitário'), 1, 0, 'L')
                self.cell(16, 8, tl('Total'), 1, 1, 'L')

                totalano = 0.00
                total = 0.00
                for despesa in outrasdespesas:

                    self.cell(16, 8, count_orcamento(despesa), 1, 0, 'L')
                    x = self.x
                    y1 = self.y
                    self.multi_cell(190, 8, tl(despesa.nome), 1, 0, 'L')
                    self.x = x + 190
                    y2 = self.y
                    self.y = y1
                    self.cell(16, 8, str(despesa.quantidade), 1, 0, 'L')

                    self.cell(16, 8, tl(despesa.unidade), 1, 0, 'L')
                    self.cell(16, 8, valor(despesa.valor_unitario), 1, 0, 'L')

                    d = float(despesa.quantidade) * despesa.valor_unitario
                    total = total + d

                    self.cell(16, 8, valor(total), 1, 1, 'L')
                    y3 = self.y
                    if y2 > y3:
                        self.y = y2
                    else:
                        self.y = y3

                self.cell(254, 8, tl('Total'), 1, 0, 'L')
                self.cell(16, 8, valor(totalano), 1, 1, 'L')

                p = 1
                totaldespesa = [0.00] * (projeto.meses + 1)
                self.ln()
                self.cell(270, 8, 'Resumo de Pagamento a Terceiros', 1, 1, 'L')
                self.cell(16, 8, tl('Orçamentos'), 1, 0, 'L')
                self.cell(190, 8, tl('Nome da Despesa'), 1, 0, 'L')

                self.cell(16, 8, 'Quantidade', 1, 0, 'L')
                self.cell(16, 8, tl('Unidade'), 1, 0, 'L')
                self.cell(16, 8, tl('Valor unitário'), 1, 0, 'L')
                self.cell(16, 8, tl('Total'), 1, 1, 'L')

                totalano = 0.00
                total = 0.00
                for despesa in terceiros:

                    self.cell(16, 8, count_orcamento(despesa), 1, 0, 'L')
                    x = self.x
                    y1 = self.y
                    self.multi_cell(190, 8, tl(despesa.nome), 1, 0, 'L')
                    self.x = x + 190
                    y2 = self.y
                    self.y = y1
                    self.cell(16, 8, str(despesa.quantidade), 1, 0, 'L')

                    self.cell(16, 8, tl(despesa.unidade), 1, 0, 'L')
                    self.cell(16, 8, valor(despesa.valor_unitario), 1, 0, 'L')

                    d = float(despesa.quantidade) * despesa.valor_unitario
                    total = total + d

                    self.cell(16, 8, valor(total), 1, 1, 'L')
                    y3 = self.y
                    if y2 > y3:
                        self.y = y2
                    else:
                        self.y = y3

                self.cell(254, 8, tl('Total'), 1, 0, 'L')
                self.cell(16, 8, valor(totalano), 1, 0, 'L')

            def documentos(self):
                pdf.add_page('P')
                documentos = db(db.documento.projeto == projeto.id).select(orderby=db.documento.id)
                self.cell(65, 8, 'Tipo de Documento', 1, 0, 'L')
                self.cell(20, 8, 'Data de envio', 1, 0, 'L')
                self.cell(75, 8, tl('Descrição'), 1, 0, 'L')
                self.cell(30, 8, tl('Tamanho do Arquivo'), 1, 1, 'L')
                for documento in documentos:
                    self.cell(65, 8, tl(documento.tipo), 1, 0, 'L')
                    self.cell(20, 8, make_data(documento.enviado_em), 1, 0, 'L')
                    x = self.x
                    y1 = self.y
                    self.multi_cell(75, 8, tl(documento.descricao), 1, 0, 'L')
                    self.x = x + 75
                    y2 = self.y
                    self.y = y1
                    self.cell(30, 8, tl(' %s kb ' % (len(documento.arquivo))), 1, 1, 'L')
                    y3 = self.y
                    if y2 > y3:
                        self.y = y2
                    else:
                        self.y = y3

            def despesas(self):
                #self.add_page('P')
                y0 = 25
                despesasincentivo = db((db.despesa.projeto == projeto.id) &
                                       (db.despesa.fonte_recurso == "Incentivo")).select(orderby=db.despesa.nome)
                outrasdespesas = db((db.despesa.projeto == projeto.id) &
                                    (db.despesa.fonte_recurso == "Outros")).select(orderby=db.despesa.nome)
                terceiros = db((db.despesa.projeto == projeto.id) &
                               (db.despesa.fonte_recurso == "Pagamento a Terceiros")).select(orderby=db.despesa.nome)
                p = 1
                totalmeses = projeto.meses
                totaldespesa = [0.00] * (projeto.meses + 1)
                # ultimo semestre
                if totalmeses % 6 == 0:
                    ultimosemestre = totalmeses / 6
                else:
                    ultimosemestre = int(totalmeses / 6) + 1
                while p < totalmeses:
                    self.set_font('Arial', '', 7)
                    pdf.add_page('L')
                    if (p + 5) % 6 == 0:
                        semestre = (p + 5) / 6
                    else:
                        semestre = int((p - 1) / 6) + 1

                    self.cell(270, 8, tl('Cronograma de metas e despesas do %sº período de 6 meses ' % (semestre)), 1,
                              1, 'L')
                    metas = db(db.meta.projeto == projeto.id).select()
                    self.ln()
                    self.cell(270, 8, tl('Metas do período'), 1, 1, 'L')
                    self.cell(30, 8, 'Quantidade total', 1, 0, 'L')
                    self.cell(140, 8, tl('Descrição da Meta'), 1, 0, 'L')
                    self.cell(100, 8, tl('Documentos comprobatórios'), 1, 1, 'L')

                    for meta in metas:
                        #qs = json.loads(meta.quantidade_semestre)
                        y1 = self.y
                        s1 = self.get_string_width(meta.meta)
                        s2 = self.get_string_width(meta.documentos_comprobatorios.rstrip())
                        if y1 > 150 and (s1 > 138 or s2 > 100):
                            self.add_page('L')
                        try:
                            ms = meta.quantidade_semestre['%s' % (semestre)]
                        except:
                            ms = '0'
                        self.cell(30, 8, str(ms), 1, 0, 'L')
                        x = self.x
                        self.multi_cell(140, 8, tl(meta.meta), 1, 0, 'L')
                        self.x = x + 140
                        y2 = self.y
                        if y2 < y1:
                            self.y = y0
                        else:
                            self.y = y1

                        self.multi_cell(100, 8, tl(meta.documentos_comprobatorios.rstrip()), 1, 1, 'L')
                        y3 = self.y
                        if y2 > y3:
                            self.y = y2
                        else:
                            self.y = y3
                    self.ln()
                    self.cell(164, 8, 'Cronograma Detalhado de Despesas Incentivadas', 1, 0, 'L')
                    self.cell(106, 8, 'Meses', 1, 1, 'L')
                    self.cell(16, 8, 'Quantidade', 1, 0, 'L')
                    self.cell(116, 8, tl('Nome da Despesa'), 1, 0, 'L')

                    self.cell(16, 8, tl('Unidade'), 1, 0, 'L')
                    self.cell(16, 8, tl('Valor unitário'), 1, 0, 'L')

                    for m in range(p, p + 6):
                        self.cell(15, 8, str(m), 1, 0, 'L')
                    self.cell(16, 8, tl('Total'), 1, 1, 'L')

                    totalano = 0.00
                    for despesa in despesasincentivo:
                        total = 0.00

                        self.cell(16, 8, str(despesa.quantidade), 1, 0, 'L')
                        x = self.x
                        y1 = self.y
                        self.multi_cell(116, 8, tl(despesa.nome), 1, 0, 'L')
                        self.x = x + 116
                        y2 = self.y
                        self.y = y1
                        self.cell(16, 8, tl(despesa.unidade), 1, 0, 'L')
                        self.cell(16, 8, valor(despesa.valor_unitario), 1, 0, 'L')
                        despesas = despesa.quantidade_mensal

                        for m in range(p, p + 6):
                            try:
                                self.cell(15, 8, str(valor(float(despesas['%s' % m]) * despesa.valor_unitario)), 1, 0,
                                          'L')

                            except:
                                self.cell(15, 8, ' ', 1, 0, 'L')
                            try:
                                d = float(despesas['%s' % m]) * despesa.valor_unitario
                                totaldespesa[m] = totaldespesa[m] + d
                                total = total + d
                                totalano = totalano + d
                                incentivo += d
                            except:
                                pass

                        self.cell(16, 8, valor(total), 1, 1, 'L')
                        y3 = self.y
                        if y2 > y3:
                            self.y = y2
                        else:
                            self.y = y3

                    self.cell(164, 8, tl('Total Mês/Período de 6 meses'), 1, 0, 'L')
                    for m in range(p, p + 6):
                        try:
                            self.cell(15, 8, str(valor(totaldespesa[m])), 1, 0, 'L')

                        except:
                            self.cell(15, 8, ' ', 1, 0, 'L')
                    self.cell(16, 8, valor(totalano), 1, 1, 'L')
                    self.ln()
                    #outras despesas
                    totaldespesa = [0.00] * (projeto.meses + 1)
                    self.cell(164, 8, 'Cronograma Detalhado de Outras Despesas', 1, 0, 'L')
                    self.cell(106, 8, 'Meses', 1, 1, 'L')
                    self.cell(16, 8, 'Quantidade', 1, 0, 'L')
                    self.cell(116, 8, tl('Nome da Despesa'), 1, 0, 'L')

                    self.cell(16, 8, tl('Unidade'), 1, 0, 'L')
                    self.cell(16, 8, tl('Valor unitário'), 1, 0, 'L')

                    for m in range(p, p + 6):
                        self.cell(15, 8, str(m), 1, 0, 'L')
                    self.cell(16, 8, tl('Total'), 1, 1, 'L')

                    totalano = 0.00
                    for despesa in outrasdespesas:
                        total = 0.00
                        self.cell(16, 8, str(despesa.quantidade), 1, 0, 'L')
                        x = self.x
                        y1 = self.y
                        self.multi_cell(116, 8, tl(despesa.nome), 1, 0, 'L')
                        self.x = x + 116
                        y2 = self.y
                        self.y = y1
                        self.cell(16, 8, tl(despesa.unidade), 1, 0, 'L')
                        self.cell(16, 8, valor(despesa.valor_unitario), 1, 0, 'L')
                        despesas = despesa.quantidade_mensal

                        for m in range(p, p + 6):
                            try:
                                self.cell(15, 8, str(valor(float(despesas['%s' % m]) * despesa.valor_unitario)), 1, 0,
                                          'L')

                            except:
                                self.cell(15, 8, ' ', 1, 0, 'L')
                            try:
                                d = float(despesas['%s' % m]) * despesa.valor_unitario
                                totaldespesa[m] = totaldespesa[m] + d
                                total = total + d
                                totalano = totalano + d
                                incentivo += d
                            except:
                                pass

                        self.cell(16, 8, valor(total), 1, 1, 'L')
                        y3 = self.y
                        if y2 > y3:
                            self.y = y2
                        else:
                            self.y = y3

                    self.cell(164, 8, tl('Total Mês/Período de 6 meses'), 1, 0, 'L')
                    for m in range(p, p + 6):
                        try:
                            self.cell(15, 8, str(valor(totaldespesa[m])), 1, 0, 'L')

                        except:
                            self.cell(15, 8, ' ', 1, 0, 'L')
                    self.cell(16, 8, valor(totalano), 1, 1, 'L')

                    self.ln()
                    #Pagamento a Terceiros
                    totaldespesa = [0.00] * (projeto.meses + 1)
                    self.cell(164, 8, 'Cronograma Detalhado de Pagamento a Terceiros', 1, 0, 'L')
                    self.cell(106, 8, 'Meses', 1, 1, 'L')
                    self.cell(16, 8, 'Quantidade', 1, 0, 'L')
                    self.cell(116, 8, tl('Nome da Despesa'), 1, 0, 'L')

                    self.cell(16, 8, tl('Unidade'), 1, 0, 'L')
                    self.cell(16, 8, tl('Valor unitário'), 1, 0, 'L')

                    for m in range(p, p + 6):
                        self.cell(15, 8, str(m), 1, 0, 'L')
                    self.cell(16, 8, tl('Total'), 1, 1, 'L')

                    totalano = 0.00
                    for despesa in terceiros:
                        total = 0.00
                        self.cell(16, 8, str(despesa.quantidade), 1, 0, 'L')
                        x = self.x
                        y1 = self.y
                        self.multi_cell(116, 8, tl(despesa.nome), 1, 0, 'L')
                        self.x = x + 116
                        y2 = self.y
                        self.y = y1
                        self.cell(16, 8, tl(despesa.unidade), 1, 0, 'L')
                        self.cell(16, 8, valor(despesa.valor_unitario), 1, 0, 'L')
                        despesas = despesa.quantidade_mensal

                        for m in range(p, p + 6):
                            try:
                                self.cell(15, 8, str(valor(float(despesas['%s' % m]) * despesa.valor_unitario)), 1, 0,
                                          'L')

                            except:
                                self.cell(15, 8, ' ', 1, 0, 'L')
                            try:
                                d = float(despesas['%s' % m]) * despesa.valor_unitario
                                totaldespesa[m] = totaldespesa[m] + d
                                total = total + d
                                totalano = totalano + d
                                incentivo += d
                            except:
                                pass

                        self.cell(16, 8, valor(total), 1, 1, 'L')
                        y3 = self.y
                        if y2 > y3:
                            self.y = y2
                        else:
                            self.y = y3

                    self.cell(164, 8, tl('Total Mês/Período de 6 meses'), 1, 0, 'L')
                    for m in range(p, p + 6):
                        try:
                            self.cell(15, 8, str(valor(totaldespesa[m])), 1, 0, 'L')

                        except:
                            self.cell(15, 8, ' ', 1, 0, 'L')
                    self.cell(16, 8, valor(totalano), 1, 1, 'L')

                    p += 6

                p = 1
                totalmeses = projeto.meses
                totaldespesa = [0.00] * (projeto.meses + 1)


            def locais(self):
                locais = db(db.local.projeto == projeto.id).select()
                i = 1
                for local in locais:
                    self.set_font('Arial', '', 7)
                    pdf.add_page('P')
                    self.cell(190, 8, tl('Local de Realização nº %s ' % (i)), 1, 1, 'L')
                    self.cell(190, 8, tl('Nome: %s' % (local.nome)), 1, 1, 'L')
                    self.cell(190, 8, tl('Município: %s' % (local.municipio.municipio)), 1, 1, 'L')

                    self.cell(190, 8, tl('Responsável: %s' % (local.responsavel)), 1, 1, 'L')
                    self.multi_cell(190, 8, tl('Endereço: %s' % (local.endereco)), 1, 1, 'L')
                    self.cell(190, 8, tl('CEP: %s' % (local.cep)), 1, 1, 'L')
                    self.cell(95, 8, tl('Tipo: %s' % (local.tipo)), 1, 0, 'L')
                    self.cell(95, 8, tl('Tipo de Piso: %s' % (local.piso)), 1, 1, 'L')
                    self.cell(95, 8, tl('Área ou Distância Total: %s' % (local.area_total)), 1, 0, 'L')
                    self.cell(95, 8, tl('Área de jogo ou distância por volta: %s' % (local.area_de_jogo)), 1, 1, 'L')
                    list = [local.foto_1, local.foto_2, local.foto_3, local.foto_4]
                    ny = self.y + 2
                    for place in list:
                        try:
                            self.image(get_file_path(place), x=self.x, y=ny, w=45, h=40, type=place[-3:])
                            nx = self.x + 45
                            if nx + 40 > 190:
                                self.ln()
                                ny = self.y + 2
                            self.set_x(nx + 2)
                        except:
                            pass
                    i += 1

        pdf = PDF()
        pdf.First_Page()
        pdf.metas()

        pdf.despesas()
        pdf.locais()
        pdf.documentos()
        ################################
        filename = "relatorio_projeto_%s_%s.pdf" % (projeto.id, request.now.strftime('%Y_%m_%d_%H_%M_%S'))

        #try:
        #    os.remove(path)
        #except:
        #    pass
        if output == 'D':
            path = "applications/%s/static/temp/%s" % (request.application, filename)
            pdf.output(path)
            redirect(URL(r=request, c='static', f='temp', args=[filename]))
        else:
            path = "applications/%s/static/declaracao/%s" % (request.application, filename)
            pdf.output(path)
            #redirect(URL(r=request, c='static', f='declaracao', args=[filename]))
        return filename
    else:
        redirect(URL(r=request, f='projeto'))


def incentivo(projeto_id):
    despesas = db(db.despesa.projeto == projeto_id).select()
    nome = db.projeto[projeto_id].nome
    st = db(db.historico.projeto == projeto_id).select(orderby=~db.historico.id).first()
    if st:
        status = st.ocorrencia
    else:
        status = db.projeto[projeto_id].status_analise
    total_incentivado = 0.0
    total_despesas = 0.0
    total_terceiro = 0.0
    for despesa in despesas:
        total_despesas += float(despesa.total)
        if despesa.fonte_recurso == "Incentivo":
            total_incentivado += float(despesa.total)
        if despesa.fonte_recurso == "Pagamento a Terceiros":
            total_terceiro += float(despesa.total)
    if total_terceiro > 0.00:
        total_incentivado = total_incentivado + total_terceiro
    return dict(nome=nome, incentivo=total_incentivado, terceiros=total_terceiro, seej=total_incentivado / 9,
                total=total_incentivado / 0.9, status=status)


def cnpj_formata(value):
    formatado = value[0:2] + '.' + value[2:5] + '.' + value[5:8] + '/ ' + value[8:12] + '-' + value[12:14]
    return formatado


def cep_formata(value):
    formatado = value[0:2] + '.' + value[2:5] + '-' + value[5:8]
    return formatado


def cpf_formata(value):
    #if value ==11:
    formatado = value[0:3] + '.' + value[3:6] + '.' + value[6:9] + '-' + value[9:11]
    #else:
    #    formatado=value
    #formatado = value
    return formatado


def repasses_tc(tc_id):
    rows = db(db.repasse.tc == tc_id).select()
    rp = 0.00
    n = len(rows)
    lista = '''Parcela     |Data do Repasse     |Valor Estimado
'''
    i = 1
    try:
        for row in rows:
            rp += row.valor
            lista += '''%s                |%s              |%s
''' % (i, make_data(row.data_repasse), money(row.valor))
            i += 1
        tc = db.tc[row.tc]
        total = rp / 0.9
        tc.update_record(valor_total=total)
        setes = rp / 9
    except:
        total = 0.00
        setes = 0.00
        lista = ''
    return dict(n=n, projeto=money(rp), total=total, seej=setes, lista=lista)


def gerar_pdf_tc(output=None):
    executor_or_admin(auth.user_id)
    if not request.args(0):
        redirect(r=request, f='index')

    projeto = db.projeto[request.args(0)]
    tc = db.tc[request.args(1)]
    import locale

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    from gluon.contrib.pyfpdf import FPDF
    from datetime import timedelta, date, datetime

    #url = URL('download')
    #if not session.register_form or not request.args(0):
    #    redirect(URL(r=request, f='user/register'))
    #else:
    class PDF(FPDF):
        def __init__(self):
            FPDF.__init__(self)
            self.municipio = ''

        def Header(self):
            #print "header"
            #Logo
            #self.Image('logo_pb.png',10,8,33)

            #Arial bold 15
            self.set_font('Arial', 'B', 10)

            return

        def Footer(self):
            #print "footer"
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, lt('Página ' + str(self.page_no())), 0, 0, 'C')
            return

        def First_Page(self):

            self.add_page()
            self.set_font('Arial', '', 8)
            if output:
                p = "Prévia do "
            else:
                p = ''
            self.multi_cell(190, 5, tl('''                                                                                  MINAS OLÍMPICA INCENTIVO AO ESPORTE
                                                                                     %s TERMO DE COMPROMISSO - TC %s/%s
                                                                                                          EDITAL %s/%s ''' % (
                p, tc.id, tc.data_cadastro.strftime('%Y'), projeto.edital, projeto.edital.data_inicio.strftime("%Y"))),
                            1,
                            1)
            ie = IS_IEMG()
            self.multi_cell(190, 5,
                            tl('''Eu, apoiador, venho por meio deste formalizar o incentivo nos seguintes termos:'''),
                            1, 1, 'C')
            self.ln(2)
            self.cell(190, 5, tl('1. INFORMAÇÕES DO APOIADOR'), 1, 1)
            self.multi_cell(190, 5, tl('''Razão Social: %s
Endereço: %s  Município: %s   CEP: %s
Inscrição Estadual: %s
CNPJ: %s
Representante Legal: %s  CPF: %s  Telefone: %s  Email: %s
''' % (tc.razao_social,
       tc.endereco,
       tc.municipio.municipio,
       cep_formata(tc.cep),
       ie.formatter(tc.inscricao_estadual),
       cnpj_formata(tc.cnpj),
       tc.representante_legal,
       cpf_formata(tc.cpf),
       to_telefone(tc.telefone), tc.email)),
                            1, 1, 'C')
            self.ln(2)
            self.cell(190, 5, tl('2. INFORMAÇÕES DO EXECUTOR'), 1, 1)
            self.multi_cell(190, 5, tl('''Razão Social: %s
CNPJ: %s
Representante Legal: %s    Email: %s Telefone: %s
''' % (projeto.empreendedor.first_name,
       cnpj_formata(projeto.empreendedor.cnpj),
       projeto.empreendedor.responsavel_legal,
       projeto.empreendedor.email,
       to_telefone(projeto.empreendedor.telefone),)),
                            1, 1, 'C')
            self.ln(2)
            self.cell(190, 5, tl('3. INFORMAÇÕES DO PROJETO ESPORTIVO'), 1, 1)
            self.multi_cell(190, 5, tl('''Nome: %s
Número da C.A.: %s/%s''' % (projeto.nome, projeto.id, projeto.criado_em.strftime(("%Y")))),
                            1, 1, 'C')
            cc = db(db.conta_corrente.projeto == projeto.id).select().first()
            self.ln(2)
            self.cell(190, 5, tl('4. DADOS DA CONTA BANCÁRIA DO PROJETO ESPORTIVO (não esquecer o dígito)'), 1, 1)
            self.multi_cell(190, 5, tl('''Nome do banco: %s  Nº do Banco.: %s
Nº da Agência: %s  Nº da Conta Corrente: %s
''' % (cc.nome_banco, cc.numero_banco, cc.numero_agencia, cc.numero_conta)),
                            1, 1, 'C')
            rp = repasses_tc(tc.id)
            self.ln(2)
            self.cell(190, 5, tl('5. ESPECIFICAÇÃO DOS RECURSOS'), 1, 1)
            self.multi_cell(190, 5, tl('''5.1 VALOR TOTAL DO INCENTIVO FISCAL:  %s

5.2 VALOR REPASSADO AO PROJETO ESPORTIVO (90%% do valor total do incentivo) : %s
%s
5.3 VALOR A SER DEPOSITADO  EM COTA ÚNICA NA DATA DE %s, POR MEIO DE DOCUMENTO DE ARRECADAÇÃO ESTADUAL-DAE A FAVOR DA SETES (10%% do valor do Incentivo Fiscal) : %s
''' % (money(rp['total']), rp['projeto'], rp['lista'], make_data(tc.data_parcela_seej), money(rp['seej']))),
                            1, 1, 'C')
            self.ln(2)
            self.cell(190, 5, tl('6. MODALIDADE DO INCENTIVO FISCAL'), 1, 1)
            self.multi_cell(190, 5, tl('''%s
''' % (tc.modalidade_incentivo)),
                            1, 1, 'C')
            self.ln(2)
            self.cell(190, 5, tl('DECLARAÇÃO'), 1, 1, 'C')
            self.multi_cell(190, 5, tl('''Declaro estar ciente das condições estabelecidas nos artigos 24 a 28 da  Lei Nº 20.824/2013 e no   Decreto 46.308/2013 em especial os Capítulos  III-DA FORMA DE OBTENÇÃO DO INCENTIVO FISCAL, IV-DA OPERACIONALIZAÇÃO DO INCENTIVO FISCAL e VII-DAS PENALIDADES.

___________________________________                                          _________________________                           ________________________
Local e Data	                                                                                              Apoiador/Contribuinte	                                                 Executor
'''),
                            1, 1, 'C')
            self.ln(4)
            self.cell(190, 5, tl('Espaço Reservado para a Subsecretaria da Receita Estadual'), 1, 1, 'C')
            self.multi_cell(190, 5, tl('''O Contribuinte acima qualificado fica autorizado a utilizar o incentivo fiscal na forma prevista neste Termo de Compromisso.

                        __________________________, aos __________ de ______________ de_________

                                                                            ______________________________________
                                                                                Subsecretário da Receita Estadual
'''),
                            1, 1, 'C')

    pdf = PDF()
    pdf.First_Page()


    ################################
    filename = "termo_compromisso_%s_%s_%s_%s.pdf" % (
        projeto.id, tc.id, auth.user_id, request.now.strftime('%Y_%m_%d_%H_%M_%S'))
    if output == 'D':
        path = "applications/%s/static/temp/%s" % (request.application, filename)
        pdf.output(path)
        redirect(URL(r=request, c='static', f='temp', args=[filename]))
    else:
        path = "applications/%s/static/tc/%s" % (request.application, filename)
        pdf.output(path)
        return filename
        #try:
        #    os.remove(path)
        #except:
        #    pass

        #return filename


def tcs_aprovados(projeto_id):
    records = db((db.tc.projeto == projeto_id) & (db.tc.aprovado == True) & (db.repasse.tc == db.tc.id)).select()
    total = 0.00
    for record in records:
        total += record.repasse.valor

    return total / 0.9


def check_reajustavel(projeto):
    p = float(tcs_aprovados(projeto.id)) / incentivo(projeto.id)['total']
    if p >= 0.350 and projeto.status_analise in zip(status_aprovados[:4], status_aprovados[-1:]):
        return True
    else:
        return False


def check_captavel(projeto):
    ml = status_aprovados[0:4]
    ml.extend(status_aprovados[-1:])
    if projeto.status_analise in ml:
        return True
    else:
        return False


status_execucao = ['Início de Execução Autorizado', 'Em readequação', 'Protocolo Readequação', 'Diligência Readequação',
                   'Readequação Aprovada', 'Readequação Reprovada']


def check_readequavel(projeto):
    #p = float(tcs_aprovados(projeto.id)) / incentivo(projeto.id)['total']
    if projeto.status_analise in status_execucao[:1]:
        return True
    else:
        return False


def check_edicao_tc(tc_id, projeto_id):
    from datetime import timedelta

    h = db((db.historico_tc.tc == tc_id) & (db.historico_tc.ocorrencia == "Protocolado")).select().first()
    ap = db((db.historico_tc.tc == tc_id) & (db.historico_tc.ocorrencia == "Aprovado")).select().first()
    projeto = db.projeto[projeto_id]
    if ap:
        return False
    elif check_captavel(projeto):
        return True
    else:
        return False


def prazo_captacao(projeto_id):
    row = db(
        (db.historico.projeto == projeto_id) & (db.historico.ocorrencia.belongs(['Aprovado', 'Prorrogado']))).select(
        orderby=~db.historico.id).first()
    from datetime import timedelta

    return make_data(row.quando + timedelta(days=365))


##valida inscrição Estadual MG
#www.sintegra.gov.br/Cad_Estados/cad_MG.html
# IEMG Cemig 062.322136.0087


class IS_IEMG(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message

    def __call__(self, value):

        c = []
        #limpa outros caracteres que não números
        for d in value:
            if d.isdigit():
                c.append(d)
        cl = str(''.join(c))
        #return (value, 'cpf incorreto'+str(cl))
        if len(cl) == 13:
            iemg = cl
        else:

            return (value, 'Número de dígitos incorreto para Inscrição Estadual de Minas Gerais')

        if iemg:

            """ Pega apenas os 11 primeiros dígitos da IEMG e gera o 1º dígito que falta """

            base = iemg[:11]

            a = base[:3]
            b = base[3:]
            nbase = a + '0' + b

            m = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
            r = []
            for i in range(0, 12):
                r.append(str(int(nbase[i]) * m[i]))
                #return(str(novoCnpj),'aquiok')
            s = ''.join(r)
            soma = 0
            for c in s:
                soma += int(c)
            d = str(soma)[:-1]
            dezena = (int(d) + 1) * 10
            digito1 = dezena - soma

            #validação do 2º digito
            nbase = base + str(digito1)
            m = [3, 2, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            s = 0
            for i in range(0, 12):
                s += int(nbase[i]) * m[i]

            resto = s % 11
            digito2 = 11 - resto
            if digito2 == 10:
                digito2 = 0
            calculado = base + str(digito1) + str(digito2)
            if calculado == iemg:  #cnpj = ''.join(novoCnpj)

                return (str(iemg), None)

            else:
                return (value, 'A Inscrição Estadual não é válida, deveria ser %s %s ' % (str(calculado), str(resto)) )

                #except:
                #    return (value, 'algum erro' + str(value))

    def formatter(self, value):
        formatado = value[0:3] + '.' + value[3:10] + '.' + value[10:13]
        return formatado


def iemg(value):
    formatado = value[0:3] + '.' + value[3:10] + '.' + value[10:13]
    return formatado


def valor_protocolados():
    rows = db.executesql("select distinct projeto from historico where ocorrencia='Protocolo'")
    incentivado = 0.00
    terceiros = 0.00
    projetos = []
    seej = 0.00
    total = 0.00
    for row in rows:
        status = db.projeto[row[0]].status_analise
        if status != 'Indeferido':
            r = incentivo(row[0])
            projetos.append(r)

            incentivado += r['incentivo']
            terceiros += r['terceiros']
            seej += r['seej']
            total += r['total']

    return dict(projetos=projetos, incentivado=incentivado, setes=seej, terceiros=terceiros, total=total)


def limite_ie(ie, ano):
    limite = db(db.anual.ano == ano).select().first()
    apoio = db.executesql(
        "select inscricao_estadual,sum(valor_total) from tc where extract(year from data_aprovacao) = %s and aprovado = 'T' and inscricao_estadual='%s' group by inscricao_estadual" % (
            ano, ie))
    if apoio:
        if apoio[0][1] >= limite.limite_ie:
            up = 'Sim'
            saldo = 0.00
        else:
            up = 'Não'
            saldo = limite.limite_ie - apoio[0][1]
        apoiado = apoio[0][1]
    else:
        up = 'Não'
        saldo = limite.limite_ie
        apoiado = 0.00
    return dict(apoio=apoiado, atingido=up, saldo=saldo, limite=limite_ie)


def limite_estadual(ano):
    limite = db(db.anual.ano == ano).select().first()
    apoio = db.executesql(
        "select sum(valor_total) from tc where extract(year from data_aprovacao) = %s and aprovado = 'T'" % (ano))
    try:
        if apoio[0][0] >= limite.limite:
            up = 'Sim'
            saldo = 0.00
        else:
            up = 'Não'
            saldo = limite.limite - apoio[0][0]
        apoiado = apoio[0][0]
    except:
        up = 'Não'
        saldo = 0.00
        apoiado = 0.00
    return dict(apoio=apoiado, limite=limite.limite, atingido=up, saldo=saldo)


def check_tc_aprovado(tc_id):
    row = db(db.historico_tc.tc == tc_id).select(orderby=~db.historico_tc.id).first()
    return row.ocorrencia


def fassumir(projeto_id):
    fassumir = '''<form><input type=hidden name='assumir' value=%s>
    <input type='submit' value='Assumir'>
    </form>''' % projeto_id

    return XML(fassumir)


def assumir(projeto_id):
    projeto = db.projeto[projeto_id]
    projeto.update_record(analista=auth.user_id)


def filtra_projetos():
    query = ''
    ordem = db.projeto.id
    if request.vars.status:
        query = (db.projeto.status_analise == db.status_analise.status)
        ordem = db.status_analise.id
    if request.vars.datastatus:
        ordem = ~db.projeto.data_status
    if request.vars.projetoid:
        query = (db.projeto.id == request.vars.projetoid)
    if request.vars.nomeprojeto:
        query = (db.projeto.nome.contains(request.vars.nomeprojeto))
    if request.vars.nomestatus:
        query = (db.projeto.status_analise.contains(request.vars.nomestatus))
    s = ['Início Cadastro', 'Protocolo', 'Diligência Protocolo', 'Retorno de Diligência Protocolo',
         'Em análise parecer técnico', 'Diligência Parecer Técnico', 'Retorno de Diligência Parecer Técnico',
         'Agendado', 'Diligência Comitê', 'Retorno de Diligência Comitê', 'Reprovado']
    if request.vars.nomeanalista:
        rows = db(db.auth_user.first_name.contains(request.vars.nomeanalista)).select()
        analista = []
        for row in rows:
            analista.append(row.id)
        query = (db.projeto.analista.belongs(analista))
    if request.vars.nomeedital:
        rows = db(db.edital.nome.contains(request.vars.nomeedital)).select()
        edital = []
        for row in rows:
            edital.append(row.id)
        query = (db.projeto.edital.belongs(edital))
    if request.vars.nomeexecutor:
        rows = db(db.auth_user.first_name.contains(request.vars.nomeexecutor)).select()
        executor = []
        for row in rows:
            executor.append(row.id)
        query = (db.projeto.empreendedor.belongs(executor))
    return query, ordem, s


def log_alteracoes(projeto_id):
    inicio = 'teste'
    log = ''
    nofields = ['projeto', 'current_record', 'id', 'empreendedor', 'readonly', 'previa', 'analisar', 'analista',
                'status_analise', 'data_status', 'criado_em', 'is_active', 'created_on', 'created_by', 'modified_on',
                'modified_by', 'data_cadastro']
    row = db(db.historico.projeto == projeto_id).select(orderby=db.historico.id).last()

    if row and row.ocorrencia[
               :22] == 'Retorno de Diligência' or row.ocorrencia == 'Protocolo Reajuste' or row.ocorrencia == "Protocolo Readequação":
        d = db(db.historico.ocorrencia.startswith('Diligência')).select(orderby=db.historico.id).last()
        inicio = d.quando
        projeto = db.projeto[projeto_id]
        rows = db((db.projeto_archive.current_record == projeto_id) & (
            db.projeto_archive.status_analise == row.ocorrencia)).select()
        fields = [x for x in db.projeto.fields if x not in nofields]
        log = 'Alterações nas Informações Básicas:\n'
        for row in rows:
            for field in fields:
                if row[field] != projeto[field]:
                    log += 'Campo %s alterado de :\n%s \n para: \n %s \n' % (field, row[field], projeto[field])


        #metas
        rows = db((db.meta.projeto == projeto_id) & (db.meta.modified_on > inicio)).select()
        fields = [x for x in db.meta.fields if x not in nofields]
        log += "\n\nAlterações em Metas: \n\n"
        for row in rows:
            olds = db((db.meta_archive.current_record == row.id) & (db.meta_archive.modified_on > inicio)).select()
            logf = ''
            if len(olds) < 1:
                log += '\nMeta "%s" adicionada \n' % row.meta
            else:

                for old in olds:
                    for field in fields:
                        if row[field] != old[field]:
                            logf += '\nCampo %s alterado de: \n %s \n para: \n %s' % (field, old[field], row[field])
            if len(logf) > 0:
                log += '\nMeta %s :\n %s' % (row.meta, logf)
        rows = db.executesql("select meta from meta where projeto = %s and is_active = 'F' " % projeto_id)
        for row in rows:
            log += '\n\nMeta "%s" excluída' % row[0]

        #despesas
        rows = db((db.despesa.projeto == projeto_id) & (db.despesa.modified_on > inicio)).select()
        fields = [x for x in db.despesa.fields if x not in nofields]
        log += "\n\nAlterações em Despesas: \n\n"
        for row in rows:
            olds = db(
                (db.despesa_archive.current_record == row.id) & (db.despesa_archive.modified_on > inicio)).select()
            logf = ''
            if len(olds) < 1:
                log += '\nDespesa "%s" adicionada \n' % row.nome
            else:

                for old in olds:
                    for field in fields:
                        if row[field] != old[field]:
                            logf += '\nCampo %s alterado de: \n %s \n para: \n %s' % (field, old[field], row[field])
            if len(logf) > 0:
                log += '\nDespesa %s :\n %s' % (row.nome, logf)
        rows = db.executesql("select nome from despesa where projeto = %s and is_active = 'F' " % projeto_id)
        for row in rows:
            log += '\n\nDespesa "%s" excluída' % row[0]

        #locais
        rows = db((db.local.projeto == projeto_id) & (db.local.modified_on > inicio)).select()
        fields = [x for x in db.local.fields if x not in nofields]
        log += "\n\nAlterações em Locais: \n\n"
        for row in rows:
            olds = db((db.local_archive.current_record == row.id) & (db.local_archive.modified_on > inicio)).select()
            logf = ''
            if len(olds) < 1:
                log += '\nLocal "%s" adicionada \n' % row.nome
            else:

                for old in olds:
                    for field in fields:
                        if row[field] != old[field]:
                            logf += '\nCampo %s alterado de: \n %s \n para: \n %s' % (field, old[field], row[field])
            if len(logf) > 0:
                log += '\nLocal %s :\n %s' % (row.nome, logf)
        rows = db.executesql("select nome from local where projeto = %s and is_active = 'F' " % projeto_id)
        for row in rows:
            log += '\n\nLocal "%s" excluído' % row[0]

        #documentos
        rows = db((db.documento.projeto == projeto_id) & (db.documento.modified_on > inicio)).select()
        fields = [x for x in db.documento.fields if x not in nofields]
        log += "\n\nAlterações em Documentos: \n\n"
        for row in rows:
            olds = db(
                (db.documento_archive.current_record == row.id) & (db.documento_archive.modified_on > inicio)).select()
            logf = ''
            if len(olds) < 1:
                log += '\nDocumento "%s" adicionado \n' % row.descricao
            else:

                for old in olds:
                    for field in fields:
                        if row[field] != old[field]:
                            logf += '\nCampo %s alterado de: \n %s \n para: \n %s' % (field, old[field], row[field])
            if len(logf) > 0:
                log += '\nDocumento %s :\n %s' % (row.descricao, logf)
        rows = db.executesql("select descricao from documento where projeto = %s and is_active = 'F' " % projeto_id)
        for row in rows:
            log += '\n\nDocumento "%s" excluído' % row[0]

        return PRE(log)
    else:
        return ''


def check_ci(projeto_id):
    row = db((db.documento.projeto == projeto_id) & (db.documento.tipo == 'CARTA DE INTENÇÃO')).select().first()
    if row:
        return 'Sim'
    else:
        return ''


def mail_retorno_diligencia(projeto, ocorrencia):
    r = mail.send(projeto.empreendedor.email,
                  'Protocolo de %s' % (ocorrencia),
                  '''Prezado Executor,

O Projeto Esportivo n° %s - %s foi finalizado e será analisado pela Equipe Técnica.
Não existe necessidade de encaminhamento de novo formulário de Cadastro do Projeto assinado pelo executor.
O projeto estará bloqueado para edição de agora em diante.
Acompanhe o status da análise pelo Sistema Minas Olímpica Incentivo ao Esporte.

Atenciosamente,

Equipe Técnica do Minas Olímpica Incentivo ao Esporte''' % (projeto.id, projeto.nome))
    return r

def ob(label):
    return XML(label + " <FONT color=red>*</FONT>")