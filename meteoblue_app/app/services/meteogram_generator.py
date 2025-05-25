# app/services/meteogram_generator.py

from urllib.parse import urlencode

METEOBLUE_API_KEY = "5ZutTfGdbKise1A2"
BASE_URL = "https://my.meteoblue.com/images"

# Lista dos tipos de meteogramas suportados
METEOGRAM_TYPES = {
    "5day": "meteogram",
    "7day": "meteogram_extended",
    "allinone": "meteogram_one",
    "snow": "meteogram_snow",
    "agro": "meteogram_agro",
    "sowing": "meteogram_sowing",
    "spraying": "meteogram_spraying",
    "soiltraffic": "meteogram_soiltraffic",
    "air": "meteogram_air",
    "sounding": "meteogram_sounding",
    "stueve": "meteogram_stueve",
    "thermal": "meteogram_thermal",
    "14day": "meteogram_14day",
    "multimodel": "meteogram_multimodel",
    "multimodelensemble": "meteogram_multimodelensemble",
    "multimodelwind": "meteogram_multimodelwind",
    "solar": "meteogram_solar_forecast",
    "sea": "meteogram_sea",
    "sea_7day": "meteogram_sea_7day",
    "surf": "meteogram_surf",
    "seasonal": "meteogram_seasonal"
}

FRIENDLY_NAMES = {
    "5day": "5 Dias",
    "7day": "7 Dias",
    "allinone": "All-in-One",
    "snow": "Neve",
    "agro": "Agro",
    "sowing": "Plantio",
    "spraying": "Pulverização",
    "soiltraffic": "Tráfego no Solo",
    "air": "Qualidade do Ar",
    "sounding": "Perfil Atmosférico",
    "stueve": "Stueve",
    "thermal": "Termal",
    "14day": "14 Dias",
    "multimodel": "Multi-modelo",
    "multimodelensemble": "Ensemble Multi-modelo",
    "multimodelwind": "Vento Multi-modelo",
    "solar": "Previsão Solar",
    "sea": "Mar",
    "sea_7day": "Mar 7 Dias",
    "surf": "Ondas",
    "seasonal": "Sazonal",
}

def generate_meteogram_url(lat, lon, meteogram_type="allinone", asl=None, extra_params=None):
    """
    Gera a URL de um meteograma com base nos parâmetros fornecidos.
    
    :param lat: Latitude (float)
    :param lon: Longitude (float)
    :param meteogram_type: Tipo do meteograma (str)
    :param asl: Altitude acima do nível do mar (opcional)
    :param extra_params: Dicionário com parâmetros extras, se necessário
    :return: URL completa (str)
    """
    endpoint = METEOGRAM_TYPES.get(meteogram_type.lower())
    if not endpoint:
        raise ValueError(f"Tipo de meteograma '{meteogram_type}' não suportado.")

    params = {
        "lat": lat,
        "lon": lon,
        "apikey": METEOBLUE_API_KEY,
        "lang": "pt"  # <-- define português
    }
    if asl:
        params["asl"] = asl
    if extra_params:
        params.update(extra_params)

    url = f"{BASE_URL}/{endpoint}?" + urlencode(params)
    return url
