INSERT INTO SIMS_COLLEGE (COLLEGE_ID, COLLEGE_NAME, SHORT_NAME, INTRO, PROFESSION_NUMBER, STUDENT_NUMBER, PRESIDENT, TENANT_ID, REVISION, CREATED_BY, CREATED_TIME, UPDATED_BY, UPDATED_TIME) VALUES
('C0001', '计算机科学与技术学院', '计算机学院', '计算机学院介绍', 5, 150, '张院长', 'T0001', 1, 'Admin', '2023-09-07 10:00:00', 'Admin', '2023-09-07 10:00:00'),
('C0002', '电子工程学院', '电子学院', '电子学院介绍', 3, 80, '李院长', 'T0001', 1, 'Admin', '2023-09-07 10:00:00', 'Admin', '2023-09-07 10:00:00'),
('C0003', '化学与化工学院', '化学学院', '化学学院介绍', 4, 100, '王院长', 'T0001', 1, 'Admin', '2023-09-07 10:00:00', 'Admin', '2023-09-07 10:00:00'),
('C0004', '文学与新闻传播学院', '文新学院', '文新学院介绍', 6, 200, '赵院长', 'T0001', 1, 'Admin', '2023-09-07 10:00:00', 'Admin', '2023-09-07 10:00:00'),
('C0005', '经济与管理学院', '经管学院', '经管学院介绍', 5, 150, '孙院长', 'T0001', 1, 'Admin', '2023-09-07 10:00:00', 'Admin', '2023-09-07 10:00:00'),
('C0006', '数学与统计学院', '数学学院', '数学学院介绍', 3, 80, '钱院长', 'T0001', 1, 'Admin', '2023-09-07 10:00:00', 'Admin', '2023-09-07 10:00:00'),
('C0007', '艺术与设计学院', '艺术学院', '艺术学院介绍', 7, 250, '周院长', 'T0001', 1, 'Admin', '2023-09-07 10:00:00', 'Admin', '2023-09-07 10:00:00'),
('C0008', '法学与政治学院', '法政学院', '法政学院介绍', 4, 100, '吴院长', 'T0001', 1, 'Admin', '2023-09-07 10:00:00', 'Admin', '2023-09-07 10:00:00'),
('C0101', '物理学院', '物理学院', '物理学院介绍', 4, 90, '陈院长', 'T0001', 1, 'Admin', '2023-09-07 11:00:00', 'Admin', '2023-09-07 11:00:00'),
('C0102', '化学工程学院', '化学工程学院', '化学工程学院介绍', 6, 180, '杨院长', 'T0001', 1, 'Admin', '2023-09-07 11:00:00', 'Admin', '2023-09-07 11:00:00'),
('C0103', '外国语学院', '外语学院', '外语学院介绍', 5, 120, '吕院长', 'T0001', 1, 'Admin', '2023-09-07 11:00:00', 'Admin', '2023-09-07 11:00:00'),
('C0104', '历史与文化学院', '历史学院', '历史学院介绍', 3, 70, '孟院长', 'T0001', 1, 'Admin', '2023-09-07 11:00:00', 'Admin', '2023-09-07 11:00:00'),
('C0105', '地理与环境科学学院', '地环学院', '地环学院介绍', 7, 250, '徐院长', 'T0001', 1, 'Admin', '2023-09-07 11:00:00', 'Admin', '2023-09-07 11:00:00'),
('C0106', '医学院', '医学院', '医学院介绍', 8, 280, '高院长', 'T0001', 1, 'Admin', '2023-09-07 11:00:00', 'Admin', '2023-09-07 11:00:00'),
('C0107', '化学与材料学院', '化材学院', '化材学院介绍', 4, 95, '卢院长', 'T0001', 1, 'Admin', '2023-09-07 11:00:00', 'Admin', '2023-09-07 11:00:00'),
('C0108', '政治与国际关系学院', '政国际学院', '政国际学院介绍', 5, 130, '金院长', 'T0001', 1, 'Admin', '2023-09-07 11:00:00', 'Admin', '2023-09-07 11:00:00');


