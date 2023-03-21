from dadata import Dadata
import os

from hello import hello_user

data = os.path.exists("data/sql_for_dadata.db")
# dadata = Dadata(token, secret)
# result = dadata.clean("address", "нск проспект карла маркса 30/1")
copy_request = {'source': 'нск проспект карла маркса 30/1', 'result': 'г Новосибирск, пр-кт Карла Маркса, д 30/1',
                'postal_code': '630087', 'country': 'Россия', 'country_iso_code': 'RU', 'federal_district': 'Сибирский',
                'region_fias_id': '1ac46b49-3209-4814-b7bf-a509ea1aecd9', 'region_kladr_id': '5400000000000',
                'region_iso_code': 'RU-NVS', 'region_with_type': 'Новосибирская обл', 'region_type': 'обл',
                'region_type_full': 'область', 'region': 'Новосибирская', 'area_fias_id': None, 'area_kladr_id': None,
                'area_with_type': None, 'area_type': None, 'area_type_full': None, 'area': None,
                'city_fias_id': '8dea00e3-9aab-4d8e-887c-ef2aaa546456', 'city_kladr_id': '5400000100000',
                'city_with_type': 'г Новосибирск', 'city_type': 'г', 'city_type_full': 'город', 'city': 'Новосибирск',
                'city_area': None, 'city_district_fias_id': None, 'city_district_kladr_id': None,
                'city_district_with_type': 'р-н Ленинский', 'city_district_type': 'р-н',
                'city_district_type_full': 'район', 'city_district': 'Ленинский', 'settlement_fias_id': None,
                'settlement_kladr_id': None, 'settlement_with_type': None, 'settlement_type': None,
                'settlement_type_full': None, 'settlement': None,
                'street_fias_id': '6c36a088-79d2-48a9-8051-97024b010f0c', 'street_kladr_id': '54000001000078100',
                'street_with_type': 'пр-кт Карла Маркса', 'street_type': 'пр-кт', 'street_type_full': 'проспект',
                'street': 'Карла Маркса', 'house_fias_id': '3cf198e3-06cb-4672-8e42-8823e8867497',
                'house_kladr_id': '5400000100007810059', 'house_cadnum': '54:35:064310:152', 'house_type': 'д',
                'house_type_full': 'дом', 'house': '30/1', 'block_type': None, 'block_type_full': None, 'block': None,
                'entrance': None, 'floor': None, 'flat_fias_id': None, 'flat_cadnum': None, 'flat_type': None,
                'flat_type_full': None, 'flat': None, 'flat_area': None, 'square_meter_price': None, 'flat_price': None,
                'postal_box': None, 'fias_id': '3cf198e3-06cb-4672-8e42-8823e8867497',
                'fias_code': '54000001000000007810059', 'fias_level': '8', 'fias_actuality_state': '0',
                'kladr_id': '5400000100007810059', 'capital_marker': '2', 'okato': '50401377000',
                'oktmo': '50701000001', 'tax_office': '5404', 'tax_office_legal': '5404', 'timezone': 'UTC+7',
                'geo_lat': '54.9914492', 'geo_lon': '82.912494', 'beltway_hit': None, 'beltway_distance': None,
                'qc_geo': 0, 'qc_complete': 5, 'qc_house': 2, 'qc': 0, 'unparsed_parts': None,
                'metro': [{'distance': 0.5, 'line': 'Ленинская', 'name': 'Студенческая'},
                          {'distance': 1.6, 'line': 'Ленинская', 'name': 'Площадь Маркса'},
                          {'distance': 2.5, 'line': 'Ленинская', 'name': 'Речной вокзал'}]}

all_length_text = 121
os.system(f"mode con:cols={all_length_text}")
only_stars = "*" * all_length_text
hello_user(only_stars, all_length_text - 1)