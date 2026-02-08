# 🔧 Documentação Técnica - BookTradutor

## Arquitetura

### Stack Tecnológico

- **Framework**: SvelteKit 2.x
- **Linguagem**: TypeScript 5.x
- **Styling**: Tailwind CSS 4.x + PostCSS
- **Build Tool**: Vite 7.x
- **Runtime**: Node.js 18+

### Estrutura de Arquivos

```
BookTradutor/
├── src/
│   ├── routes/
│   │   ├── +page.svelte        # Página principal do aplicativo
│   │   └── +layout.svelte      # Layout global (importa CSS)
│   ├── lib/
│   │   ├── assets/             # Imagens, ícones
│   │   └── index.ts            # Exports da biblioteca
│   ├── app.css                 # Tailwind directives
│   ├── app.d.ts                # TypeScript declarations
│   └── app.html                # Template HTML base
├── static/                     # Arquivos estáticos
├── .gitignore                  # Git ignore rules
├── package.json                # Dependências
├── svelte.config.js            # Configuração SvelteKit
├── tailwind.config.js          # Configuração Tailwind
├── tsconfig.json               # Configuração TypeScript
└── vite.config.ts              # Configuração Vite
```

## Componentes Principais

### +page.svelte

Componente único que contém toda a lógica da aplicação.

#### Estado (State Management)

Usa Svelte 5 runes para gerenciamento de estado reativo:

```typescript
// Imagem carregada (base64)
let uploadedImage = $state<string | null>(null);

// Nome do arquivo
let fileName = $state<string>('');

// Array de balões
let bubbles = $state<Array<BubbleType>>([]);

// ID do balão selecionado
let selectedBubble = $state<number | null>(null);

// Modo de adição de balão
let isAddingBubble = $state(false);

// Toggle visualização
let showTranslations = $state(false);
```

#### Tipo Bubble

```typescript
interface Bubble {
  id: number;           // Timestamp único
  x: number;            // Posição X (pixels)
  y: number;            // Posição Y (pixels)
  width: number;        // Largura do retângulo
  height: number;       // Altura do retângulo
  originalText: string; // Texto original
  translatedText: string; // Texto traduzido
}
```

### Funções Principais

#### handleImageUpload(event: Event)
- Lê arquivo de input
- Converte para base64 usando FileReader
- Atualiza estado `uploadedImage` e `fileName`

#### startAddingBubble()
- Ativa modo de adição (`isAddingBubble = true`)
- UI mostra instrução para clicar na imagem

#### addBubble(x: number, y: number)
- Cria novo balão centrado nas coordenadas do clique
- Dimensões padrão: 100x50 pixels
- ID único: timestamp do Date.now()
- Adiciona ao array `bubbles`
- Auto-seleciona o novo balão

#### selectBubble(id: number)
- Define `selectedBubble` para o ID fornecido
- Atualiza UI para mostrar editor do balão

#### updateBubbleText(id, text, isOriginal)
- Atualiza `originalText` ou `translatedText`
- Usa imutabilidade: `bubbles = bubbles.map(...)`

#### translateBubble(id: number)
- Busca balão por ID
- Simula tradução: `[PT] ${originalText}`
- **TODO**: Integrar API real de tradução

#### translateAll()
- Itera sobre todos os balões
- Traduz cada um que tem `originalText`
- Usa `await` para suportar chamadas async futuras

#### removeBubble(id: number)
- Remove balão do array
- Limpa `selectedBubble` se era o removido

#### handleImageClick(event: MouseEvent)
- Calcula coordenadas relativas à imagem
- Chama `addBubble()` se em modo de adição

## Styling

### Tailwind CSS

Configuração customizada:

```javascript
// tailwind.config.js
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  plugins: [
    require('@tailwindcss/forms'),      // Estilos para forms
    require('@tailwindcss/typography'), // Typography plugin
  ],
}
```

### Classes Principais

- **Gradiente de fundo**: `bg-gradient-to-br from-blue-50 to-purple-50`
- **Cards**: `bg-white rounded-lg shadow-lg`
- **Botões primários**: `bg-blue-600 hover:bg-blue-700 text-white`
- **Botões secundários**: `bg-green-600` / `bg-purple-600`
- **Inputs**: `border-gray-300 focus:ring-2 focus:ring-blue-500`

### Indicadores de Estado

Balões usam classes condicionais:

```svelte
class:border-blue-500={selectedBubble === bubble.id}
class:border-green-400={bubble.translatedText && !selected}
class:border-gray-400={!bubble.translatedText && !selected}
```

## Fluxo de Dados

### Upload → Processamento

```
User clicks upload
    ↓
FileReader reads file
    ↓
Convert to base64
    ↓
Update uploadedImage state
    ↓
Svelte rerenders UI
```

### Adicionar Balão

```
Click "Adicionar Balão"
    ↓
isAddingBubble = true
    ↓
User clicks image
    ↓
Get coordinates (x, y)
    ↓
Create bubble object
    ↓
Add to bubbles array
    ↓
Svelte rerenders with new bubble
```

### Traduzir

