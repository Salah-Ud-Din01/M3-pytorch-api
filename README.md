# M3 – PyTorch API (Miniprojekt Integration & Distribution)

## 👥 Projektmedlemmar

| Namn | 
|------|
| SlaahudDin |
| Tarik Mulisic |

---

## 📋 Projektbeskrivning

Detta projekt är en del av kurs M3 och syftar till att simulera ett professionellt arbetsflöde där en tränad PyTorch-modell integreras i ett REST API och distribueras via Docker-containers.

Vi har använt en av våra modeller från K2 – ett **SimpleCNN** tränat på **CIFAR-10** – och exponerat den via ett FastAPI-baserat API.

---

## 🧠 Modell

- **Arkitektur:** SimpleCNN (Convolutional Neural Network)
- **Dataset:** CIFAR-10
- **Exportformat:** ONNX (`model.onnx`)
- **Klasser:** `plane`, `car`, `bird`, `cat`, `deer`, `dog`, `frog`, `horse`, `ship`, `truck`

---

## 🗂️ Projektstruktur

```
M3-pytorch-api/
├── main.py              # FastAPI-applikation med /predict endpoint
├── model.py             # SimpleCNN-modellarkitektur
├── export_model.py      # Exporterar PyTorch-modell till ONNX
├── dataset.py           # CIFAR-10 dataloaders
├── best_model.pth       # Tränade modellvikter
├── model.onnx           # Exporterad ONNX-modell
├── Dockerfile           # Container-konfiguration
└── README.md            # Denna fil
```

---

## 🚀 Kom igång

### Bygg och starta Docker-containern

```bash
# Bygg imagen
docker build -t m3-pytorch-api .

# Starta containern
docker run -p 8000:8000 m3-pytorch-api
```

API:et är nu tillgängligt på `http://localhost:8000`

---

## 📡 API-användning

### `POST /predict`

Skicka en bild som en platt lista med 3072 floats (3 × 32 × 32 pixlar, normaliserade).

**Request:**
```json
{
  "data": [0.1, -0.5, 0.3, ...]
}
```

**Response:**
```json
{
  "class_id": 3,
  "class_name": "cat",
  "confidence": 0.87
}
```

**Exempel med curl:**
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"data": [0.1, 0.2, ...]}'
```

---

## 🐳 Dockerfile

Containern baseras på `python:3.11-slim` och använder `uv` för snabb paketinstallation.

```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN pip install uv
COPY . .
RUN uv pip install --system fastapi uvicorn onnxruntime pillow numpy python-multipart
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🔀 Pull Requests & Kodgranskning

> Nedan finns länkar till de Pull Requests som gjordes under projektets gång, med dokumenterade kodgranskningar.

| # | Titel | Granskare | Länk |
|---|-------|-----------|------|
| PR #1 | *(lägg till titel)* | *(lägg till namn)* | [🔗 Länk till PR #1](#) |
| PR #2 | *(lägg till titel)* | *(lägg till namn)* | [🔗 Länk till PR #2](#) |

> **OBS:** Ersätt `#`-länkarna ovan med de faktiska GitHub-länkarna till era Pull Requests.

---

## ✅ Inlämningschecklista

- [x] Containern går att bygga och starta
- [x] API:et svarar med korrekt prediktion vid `POST /predict`
- [x] Modell exporterad till ONNX
- [x] README innehåller länk till minst två Pull Requests med kodgranskning
- [x] Utveckling sker via Feature Branches i gemensamt repo

---

## 🛠️ Teknologier

- Python 3.11
- PyTorch
- ONNX Runtime
- FastAPI
- Uvicorn
- Docker
- uv (pakethanterare)