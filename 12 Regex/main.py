import re

holy_grail_pattern = '<td class=\"mainCellClone\"><b>[0-9]+\.<\/b><a class=\"xg_stag_a_ent \" href=\"/portal/\.\.\.\">\S*<\/a>,</td><td class=\"mainCell hideForDesktop \" data-header=\"Por.: \"><b>([0-9]+)\.</b><a class=\"xg_stag_a_ent \" href=\"/portal/\.\.\.\">\S*</a>,</td><td class=\"text-center hideForMobile\"><span class=\"xg_hide\">[0-9]+</span> [0-9]+\.</td><td class=\"text-center hideForMobile\" data-header=\"Prijmeni: \"><a href=\"javascript:void\(0\);\" onclick=\"void 0\"></a></td><td class=\"text-lefthideForMobile\" data-header=\"Jmeno: \"><span class=\"xg_hide\">(\S*)</span><a class=\"xg_stag_a_ent\" href=\"/portal/\.\.\.\">\S*</a></td><td class=\"text-lefthideForMobile\" data-header=\"Tituly: \">(\S*)</td><td class=\" hideForMobile\" data-header=\"Os\. cislo: \"></td><td class=\"text-left hideForMobile\" data-header=\"Fakulta: \">(\w[0-9]{8})&nbsp;<a class=\"prunik_casu prunik_casu_type_student prunik_casu_size_1\" href=\"javascript:void\(0\);\"aria-hidden=\"true\" title=\"Zahrne zvolenou osobu do vypoctu pruniku casu rozvrhu\.\"onclick=\"void 0\"></span></td><td class=\"hideForMobile\" data-header=\"St\.pr\.: \"><span class=\"xg_hide\">(\w\w)</span><a class=\"xg_stag_a_ent\" href=\"/portal/\.\.\.\">\w\w</a></td><td class=\"text-left\" data-header=\"Obor/Specializace/Kombinace: \"><span class=\"xg_hide\">(\w\d+\w*\d* - \w - \w)</span><a class=\"xg_stag_a_ent\" href=\"/portal/\.\.\.\">\w\d+\w*\d*</a>- \w- \w</td><td class=\"text-left\" data-header=\"Stav: \">(\w{2,})</td><td class=\"hideForMobile\" data-header=\"Rok st\.: \">(\w+)</td><td class=\"text-center\" data-header=\"Statut: \">(\d)</td><td data-header=\"Sem\.: \">(\w)</td><td data-header=\"Misto vyuky: \">(\w{2})</td><td class=\"hideForMobile\" data-header=\"Individualni studijni plan: \">(\w+)</td><td class=\"text-center hideForMobile\"data-header=\"Pocet, kolikrat si jiz student zapsal predmet v ramci aktualniho studia: \"><span style=\"display:none;\">\w</span>(\w*)</td><td class=\"hideForMobile\" data-header=\"Vyjezd&nbsp;od - do: \"><span style=\"display:none;\">\d</span>(\d)</td><td class=\"hideForMobile\" data-header=\"Rodicovska/materska dovolena: \"><span></span></td><td><span></span></td>'
fields = (
    'index', 'last_name', 'first_name', 'os_cislo', 'fakulta', 'nejaky_random_id', 'obor', 'stav', 'rok_studia',
    'status', 'sem', 'misto_vyuky', 'isp', 'pocet_zapisu'
)
obory = ('AI', 'AVI', 'IS', 'IT')


def construct_name(first, last):
    return f'{last.upper()} {first}'


def categorize(students):
    categorized = {}
    for obor in obory:
        obor_students = []
        for student in sorted(sorted(students, key=lambda x: int(x[3][1:])), key=lambda x: int(x[3][1:]) % 2 == 0):
            if student[6] == obor:
                obor_students.append(student)
        categorized[obor] = tuple(obor_students)
    return categorized


with open('vstup.html', mode='r') as file:
    tbody = re.sub(
        ' {2,}', '', re.findall(r'<tbody>([\S\s]*)</table>', file.read())[0].replace('\n', '')
    ).replace('"display:none;" ', '"display:none;">')
    student_data = re.findall(holy_grail_pattern, tbody)

    for obor, students in categorize(student_data).items():
        print(obor)
        for index, student in enumerate(students):
            student = dict(zip(fields, student))
            print(
                f'{index + 1:>2}: {student["os_cislo"][0]} '
                f'{construct_name(student["first_name"], student["last_name"]):18} '
                f'{student["obor"]:<3} '
                f'{student["os_cislo"][1:]}'
            )
        print()
