<script lang="ts">
	let uploadedImage = $state<string | null>(null);
	let fileName = $state<string>('');
	let bubbles = $state<Array<{id: number, x: number, y: number, width: number, height: number, originalText: string, translatedText: string}>>([]);
	let selectedBubble = $state<number | null>(null);
	let isAddingBubble = $state(false);
	let showTranslations = $state(false);
	
	function handleImageUpload(event: Event) {
		const target = event.target as HTMLInputElement;
		const file = target.files?.[0];
		if (file) {
			fileName = file.name;
			const reader = new FileReader();
			reader.onload = (e) => {
				uploadedImage = e.target?.result as string;
			};
			reader.readAsDataURL(file);
		}
	}
	
	function startAddingBubble() {
		isAddingBubble = true;
	}
	
	function addBubble(x: number, y: number) {
		if (!isAddingBubble) return;
		
		const newBubble = {
			id: Date.now(),
			x: x - 50,
			y: y - 25,
			width: 100,
			height: 50,
			originalText: '',
			translatedText: ''
		};
		bubbles = [...bubbles, newBubble];
		selectedBubble = newBubble.id;
		isAddingBubble = false;
	}
	
	function selectBubble(id: number) {
		selectedBubble = id;
	}
	
	function updateBubbleText(id: number, text: string, isOriginal: boolean) {
		bubbles = bubbles.map(b => 
			b.id === id 
				? { ...b, [isOriginal ? 'originalText' : 'translatedText']: text }
				: b
		);
	}
	
	async function translateBubble(id: number) {
		const bubble = bubbles.find(b => b.id === id);
		if (!bubble || !bubble.originalText) return;
		
		// Simulando tradução - em produção, usar API real
		const translated = `[PT] ${bubble.originalText}`;
		updateBubbleText(id, translated, false);
	}
	
	async function translateAll() {
		for (const bubble of bubbles) {
			if (bubble.originalText) {
				await translateBubble(bubble.id);
			}
		}
	}
	
	function removeBubble(id: number) {
		bubbles = bubbles.filter(b => b.id !== id);
		if (selectedBubble === id) {
			selectedBubble = null;
		}
	}
	
	function handleImageClick(event: MouseEvent) {
		if (!isAddingBubble || !uploadedImage) return;
		
		const target = event.currentTarget as HTMLElement;
		const rect = target.getBoundingClientRect();
		const x = event.clientX - rect.left;
		const y = event.clientY - rect.top;
		
		addBubble(x, y);
	}
</script>

