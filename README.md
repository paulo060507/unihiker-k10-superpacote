# Unihiker K10 — IA, sensores e educação tecnológica

Coleção em desenvolvimento para explorar programação, sensores, conectividade e inteligência artificial com foco educacional.

> **Status: material experimental em organização.** A presença de uma pasta não significa que o exemplo foi concluído ou validado no K10. Os módulos marcados como `mock` ou `placeholder` são demonstrações incompletas, não funcionalidades prontas.

## Mapa do repositório

| Pasta | Conteúdo organizado |
| --- | --- |
| [ai/](ai/) | Visão computacional e experiências de IA |
| [sensores/](sensores/) | Atividades relacionadas a sensores |
| [tela_audio/](tela_audio/) | Interface, tela e áudio |
| [rede/](rede/) | Experimentos de conectividade |
| [docs/](docs/) | Documentação e materiais de apoio |

Em `ai/`, os diretórios abordam classificação TFLite, detecção facial com Haar, diferença entre frames, leitura de QR code e rastreamento de cor. `06_keyword_spotting_mock` e `07_objetos_yolovX_placeholder` estão explicitamente identificados como simulação ou estrutura inicial. Verifique os arquivos de cada atividade antes de planejar sua execução.

## Por onde começar

1. Escolha uma atividade e leia seus arquivos e requisitos.
2. Identifique o ambiente de execução: placa, computador de apoio ou ambos. Não suponha que uma biblioteca de PC execute diretamente no microcontrolador.
3. Confira alimentação, pinagem e compatibilidade do hardware antes de conectar componentes.
4. Consulte [requirements-pc.txt](requirements-pc.txt) para as dependências indicadas para computador; use um ambiente isolado e verifique as versões necessárias ao exemplo.
5. Registre o resultado e as adaptações necessárias no seu ambiente.

## Trilhas sugeridas

- **Primeiros passos:** identificar recursos do dispositivo e executar uma atividade pequena de interface ou sensores.
- **Visão computacional:** observar entrada de câmera, pré-processamento e saída de um algoritmo, distinguindo execução local de processamento em PC.
- **Projeto integrado:** combinar uma entrada, uma regra de decisão e uma saída, documentando os limites do protótipo.

Estas trilhas são sugestões didáticas, não um curso já validado em todas as plataformas.

## Checklist de validação de cada exemplo

- [ ] Objetivo e resultado esperado descritos.
- [ ] Hardware, firmware, sistema e dependências registrados.
- [ ] Instalação e execução reproduzíveis.
- [ ] Evidência do teste real, com data e plataforma.
- [ ] Limitações e módulos simulados identificados.
- [ ] Modelos, datasets e bibliotecas com suas licenças verificadas.

Use dados de demonstração ou dados autorizados. Não publique imagens pessoais, senhas de rede ou chaves de serviços nos exemplos.

## Contribuições e próximos passos

Relatos de problemas devem indicar a atividade, o ambiente e os passos de reprodução. Sugestões de melhoria podem ser abertas nas Issues. O próximo passo é substituir descrições genéricas por instruções verificadas e resultados reais por atividade.

Este README organiza o material existente; não declara validação de hardware, desempenho de modelos ou conclusão dos módulos. Consulte os arquivos e as condições de licença de cada dependência antes de reutilizar o conteúdo.
