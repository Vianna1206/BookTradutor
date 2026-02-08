# 📖 Guia de Uso - BookTradutor

## Visão Geral

BookTradutor é uma aplicação web interativa para traduzir histórias em quadrinhos. Perfeita para estudantes de idiomas que querem ler comics no idioma original enquanto aprendem.

## Como Funciona

### 1. Carregar Imagem
- Clique na área de upload ou arraste uma imagem
- Formatos suportados: PNG, JPG, GIF (máx. 10MB)
- A imagem do quadrinho será exibida no editor

### 2. Marcar Balões de Fala

**Passo a passo:**
1. Clique no botão "**+ Adicionar Balão**" no painel lateral
2. O botão mudará para "✓ Clique na imagem"
3. Clique na imagem onde o balão de fala está localizado
4. Um retângulo azul semi-transparente aparecerá marcando o balão
5. Repita para todos os balões que deseja traduzir

**Dica:** Você pode adicionar quantos balões quiser!

### 3. Editar Texto Original

Quando você seleciona um balão (clicando nele):
1. O painel "**Editar Balão**" aparece à direita
2. Digite ou cole o texto original do balão no campo "**Texto Original**"
3. O texto é salvo automaticamente enquanto você digita

### 4. Traduzir

Você tem duas opções:

#### Opção A: Traduzir Balão Individual
1. Selecione o balão que deseja traduzir
2. Digite o texto original
3. Clique em "**🔄 Traduzir Este Balão**"
4. A tradução aparecerá no campo "**Tradução**"

#### Opção B: Traduzir Tudo de Uma Vez
1. Adicione todos os balões
2. Digite o texto original em cada um
3. Clique em "**🌐 Traduzir Tudo**" no painel de ações
4. Todos os balões serão traduzidos automaticamente

### 5. Visualizar Traduções

Use o botão "**👁️ Ver Tradução**" para:
- Alternar entre visualização original e traduzida
- Ver as traduções sobrepostas na imagem
- Balões traduzidos ficam verdes
- Balões pendentes ficam cinzas

### 6. Editar e Ajustar

Você pode:
- **Editar traduções manualmente** no campo "Tradução"
- **Excluir balões** clicando no botão "🗑️ Excluir"
- **Reposicionar** adicionando novos balões no lugar correto

## Interface Visual

### Cores dos Balões

- 🔵 **Azul**: Balão atualmente selecionado
- 🟢 **Verde**: Balão já traduzido
- ⚪ **Cinza**: Balão sem tradução (pendente)

### Painel de Estatísticas

O painel mostra em tempo real:
- **Total de Balões**: Quantos balões foram adicionados
- **Traduzidos**: Quantos já têm tradução (verde)
- **Pendentes**: Quantos ainda precisam ser traduzidos (laranja)

## Casos de Uso

### Para Estudantes de Idiomas
1. Carregue um quadrinho em inglês
2. Tente ler e entender
3. Traduza apenas os balões que não entendeu
4. Aprenda novo vocabulário no contexto

### Para Tradutores
1. Carregue a imagem completa
2. Marque todos os balões
3. Digite os textos originais
4. Use "Traduzir Tudo" como base
5. Revise e ajuste as traduções manualmente

### Para Leitura Casual
1. Carregue o quadrinho
2. Marque os balões rapidamente
3. Traduza tudo
4. Leia com conforto no seu idioma

## Dicas e Truques

### ✨ Dica 1: Marcação Precisa
- Tente centralizar o clique no balão
- Os retângulos podem ser ajustados (nota: funcionalidade de redimensionar virá em versão futura)

### ✨ Dica 2: Ordem de Leitura
- Marque os balões na ordem de leitura (esquerda→direita, cima→baixo)
- Isso ajuda a manter contexto nas traduções

### ✨ Dica 3: Revisão Manual
- Sempre revise as traduções automáticas
- Você pode editar livremente o campo "Tradução"
- Traduções automáticas são um ponto de partida, não a palavra final

### ✨ Dica 4: Múltiplas Páginas
- Para múltiplas páginas, processe uma de cada vez
- Clique em "← Nova Imagem" para recomeçar

## Limitações Atuais

⚠️ **Importante saber:**
- A tradução atual é simulada (adiciona "[PT]" antes do texto)
- Em versão futura, será integrada API de tradução real
- Não há persistência: se você sair, perde o trabalho
- Não é possível redimensionar balões após criá-los
- Não suporta OCR (reconhecimento automático de texto)

## Futuras Funcionalidades

Planejadas para próximas versões:
- 🌐 Integração com Google Translate / DeepL
- 💾 Salvar e carregar projetos
- 📤 Exportar imagem final com traduções
- 🔍 OCR para detectar texto automaticamente
- 📏 Redimensionar e ajustar balões
- 🎨 Escolher fonte e cores
- 📱 Melhor suporte mobile
- 🔄 Histórico de traduções

## Suporte e Contribuições

- Encontrou um bug? Abra uma issue no GitHub
- Tem uma sugestão? Compartilhe conosco!
- Quer contribuir? Pull requests são bem-vindos!

## Tecnologia

Desenvolvido com:
- SvelteKit (framework moderno e rápido)
- TypeScript (segurança de tipos)
- Tailwind CSS (design responsivo)
- Svelte 5 (com runes para reatividade)

---

**Aproveite a experiência de ler e aprender com quadrinhos! 📚✨**
