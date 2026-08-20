# Projeto-de-Relogio-em-Python
Aplicação desktop desenvolvida em Python utilizando PyQt5 e Pygame, reúne três funcionalidades principais:

- 🕒 **Relógio Digital** — tela inicial, sempre em execução
- ⏱️ **Cronômetro** — start, stop e reset
- ⏰ **Alarme** — define um horário e toca uma música quando ele chega

Cada tela é independente e continua rodando em segundo plano mesmo quando você
navega para outra — o cronômetro não para, o relógio não trava, e o alarme
continua contando até o horário definido. Tudo só é encerrado quando a janela
principal é fechada.

## Preview

```
┌─────────────────────────────────────┐
│             18:42:31                │
│                                     │
│   [ Cronômetro ]   [ Alarme ]       │
└─────────────────────────────────────┘
```

Ao clicar em um dos botões, a página é trocada; um botão **"Voltar ao Menu"**
retorna para o relógio a qualquer momento.

## Estrutura do projeto

```
MeuRelogio/
│
├── janela_principal.py    # QMainWindow — ponto de entrada da aplicação e alterna entre as páginas
├── base_page.py           # classe-base compartilhada (herança)
├── relogio_digital.py     # página do relógio (tela inicial)
├── cronometro.py          # página do cronômetro
├── alarme.py              # página do alarme
│
└── assets/            
    ├── iconeRelogio.jpg
    ├── Would It Matter - Rose Campbell.mp3
    ├── Wildfire - Jessie Villa.mp3
    └── Wooden Train Whistle.mp3
```

## Requisitos

- Python 3.8+
- [PyQt5](https://pypi.org/project/PyQt5/)
- [pygame](https://pypi.org/project/pygame/) (usado para tocar o som do alarme)

Instalar as dependências:

```bash
pip install PyQt5 pygame
```

## Como rodar

```bash
python main.py
```
> Desempacote os assets.rar.
> Para o alarme tocar corretamente, os arquivos de música referenciados em
> `alarme.py` (`soundFile1`, `soundFile2`, `soundFile3`) precisam existir no
> caminho indicado. Com a pasta assets e todos os arquivos .py baixados e reunidos
> rode o sistema pelo janela_principal.py

## Funcionalidades

| Página        | O que faz |
|---------------|-----------|
| Relógio       | Mostra a hora atual, atualizada a cada segundo |
| Cronômetro    | Start / Stop / Reset, com precisão de milissegundos |
| Alarme        | Escolha de música + horário no formato `HH:MM:SS` |


## Autores

- João Marcelo Paes Gonçalves
