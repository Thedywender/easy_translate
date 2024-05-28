<summary>🧑‍💻 O que foi desenvolvido neste Projeto?</summary><br>
<p>Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side.</p>
<details>
    <summary>📝 Habilidades que foram desenvolvidas:</summary><br>
        <li>Implementação de uma API utilizando arquitetura em camadas MVC;</li>
        <li>Utilização de Docker para projetos Python;</li>
        <li>Aplicação de POO;</li>
        <li>Escrita de testes para APIS garantindo a implementação de endpoints;</li>
        <li>Desenvolvimento de páginas Web Server Side;</li>
    </ul>
    </details>
    <details>
    <summary>🐳 Como rodar o projeto em sua máquina:</summary><br>
        <details><summary>Crie um ambiente virtual:</summary>
            <pre><code class="language-bash">python3 -m venv .venv && source .venv/bin/activate</code></pre>
        </details>
        <details><summary>Instale as dependências:</summary>
            <pre><code class="language-bash">python3 -m pip install -r dev-requirements.txt</code></pre>
        </details>      
        <details><summary>Primeira opção para subir o banco(recomendado):</summary><br>
        <summary>Subir o Banco e o Flask pelo docker-compose:</summary>
        <pre><code class="language-bash">docker compose up --build translate</code></pre>
            <p>Execute os seeders para popular o banco:</p>
            <pre><code class="language-bash">docker compose exec -it translate python3 src/run_seeds.py</code></pre>            
        </details>          
         <details><summary>Outra opção para subir o banco:</summary><br>
           <summary>Subir o Banco pelo Docker e o FLASK localmente:</summary>
            <pre><code class="language-bash">docker compose up -d mongodb

python3 src/app.py</code></pre>
            <p>Execute os seeders para popular o banco:</p>
            <pre><code class="language-bash">python3 src/run_seeds.py</code></pre>
    </ul>
    </details>