```
User types original text
    ↓
updateBubbleText() called
    ↓
User clicks "Traduzir"
    ↓
translateBubble() called
    ↓
[Simulate translation] → TODO: API call
    ↓
updateBubbleText() with translation
    ↓
Svelte rerenders
```

## Integrações Futuras

### API de Tradução

#### Opção 1: Google Cloud Translation API

```typescript
async function translateBubble(id: number) {
  const bubble = bubbles.find(b => b.id === id);
  if (!bubble?.originalText) return;
  
  const response = await fetch('https://translation.googleapis.com/language/translate/v2', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      q: bubble.originalText,
      source: 'en',
      target: 'pt',
      key: API_KEY, // Usar variável de ambiente
    }),
  });
  
  const data = await response.json();
  const translated = data.data.translations[0].translatedText;
  
  updateBubbleText(id, translated, false);
}
```

#### Opção 2: DeepL API

```typescript
async function translateWithDeepL(text: string, targetLang: string) {
  const response = await fetch('https://api-free.deepl.com/v2/translate', {
    method: 'POST',
    headers: {
      'Authorization': `DeepL-Auth-Key ${DEEPL_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: [text],
      target_lang: targetLang,
    }),
  });
  
  const data = await response.json();
  return data.translations[0].text;
}
```

### OCR (Reconhecimento de Texto)

#### Opção: Tesseract.js

```typescript
import Tesseract from 'tesseract.js';

async function extractTextFromBubble(imageData: string, coords: BubbleCoords) {
  // Crop image to bubble coordinates
  const croppedImage = cropImage(imageData, coords);
  
  // Run OCR
  const result = await Tesseract.recognize(croppedImage, 'eng', {
    logger: m => console.log(m),
  });
  
  return result.data.text;
}
```

### Persistência

#### LocalStorage

```typescript
// Salvar
function saveProject() {
  const project = {
    image: uploadedImage,
    fileName: fileName,
    bubbles: bubbles,
    timestamp: Date.now(),
  };
  localStorage.setItem('booktradutor_project', JSON.stringify(project));
}

// Carregar
function loadProject() {
  const saved = localStorage.getItem('booktradutor_project');
  if (saved) {
    const project = JSON.parse(saved);
    uploadedImage = project.image;
    fileName = project.fileName;
    bubbles = project.bubbles;
  }
}
```

#### IndexedDB (para projetos maiores)

```typescript
import { openDB } from 'idb';

const db = await openDB('BookTradutor', 1, {
  upgrade(db) {
    db.createObjectStore('projects', { keyPath: 'id' });
  },
});

// Salvar
await db.put('projects', {
  id: projectId,
  image: uploadedImage,
  bubbles: bubbles,
  createdAt: Date.now(),
});

// Carregar
const project = await db.get('projects', projectId);
```

## Build e Deploy

### Build Local

```bash
npm run build
```

Gera arquivos otimizados em `.svelte-kit/output/`

### Adapters

#### Vercel
```bash
npm i -D @sveltejs/adapter-vercel
```

```javascript
// svelte.config.js
import adapter from '@sveltejs/adapter-vercel';
```

#### Netlify
```bash
npm i -D @sveltejs/adapter-netlify
```

#### Node.js
```bash
npm i -D @sveltejs/adapter-node
```

### Variáveis de Ambiente

Criar arquivo `.env`:

```bash
PUBLIC_TRANSLATE_API=your_api_endpoint
TRANSLATE_API_KEY=your_secret_key
```

Usar no código:

```typescript
import { env } from '$env/dynamic/public';

const apiKey = env.TRANSLATE_API_KEY;
```

## Performance

### Otimizações Atuais

- ✅ Vite para build rápido
- ✅ Tailwind CSS tree-shaking
- ✅ TypeScript para catch de erros em build
- ✅ Svelte 5 com compilação otimizada

### Otimizações Futuras

- [ ] Image lazy loading
- [ ] Virtual scrolling para muitos balões
- [ ] Web Workers para processamento pesado
- [ ] Service Worker para cache
- [ ] Code splitting por rota

## Testes

### Unit Tests (Futuro)

```typescript
import { render } from '@testing-library/svelte';
import Page from './+page.svelte';

test('should add bubble on click', () => {
  const { component } = render(Page);
  // Test logic
});
```

### E2E Tests (Futuro)

```typescript
import { test, expect } from '@playwright/test';

test('upload and translate workflow', async ({ page }) => {
  await page.goto('/');
  await page.setInputFiles('input[type="file"]', 'test-comic.png');
  await page.click('button:has-text("Adicionar Balão")');
  // Continue test...
});
```

## Contribuindo

### Setup de Desenvolvimento

```bash
# Clone
git clone https://github.com/Vianna1206/BookTradutor.git
cd BookTradutor

# Instale dependências
npm install

# Execute em modo dev
npm run dev

# Teste build
npm run build
```

### Code Style

- Use TypeScript para novas features
- Siga convenções Svelte
- Use Tailwind para styling
- Comente código complexo
- Mantenha componentes pequenos e focados

### Pull Requests

1. Fork o repositório
2. Crie branch para feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Add: nova feature'`)
4. Push para branch (`git push origin feature/MinhaFeature`)
5. Abra Pull Request

---

**Happy Coding! 🚀**
