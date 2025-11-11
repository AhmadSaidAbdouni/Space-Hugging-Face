<h1 align="center">Criando um Space no Hugging Face</h1>
<h2 align="center">Assistente Virtual para WhatsApp</h2>

<img width="1890" height="591" alt="Cópia de Cópia de ↓ Read More ↓" src="https://github.com/user-attachments/assets/deb56c28-9637-4557-b9bf-44ce1a0499b7" />


## :dart: Descrição do Projeto

Este projeto demonstra como criar um **Space** na plataforma Hugging Face e integrá-lo com um modelo de IA para implementar um **assistente virtual para WhatsApp**.

## :white_check_mark: Pré-requisitos

- Criar uma conta no Hugging Face: [https://huggingface.co/](https://huggingface.co/)  
- Gerar um **token de acesso** do tipo `READ`: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)  
  > Guarde este token, ele será usado para autenticação no Space.  
- Criar um **Space**: [https://huggingface.co/new-space](https://huggingface.co/new-space)  
  - SDK: **Gradio**  
  - Hardware: **CPU Basic**  
  - Visibilidade: **Public** ou **Private**, dependendo do seu objetivo  
- Criar os arquivos `app.py` e `requirements.txt` e colocar o conteúdo correspondente deste repositório  
- No Space, acessar **Settings → New Secret**, criar um secret chamado `HF_TOKEN` e inserir o token gerado anteriormente  
- Finalizado, vá para a aba **App** e teste o Space  

## :hammer: Tecnologias Utilizadas

- Python  
- Gradio  
- Hugging Face Inference API  

## :raising_hand: Autor

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/75034691?v=4" width=115><br><sub>Ahmad Said Abdouni</sub>](https://github.com/AhmadSaidAbdouni) |
| :---: |
