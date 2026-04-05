# Cartilha do Serviço Radioamador

Este repositório contém o código-fonte e as ferramentas necessárias para gerar a **Cartilha do Serviço Radioamador** em diversos formatos digitais.

## Conteúdo Original

Este trabalho é uma reprodução adaptada da cartilha original da Anatel:
**[Cartilha do Serviço Radioamador 2026-03.1](https://sistemas.anatel.gov.br/anexar-api/publico/anexos/download/6067372ab14ee1c9702eb7ff93f11323)**.

Embora busquemos manter a precisão das informações, os textos oficiais da Anatel e a legislação vigente sempre prevalecem.

## Propósito do Repositório

O objetivo deste projeto é fornecer uma versão digital, acessível e multi-plataforma da cartilha original da Anatel. Utilizando Asciidoc como linguagem de marcação, o conteúdo pode ser facilmente convertido para formatos como PDF, EPUB e HTML, facilitando o estudo e a consulta por futuros e atuais radioamadores.

## Sobre este Livro

A Cartilha do Serviço Radioamador é um guia essencial para quem deseja ingressar ou já atua no radioamadorismo no Brasil. Ela cobre desde os conceitos básicos do que é ser um radioamador, passando pelo processo de licenciamento, legislação, ética operacional, até conhecimentos técnicos de eletrônica e ondulatória.

Este projeto busca manter a fidelidade ao conteúdo original, permitindo melhorias e extensões através de "versões da comunidade".

## Como Compilar (Build)

Este projeto utiliza **Ruby** e **Rake** para automatizar o processo de build.

### Pré-requisitos

1.  **Ruby**: Certifique-se de ter o Ruby instalado (versão definida no arquivo `.ruby-version`).
2.  **Bundler**: Instale o bundler se ainda não o tiver:
    ```bash
    gem install bundler
    ```
3.  **Dependências**: Instale as dependências do projeto:
    ```bash
    bundle install
    ```

### Comandos de Build

Para gerar todos os formatos de uma vez, execute:

```bash
rake book:build
```

Você também pode gerar formatos específicos:

*   `rake book:build_html`: Gera a versão HTML.
*   `rake book:build_pdf`: Gera a versão PDF.
*   `rake book:build_epub`: Gera a versão EPUB.
*   `rake book:build_mobi`: Gera a versão Mobi (Kindle).
*   `rake book:build_fb2`: Gera a versão FB2.

Para limpar os arquivos gerados:
```bash
rake book:clean
```

## Artefatos e Variantes

O processo de build gera diferentes variantes do livro para atender a diferentes necessidades:

*   **`default`**: A versão básica, seguindo estritamente o conteúdo original.
*   **`fix`**: Inclui correções de erros conhecidos ou atualizações pontuais.
*   **`ext` (Extended)**: Uma versão estendida que inclui as correções (`fix`) e conteúdos adicionais ou funcionalidades extras.

Os nomes dos arquivos seguirão o padrão `cartilha_radioamador_[variante].[extensão]` (exceto para a variante `default`, que não possui o sufixo no nome).

## Referência do Projeto

A estrutura e o fluxo de trabalho deste repositório foram baseados e inspirados no projeto [Pro Git 2](https://github.com/progit/progit2).