INSERT INTO SIMS_MAJOR (MAJOR_ID, MAJOR_NAME, SHORT_NAME, ESTAB_DATE, INTRO, TUITION_FEE, TENANT_ID, REVISION, CREATED_BY, CREATED_TIME, UPDATED_BY, UPDATED_TIME)
VALUES
('M0001', '计算机科学与技术', '计科', '2020-09-01 00:00:00', '这是计算机科学与技术专业的介绍', 8000.000000, 'T0001', 1, 'User1', '2023-09-07 10:00:00', 'User1', '2023-09-07 10:00:00'),
('M0002', '电子工程', '电工', '2019-08-15 00:00:00', '这是电子工程专业的介绍', 7500.500000, 'T0001', 1, 'User2', '2023-09-07 10:15:00', 'User2', '2023-09-07 10:15:00'),
('M0003', '化学工程', '化工', '2020-03-20 00:00:00', '这是化学工程专业的介绍', 8200.750000, 'T0001', 1, 'User3', '2023-09-07 10:30:00', 'User3', '2023-09-07 10:30:00'),
('M0004', '机械工程', '机械', '2021-01-10 00:00:00', '这是机械工程专业的介绍', 7800.250000, 'T0001', 1, 'User4', '2023-09-07 10:45:00', 'User4', '2023-09-07 10:45:00'),
('M0005', '经济学', '经济', '2019-09-05 00:00:00', '这是经济学专业的介绍', 7000.000000, 'T0001', 1, 'User5', '2023-09-07 11:00:00', 'User5', '2023-09-07 11:00:00'),
('M0006', '心理学', '心理', '2018-11-25 00:00:00', '这是心理学专业的介绍', 7200.750000, 'T0001', 1, 'User6', '2023-09-07 11:15:00', 'User6', '2023-09-07 11:15:00'),
('M0007', '建筑工程', '建筑', '2021-05-08 00:00:00', '这是建筑工程专业的介绍', 8300.500000, 'T0001', 1, 'User7', '2023-09-07 11:30:00', 'User7', '2023-09-07 11:30:00'),
('M0008', '生物学', '生物', '2019-03-12 00:00:00', '这是生物学专业的介绍', 7100.250000, 'T0001', 1, 'User8', '2023-09-07 11:45:00', 'User8', '2023-09-07 11:45:00'),
('M0009', '法学', '法学', '2020-08-03 00:00:00', '这是法学专业的介绍', 7800.000000, 'T0001', 1, 'User9', '2023-09-07 12:00:00', 'User9', '2023-09-07 12:00:00'),
('M0010', '文学', '文学', '2019-06-20 00:00:00', '这是文学专业的介绍', 6900.750000, 'T0001', 1, 'User10', '2023-09-07 12:15:00', 'User10', '2023-09-07 12:15:00'),
('M0011', '化学', '化学', '2021-02-15 00:00:00', '这是化学专业的介绍', 8200.500000, 'T0001', 1, 'User11', '2023-09-07 12:30:00', 'User11', '2023-09-07 12:30:00'),
('M0012', '医学', '医学', '2020-04-18 00:00:00', '这是医学专业的介绍', 8900.250000, 'T0001', 1, 'User12', '2023-09-07 12:45:00', 'User12', '2023-09-07 12:45:00'),
('M0013', '历史学', '历史', '2019-09-12 00:00:00', '这是历史学专业的介绍', 7000.000000, 'T0001', 1, 'User13', '2023-09-07 13:00:00', 'User13', '2023-09-07 13:00:00'),
('M0014', '物理学', '物理', '2021-03-25 00:00:00', '这是物理学专业的介绍', 8100.750000, 'T0001', 1, 'User14', '2023-09-07 13:15:00', 'User14', '2023-09-07 13:15:00'),
('M0015', '艺术学', '艺术', '2020-01-30 00:00:00', '这是艺术学专业的介绍', 7300.500000, 'T0001', 1, 'User15', '2023-09-07 13:30:00', 'User15', '2023-09-07 13:30:00'),
('M0016', '地理学', '地理', '2018-07-05 00:00:00', '这是地理学专业的介绍', 7000.250000, 'T0001', 1, 'User16', '2023-09-07 13:45:00', 'User16', '2023-09-07 13:45:00'),
('M0017', '政治学', '政治', '2021-06-28 00:00:00', '这是政治学专业的介绍', 7800.000000, 'T0001', 1, 'User17', '2023-09-07 14:00:00', 'User17', '2023-09-07 14:00:00'),
('M0018', '地质学', '地质', '2019-10-09 00:00:00', '这是地质学专业的介绍', 7100.750000, 'T0001', 1, 'User18', '2023-09-07 14:15:00', 'User18', '2023-09-07 14:15:00'),
('M0019', '音乐学', '音乐', '2020-02-14 00:00:00', '这是音乐学专业的介绍', 6900.500000, 'T0001', 1, 'User19', '2023-09-07 14:30:00', 'User19', '2023-09-07 14:30:00'),
('M0020', '社会学', '社会', '2021-04-22 00:00:00', '这是社会学专业的介绍', 7900.250000, 'T0001', 1, 'User20', '2023-09-07 14:45:00', 'User20', '2023-09-07 14:45:00');


INSERT INTO SIMS_CLASS (COLLEGE_ID, MAJOR_ID, CLASS_ID, CLASS_NAME, STUDENT_NUMBER, ADVISER, ESTAB_DATE, YEAR_NUMBER, TENANT_ID, REVISION, CREATED_BY, CREATED_TIME, UPDATED_BY, UPDATED_TIME) VALUES
('C0001', 'M0001', 'C0001', '计算机科学班', 30, '张老师', '2020-09-01 10:00:00', 4, 'T0001', 1, 'Admin', '2023-09-07 08:30:00', 'Admin', '2023-09-07 08:30:00'),
('C0002', 'M0002', 'C0002', '电子工程班', 25, '李老师', '2019-08-15 09:15:00', 3, 'T0001', 1, 'Admin', '2023-09-07 08:30:00', 'Admin', '2023-09-07 08:30:00'),
('C0003', 'M0003', 'C0003', '化学班', 28, '王老师', '2021-03-20 14:45:00', 4, 'T0001', 1, 'Admin', '2023-09-07 08:30:00', 'Admin', '2023-09-07 08:30:00'),
('C0004', 'M0004', 'C0004', '机械工程班', 32, '陈老师', '2020-10-10 11:30:00', 4, 'T0001', 1, 'Admin', '2023-09-07 08:30:00', 'Admin', '2023-09-07 08:30:00'),
('C0005', 'M0005', 'C0005', '英语班', 20, '刘老师', '2019-11-25 13:20:00', 3, 'T0001', 1, 'Admin', '2023-09-07 08:30:00', 'Admin', '2023-09-07 08:30:00'),
('C0006', 'M0006', 'C0006', '数学班', 26, '赵老师', '2021-02-05 10:45:00', 4, 'T0001', 1, 'Admin', '2023-09-07 08:30:00', 'Admin', '2023-09-07 08:30:00'),
('C0007', 'M0007', 'C0007', '物理班', 22, '黄老师', '2020-12-30 15:10:00', 4, 'T0001', 1, 'Admin', '2023-09-07 08:30:00', 'Admin', '2023-09-07 08:30:00');
