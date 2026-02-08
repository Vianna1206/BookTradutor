# BookTradutor 📚🌍

Um projeto de aprendizado para traduzir qualquer livro, história em quadrinhos, etc.

A learning project to translate any book, comic book, and other documents using Python and Google Translate API.

## 🎯 Objetivo / Goal

Este é um projeto educacional que permite traduzir documentos de texto, PDFs e outros formatos de arquivo entre diferentes idiomas automaticamente.

This is an educational project that allows you to translate text documents, PDFs, and other file formats between different languages automatically.

## 📋 Funcionalidades / Features

- ✅ Tradução automática de arquivos de texto (.txt, .md)
- ✅ Extração e tradução de conteúdo PDF
- ✅ Detecção automática do idioma de origem
- ✅ Suporte para múltiplos idiomas
- ✅ Interface de linha de comando (CLI)
- ✅ Barra de progresso para traduções longas
- ✅ Tratamento robusto de erros

## 🚀 Instalação / Installation

### Pré-requisitos / Prerequisites

- Python 3.7 ou superior / Python 3.7 or higher
- pip (gerenciador de pacotes Python)

### Passos / Steps

1. Clone o repositório:
```bash
git clone https://github.com/Vianna1206/BookTradutor.git
cd BookTradutor
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 💻 Uso / Usage

### Traduzir um arquivo de texto / Translate a text file

```bash
python main.py input.txt -t pt
```

### Traduzir com idiomas específicos / Translate with specific languages

```bash
# Inglês para Português
python main.py book.txt -s en -t pt -o livro_pt.txt

# Espanhol para Francês
python main.py libro.txt -s es -t fr

# Auto-detectar idioma de origem
python main.py document.txt -t ja
```

### Traduzir um PDF / Translate a PDF

```bash
python main.py book.pdf -s en -t pt
```

### Opções disponíveis / Available options

```
positional arguments:
  input                 Arquivo de entrada para traduzir / Input file to translate

optional arguments:
  -h, --help            Mostrar mensagem de ajuda / Show help message
  -s, --source SOURCE   Código do idioma de origem (padrão: auto-detectar)
                        Source language code (default: auto-detect)
  -t, --target TARGET   Código do idioma de destino (obrigatório)
                        Target language code (required)
  -o, --output OUTPUT   Caminho do arquivo de saída
                        Output file path (default: translated_<input_file>)
  -v, --verbose         Saída detalhada / Verbose output
```

## 🌐 Códigos de Idioma / Language Codes

Alguns códigos de idioma comuns / Some common language codes:

- `pt` - Português / Portuguese
- `en` - Inglês / English
- `es` - Espanhol / Spanish
- `fr` - Francês / French
- `de` - Alemão / German
- `it` - Italiano / Italian
- `ja` - Japonês / Japanese
- `ko` - Coreano / Korean
- `zh-cn` - Chinês Simplificado / Simplified Chinese
- `ru` - Russo / Russian

[Lista completa de códigos de idioma](https://cloud.google.com/translate/docs/languages)

## 📁 Estrutura do Projeto / Project Structure

```
BookTradutor/
├── main.py              # Ponto de entrada da aplicação / Application entry point
├── translator.py        # Módulo principal de tradução / Main translation module
├── requirements.txt     # Dependências do projeto / Project dependencies
├── .gitignore          # Arquivos ignorados pelo Git / Git ignored files
├── README.md           # Este arquivo / This file
└── examples/           # Arquivos de exemplo / Example files
    └── sample_book_en.txt
```

## 🛠️ Tecnologias Utilizadas / Technologies Used

- **Python 3** - Linguagem de programação principal
- **googletrans** - API de tradução do Google
- **PyPDF2** - Extração de texto de PDFs
- **tqdm** - Barras de progresso
- **Pillow** - Processamento de imagens (futuro suporte para comics)

## 📚 Exemplos / Examples

### Exemplo 1: Traduzir um livro simples

```bash
cd examples
python ../main.py sample_book_en.txt -s en -t pt
```

Isso criará um arquivo `translated_sample_book_en.txt` com o conteúdo traduzido.

### Exemplo 2: Com saída personalizada

```bash
python main.py examples/sample_book_en.txt -t es -o ejemplos/libro_es.txt
```

## 🔮 Melhorias Futuras / Future Improvements

- [ ] Suporte para formatos de quadrinhos (CBR, CBZ)
- [ ] Interface gráfica (GUI)
- [ ] Tradução de imagens com texto (OCR)
- [ ] Cache de traduções
- [ ] Suporte para múltiplos serviços de tradução
- [ ] Preservação de formatação em documentos complexos
- [ ] Modo batch para traduzir múltiplos arquivos

## 🤝 Contribuindo / Contributing

Este é um projeto de aprendizado, contribuições são bem-vindas!

This is a learning project, contributions are welcome!

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Licença / License

Este é um projeto educacional de código aberto.

This is an open-source educational project.

## ⚠️ Avisos / Warnings

- Este projeto usa a API não oficial do Google Translate através da biblioteca `googletrans`
- Pode haver limites de taxa para traduções em larga escala
- Para uso em produção, considere usar a API oficial do Google Cloud Translation
- A qualidade da tradução depende do serviço de tradução utilizado

## 🙋 Suporte / Support

Para questões ou sugestões, abra uma issue no GitHub.

For questions or suggestions, open an issue on GitHub.

---

Feito com ❤️ para aprendizado / Made with ❤️ for learning