<div class="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50">
	<div class="container mx-auto px-4 py-8">
		<!-- Header -->
		<div class="text-center mb-8">
			<h1 class="text-4xl font-bold text-gray-800 mb-2">📚 BookTradutor</h1>
			<p class="text-gray-600">Tradutor Interativo de Histórias em Quadrinhos</p>
		</div>

		{#if !uploadedImage}
			<!-- Upload Section -->
			<div class="max-w-2xl mx-auto">
				<div class="bg-white rounded-lg shadow-lg p-8">
					<h2 class="text-2xl font-semibold text-gray-800 mb-4">Carregar Quadrinho</h2>
					<p class="text-gray-600 mb-6">
						Faça upload de uma imagem de quadrinho para começar a traduzir os balões de fala.
					</p>
					
					<label class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100 transition-colors">
						<div class="flex flex-col items-center justify-center pt-5 pb-6">
							<svg class="w-16 h-16 mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
							</svg>
							<p class="mb-2 text-sm text-gray-500"><span class="font-semibold">Clique para fazer upload</span> ou arraste e solte</p>
							<p class="text-xs text-gray-500">PNG, JPG, GIF (MAX. 10MB)</p>
						</div>
						<input type="file" class="hidden" accept="image/*" onchange={handleImageUpload} />
					</label>
					
					<div class="mt-6 bg-blue-50 border border-blue-200 rounded-lg p-4">
						<h3 class="text-sm font-semibold text-blue-800 mb-2">💡 Como usar:</h3>
						<ol class="text-sm text-blue-700 space-y-1">
							<li>1. Faça upload de uma imagem de quadrinho</li>
							<li>2. Clique em "Adicionar Balão" e depois na imagem para marcar balões</li>
							<li>3. Digite o texto original em cada balão</li>
							<li>4. Traduza balões individuais ou todos de uma vez</li>
							<li>5. Alterne entre visualização original e traduzida</li>
						</ol>
					</div>
				</div>
			</div>
		{:else}
			<!-- Main Editor -->
			<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
				<!-- Image Viewer -->
				<div class="lg:col-span-2">
					<div class="bg-white rounded-lg shadow-lg p-4">
						<div class="flex items-center justify-between mb-4">
							<h2 class="text-xl font-semibold text-gray-800">{fileName}</h2>
							<button 
								onclick={() => { uploadedImage = null; bubbles = []; selectedBubble = null; }}
								class="px-4 py-2 text-sm text-red-600 hover:text-red-700 hover:bg-red-50 rounded-lg transition-colors"
							>
								← Nova Imagem
							</button>
						</div>
						
						<div class="relative inline-block">
							<img 
								src={uploadedImage} 
								alt="Comic" 
								class="max-w-full h-auto rounded-lg shadow-md cursor-crosshair"
								onclick={handleImageClick}
							/>
							
							<!-- Bubble Overlays -->
							{#each bubbles as bubble}
								<div 
									class="absolute border-2 cursor-pointer transition-all"
									class:border-blue-500={selectedBubble === bubble.id}
									class:border-green-400={selectedBubble !== bubble.id && bubble.translatedText}
									class:border-gray-400={selectedBubble !== bubble.id && !bubble.translatedText}
									class:bg-blue-100={selectedBubble === bubble.id}
									class:bg-green-50={selectedBubble !== bubble.id && bubble.translatedText && showTranslations}
									style="left: {bubble.x}px; top: {bubble.y}px; width: {bubble.width}px; height: {bubble.height}px; opacity: 0.6;"
									onclick={(e) => { e.stopPropagation(); selectBubble(bubble.id); }}
								>
									{#if showTranslations && bubble.translatedText}
										<div class="absolute inset-0 flex items-center justify-center p-1 text-xs font-medium text-gray-800 text-center overflow-hidden">
											{bubble.translatedText}
										</div>
									{/if}
								</div>
							{/each}
						</div>
						
						{#if isAddingBubble}
							<div class="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-lg text-yellow-800 text-sm">
								✨ Clique na imagem onde deseja adicionar um balão
							</div>
						{/if}
					</div>
				</div>

				<!-- Control Panel -->
				<div class="space-y-4">
					<!-- Actions -->
					<div class="bg-white rounded-lg shadow-lg p-4">
						<h3 class="text-lg font-semibold text-gray-800 mb-4">Ações</h3>
						<div class="space-y-2">
							<button 
								onclick={startAddingBubble}
								class="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium"
								disabled={isAddingBubble}
							>
								{isAddingBubble ? '✓ Clique na imagem' : '+ Adicionar Balão'}
							</button>
							
							<button 
								onclick={translateAll}
								class="w-full px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors font-medium"
								disabled={bubbles.length === 0}
							>
								🌐 Traduzir Tudo
							</button>
							
							<button 
								onclick={() => showTranslations = !showTranslations}
								class="w-full px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors font-medium"
								disabled={bubbles.length === 0}
							>
								{showTranslations ? '👁️ Ver Original' : '👁️ Ver Tradução'}
							</button>
						</div>
					</div>

					<!-- Bubble Editor -->
					{#if selectedBubble !== null}
						{@const bubble = bubbles.find(b => b.id === selectedBubble)}
						{#if bubble}
							<div class="bg-white rounded-lg shadow-lg p-4">
								<div class="flex items-center justify-between mb-4">
									<h3 class="text-lg font-semibold text-gray-800">Editar Balão</h3>
									<button 
										onclick={() => removeBubble(bubble.id)}
										class="px-3 py-1 text-sm text-red-600 hover:bg-red-50 rounded transition-colors"
									>
										🗑️ Excluir
									</button>
								</div>
								
								<div class="space-y-4">
									<div>
										<label class="block text-sm font-medium text-gray-700 mb-2">Texto Original</label>
										<textarea 
											value={bubble.originalText}
											oninput={(e) => updateBubbleText(bubble.id, (e.target as HTMLTextAreaElement).value, true)}
											class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
											rows="3"
											placeholder="Digite o texto original..."
										></textarea>
									</div>
									
									<button 
										onclick={() => translateBubble(bubble.id)}
										class="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium"
										disabled={!bubble.originalText}
									>
										🔄 Traduzir Este Balão
									</button>
									
									<div>
										<label class="block text-sm font-medium text-gray-700 mb-2">Tradução</label>
										<textarea 
											value={bubble.translatedText}
											oninput={(e) => updateBubbleText(bubble.id, (e.target as HTMLTextAreaElement).value, false)}
											class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
											rows="3"
											placeholder="A tradução aparecerá aqui..."
										></textarea>
									</div>
								</div>
							</div>
						{/if}
					{:else}
						<div class="bg-white rounded-lg shadow-lg p-4">
							<p class="text-gray-500 text-center py-8">
								Selecione um balão para editar ou adicione um novo
							</p>
						</div>
					{/if}

					<!-- Statistics -->
					<div class="bg-white rounded-lg shadow-lg p-4">
						<h3 class="text-lg font-semibold text-gray-800 mb-3">Estatísticas</h3>
						<div class="space-y-2 text-sm">
							<div class="flex justify-between">
								<span class="text-gray-600">Total de Balões:</span>
								<span class="font-semibold">{bubbles.length}</span>
							</div>
							<div class="flex justify-between">
								<span class="text-gray-600">Traduzidos:</span>
								<span class="font-semibold text-green-600">{bubbles.filter(b => b.translatedText).length}</span>
							</div>
							<div class="flex justify-between">
								<span class="text-gray-600">Pendentes:</span>
								<span class="font-semibold text-orange-600">{bubbles.filter(b => !b.translatedText).length}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		{/if}
	</div>
</div>
