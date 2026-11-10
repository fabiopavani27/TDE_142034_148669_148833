from gestorDados import GestorDados
from meta import Meta

class Gestor:
    def __init__(self):
        self.lista_alunos = []
        self.lista_atividades = []
        self.lista_resultados = []
        self.lista_metas = []

    def carregar_datasets(self):
        gd = GestorDados()
        dados = gd.carregar_datasets()
        if dados is not None:
            self.lista_alunos, self.lista_atividades, self.lista_resultados = dados
            print("Datasets carregados com sucesso!")
        else:
            print("Falha ao carregar os datasets.")
        input("\nPrima Enter para continuar...")

    def listar_alunos(self):
        if not self.lista_alunos:
            print("Não existem alunos carregados.")
            input("\nPrima Enter para continuar...")
            return

        print("\n--- LISTAR ALUNOS ---")
        print("1 - Todos os alunos")
        print("2 - Filtrar por turma")
        opcao = input("Escolha uma opção: ").strip()

        # Ordenar por ordem alfabética do nome (RF2)
        alunos_ordenados = sorted(self.lista_alunos, key=lambda a: a.get_nome())

        if opcao == '2':
            turmas = sorted(list(set(a.get_turma() for a in self.lista_alunos)))
            print(f"Turmas disponíveis: {', '.join(turmas)}")
            turma_sel = input("Turma selecionada: ").strip()
            filtrados = [a for a in alunos_ordenados if a.get_turma().lower() == turma_sel.lower()]
            
            print(f"\nCÓDIGO\tNOME\t\tTURMA")
            for a in filtrados:
                print(f"{a.get_codigo_aluno()}\t{a.get_nome()}\t{a.get_turma()}")
            print(f"Total de alunos listados: {len(filtrados)}")
        else:
            print(f"\nCÓDIGO\tNOME\t\tTURMA")
            for a in alunos_ordenados:
                print(f"{a.get_codigo_aluno()}\t{a.get_nome()}\t{a.get_turma()}")
            print(f"Total de alunos listados: {len(alunos_ordenados)}")
        
        input("\nPrima Enter para voltar à listagem:")

    def calcular_indicadores(self, codigo_aluno):
        total_atividades = len(self.lista_atividades)
        resultados_aluno = [r for r in self.lista_resultados if r.get_codigo_aluno() == codigo_aluno]

        # 1. Taxa de conclusão (%)
        if total_atividades == 0:
            taxa_conclusao = None
        else:
            concluidas = sum(1 for r in resultados_aluno if r.get_estado() == 'concluida')
            taxa_conclusao = (concluidas / total_atividades) * 100

        # 2. Classificação média (0 a 100)
        notas_validas = [r.get_classificacao() for r in resultados_aluno if r.get_estado() == 'concluida' and r.get_classificacao() is not None]
        if len(notas_validas) == 0:
            classificacao_media = None
        else:
            classificacao_media = sum(notas_validas) / len(notas_validas)

        # 3. Tempo total (minutos)
        tempo_total = sum(r.get_tempo_gasto_min() for r in resultados_aluno)

        return {
            'taxa_conclusao': taxa_conclusao,
            'classificacao_media': classificacao_media,
            'tempo_total': tempo_total
        }

    def consultar_aluno(self):
        codigo = input("Introduza o código do aluno: ").strip()
        aluno = next((a for a in self.lista_alunos if a.get_codigo_aluno() == codigo), None)
        
        if not aluno:
            print("Erro: O código do aluno não existe.")
            input("\nPrima Enter para continuar...")
            return

        print(f"\nCONSULTAR ALUNO")
        print(f"Código: {aluno.get_codigo_aluno()}")
        print(f"Nome: {aluno.get_nome()} | Turma: {aluno.get_turma()}\n")
        
        print(f"{'ATIVIDADE':<25} {'ESTADO':<15} {'NOTA':<8} {'TEMPO (min)':<12}")
        for ativ in self.lista_atividades:
            res = next((r for r in self.lista_resultados if r.get_codigo_aluno() == codigo and r.get_codigo_atividade() == ativ.get_codigo_atividade()), None)
            
            if not res:
                estado = "não iniciada"
                nota = "-"
                tempo = "-"
            else:
                estado = res.get_estado()
                nota = str(res.get_classificacao()) if res.get_classificacao() is not None else "-"
                tempo = str(res.get_tempo_gasto_min())
                
            print(f"{ativ.get_codigo_atividade()} {ativ.get_titulo():<20} {estado:<15} {nota:<8} {tempo:<12}")

        inds = self.calcular_indicadores(codigo)
        print("\nINDICADORES")
        taxa_str = f"{inds['taxa_conclusao']:.2f}%" if inds['taxa_conclusao'] is not None else "sem dados"
        media_str = f"{inds['classificacao_media']:.2f} (0 a 100)" if inds['classificacao_media'] is not None else "sem dados"
        tempo_str = f"{inds['tempo_total']:.2f} min"
        
        print(f"Taxa de conclusão: {taxa_str}")
        print(f"Classificação média: {media_str}")
        print(f"Tempo total de participação: {tempo_str}")
        input("\nPrima Enter para continuar...")

    def comparar_alunos(self):
        c1 = input("Código do primeiro aluno: ").strip()
        c2 = input("Código do segundo aluno: ").strip()
        
        a1 = next((a for a in self.lista_alunos if a.get_codigo_aluno() == c1), None)
        a2 = next((a for a in self.lista_alunos if a.get_codigo_aluno() == c2), None)
        
        if not a1 or not a2:
            print("Erro: Um ou ambos os códigos de aluno não existem.")
            input("\nPrima Enter para continuar...")
            return

        ind1 = self.calcular_indicadores(c1)
        ind2 = self.calcular_indicadores(c2)

        print(f"\nCOMPARAÇÃO DE ALUNOS: {a1.get_nome()} vs {a2.get_nome()}")
        print("-" * 50)
        
        for indicador, nome_bonito in [('taxa_conclusao', 'Taxa de Conclusão (%)'), 
                                      ('classificacao_media', 'Classificação Média'), 
                                      ('tempo_total', 'Tempo Total (min)')]:
            v1 = ind1[indicador]
            v2 = ind2[indicador]
            
            s1 = f"{v1:.2f}" if v1 is not None else "sem dados"
            s2 = f"{v2:.2f}" if v2 is not None else "sem dados"
            
            print(f"{nome_bonito}:")
            print(f"  - {a1.get_nome()}: {s1}")
            print(f"  - {a2.get_nome()}: {s2}")
            
            if v1 is not None and v2 is not None:
                if v1 > v2:
                    print(f"  => Maior valor: {a1.get_nome()}")
                elif v2 > v1:
                    print(f"  => Maior valor: {a2.get_nome()}")
                else:
                    print("  => Valores iguais.")
            else:
                print("  => Comparação indisponível (falta de dados).")
            print()
        input("\nPrima Enter para continuar...")

    def criar_meta(self):
        print("\n--- CRIAR META DE APRENDIZAGEM ---")
        codigo = input("Código da meta: ").strip()
        if any(m.get_codigo_meta() == codigo for m in self.lista_metas) or codigo == "":
            print("Erro: Código inválido ou já existente.")
            input("\nPrima Enter para continuar...")
            return
            
        nome = input("Nome da meta: ").strip()
        if nome == "":
            print("Erro: Nome obrigatório.")
            input("\nPrima Enter para continuar...")
            return
            
        print("Indicadores permitidos: taxa_conclusao, classificacao_media, tempo_total")
        indicador = input("Indicador: ").strip()
        if indicador not in ['taxa_conclusao', 'classificacao_media', 'tempo_total']:
            print("Erro: Indicador inválido.")
            input("\nPrima Enter para continuar...")
            return
            
        relacao = input("Relação (>, <, ==, >=, <=): ").strip()
        if relacao not in ['>', '<', '==', '>=', '<=']:
            print("Erro: Relação inválida.")
            input("\nPrima Enter para continuar...")
            return
            
        try:
            valor = float(input("Valor objetivo: ").strip())
            if indicador in ['taxa_conclusao', 'classificacao_media'] and not (0 <= valor <= 100):
                raise ValueError()
            if indicador == 'tempo_total' and valor < 0:
                raise ValueError()
        except ValueError:
            print("Erro: Valor objetivo inválido.")
            input("\nPrima Enter para continuar...")
            return

        meta = Meta(codigo, nome, indicador, valor, relacao)
        self.lista_metas.append(meta)
        print("Meta criada com sucesso!")
        input("\nPrima Enter para continuar...")

    def listar_metas(self):
        if not self.lista_metas:
            print("Não existem metas criadas.")
            input("\nPrima Enter para continuar...")
            return
        print("\n--- LISTA DE METAS ---")
        for m in self.lista_metas:
            print(m)
        input("\nPrima Enter para continuar...")

    def editar_meta(self):
        codigo = input("Código da meta a editar: ").strip()
        meta = next((m for m in self.lista_metas if m.get_codigo_meta() == codigo), None)
        if not meta:
            print("Erro: Meta não encontrada.")
            input("\nPrima Enter para continuar...")
            return
            
        print(f"A editar meta: {meta.get_nome()}")
        novo_nome = input(f"Novo nome [{meta.get_nome()}]: ").strip()
        if novo_nome:
            meta.set_nome(novo_nome)
            
        print("Indicadores: taxa_conclusao, classificacao_media, tempo_total")
        novo_ind = input(f"Novo indicador [{meta.get_indicador()}]: ").strip()
        if novo_ind in ['taxa_conclusao', 'classificacao_media', 'tempo_total']:
            meta.set_indicador(novo_ind)
            
        nova_rel = input(f"Nova relação [{meta.get_relacao()}]: ").strip()
        if nova_rel in ['>', '<', '==', '>=', '<=']:
            meta.set_relacao(nova_rel)
            
        try:
            val_str = input(f"Novo valor objetivo [{meta.get_valor_objetivo()}]: ").strip()
            if val_str:
                meta.set_valor_objetivo(float(val_str))
        except ValueError:
            print("Valor inválido ignorado, mantido o anterior.")
            
        print("Meta atualizada com sucesso!")
        input("\nPrima Enter para continuar...")

    def apagar_meta(self):
        codigo = input("Código da meta a apagar: ").strip()
        meta = next((m for m in self.lista_metas if m.get_codigo_meta() == codigo), None)
        if not meta:
            print("Erro: Meta não encontrada.")
            input("\nPrima Enter para continuar...")
            return
        self.lista_metas.remove(meta)
        print("Meta apagada com sucesso.")
        input("\nPrima Enter para continuar...")

    def visualizar_alunos_cumprem_meta(self):
        if not self.lista_metas:
            print("Não existem metas criadas.")
            input("\nPrima Enter para continuar...")
            return
            
        codigo = input("Código da meta: ").strip()
        meta = next((m for m in self.lista_metas if m.get_codigo_meta() == codigo), None)
        if not meta:
            print("Erro: Meta não encontrada.")
            input("\nPrima Enter para continuar...")
            return

        cumprem = []
        sem_dados = 0

        for aluno in self.lista_alunos:
            inds = self.calcular_indicadores(aluno.get_codigo_aluno())
            val = inds[meta.get_indicador()]
            
            if val is None:
                sem_dados += 1
            else:
                if meta.cumprida(val):
                    cumprem.append((aluno, val))

        print(f"\nALUNOS QUE CUMPREM A META {meta.get_codigo_meta()}")
        print(f"Condição: {meta.get_indicador()} {meta.get_relacao()} {meta.get_valor_objetivo()}")
        print(f"\nCÓDIGO\tNOME\t\tTURMA\tVALOR")
        for aluno, val in cumprem:
            print(f"{aluno.get_codigo_aluno()}\t{aluno.get_nome()}\t{aluno.get_turma()}\t{val:.2f}")
            
        print(f"\nTotal de alunos que cumprem: {len(cumprem)}")
        print(f"Alunos sem dados no indicador: {sem_dados}")
        input("\nPrima Enter para continuar...")