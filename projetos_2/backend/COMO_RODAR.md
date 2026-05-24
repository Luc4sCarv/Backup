# Como rodar (rápido)

No terminal, dentro da pasta do projeto:

```bash
cd /home/lucas/Documentos/Faculdade/PJ2/projetos_2
uv sync
uv run python manage.py migrate --fake-initial
uv run python manage.py runserver 127.0.0.1:8000
```

## Checar no navegador

- App: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin/

Se abrir, o servidor está ok.
