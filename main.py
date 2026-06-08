# Sistema de Gestão de Clínica - Ponto de Entrada

from controlador_principal import ControladorPrincipal


def main():
    """
    Função principal para iniciar o sistema de gestão de clínica.
    
    Este sistema gerencia:
    - Pacientes
    - Profissionais
    - Atendimentos
    - Agendamentos
    - Exames
    - Procedimentos
    - Pagamentos
    - Clínicas
    - Relatórios
    """
    
    print("\n" + "="*50)
    print("  BEM-VINDO AO SISTEMA DE GESTÃO DE CLÍNICA  ")
    print("="*50)
    
    try:
        controlador = ControladorPrincipal()
        controlador.iniciar_sistema()
    except KeyboardInterrupt:
        print("\n\n❌ Sistema interrompido pelo usuário.")
    except Exception as e:
        print(f"\n\n❌ Erro fatal no sistema: {e}")
    finally:
        print("\n" + "="*50)
        print("  Sistema encerrado com sucesso!  ")
        print("="*50 + "\n")


if __name__ == "__main__":
    main()
