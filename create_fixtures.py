# import os, json, sqlite3
# from pathlib import Path
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
# import django; django.setup()
# from django.apps import apps

# db = next(Path().rglob("*.sqlite3"), None)
# if not db:
#     exit("❌ БД не найдена")

# conn = sqlite3.connect(db)
# conn.row_factory = sqlite3.Row

# for m in apps.get_models():
#     if m._meta.app_label in ('auth', 'contenttypes', 'sessions', 'admin'):
#         continue
#     t = m._meta.db_table
#     rows = conn.execute(f"SELECT * FROM {t}").fetchall()
#     if not rows:
#         continue
#     data = []
#     for r in rows:
#         fields = {k: r[k] for k in r.keys() if k != 'id'}
#         data.append({
#             "model": f"{m._meta.app_label}.{m.__name__.lower()}",
#             "pk": r["id"],
#             "fields": fields
#         })
#     (Path(m._meta.app_label) / "fixtures").mkdir(exist_ok=True)
#     with open(f"{m._meta.app_label}/fixtures/{m.__name__.lower()}.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)

# conn.close()
# print("✅ Фикстуры созданы")

import os, json
from pathlib import Path
from django.core.serializers.json import DjangoJSONEncoder
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django; django.setup()
from django.apps import apps
from django.db.models import ForeignKey, FileField, ImageField

for model in apps.get_models():
    app_label = model._meta.app_label
    if app_label in ('auth', 'contenttypes', 'sessions', 'admin'):
        continue

    data = []
    for obj in model.objects.all():
        fields = {}
        for field in obj._meta.fields:
            if field.name == 'id':
                continue
            value = getattr(obj, field.name)
            # Обработка ForeignKey
            if isinstance(field, ForeignKey):
                fields[field.name + '_id'] = value.pk if value else None
            # Обработка FileField / ImageField — сохраняем путь как строку
            elif isinstance(field, (FileField, ImageField)):
                fields[field.name] = str(value) if value else ""
            # Остальные поля — как есть
            else:
                fields[field.name] = value

        data.append({
            "model": f"{app_label}.{model.__name__.lower()}",
            "pk": obj.pk,
            "fields": fields
        })

    (Path(app_label) / "fixtures").mkdir(exist_ok=True)
    with open(f"{app_label}/fixtures/{model.__name__.lower()}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, cls=DjangoJSONEncoder, ensure_ascii=False, indent=2)

print("✅ Фикстуры созданы")