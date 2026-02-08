# 📚 BookTradutor

**Tradutor Interativo de Histórias em Quadrinhos**

Uma aplicação web moderna construída com SvelteKit para traduzir histórias em quadrinhos de forma interativa. Perfeita para quem está aprendendo novos idiomas através de comics e mangás!

## 🎯 Funcionalidades

- **Upload de Imagens**: Carregue qualquer imagem de quadrinho (PNG, JPG, GIF)
- **Marcação de Balões**: Adicione marcadores nos balões de fala da imagem
- **Tradução Individual**: Selecione e traduza balões específicos que não entendeu
- **Tradução em Massa**: Traduza todos os balões de uma vez
- **Visualização Alternada**: Alterne entre texto original e traduzido
- **Interface Intuitiva**: Design moderno e responsivo com Tailwind CSS

## 🚀 Como Usar

1. **Carregar Quadrinho**: Faça upload de uma imagem de quadrinho
2. **Adicionar Balões**: Clique em "Adicionar Balão" e marque os balões na imagem
3. **Texto Original**: Digite ou cole o texto original de cada balão
4. **Traduzir**: Traduza balões individuais ou todos de uma vez
5. **Visualizar**: Alterne entre ver o original e as traduções

## 🛠️ Tecnologias

- [SvelteKit](https://kit.svelte.dev/) - Framework principal
- [TypeScript](https://www.typescriptlang.org/) - Tipagem estática
- [Tailwind CSS](https://tailwindcss.com/) - Estilização
- [Vite](https://vitejs.dev/) - Build tool

## 💻 Desenvolvimento

### Pré-requisitos

- Node.js 18+ 
- npm ou pnpm

### Instalação

```bash
# Instalar dependências
npm install

# Iniciar servidor de desenvolvimento
npm run dev

# Ou abrir automaticamente no navegador
npm run dev -- --open
```

### Build para Produção

```bash
# Criar build otimizado
npm run build

# Visualizar build de produção
npm run preview
```

## 📝 Estrutura do Projeto

```
BookTradutor/
├── src/
│   ├── routes/          # Páginas SvelteKit
│   │   ├── +page.svelte # Página principal do app
│   │   └── +layout.svelte
│   ├── lib/             # Componentes reutilizáveis
│   └── app.css          # Estilos globais Tailwind
├── static/              # Arquivos estáticos
└── package.json
```

## 🎨 Próximas Funcionalidades

- [ ] Integração com APIs de tradução reais (Google Translate, DeepL)
- [ ] Salvar e carregar projetos de tradução
- [ ] Exportar imagem com traduções
- [ ] Suporte a OCR para extrair texto automaticamente
- [ ] Histórico de traduções
- [ ] Suporte a múltiplos idiomas
- [ ] Ajuste automático de tamanho de texto nos balões
- [ ] Compartilhamento de traduções

## 📄 Licença

Este projeto é de código aberto e disponível sob a licença MIT.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

Desenvolvido com ❤️ usando SvelteKit

