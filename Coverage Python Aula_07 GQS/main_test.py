import coverage
import pytest

# Inicia o coverage
cov = coverage.Coverage()
cov.start()

# Executa os testes usando pytest (especifica a localização do arquivo de testes)
pytest.main(["-q", "--tb=line", "test_operacoes.py"])  # Passando o arquivo de testes para o pytest

# Para o coverage e gera o relatório
cov.stop()
cov.save()

# Gerar o relatório de cobertura no terminal
print("\nRelatório de cobertura no terminal:")
cov.report(show_missing=True)  # Inclui informações sobre linhas não cobertas

# Gerar o relatório HTML na pasta 'htmlcov'
cov.html_report(directory='htmlcov')

print("\nRelatório de cobertura gerado em 'htmlcov/index.html'.")
