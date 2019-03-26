import pymysql


def insert(json1,json2):
    db = pymysql.connect("localhost", "root", "123456", "sql_db")
    cursor = db.cursor()
    sql_delete = "DELETE FROM REPORT_DETAIL WHERE REPORT_ID = '1'"
    try:
        cursor.execute(sql_delete)
        print("commit delete")
        db.commit()
    except:
        db.rollback()
        print("rollback delete")
    a_size_fb = json1["手术"]["右叶"]["大小"]["前后径"]
    a_size_lr = json1["手术"]["右叶"]["大小"]["左右径"]
    a_shape = json1["手术"]["右叶"]["形态"]
    a_echo = json1["手术"]["右叶"]["回声"]
    a_echo_division = json1["手术"]["右叶"]["回声分布"]
    a_edge = json1["手术"]["右叶"]["边界"]
    a_surface = json1["手术"]["右叶"]["表面"]
    a_envelop = json1["手术"]["右叶"]["包膜"]
    a_cdfi = json1["手术"]["右叶"]["CDFI"]
    print(json1["手术"]["右叶"]["大小"]["前后径"])
    sql_insert_normal_info_a = "INSERT INTO normal_info (size_FB, size_LR, shape, echo, echo_division, edge, surface,\
                                envelope, cdfi) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (a_size_fb,\
                                a_size_lr, a_shape, a_echo, a_echo_division, a_edge, a_surface, a_envelop, a_cdfi)
    try:
        cursor.execute(sql_insert_normal_info_a)
        print("commit normal_info_a")
        db.commit()
    except:
        db.rollback()
        print("rollback normal_info_a")

    cursor.execute("SELECT normal_id FROM normal_info order by normal_id desc limit 1")
    normal_right = cursor.fetchone()
    #normal_right[0] 是report_detail表中normal_right的值

    b_size_fb = json1["手术"]["左叶"]["大小"]["前后径"]
    b_size_lr = json1["手术"]["左叶"]["大小"]["左右径"]
    b_shape = json1["手术"]["左叶"]["形态"]
    b_echo = json1["手术"]["左叶"]["回声"]
    b_echo_division = json1["手术"]["左叶"]["回声分布"]
    b_edge = json1["手术"]["左叶"]["边界"]
    b_surface = json1["手术"]["左叶"]["表面"]
    b_envelop = json1["手术"]["左叶"]["包膜"]
    b_cdfi = json1["手术"]["左叶"]["CDFI"]
    print(json1["手术"]["左叶"]["大小"]["前后径"])
    sql_insert_normal_info_b = "INSERT INTO normal_info (size_FB, size_LR, shape, echo, echo_division, edge, surface,\
                                    envelope, cdfi) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (b_size_fb, \
                                     b_size_lr, b_shape, b_echo, b_echo_division, b_edge, b_surface, b_envelop, b_cdfi)
    try:
        cursor.execute(sql_insert_normal_info_b)
        print("commit normal_info_b")
        db.commit()
    except:
        db.rollback()
        print("rollback normal_info_b")

    cursor.execute("SELECT normal_id FROM normal_info order by normal_id desc limit 1")
    normal_left = cursor.fetchone()
    # normal_left[0]

    l_change_positon = json2["左侧"]["位置补充"]
    l_change_type = json2["左侧"]["多发结节类型"]
    l_change_num = json2["左侧"]["个数"]
    l_change_size = json2["左侧"]["大小"]
    l_change_grow = json2["左侧"]["生长"]
    l_change_shape = json2["左侧"]["形状"]
    l_change_edge = json2["左侧"]["边缘"]
    l_change_boundary = json2["左侧"]["边界"]
    l_change_echo_inside = json2["左侧"]["内部回声"]
    l_change_structure = json2["左侧"]["内部结构"]
    l_change_echo_back = json2["左侧"]["后方回声"]
    l_change_cdfi = json2["左侧"]["CDFI/CFI"]
    l_change_calcification = json2["左侧"]["钙化"]
    l_change_echo_strong = json2["左侧"]["强回声"]
    l_change_sound = json2["左侧"]["声影"]
    l_change_halo = json2["左侧"]["声晕"]
    l_change_supplement = json2["左侧"]["补充"]
    sql_insert_change_info_l = "INSERT INTO change_info (position, type, num, size,\
     grow,shape, edge, boundary, echo_inside, structure, echo_back, cdfi, calcification, echo_strong,\
     sound, halo, supplement) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                               % (l_change_positon, l_change_type, l_change_num, l_change_size, l_change_grow,
                                  l_change_shape, l_change_edge, l_change_boundary, l_change_echo_inside,
                                  l_change_structure, l_change_echo_back, l_change_cdfi, l_change_calcification,
                                  l_change_echo_strong, l_change_sound, l_change_halo, l_change_supplement)

    try:
        cursor.execute(sql_insert_change_info_l)
        print("commit change_info_l")
        db.commit()
    except:
        db.rollback()
        print("rollback change_info_l")

    cursor.execute("SELECT change_id FROM change_info order by change_id desc limit 1")
    change_left = cursor.fetchone()
    # change_left[0]

    r_change_positon = json2["右侧"]["位置补充"]
    r_change_type = json2["右侧"]["多发结节类型"]
    r_change_num = json2["右侧"]["个数"]
    r_change_size = json2["右侧"]["大小"]
    r_change_grow = json2["右侧"]["生长"]
    r_change_shape = json2["右侧"]["形状"]
    r_change_edge = json2["右侧"]["边缘"]
    r_change_boundary = json2["右侧"]["边界"]
    r_change_echo_inside = json2["右侧"]["内部回声"]
    r_change_structure = json2["右侧"]["内部结构"]
    r_change_echo_back = json2["右侧"]["后方回声"]
    r_change_cdfi = json2["右侧"]["CDFI/CFI"]
    r_change_calcification = json2["右侧"]["钙化"]
    r_change_echo_strong = json2["右侧"]["强回声"]
    r_change_sound = json2["右侧"]["声影"]
    r_change_halo = json2["右侧"]["声晕"]
    r_change_supplement = json2["右侧"]["补充"]
    sql_insert_change_info_r = "INSERT INTO change_info (position, type, num, size,\
     grow,shape, edge, boundary, echo_inside, structure, echo_back, cdfi, calcification, echo_strong,\
     sound, halo, supplement) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                               % (r_change_positon, r_change_type, r_change_num, r_change_size, r_change_grow,
                                  r_change_shape, r_change_edge, r_change_boundary, r_change_echo_inside,
                                  r_change_structure, r_change_echo_back, r_change_cdfi, r_change_calcification,
                                  r_change_echo_strong, r_change_sound, r_change_halo, r_change_supplement)

    try:
        cursor.execute(sql_insert_change_info_r)
        print("commit change_info_r")
        db.commit()
    except:
        db.rollback()
        print("rollback change_info_r")

    cursor.execute("SELECT change_id FROM change_info order by change_id desc limit 1")
    change_right = cursor.fetchone()
    # change_right[0]

    t_change_positon = json2["峡部"]["位置补充"]
    t_change_type = json2["峡部"]["多发结节类型"]
    t_change_num = json2["峡部"]["个数"]
    t_change_size = json2["峡部"]["大小"]
    t_change_grow = json2["峡部"]["生长"]
    t_change_shape = json2["峡部"]["形状"]
    t_change_edge = json2["峡部"]["边缘"]
    t_change_boundary = json2["峡部"]["边界"]
    t_change_echo_inside = json2["峡部"]["内部回声"]
    t_change_structure = json2["峡部"]["内部结构"]
    t_change_echo_back = json2["峡部"]["后方回声"]
    t_change_cdfi = json2["峡部"]["CDFI/CFI"]
    t_change_calcification = json2["峡部"]["钙化"]
    t_change_echo_strong = json2["峡部"]["强回声"]
    t_change_sound = json2["峡部"]["声影"]
    t_change_halo = json2["峡部"]["声晕"]
    t_change_supplement = json2["峡部"]["补充"]
    sql_insert_change_info_t = "INSERT INTO change_info (position, type, num, size,\
     grow,shape, edge, boundary, echo_inside, structure, echo_back, cdfi, calcification, echo_strong,\
     sound, halo, supplement) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                               % (t_change_positon, t_change_type, t_change_num, t_change_size, t_change_grow,
                                  t_change_shape, t_change_edge, t_change_boundary, t_change_echo_inside,
                                  t_change_structure, t_change_echo_back, t_change_cdfi, t_change_calcification,
                                  t_change_echo_strong, t_change_sound, t_change_halo, t_change_supplement)

    try:
        cursor.execute(sql_insert_change_info_t)
        print("commit change_info_t")
        db.commit()
    except:
        db.rollback()
        print("rollback _change_info_t")

    cursor.execute("SELECT change_id FROM change_info order by change_id desc limit 1")
    change_thickness = cursor.fetchone()
    # change_thickness[0]

    size_thickness = json1['手术']['峡部']
    print(size_thickness, normal_right[0], normal_left[0], change_left[0],\
                        change_right[0], change_thickness[0])
    # sql_insert_report = "INSERT INTO report_detail(report_id, patient_id, department_name, check_item, machine_number,\
    #                     check_number, clinic_number, size_thickness,\
    #                     normal_right, normal_left, change_left, change_right, change_thickness) values ('%s','%s','%s',\
    #                     '%s', '%s', '%s', '%s','%s', '%d', '%d','%d','%d','%d')" % ('1', 'temp', '门诊', '超声', '1', 'xxx',
    #                                                                                 'clinic_num', size_thickness,
    #                                                                                 normal_right[0], normal_left[0],
    #                                                                                 change_left[0], change_right[0],
    #                                                                                 change_thickness[0])
    sql_insert_report = "INSERT INTO REPORT_DETAIL(report_id, patient_id, department_name, check_item, machine_number,\
    check_number, clinic_number, size_thickness,normal_right, normal_left, change_left, change_right, change_thickness)\
     VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%d','%d','%d','%d','%d')" % ('1', 'temp', '门诊', '超声', '1', \
                                        'check number', 'clinic number', size_thickness, normal_right[0], normal_left[0],\
                                        change_left[0], change_right[0], change_thickness[0])
    try:
        cursor.execute(sql_insert_report)
        print("commit insert_report")
        db.commit()
    except:
        db.rollback()
        print("rollback insert_report")

    # print(json1, json2)


