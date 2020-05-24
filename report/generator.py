# -*- coding: utf-8 -*-

from fpdf import FPDF
import sys
import os
import cgi

from report import report_data


def create_report(
    output_file,
    spacing=1,
    _name="",
    _number="",
    _age="",
    _card="",
    _room="",
    _weight="",
    _height="",
    _yawleft="",
    _yawright="",
    _rollleft="",
    _rollright="",
    _pitchdown="",
    _pitchup="",
):
    pdf = FPDF()
    pdf.add_font("DejaVu", "", "DejaVuSansCondensed.ttf", uni=True)
    pdf.add_page()
    pdf.set_font("DejaVu", "", 10)
    pdf.set_left_margin(5)

    pdf.cell(
        200, 12, txt="Лист обстеження загальний   Дата_______________", ln=1, align="C"
    )

    header = report_data.get_header_table(
        name=_name,
        age=_age,
        card=_card,
        room=_room,
        weight=_weight,
        height=_height,
        number=_number,
    )

    row_height = pdf.font_size * 1.1

    pdf.cell(150, row_height * spacing, txt=header[0][0], border=1)
    pdf.cell(50, row_height * spacing, txt=header[0][1], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(150, row_height * spacing, txt=header[1][0], border=1)
    pdf.cell(50, row_height * spacing, txt=header[1][1], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(130, row_height * 2, txt=header[2][0], border=1)
    pdf.cell(20, row_height * 2, txt=header[2][1], border=1)
    pdf.cell(25, row_height * 2, txt=header[2][2], border=1)
    pdf.cell(25, row_height * 2, txt=header[2][3], border=1)
    pdf.ln(row_height * 2)
    pdf.cell(60, row_height * 2, txt=header[3][0], border=1)
    pdf.cell(45, row_height * 2, txt=header[3][1], border=1)
    pdf.cell(45, row_height * 2, txt=header[3][2], border=1)
    pdf.cell(16, row_height * 2, txt=header[3][3], border=1)
    pdf.cell(16, row_height * 2, txt=header[3][4], border=1)
    pdf.cell(18, row_height * 2, txt=header[3][5], border=1)
    pdf.ln(row_height * 2)
    pdf.cell(160, row_height * 2, txt=header[4][0], border=1)
    pdf.cell(40, row_height * 2, txt=header[4][1], border=1)
    pdf.ln(row_height * 2)
    pdf.cell(160, row_height * 2, txt=header[5][0], border=1)
    pdf.cell(40, row_height * 2, txt=header[5][1], border=1)
    pdf.ln(row_height * 2)
    pdf.cell(200, row_height * spacing, txt=header[6][0], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(200, row_height * spacing, txt=header[7][0], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(200, row_height * spacing, txt=header[8][0], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(200, row_height * spacing, txt=header[9][0], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[10][0], border=1)
    pdf.cell(100, row_height * spacing, txt=header[10][1], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(25, row_height * spacing, txt=header[11][0], border=1)
    pdf.cell(25, row_height * spacing, txt=header[11][1], border=1)
    pdf.cell(25, row_height * spacing, txt=header[11][2], border=1)
    pdf.cell(25, row_height * spacing, txt=header[11][3], border=1)
    pdf.cell(40, row_height * spacing, txt=header[11][4], border=1)
    pdf.cell(30, row_height * spacing, txt=header[11][5], border=1)
    pdf.cell(30, row_height * spacing, txt=header[11][6], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[12][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[12][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[12][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[12][3], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[13][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[13][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[13][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[13][3], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(34, row_height * spacing, txt=header[14][0], border=1)
    pdf.cell(33, row_height * spacing, txt=header[14][1], border=1)
    pdf.cell(33, row_height * spacing, txt=header[14][2], border=1)
    pdf.cell(40, row_height * spacing, txt=header[14][3], border=1)
    pdf.cell(30, row_height * spacing, txt=header[14][4], border=1)
    pdf.cell(30, row_height * spacing, txt=header[14][5], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[15][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[15][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[15][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[15][3], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[16][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[16][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[16][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[16][3], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[17][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[17][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[17][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[17][3], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(34, row_height * spacing, txt=header[18][0], border=1)
    pdf.cell(33, row_height * spacing, txt=header[18][1], border=1)
    pdf.cell(33, row_height * spacing, txt=header[18][2], border=1)
    pdf.cell(40, row_height * spacing, txt=header[18][3], border=1)
    pdf.cell(30, row_height * spacing, txt=header[18][4], border=1)
    pdf.cell(30, row_height * spacing, txt=header[18][5], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[19][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[19][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[19][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[19][3], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[20][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[20][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[20][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[20][3], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[21][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[21][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[21][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[21][3], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[22][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[22][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[22][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[22][3], border=1)
    pdf.ln(row_height * spacing)
    pdf.cell(100, row_height * spacing, txt=header[23][0], border=1)
    pdf.cell(40, row_height * spacing, txt=header[23][1], border=1)
    pdf.cell(30, row_height * spacing, txt=header[23][2], border=1)
    pdf.cell(30, row_height * spacing, txt=header[23][3], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(
        200,
        10,
        txt="1. Функціональна програма «Бігова доріжка»  /до втоми/",
        ln=1,
        align="C",
    )

    rtp = report_data.get_running_truck_program_table()

    pdf.cell(24, row_height * 2, txt=rtp[0][0], border=1, align="C")
    pdf.cell(24, row_height * 2, txt=rtp[0][1], border=1, align="C")
    pdf.cell(24, row_height * 2, txt=rtp[0][2], border=1, align="C")
    pdf.cell(23, row_height * 2, txt=rtp[0][3], border=1, align="C")
    pdf.cell(45, row_height * 2, txt=rtp[0][4], border=1, align="C")
    pdf.cell(60, row_height * 2, txt=rtp[0][5], border=1, align="C")
    pdf.ln(row_height * 2)

    pdf.cell(24, row_height * spacing, txt=rtp[1][0], border=1, align="C")
    pdf.cell(24, row_height * spacing, txt=rtp[1][1], border=1, align="C")
    pdf.cell(24, row_height * spacing, txt=rtp[1][2], border=1, align="C")
    pdf.cell(23, row_height * spacing, txt=rtp[1][3], border=1, align="C")
    pdf.cell(15, row_height * spacing, txt=rtp[1][4], border=1, align="C")
    pdf.cell(15, row_height * spacing, txt=rtp[1][5], border=1, align="C")
    pdf.cell(15, row_height * spacing, txt=rtp[1][6], border=1, align="C")
    pdf.cell(12, row_height * spacing, txt=rtp[1][7], border=1, align="C")
    pdf.cell(12, row_height * spacing, txt=rtp[1][8], border=1, align="C")
    pdf.cell(12, row_height * spacing, txt=rtp[1][9], border=1, align="C")
    pdf.cell(24, row_height * spacing, txt=rtp[1][10], border=1, align="C")
    pdf.ln(row_height * spacing)

    pdf.cell(24, row_height * spacing, txt=rtp[2][0], border=1)
    pdf.cell(24, row_height * spacing, txt=rtp[2][1], border=1)
    pdf.cell(24, row_height * spacing, txt=rtp[2][2], border=1)
    pdf.cell(23, row_height * spacing, txt=rtp[2][3], border=1)
    pdf.cell(15, row_height * spacing, txt=rtp[2][4], border=1)
    pdf.cell(15, row_height * spacing, txt=rtp[2][5], border=1)
    pdf.cell(15, row_height * spacing, txt=rtp[2][6], border=1)
    pdf.cell(12, row_height * spacing, txt=rtp[2][7], border=1)
    pdf.cell(12, row_height * spacing, txt=rtp[2][8], border=1)
    pdf.cell(12, row_height * spacing, txt=rtp[2][9], border=1)
    pdf.cell(24, row_height * spacing, txt=rtp[2][10], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(24, row_height * spacing, txt=rtp[3][0], border=1)
    pdf.cell(24, row_height * spacing, txt=rtp[3][1], border=1)
    pdf.cell(24, row_height * spacing, txt=rtp[3][2], border=1)
    pdf.cell(23, row_height * spacing, txt=rtp[3][3], border=1)
    pdf.cell(15, row_height * spacing, txt=rtp[3][4], border=1)
    pdf.cell(15, row_height * spacing, txt=rtp[3][5], border=1)
    pdf.cell(15, row_height * spacing, txt=rtp[3][6], border=1)
    pdf.cell(12, row_height * spacing, txt=rtp[3][7], border=1)
    pdf.cell(12, row_height * spacing, txt=rtp[3][8], border=1)
    pdf.cell(12, row_height * spacing, txt=rtp[3][9], border=1)
    pdf.cell(24, row_height * spacing, txt=rtp[3][10], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(200, row_height * spacing, txt=rtp[4][0], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(200, 10, txt="2. Стрибки на місці до втоми.", ln=1, align="C")

    jotsp = report_data.get_jumping_on_the_spot_program_table()

    pdf.cell(24, row_height * 2, txt=jotsp[0][0], border=1, align="C")
    pdf.cell(24, row_height * 2, txt=jotsp[0][1], border=1, align="C")
    pdf.cell(24, row_height * 2, txt=jotsp[0][2], border=1, align="C")
    pdf.cell(54, row_height * 2, txt=jotsp[0][3], border=1, align="C")
    pdf.cell(74, row_height * 2, txt=jotsp[0][4], border=1, align="C")
    pdf.ln(row_height * 2)

    pdf.cell(24, row_height * spacing, txt=jotsp[1][0], border=1, align="C")
    pdf.cell(24, row_height * spacing, txt=jotsp[1][1], border=1, align="C")
    pdf.cell(24, row_height * spacing, txt=jotsp[1][2], border=1, align="C")
    pdf.cell(18, row_height * spacing, txt=jotsp[1][3], border=1, align="C")
    pdf.cell(18, row_height * spacing, txt=jotsp[1][4], border=1, align="C")
    pdf.cell(18, row_height * spacing, txt=jotsp[1][5], border=1, align="C")
    pdf.cell(18, row_height * spacing, txt=jotsp[1][6], border=1, align="C")
    pdf.cell(18, row_height * spacing, txt=jotsp[1][7], border=1, align="C")
    pdf.cell(18, row_height * spacing, txt=jotsp[1][8], border=1, align="C")
    pdf.cell(20, row_height * spacing, txt=jotsp[1][9], border=1, align="C")
    pdf.ln(row_height * spacing)

    pdf.cell(24, row_height * spacing, txt=jotsp[2][0], border=1)
    pdf.cell(24, row_height * spacing, txt=jotsp[2][1], border=1)
    pdf.cell(24, row_height * spacing, txt=jotsp[2][2], border=1)
    pdf.cell(18, row_height * spacing, txt=jotsp[2][3], border=1)
    pdf.cell(18, row_height * spacing, txt=jotsp[2][3], border=1)
    pdf.cell(18, row_height * spacing, txt=jotsp[2][3], border=1)
    pdf.cell(18, row_height * spacing, txt=jotsp[2][3], border=1)
    pdf.cell(18, row_height * spacing, txt=jotsp[2][3], border=1)
    pdf.cell(18, row_height * spacing, txt=jotsp[2][3], border=1)
    pdf.cell(20, row_height * spacing, txt=jotsp[2][3], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(200, row_height * spacing, txt=jotsp[3][0], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(200, 10, txt="3. Тест  ЛЮШЕРА", ln=1, align="C")

    lt = report_data.get_lusher_test_table()

    pdf.cell(24, row_height * spacing, txt=lt[0][0], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[0][1], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[0][2], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[0][3], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[0][4], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[0][5], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[0][6], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[0][7], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[0][8], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(24, row_height * spacing, txt=lt[1][0], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[1][1], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[1][2], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[1][3], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[1][4], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[1][5], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[1][6], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[1][7], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[1][8], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(24, row_height * spacing, txt=lt[2][0], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[2][1], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[2][2], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[2][3], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[2][4], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[2][5], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[2][6], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[2][7], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[2][8], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(24, row_height * spacing, txt=lt[3][0], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[3][1], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[3][2], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[3][3], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[3][4], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[3][5], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[3][6], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[3][7], border=1)
    pdf.cell(22, row_height * spacing, txt=lt[3][8], border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(
        200,
        12,
        txt="ПРИЗГАЧЕННЯ :    Інд. Заняття       ФЕС ____________      Нордична хода    ЗАЛ  ІР",
        ln=1,
    )

    pdf.ln(row_height * 3)

    pdf.cell(200, 10, txt="Надання  послуг: ", ln=1)

    for i in range(14):
        pdf.cell(14, 10, txt="", border=1)
    pdf.ln(row_height * spacing)

    pdf.cell(200, 10, txt=" ", ln=10)

    pdf.cell(
        200,
        10,
        txt="        Реабілітолог______________                   "
        + "                                                                              Лікар_________________",
        ln=1,
    )

    pdf.add_page()
    pdf.cell(200, 12, txt="Обследование", ln=1, align="C")

    exam = report_data.get_examination_table(
        yawleft=str(_yawleft),
        yawright=str(_yawright),
        rollleft=str(_rollleft),
        rollright=str(_rollright),
        pitchdown=str(_pitchdown),
        pitchup=str(_pitchup),
    )

    pdf.cell(200, row_height * spacing, txt=exam[0][0], border=1)
    pdf.ln(row_height * spacing)

    for i in range(1, 19):
        pdf.cell(5, row_height * spacing, txt=exam[i][0], border=1)
        pdf.cell(125, row_height * spacing, txt=exam[i][1], border=1)
        pdf.cell(15, row_height * spacing, txt=exam[i][2], border=1)
        pdf.cell(20, row_height * spacing, txt=exam[i][3], border=1)
        pdf.cell(15, row_height * spacing, txt=exam[i][4], border=1)
        pdf.cell(20, row_height * spacing, txt=exam[i][5], border=1)
        pdf.ln(row_height * spacing)

    pdf.cell(200, row_height * spacing, txt=exam[19][0], border=1)
    pdf.ln(row_height * spacing)

    for i in range(20, 29):
        pdf.cell(5, row_height * spacing, txt=exam[i][0], border=1)
        pdf.cell(125, row_height * spacing, txt=exam[i][1], border=1)
        pdf.cell(15, row_height * spacing, txt=exam[i][2], border=1)
        pdf.cell(20, row_height * spacing, txt=exam[i][3], border=1)
        pdf.cell(15, row_height * spacing, txt=exam[i][4], border=1)
        pdf.cell(20, row_height * spacing, txt=exam[i][5], border=1)
        pdf.ln(row_height * spacing)

    for i in range(29, 36):
        pdf.cell(200, row_height * spacing, txt=exam[i][0], border=1)
        pdf.ln(row_height * spacing)

    for i in range(36, 43):
        pdf.cell(5, row_height * spacing, txt=exam[i][0], border=1)
        pdf.cell(31, row_height * spacing, txt=exam[i][1], border=1)
        pdf.cell(8, row_height * spacing, txt=exam[i][2], border=1)
        pdf.cell(8, row_height * spacing, txt=exam[i][3], border=1)
        pdf.cell(8, row_height * spacing, txt=exam[i][4], border=1)
        pdf.cell(30, row_height * spacing, txt=exam[i][5], border=1)
        pdf.cell(35, row_height * spacing, txt=exam[i][6], border=1)
        pdf.cell(35, row_height * spacing, txt=exam[i][7], border=1)
        pdf.cell(40, row_height * spacing, txt=exam[i][8], border=1)
        pdf.ln(row_height * spacing)

    pdf.output(output_file)
