import re
with open("raw.txt","r",encoding="utf-8") as file:
    text= file.read()
    BINPattern = r"\nБИН(?P<BIN>.*)"
    CHECKPattern = r"\nЧек(?P<CHECK>.*)"
    TIME_ADDRESSPattern = r"\nВремя:(?P<TIME>.*)\n(?P<ADDRESS>.*)"
    ZNMPattern = r"\nЗНМ:(?P<ZNM>.*)"
    item_pattern_text = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}(?P<title>Стоимость)\n{1}(?P<total2>.*)"
    item_pattern = re.compile(item_pattern_text)
    BINText = re.search(BINPattern, text).group("BIN").strip()
    CHECKText = re.search(CHECKPattern, text).group("CHECK").strip()
    ADDRESSText = re.search(TIME_ADDRESSPattern, text).group("ADDRESS").strip()
    TIMEText = re.search(TIME_ADDRESSPattern, text).group("TIME").strip()
    ZNMText = re.search(ZNMPattern, text).group("ZNM").strip()
    
    item = re.findall(item_pattern,text)
        