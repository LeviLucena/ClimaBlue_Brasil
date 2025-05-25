from flask import Blueprint, request, jsonify, render_template
from app.services.meteogram_generator import generate_meteogram_url
from app.services.meteogram_generator import METEOGRAM_TYPES, FRIENDLY_NAMES

meteogram_bp = Blueprint('meteogram', __name__)

# Seu dicionário estados e capitais aqui (ou importe de outro módulo se quiser)
estados = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins",
}
# Dicionário com lat/lon aproximados das capitais para preencher automaticamente
capitais = {
    "AC": {"nome": "Rio Branco", "lat": -9.97499, "lon": -67.8243},
    "AL": {"nome": "Maceió", "lat": -9.66599, "lon": -35.735},
    "AP": {"nome": "Macapá", "lat": 0.034934, "lon": -51.0694},
    "AM": {"nome": "Manaus", "lat": -3.10194, "lon": -60.025},
    "BA": {"nome": "Salvador", "lat": -12.9714, "lon": -38.5014},
    "CE": {"nome": "Fortaleza", "lat": -3.71722, "lon": -38.5434},
    "DF": {"nome": "Brasília", "lat": -15.7939, "lon": -47.8828},
    "ES": {"nome": "Vitória", "lat": -20.3155, "lon": -40.3128},
    "GO": {"nome": "Goiânia", "lat": -16.6864, "lon": -49.2643},
    "MA": {"nome": "São Luís", "lat": -2.53074, "lon": -44.3068},
    "MT": {"nome": "Cuiabá", "lat": -15.601, "lon": -56.0979},
    "MS": {"nome": "Campo Grande", "lat": -20.4697, "lon": -54.6201},
    "MG": {"nome": "Belo Horizonte", "lat": -19.9208, "lon": -43.9378},
    "PA": {"nome": "Belém", "lat": -1.45502, "lon": -48.5024},
    "PB": {"nome": "João Pessoa", "lat": -7.11522, "lon": -34.8641},
    "PR": {"nome": "Curitiba", "lat": -25.4297, "lon": -49.2719},
    "PE": {"nome": "Recife", "lat": -8.05389, "lon": -34.8811},
    "PI": {"nome": "Teresina", "lat": -5.08921, "lon": -42.8016},
    "RJ": {"nome": "Rio de Janeiro", "lat": -22.9068, "lon": -43.1729},
    "RN": {"nome": "Natal", "lat": -5.79448, "lon": -35.211},
    "RS": {"nome": "Porto Alegre", "lat": -30.0346, "lon": -51.2177},
    "RO": {"nome": "Porto Velho", "lat": -8.76077, "lon": -63.8999},
    "RR": {"nome": "Boa Vista", "lat": 2.81972, "lon": -60.6733},
    "SC": {"nome": "Florianópolis", "lat": -27.5954, "lon": -48.548},
    "SP": {"nome": "São Paulo", "lat": -23.5475, "lon": -46.6361},
    "SE": {"nome": "Aracaju", "lat": -10.9472, "lon": -37.0731},
    "TO": {"nome": "Palmas", "lat": -10.2455, "lon": -48.3243},
}

@meteogram_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        estado = request.form.get("estado")
        if estado in estados:
            lat = capitais[estado]["lat"]
            lon = capitais[estado]["lon"]
            return render_template(
                "index.html",
                estados=estados,
                capitais=capitais,
                estado_selecionado=estado,
                lat=lat,
                lon=lon,
            )
        else:
            return render_template("index.html", estados=estados, capitais=capitais, meteogram_types=METEOGRAM_TYPES, friendly_names=FRIENDLY_NAMES, erro="Estado inválido")
    return render_template("index.html", estados=estados, capitais=capitais, meteogram_types=METEOGRAM_TYPES, friendly_names=FRIENDLY_NAMES)

@meteogram_bp.route('/api/meteogram')
def get_meteogram():
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    meteogram_type = request.args.get('type', default='allinone')
    asl = request.args.get('asl', type=int)
    
    if lat is None or lon is None:
        return jsonify({"error": "Latitude e longitude são obrigatórios"}), 400
    
    try:
        url = generate_meteogram_url(lat, lon, meteogram_type, asl)
        return jsonify({"url": url})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
