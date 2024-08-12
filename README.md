# Isaac Newton e Suas Maçãs

Bem-vindo ao jogo "Isaac Newton e Suas Maçãs"! Este é um jogo simples, mas desafiador, desenvolvido com Pygame, onde você controla Isaac Newton e deve ajudá-lo a desviar das maçãs que caem de uma árvore.

## 🎮 Objetivo do Jogo

O objetivo é simples: mover Isaac Newton para evitar ser atingido por maçãs que caem de uma árvore. O jogo termina quando Isaac colide com uma maçã, e a sua pontuação é medida pela quantidade de maçãs evitadas.

## ✨ Funcionalidades

- **Controle de Personagem:** Controle Isaac usando as teclas de seta para movê-lo em quatro direções: esquerda, direita, cima e baixo.
- **Queda de Maçãs:** Maçãs caem aleatoriamente de diferentes pontos da árvore, aumentando o desafio.
- **Detecção de Colisão:** Se Isaac colidir com uma maçã, o jogo termina imediatamente.
- **Tela de Fim de Jogo:** Uma mensagem de "Você Perdeu!" é exibida quando o jogo termina.
- **Interface de Pontuação:** A quantidade de maçãs que você evitou é exibida na tela durante o jogo.

## 📦 Instalação

Siga as instruções abaixo para configurar e executar o jogo no seu ambiente local.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/isaac-newton-macas.git

2. **Navege ate o diretorio do projeto:**
    ```bash
   cd isaac-newton-macas

3. **Crie um ambiente virtual (opcional, mas recomendado):**
    ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

4. **Instale as dependências necessárias:**
    ```bash
   pip install -r requirements.txt


## 🚀 Como Jogar

Execute o jogo com o comando:

```bash
python main.py


### Controles do Jogo:

- **Seta Esquerda:** Mover Isaac para a esquerda.
- **Seta Direita:** Mover Isaac para a direita.
- **Seta Cima:** Mover Isaac para cima.
- **Seta Baixo:** Mover Isaac para baixo.

### Objetivo:

Desvie das maçãs que caem da árvore. A cada maçã evitada, sua pontuação aumenta. Se uma maçã atingir Isaac, o jogo termina.

### Fim de Jogo:

Quando Isaac colide com uma maçã, uma mensagem de "Você Perdeu!" aparecerá, indicando o fim do jogo.

## 🖼️ Recursos Visuais

O jogo utiliza os seguintes recursos visuais que devem estar presentes no diretório `images/`:

- **Fundo:** `windows-xp.jpg` - A imagem de fundo do jogo.
- **Isaac Newton:** `small_preview_rev_1.png` - A imagem do personagem Isaac.
- **Maçã:** `apple.png` - A imagem das maçãs que caem.
- **Árvore:** `desenho-de-arvore_preview_rev_1.png` - A imagem da árvore de onde as maçãs caem.

## 🚧 Controle de Erros

Este projeto inclui controle de erros para garantir que o jogo não quebre caso algum recurso visual ou fonte esteja ausente ou corrompido. Se ocorrer um erro ao carregar uma imagem ou fonte, o jogo exibirá uma mensagem de erro no console e será encerrado de forma segura.

## 🛠️ Contribuição

Contribuições são bem-vindas! Se você encontrou um bug, tem uma ideia para uma nova funcionalidade ou deseja melhorar o código, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📝 Licença

Este projeto está licenciado sob a MIT License. Isso significa que você é livre para usar, modificar e distribuir este código, desde que mantenha a atribuição original.




