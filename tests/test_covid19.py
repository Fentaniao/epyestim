import unittest

import pandas as pd
import numpy as np
from numpy.testing import assert_array_almost_equal

from epyestim.covid19 import r_covid, generate_onset_to_reporting_distribution_singapore


class CovidTest(unittest.TestCase):
    def test_r_covid(self):
        np.random.seed(5764)

        confirmed_cases = pd.Series([
            1, 0, 7, 0, 10, 9,
            15, 14, 34, 24, 100, 54, 69, 37, 117, 161, 0, 487, 220, 841,
            0, 500, 328, 1047, 1219, 1281, 899, 1321, 1082, 1020, 914,
            1117, 1148, 753, 1093, 683, 1163, 1059, 779, 899, 595, 557,
            596, 1027, 771, 500, 556, 308, 273, 248, 400, 396, 346, 326,
            336, 204, 119, 205, 228, 181, 217, 167, 103, 100, 143, 179,
            119, 112, 88, 76, 28, 51, 66, 81, 44, 54, 39, 36, 33, 50, 51,
            58, 15, 10, 21, 40, 36, 13, 18, 11, 10, 15, 15, 20, 32, 17,
            17, 9, 3, 19, 20, 23, 20, 9, 7, 16, 23, 33, 19, 31, 23, 14,
            23, 33, 13, 35, 8, 49, 18, 22, 44, 52, 58, 69, 62, 35, 62,
            137, 116, 134, 97, 70, 47, 54, 129, 88, 104, 127, 66, 63,
            70, 132, 142, 92, 110, 99, 43, 108, 141, 117, 154, 148, 110,
            65, 132, 193, 220, 210, 180, 138, 66, 130, 181, 181, 161,
            182, 152, 105, 187, 274, 234, 268, 253, 200, 128, 197, 311,
            266, 306, 295, 276, 157, 202, 383, 361, 340, 376, 292, 163,
            216, 370, 364, 405, 425, 444, 191, 245, 469, 405, 528, 465,
            475, 257, 315, 514, 530, 488, 0, 0, 1095, 286, 437, 391, 372,
            0, 0, 782, 225, 411, 550, 552, 0, 0, 1548, 700, 1077, 1172,
            1487, 0, 0, 4068, 1445, 2823, 2613, 3105, 0, 0, 8737, 3008,
            5596, 5256, 6634, 0, 0, 17440, 5949, 8616, 9386, 9207, 0, 0,
            21926, 6126, 10073, 10128, 9409, 0, 0, 17309
        ], index=pd.date_range('2020-02-25', '2020-11-09'))

        result = r_covid(
            confirmed_cases=confirmed_cases,
            delay_distribution=generate_onset_to_reporting_distribution_singapore(),
            quantiles=[0.5]
        )

        self.assertTrue(result.index.equals(pd.date_range('2020-03-01', '2020-11-03')))

        expected_result = [
            4.58, 3.39, 2.63, 2.31, 2.25, 2.33, 2.36, 2.31, 2.23, 2.17,
            2.14, 2.12, 2.07, 1.97, 1.83, 1.67, 1.52, 1.39, 1.28, 1.20,
            1.13, 1.07, 1.02, 0.97, 0.92, 0.88, 0.85, 0.83, 0.82, 0.81,
            0.81, 0.81, 0.81, 0.80, 0.78, 0.75, 0.73, 0.71, 0.70, 0.70,
            0.70, 0.70, 0.70, 0.69, 0.68, 0.68, 0.69, 0.72, 0.75, 0.77,
            0.78, 0.77, 0.75, 0.74, 0.74, 0.74, 0.74, 0.74, 0.73, 0.71,
            0.70, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.70, 0.73, 0.76,
            0.79, 0.82, 0.83, 0.82, 0.81, 0.80, 0.78, 0.77, 0.76, 0.76,
            0.76, 0.79, 0.82, 0.87, 0.91, 0.93, 0.96, 1.00, 1.04, 1.09,
            1.11, 1.11, 1.12, 1.12, 1.14, 1.16, 1.19, 1.22, 1.24, 1.23,
            1.22, 1.19, 1.18, 1.18, 1.18, 1.19, 1.19, 1.22, 1.26, 1.32,
            1.38, 1.44, 1.49, 1.53, 1.57, 1.58, 1.56, 1.50, 1.41, 1.31,
            1.22, 1.15, 1.11, 1.08, 1.06, 1.03, 1.00, 0.98, 0.97, 0.98,
            1.00, 1.03, 1.05, 1.06, 1.07, 1.07, 1.09, 1.10, 1.11, 1.12,
            1.13, 1.14, 1.15, 1.17, 1.19, 1.20, 1.19, 1.15, 1.11, 1.07,
            1.05, 1.05, 1.04, 1.04, 1.04, 1.04, 1.06, 1.08, 1.11, 1.15,
            1.17, 1.17, 1.17, 1.16, 1.16, 1.16, 1.15, 1.14, 1.12, 1.10,
            1.08, 1.08, 1.09, 1.10, 1.10, 1.09, 1.08, 1.06, 1.06, 1.07,
            1.09, 1.10, 1.09, 1.08, 1.08, 1.07, 1.09, 1.10, 1.11, 1.11,
            1.09, 1.07, 1.04, 1.01, 0.99, 0.98, 0.98, 0.98, 0.97, 0.96,
            0.94, 0.91, 0.91, 0.91, 0.94, 0.97, 1.01, 1.05, 1.09, 1.15,
            1.23, 1.34, 1.47, 1.57, 1.62, 1.64, 1.65, 1.68, 1.72, 1.74,
            1.71, 1.64, 1.57, 1.52, 1.52, 1.54, 1.56, 1.55, 1.51, 1.46,
            1.42, 1.41, 1.42, 1.43, 1.40, 1.35, 1.28, 1.22, 1.18, 1.16,
            1.15, 1.12, 1.08, 1.03, 0.99, 0.98, 0.98, 0.99
        ]

        assert_array_almost_equal(expected_result, result['Q0.5'], 2)

    def test_r_covid_cutoff(self):

        np.random.seed(5764)

        confirmed_cases = pd.Series([
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 1, 0,
             7, 0, 10, 9, 15, 14, 34, 24, 100,
             54, 69, 37, 117, 161, 0, 487, 220, 841,
             0, 500, 328, 1047, 1219, 1281, 899, 1321, 1082,
             1020, 914, 1117, 1148, 753, 1093, 683, 1163, 1059,
             779, 899, 595, 557, 596, 1027, 771, 500, 556,
             308, 273, 248, 400, 396, 346, 326, 336, 204,
             119, 205, 228, 181, 217, 167, 103, 100, 143,
             179, 119, 112, 88, 76, 28, 51, 66, 81,
             44, 54, 39, 36, 33, 50, 51, 58, 15,
             10, 21, 40, 36, 13, 18, 11, 10, 15,
             15, 20, 32, 17, 17, 9, 3, 19, 20,
             23, 20, 9, 7, 16, 23, 33, 19, 31,
             23, 14, 23, 33, 13, 35, 8, 49, 18,
             22, 44, 52, 58, 69, 62, 35, 62, 137,
             116, 134, 97, 70, 47, 54, 129, 88, 104,
             127, 66, 63, 70, 132, 142, 92, 110, 99,
             43, 108, 141, 117, 154, 148, 110, 65, 132,
             193, 220, 210, 180, 138, 66, 130, 181, 181,
             161, 182, 152, 105, 187, 274, 234, 268, 253,
             200, 128, 197, 311, 266, 306, 295, 276, 157,
             202, 383, 361, 340, 376, 292, 163, 216, 370,
             364, 405, 425, 444, 191, 245, 469, 405, 528,
             465, 475, 257, 315, 514, 530, 488, 0, 0,
             1095, 286, 437, 391, 372, 0, 0, 782, 225,
             411, 550, 552, 0, 0, 1548, 700, 1077, 1172,
             1487, 0, 0, 4068, 1445, 2823, 2613, 3105, 0,
             0, 8737, 3008, 5596, 5256, 6634, 0, 0, 17440,
             5949, 8616, 9386, 9207, 0, 0, 21926, 6126, 10073,
             10128, 9409, 0, 0, 17309
        ], index=pd.date_range('2020-01-22', periods=293))

        result = r_covid(
            confirmed_cases=confirmed_cases,
            delay_distribution=generate_onset_to_reporting_distribution_singapore(),
            quantiles=[0.5]
        )

        expected_result = [
             2.59960214, 2.42713596, 2.36801365, 2.44343708, 2.54371424,
             2.59963764, 2.53764468, 2.39790211, 2.25661617, 2.1689964,
             2.13205504, 2.10722693, 2.05398289, 1.96185502, 1.82583515,
             1.67238124, 1.52266781, 1.39083715, 1.28338702, 1.19770325,
             1.12809483, 1.06886891, 1.01726886, 0.96890564, 0.92362263,
             0.88377431, 0.85152062, 0.82804287, 0.81421856, 0.80843819,
             0.80883319, 0.80933912, 0.80606134, 0.79563434, 0.77692084,
             0.7529111, 0.72841375, 0.70834919, 0.69675028, 0.69548764,
             0.69848636, 0.70033662, 0.6964799, 0.68619966, 0.67762849,
             0.67691045, 0.69190406, 0.71940879, 0.75094328, 0.77253703,
             0.77903016, 0.77054792, 0.75845293, 0.74712806, 0.74087147,
             0.73948702, 0.74120346, 0.73805086, 0.72855332, 0.71533214,
             0.70149376, 0.6932034, 0.68991684, 0.68851331, 0.68835197,
             0.68483663, 0.68632654, 0.70099351, 0.72582877, 0.76086942,
             0.79663442, 0.81960689, 0.82568108, 0.82178255, 0.80762545,
             0.79448565, 0.78327463, 0.77209426, 0.76407495, 0.76222464,
             0.7704921, 0.79284348, 0.82959292, 0.86446548, 0.89962207,
             0.9311943, 0.9579237, 0.98441243, 1.0352803, 1.08957905,
             1.11678579, 1.12860319, 1.12464211, 1.11692886, 1.12750097,
             1.15296689, 1.1838994, 1.22107088, 1.23894021, 1.2328738,
             1.21126435, 1.19421602, 1.18040038, 1.17694589, 1.18363591,
             1.19113706, 1.19995364, 1.22028044, 1.26160559, 1.32272207,
             1.38064407, 1.44175695, 1.48599467, 1.52381945, 1.55364961,
             1.57350822, 1.55720066, 1.49823225, 1.40417142, 1.3034397,
             1.21622314, 1.14951094, 1.10627253, 1.07663047, 1.05578566,
             1.03038797, 1.00369567, 0.98196295, 0.97145419, 0.97741591,
             0.99761393, 1.02539234, 1.05030807, 1.06660386, 1.07399873,
             1.08003171, 1.08947449, 1.10413773, 1.11814489, 1.12648959,
             1.13177592, 1.13838639, 1.15194605, 1.17238448, 1.19432446,
             1.20100826, 1.18565284, 1.15206383, 1.11238385, 1.07845761,
             1.05709792, 1.04774574, 1.04638855, 1.04756145, 1.04612918,
             1.0469924, 1.05948666, 1.07980256, 1.11200442, 1.14287345,
             1.16462608, 1.17054932, 1.16668208, 1.15999564, 1.15751063,
             1.15835069, 1.15497534, 1.14132904, 1.11762787, 1.0956717,
             1.08353587, 1.08382907, 1.09196015, 1.10182822, 1.10281747,
             1.091496, 1.07380952, 1.06056518, 1.05967571, 1.06934734,
             1.08446026, 1.09413929, 1.09177153, 1.08346686, 1.07614132,
             1.0780672, 1.08780339, 1.10104586, 1.11195392, 1.10750554,
             1.09311454, 1.07002757, 1.03841093, 1.00912397, 0.98801527,
             0.97950988, 0.97873168, 0.97970125, 0.97381753, 0.95784123,
             0.93552611, 0.91356957, 0.90312199, 0.90995052, 0.93441949,
             0.97278021, 1.01274102, 1.05082948, 1.09286146, 1.14838029,
             1.2297979, 1.34413185, 1.47177478, 1.57404505, 1.62573053,
             1.64020524, 1.65240012, 1.68002175, 1.71706891, 1.7367423,
             1.70830268, 1.64205551, 1.56982027, 1.52576074, 1.5187258,
             1.54104773, 1.5622353, 1.55376551, 1.51205394, 1.45996614,
             1.42411088, 1.4130697, 1.42072672, 1.42542989, 1.40307067,
             1.351099, 1.28347502, 1.22232452, 1.18062028, 1.15925023,
             1.14822265, 1.12199702, 1.07887335, 1.02846493, 0.99358597,
             0.97897602, 0.98055132, 0.99108749
        ]

        assert_array_almost_equal(expected_result, result['Q0.5'], 1)

    def test_r_covid_nocutoff(self):
        np.random.seed(5764)

        confirmed_cases = pd.Series([
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 1, 0,
            7, 0, 10, 9, 15, 14, 34, 24, 100,
            54, 69, 37, 117, 161, 0, 487, 220, 841,
            0, 500, 328, 1047, 1219, 1281, 899, 1321, 1082,
            1020, 914, 1117, 1148, 753, 1093, 683, 1163, 1059,
            779, 899, 595, 557, 596, 1027, 771, 500, 556,
            308, 273, 248, 400, 396, 346, 326, 336, 204,
            119, 205, 228, 181, 217, 167, 103, 100, 143,
            179, 119, 112, 88, 76, 28, 51, 66, 81,
            44, 54, 39, 36, 33, 50, 51, 58, 15,
            10, 21, 40, 36, 13, 18, 11, 10, 15,
            15, 20, 32, 17, 17, 9, 3, 19, 20,
            23, 20, 9, 7, 16, 23, 33, 19, 31,
            23, 14, 23, 33, 13, 35, 8, 49, 18,
            22, 44, 52, 58, 69, 62, 35, 62, 137,
            116, 134, 97, 70, 47, 54, 129, 88, 104,
            127, 66, 63, 70, 132, 142, 92, 110, 99,
            43, 108, 141, 117, 154, 148, 110, 65, 132,
            193, 220, 210, 180, 138, 66, 130, 181, 181,
            161, 182, 152, 105, 187, 274, 234, 268, 253,
            200, 128, 197, 311, 266, 306, 295, 276, 157,
            202, 383, 361, 340, 376, 292, 163, 216, 370,
            364, 405, 425, 444, 191, 245, 469, 405, 528,
            465, 475, 257, 315, 514, 530, 488, 0, 0,
            1095, 286, 437, 391, 372, 0, 0, 782, 225,
            411, 550, 552, 0, 0, 1548, 700, 1077, 1172,
            1487, 0, 0, 4068, 1445, 2823, 2613, 3105, 0,
            0, 8737, 3008, 5596, 5256, 6634, 0, 0, 17440,
            5949, 8616, 9386, 9207, 0, 0, 21926, 6126, 10073,
            10128, 9409, 0, 0, 17309
        ], index=pd.date_range('2020-01-22', periods=293))

        result = r_covid(
            confirmed_cases=confirmed_cases,
            delay_distribution=generate_onset_to_reporting_distribution_singapore(),
            quantiles=[0.5],
            auto_cutoff=False
        )

        expected_result = [
            2.67477027, 2.67503516, 2.6765143, 2.67579242, 2.67435824,
            2.67366014, 2.67228503, 2.66813883, 2.6664331, 2.6652005,
            2.66429812, 2.66335013, 2.66284292, 2.66251748, 2.66227333,
            2.66208566, 2.66193987, 2.66182693, 2.66174034, 2.66167415,
            2.66162277, 2.66158126, 2.66154595, 2.6615145, 2.66148555,
            2.66145828, 2.66143207, 2.66140636, 2.66138063, 2.66135445,
            2.66132749, 2.66129945, 2.66127012, 2.66123926, 2.66120667,
            2.66117211, 2.66113535, 2.66109615, 2.66105427, 2.66100944,
            2.66096143, 2.66091003, 2.66085507, 2.66079652, 2.66073461,
            2.66067002, 2.66060435, 2.66054096, 2.66048679, 2.66045644,
            2.67614386, 2.7108038, 2.83118877, 3.1042558, 3.68530514,
            4.35559035, 5.04091675, 5.13439037, 4.97294146, 4.60022336,
            4.32381273, 4.15238163, 3.95815843, 3.64616716, 3.25072948,
            2.86789867, 2.58790988, 2.40624555, 2.36336113, 2.43122115,
            2.5517192, 2.61249985, 2.55187515, 2.40775645, 2.26543759,
            2.1748591, 2.13355022, 2.10867727, 2.05863056, 1.96163533,
            1.82530735, 1.67031715, 1.52064704, 1.38938483, 1.28345626,
            1.19752334, 1.12879877, 1.07047999, 1.01775681, 0.96921463,
            0.92384124, 0.88419972, 0.8517323, 0.8292913, 0.81584407,
            0.81023121, 0.80962284, 0.81023937, 0.80666367, 0.79532552,
            0.77620566, 0.75220246, 0.72783173, 0.70802502, 0.69637919,
            0.69447679, 0.69777129, 0.69951439, 0.69494705, 0.68466738,
            0.67563275, 0.67604472, 0.69116822, 0.7182239, 0.74793807,
            0.77107427, 0.77786591, 0.77073115, 0.75651137, 0.74430292,
            0.74023878, 0.74090278, 0.74357078, 0.74070345, 0.73076076,
            0.71651026, 0.70347542, 0.69707372, 0.69417504, 0.6939483,
            0.6904897, 0.68724005, 0.68965708, 0.70387242, 0.72932035,
            0.76480186, 0.79972799, 0.82366336, 0.83548514, 0.83009186,
            0.81643837, 0.80137085, 0.79045859, 0.77531069, 0.76687918,
            0.75689582, 0.7626225, 0.78268831, 0.81589598, 0.86016739,
            0.89777442, 0.92513174, 0.95368902, 0.98245474, 1.02422849,
            1.0720807, 1.10172552, 1.12151048, 1.12211188, 1.12466465,
            1.13778321, 1.17198166, 1.21107023, 1.23399194, 1.25013563,
            1.24622543, 1.2246863, 1.1966561, 1.17677295, 1.1683622,
            1.16829106, 1.16966643, 1.18121422, 1.216796, 1.25843665,
            1.31860528, 1.38342143, 1.43735377, 1.48825321, 1.53837247,
            1.57611169, 1.59427906, 1.57625857, 1.50407531, 1.4114242,
            1.30777339, 1.21785231, 1.1483579, 1.10339699, 1.073178,
            1.04985157, 1.02278093, 0.99686965, 0.97518828, 0.9649719,
            0.97218441, 0.99343942, 1.02322904, 1.05119824, 1.0672097,
            1.07560888, 1.08483366, 1.09561559, 1.11116362, 1.12594634,
            1.13290766, 1.1358046, 1.14119706, 1.15404562, 1.17399877,
            1.19052873, 1.19803373, 1.18093141, 1.14880997, 1.10945235,
            1.07616391, 1.05655333, 1.04871199, 1.04626317, 1.04602325,
            1.04599882, 1.04823371, 1.05977679, 1.08163564, 1.11232095,
            1.14319732, 1.16564725, 1.17245079, 1.16769217, 1.1595463,
            1.15453526, 1.15341571, 1.14944612, 1.13429736, 1.11286179,
            1.09308897, 1.08169637, 1.08271208, 1.09263419, 1.10108366,
            1.09991749, 1.08918355, 1.071548, 1.05982829, 1.06094269,
            1.0708761, 1.0867783, 1.09556559, 1.09437084, 1.08470383,
            1.07682695, 1.07828595, 1.09023204, 1.10613722, 1.11361135,
            1.11099465, 1.09554854, 1.07089245, 1.03988541, 1.00988064,
            0.9877387, 0.97851494, 0.97784726, 0.97785721, 0.97244106,
            0.9559814, 0.9343946, 0.91350672, 0.90262225, 0.90806148,
            0.93136364, 0.96965116, 1.01099082, 1.05055134, 1.0923185,
            1.14719598, 1.22791172, 1.34454711, 1.47256076, 1.57461365,
            1.62729981, 1.64250724, 1.65486926, 1.68094092, 1.71830115,
            1.73620819, 1.70866107, 1.64266513, 1.57038994, 1.52541715,
            1.5179016, 1.54061814, 1.56221099, 1.55393005, 1.51256916,
            1.46091186, 1.42532821, 1.41459374, 1.42245536, 1.42605668,
            1.40455494, 1.35217455, 1.28428105, 1.22288593, 1.18084635,
            1.15927059, 1.14800207, 1.12161591, 1.07839483, 1.02805631,
            0.9935213, 0.97856653, 0.98022276, 0.99093923, 1.00323912,
            1.01250703, 1.01710474, 1.01631484, 1.01205281, 1.006433
        ]

        assert_array_almost_equal(expected_result, result['Q0.5'], 1)


if __name__ == '__main__':
    unittest.main()
