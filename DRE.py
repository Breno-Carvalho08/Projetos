

valor = float(input('Receita Bruta: '))
def receita_op_bruta_funcao(a):
    escolha = int(input('Possui devoluções, abatimentos ou impostos?\n1 - Sim\n2 - Não\n'))
    match escolha:
        case 1:
            devolucoes = float(input('Valor das devoluções: '))
            abatimento = float(input('Valor dos abatimentos: '))
            impostos = float(input('Valor dos impostos: '))
            valor_receita_liquida = a - (devolucoes + abatimento + impostos)
            return valor_receita_liquida
        case 2:
            valor_receita_liquida = a
            return valor_receita_liquida

receita_liquida = receita_op_bruta_funcao(valor)

def receita_liq_funcao(b):
    escolha = int(input('Dentro de receita liquida, temos CMV, CSP ou CPV?\n1 - Sim\n2 - Não\n'))
    match escolha:
        case 1:
            cmv = float(input('CMV: '))
            csp = float(input('CSP: '))
            cpv = float(input('CPV: '))
            valor_resultado_bruto = b - (cmv + csp + cpv)
            return valor_resultado_bruto
        case 2:
            valor_resultado_bruto = b
            return valor_resultado_bruto

resultado_bruto = receita_liq_funcao(receita_liquida)

def resultado_bruto_funcao(c):
    escolha = int(input('Possui outras despesas?\n1 - Sim\n2 - Não\n'))
    match escolha:
        case 1:
            desp_adm = float(input('Despesas administrativas: '))
            desp_comerciais = float(input('Despesas comerciais: '))
            desp_c_depreciacao = float(input('Despesas c/depreciação: '))
            resultado_op = c - (desp_adm + desp_c_depreciacao + desp_comerciais)
            escolha2 = int(input('Possui receita ou despesas financeiras?\n1 - Sim\n2 - Não\n'))
            match escolha2:
                case 1:
                    receita_financeira = float(input('Receita financeira: '))
                    desp_financeira = float(input('Despesas financeiras: '))
                    resultado_op += receita_financeira
                    resultado_op -= desp_financeira
                case 2:
                    pass
            return resultado_op
        case 2:
            resultado_op = c
            escolha2 = int(input('Possui receita ou despesas financeiras?\n1 - Sim\n2 - Não\n'))
            match escolha2:
                case 1:
                    receita_financeira = float(input('Receita financeira: '))
                    desp_financeira = float(input('Despesas financeiras: '))
                    resultado_op += receita_financeira
                    resultado_op -= desp_financeira
                case 2:
                    pass
            return resultado_op

resultado_operacional = resultado_bruto_funcao(resultado_bruto)

def resultado_op_funcao(d):
    escolha = int(input('Possui receitas ou despesas não operacionais?\n1 - Sim\n2 - Não\n'))
    match escolha:
        case 1:
            receita_n_op = float(input('Receitas não operacionais: '))
            desp_n_op = float(input('Despesas não operacionais: '))
            valor_resultado_antes_impostos = d + receita_n_op - desp_n_op
            return valor_resultado_antes_impostos
        case 2:
            valor_resultado_antes_impostos = d
            return valor_resultado_antes_impostos

resultado_antes_IR_CSLL = resultado_op_funcao(resultado_operacional)

def resultado_antes_impostos_funcao(e):
    ir = e * 0.15
    csll = e * 0.09
    valor_resultado_antes_partipacao = e - (ir + csll)
    return valor_resultado_antes_partipacao

resultado_antes_participacao = resultado_antes_impostos_funcao(resultado_antes_IR_CSLL)

def resultado_antes_participacao_funcao(f):
    escolha = int(input('Possui participações?\n1 - Sim\n2 - Não\n'))
    match escolha:
        case 1:
            porcetagem_plr = float(input('Porcentagem PLR: ')) / 100
            plr = f * porcetagem_plr
            part_debentures = float(input('Participação debenturistas: '))
            part_adm = float(input('Participação administrativa: '))
            valor_lucro_liquido = f - (plr + part_debentures + part_adm)
            return valor_lucro_liquido
        case 2:
            valor_lucro_liquido = f
            return valor_lucro_liquido

lucro_liquido = resultado_antes_participacao_funcao(resultado_antes_participacao)

print(receita_liquida)
print(resultado_bruto)
print(resultado_operacional)
print(resultado_antes_IR_CSLL)
print(resultado_antes_participacao)
print(lucro_liquido)
