#add parent dir to find package. Only needed for source code build, pip install doesn't need it.
import os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
os.sys.path.insert(0,parentdir)

import gym
import numpy as np
import pybullet as p
import pybullet_envs
import time

def relu(x):
    return np.maximum(x, 0)

class SmallReactivePolicy:
    "Simple multi-layer perceptron policy, no internal state"
    def __init__(self, observation_space, action_space):
        assert weights_dense1_w.shape == (observation_space.shape[0], 64)
        assert weights_dense2_w.shape == (64, 32)
        assert weights_final_w.shape  == (32, action_space.shape[0])

    def act(self, ob):
        x = ob
        x = relu(np.dot(x, weights_dense1_w) + weights_dense1_b)
        x = relu(np.dot(x, weights_dense2_w) + weights_dense2_b)
        x = np.dot(x, weights_final_w) + weights_final_b
        return x

def main():
    print("create env")
    env = gym.make("InvertedPendulumBulletEnv-v0")
    env.render(mode="human")
    pi = SmallReactivePolicy(env.observation_space, env.action_space)

    while 1:
        frame = 0
        score = 0
        restart_delay = 0
        obs = env.reset()
        print("frame")
        while 1:
            time.sleep(0.05)
            a = pi.act(obs)
            obs, r, done, _ = env.step(a)
            score += r
            frame += 1
            still_open = env.render("human")
            if still_open==False:
                return
            if not done: continue
            if restart_delay==0:
                print("score=%0.2f in %i frames" % (score, frame))
                restart_delay = 60*2  # 2 sec at 60 fps
            else:
                restart_delay -= 1
                if restart_delay==0: break

weights_dense1_w = np.array([
[ +0.8621, +0.3260, +0.0986, -0.1225, +0.2038, -0.8051, -0.7498, +0.1905, -0.3418, +0.5002, -0.1093, +0.0285, +0.3480, -0.1596, -0.1781, +0.3643, -0.4283, -0.3715, -0.1571, +0.3531, +0.0934, -0.2215, -0.3085, +0.9581, +0.2485, -0.6232, -0.3175, +0.9771, +0.3651, -0.8850, -0.4212, -0.0301, +0.0432, +0.3390, +0.7537, +0.1649, -0.0128, -0.1374, +0.3793, +1.0430, +0.8043, -0.9001, +0.4334, -0.1243, +1.2373, +0.1890, +0.3333, -0.0520, +0.1654, +0.2521, -0.0168, +0.8439, -0.6960, +0.1884, +0.0991, +0.5242, -0.6837, +0.6844, -0.2593, -0.3298, +0.2212, +0.0281, +0.2608, +0.6527],
[ -0.9350, -0.2122, +0.0162, +0.5306, -0.2914, -0.8573, +0.2552, +0.7069, +0.7862, -0.0315, -1.0844, +0.2707, +0.5102, -1.1359, +0.3066, +0.0357, +0.1833, -0.1946, +0.0948, +0.6685, -0.6101, +0.4774, -0.3017, +0.3823, -0.2835, -0.6760, +1.2963, +0.4466, -0.7132, -0.9109, -0.0589, -0.8726, +0.6972, -0.2256, -0.0286, +0.4646, -0.5113, -0.1692, +0.7638, +0.2274, -0.5734, +0.7430, +0.9680, +0.7809, -0.2457, -0.4952, +0.0197, -0.6428, +0.2367, -0.5887, -0.5167, +0.2299, -0.5853, -0.4101, +0.9042, +0.0913, +0.5774, +0.2756, +0.2436, -0.6068, -0.2232, -0.1415, -0.5094, -0.1012],
[ +0.0983, -0.3266, +0.2611, +0.0664, +0.6222, +0.0773, -0.2516, -0.4416, -0.3770, +0.0535, +0.3391, -0.7475, +0.5874, -0.0405, -0.2058, -0.5957, +0.2659, -0.8477, -0.5814, -0.0494, -0.1678, +0.2650, -0.4039, +0.1414, -0.6635, +0.0447, +0.2932, +0.1167, +0.1195, +0.0669, -0.4223, +0.1196, +0.0553, -0.7123, -0.4011, +0.3557, -0.4503, +0.7047, -0.4471, +0.0807, +0.3926, -0.1427, +0.4355, -0.3678, +0.3453, +0.1597, -0.3076, +0.4689, +0.3128, -0.7050, +0.6505, +0.3427, +0.1981, +0.1190, +0.2554, +0.8283, +0.1647, -0.4257, +0.1481, +0.4361, -0.5497, -0.6114, -0.0138, +0.0932],
[ +0.1866, +0.6408, -1.8201, +1.0946, +0.7742, -0.7651, +0.1082, +0.6842, +0.3794, +0.3547, -0.8172, -0.0921, -0.6736, +1.0251, -0.9618, -0.6869, +1.8465, +0.2425, +0.7910, +1.0009, -0.8031, +1.6697, -0.8962, +0.1873, +0.4960, -0.6812, +0.6860, +1.1932, -0.7019, +0.4028, +0.4841, +0.6497, +1.6490, -0.5464, +0.7060, +1.8087, -0.6118, -0.7955, -0.3797, -1.2048, +1.2356, -0.6141, +1.2502, +0.5641, -0.1019, -1.7516, -0.1134, -0.6719, +1.5014, -0.2718, -0.5933, +0.1714, -1.3590, -0.3656, +1.0083, -0.8511, -0.5597, -0.4446, -1.7158, -0.0851, +0.3089, +0.0967, -1.0121, +0.3048],
[ +0.3329, +0.5382, +0.1585, +0.8205, +0.5510, +0.2796, -0.7120, +0.3434, +0.2931, +1.2275, +0.4191, -0.6828, -0.5091, +0.8408, -0.3101, -0.5183, +0.2651, +0.2073, -0.1383, +0.6539, -0.2167, +0.7798, -0.5690, +0.3750, +0.4358, +0.6537, -0.2202, -0.0563, +0.6605, +0.4599, -0.5327, +0.6610, +0.8387, +0.1887, -0.2593, +0.7904, -0.3567, +0.4121, +0.4378, -0.2935, +0.1291, +0.0021, -0.3416, -0.5920, -0.2895, -0.4610, +0.7380, -0.6322, +0.6738, -0.1378, -0.3304, -0.2894, -0.3582, -0.8311, +0.2660, -0.2079, -0.1765, -0.6825, -0.1754, -0.4455, +0.7202, -0.8177, -0.9900, -0.7425]
])

weights_dense1_b = np.array([ +0.0009, -0.2179, -0.0299, +0.2069, -0.0099, +0.0907, +0.0271, +0.1957, +0.0185, +0.1671, -0.0699, -0.0332, -0.0244, +0.0022, +0.1877, -0.0801, +0.0235, -0.0097, -0.0088, +0.1961, -0.1055, +0.0605, -0.0913, +0.0884, -0.0638, +0.0229, -0.1101, +0.1966, -0.0042, +0.0221, -0.0966, +0.1554, +0.1623, -0.0454, +0.1068, +0.0114, +0.0544, +0.0201, +0.0257, +0.0637, +0.0761, +0.2120, +0.0225, +0.2023, -0.0931, +0.0585, -0.2253, -0.0302, +0.0682, +0.0000, -0.1215, -0.1105, +0.1376, +0.0583, -0.1706, -0.0262, -0.0897, +0.0728, +0.0787, +0.0912, -0.0964, -0.0959, -0.0195, +0.0232])

weights_dense2_w = np.array([
[ +0.0089, +0.2241, -0.0391, +0.1459, -0.0854, -0.0878, +0.2829, -0.1620, -0.1694, -0.5211, +0.0155, -0.1298, -0.0629, +0.1074, +0.0150, -0.3583, +0.0427, +0.1813, +0.2140, -0.4230, +0.1577, +0.1223, -0.0096, +0.0183, -0.1038, -0.5612, -0.0614, -0.0820, -0.0057, -0.2471, +0.0355, -0.1525],
[ +0.1555, -0.2934, +0.2690, -0.3218, +0.0101, -0.1188, -0.1798, -0.1405, +0.2701, -0.0972, +0.2338, -0.0122, -0.2254, -0.3225, -0.0268, -0.0829, +0.4085, +0.0691, -0.1448, -0.0429, -0.2750, -0.2479, +0.0396, +0.0427, +0.0205, -0.1462, -0.1481, +0.1365, -0.0903, +0.0094, +0.3665, +0.1163],
[ +0.0119, -0.3100, +0.1201, -0.2257, +0.1246, -0.1335, -0.3369, -0.0408, +0.3145, +0.2030, +0.1506, +0.0899, -0.1192, -0.2429, +0.0356, +0.0634, -0.0706, +0.1119, -0.0402, +0.1011, +0.1281, +0.4318, -0.4644, +0.0039, +0.0932, -0.0521, -0.1528, +0.1946, -0.0921, -0.0646, -0.0241, +0.1598],
[ -0.1007, +0.3939, -0.2066, +0.0752, -0.1709, -0.0286, +0.0196, +0.1853, -0.3619, -0.0449, +0.0334, -0.2673, +0.0640, +0.3055, -0.1184, -0.4550, +0.0951, -0.2168, +0.1502, -0.4816, +0.1392, -0.3708, -0.0849, -0.4331, -0.0800, -0.0967, +0.1334, -0.3169, -0.0004, -0.3002, -0.0841, -0.1763],
[ -0.0492, +0.0308, +0.0824, +0.0568, -0.0038, +0.3196, +0.5089, +0.0391, -0.1373, -0.1579, +0.0219, -0.2990, -0.0113, -0.2136, -0.0240, +0.1241, -0.1723, -0.0064, -0.0213, -0.2213, -0.0996, -0.0333, -0.4110, -0.2074, +0.0427, +0.0323, -0.0920, -0.1846, -0.1037, -0.0381, -0.0763, +0.0875],
[ +0.0965, -0.1536, -0.0270, -0.0834, +0.0270, +0.0908, -0.0257, -0.1284, +0.1994, +0.2317, +0.0193, +0.0493, -0.0723, -0.2748, +0.0248, -0.0021, -0.0483, +0.0610, -0.0056, -0.0575, +0.0930, +0.0749, -0.2599, +0.0223, +0.0050, -0.0569, -0.6755, +0.2190, +0.0009, +0.1493, -0.1822, +0.0763],
[ -0.0435, +0.3829, -0.2358, +0.3554, -0.1800, +0.0008, -0.0282, -0.0139, -0.2745, -0.2293, -0.4456, +0.1709, +0.0687, -0.0696, -0.0877, -0.0978, -0.0620, -0.4380, +0.2052, -0.1479, +0.0971, -0.0031, +0.0783, -0.0749, -0.2695, -0.0151, -0.0066, +0.0592, -0.0088, -0.0507, -0.0167, -0.2891],
[ -0.1797, -0.1446, -0.0609, -0.2840, +0.1933, +0.0366, -0.3077, -0.0018, -0.1564, +0.0283, +0.1447, +0.2110, -0.0047, -0.2123, +0.0041, +0.0171, +0.2826, +0.1549, -0.1211, +0.1360, +0.1473, +0.1541, -0.1583, +0.0955, -0.1047, +0.0530, +0.0667, +0.1454, -0.0860, +0.0602, +0.1970, +0.0716],
[ +0.0119, +0.1858, -0.1746, +0.0911, -0.0948, -0.0898, -0.0680, -0.2266, -0.1098, +0.0161, +0.0265, +0.1100, -0.3467, -0.0128, -0.2249, +0.0344, +0.1421, -0.1222, -0.0196, -0.1188, +0.0428, -0.2318, +0.0998, +0.1017, +0.0298, -0.1391, +0.1229, +0.1193, +0.0565, +0.1296, +0.0939, -0.0234],
[ +0.1817, +0.2432, -0.2712, +0.0668, -0.1836, +0.0232, -0.0793, +0.0161, -0.1585, -0.3731, -0.0243, -0.1066, +0.0928, -0.0499, -0.0692, -0.3354, +0.0754, +0.0468, -0.2522, -0.7501, +0.0235, -0.5134, -0.3031, -0.1907, -0.2166, -0.1713, -0.0422, +0.0831, +0.0664, -0.0462, +0.1627, -0.4927],
[ -0.0342, +0.2310, +0.2736, -0.0703, +0.1941, -0.0428, -0.0868, -0.2146, +0.1371, +0.0117, +0.0218, +0.0133, -0.0416, +0.1012, +0.1689, +0.3113, +0.0199, +0.1176, +0.0256, +0.0907, +0.0622, +0.3312, -0.0225, -0.0187, +0.2089, +0.1381, -0.2949, +0.1525, -0.0514, -0.1416, -0.0381, -0.0133],
[ -0.0885, +0.3841, -0.3811, +0.1388, -0.1801, -0.0434, +0.1371, -0.0393, +0.2549, -0.4207, -0.2308, +0.0187, -0.0975, +0.2137, -0.0840, -0.0491, +0.0424, +0.0060, +0.1007, +0.0315, +0.3005, +0.0501, +0.0516, -0.0521, -0.0100, +0.0984, +0.3092, +0.0031, -0.0380, +0.2344, +0.0808, -0.0694],
[ -0.0631, +0.0290, +0.1733, -0.0555, +0.1311, -0.0812, +0.1056, -0.1663, -0.1272, +0.2717, +0.0247, +0.0730, -0.3714, +0.0042, -0.0490, +0.0222, -0.0429, -0.1618, +0.1476, +0.1699, -0.1660, +0.1571, -0.0225, +0.1582, +0.1622, -0.0721, -0.1198, +0.1388, -0.1661, +0.0103, -0.1386, +0.0883],
[ +0.0306, +0.1041, -0.2540, +0.0423, +0.1098, -0.0204, +0.1478, +0.1917, +0.1102, +0.0045, -0.0263, +0.0818, -0.0245, -0.0047, -0.2407, -0.6658, +0.0834, +0.0400, +0.1785, -0.5141, +0.3379, -0.5638, -0.0012, -0.2549, -0.4172, -0.2134, -0.3793, -0.0736, -0.3442, +0.1044, -0.0489, -0.2967],
[ -0.0446, -0.1153, -0.0839, +0.0948, +0.3570, -0.0520, -0.1016, -0.0265, +0.4342, +0.2325, +0.1763, -0.2663, -0.0676, -0.0759, +0.0654, +0.2983, +0.1185, -0.0233, -0.5232, +0.1075, -0.3284, +0.2703, +0.2164, +0.0092, +0.2988, +0.1956, +0.0582, +0.3342, +0.0949, -0.1936, -0.0465, +0.4223],
[ +0.0737, -0.0069, -0.1301, +0.3047, -0.2603, +0.0369, -0.2049, +0.0378, -0.1846, -0.3474, -0.1353, +0.0965, +0.0956, -0.0692, -0.0440, -0.1767, -0.1616, -0.2183, +0.1853, -0.0618, +0.1210, -0.2178, +0.1066, -0.3849, -0.2628, +0.1444, +0.2814, -0.2963, +0.0673, +0.0983, +0.0442, +0.0020],
[ -0.0978, +0.2645, -0.3750, +0.2824, -0.3906, -0.0070, +0.1920, +0.0911, -0.0510, -0.1050, -0.2411, -0.2135, +0.0784, +0.3348, -0.0396, -0.4209, -0.0686, -0.2212, +0.3039, -0.4649, -0.0692, -0.5387, +0.0479, -0.4205, -0.2557, -0.1031, +0.1378, -0.3875, -0.1900, -0.0253, +0.1212, -0.4374],
[ -0.1067, +0.1545, +0.2016, -0.0620, -0.1419, -0.0661, -0.1224, -0.0560, +0.1045, -0.2062, -0.2551, +0.2440, -0.1116, +0.1544, -0.2324, +0.0999, -0.1832, -0.1226, -0.1774, +0.0629, -0.1170, -0.1375, +0.0839, +0.2029, +0.0551, +0.0359, +0.0967, +0.2290, -0.0312, -0.1228, +0.2831, +0.1785],
[ -0.1420, +0.1163, +0.0488, -0.0011, -0.1311, -0.1558, -0.0766, -0.0088, +0.1877, -0.1547, +0.1304, +0.0347, +0.1132, +0.2750, -0.0574, +0.0080, -0.2256, -0.0951, +0.1987, +0.2256, +0.0270, -0.0155, +0.0636, +0.0372, +0.2483, -0.1469, -0.2010, -0.0994, -0.1731, +0.0224, +0.0085, -0.1891],
[ +0.1037, +0.0015, -0.1525, -0.0444, -0.3130, -0.0318, +0.2370, -0.1492, -0.4707, -0.0023, +0.0884, +0.1722, -0.0421, +0.0858, -0.1036, -0.5701, +0.1249, -0.2643, -0.0203, -0.1380, +0.0973, -0.2060, +0.1806, +0.3054, -0.6548, -0.3282, -0.2969, -0.3984, -0.0448, -0.1802, +0.3282, -0.1891],
[ -0.1116, +0.3646, -0.0542, +0.3672, -0.4207, +0.2700, +0.3827, -0.0599, -0.3415, -0.2832, -0.0345, +0.1987, +0.0669, +0.1301, -0.3806, -0.2981, -0.1917, -0.2028, +0.1687, -0.2010, +0.3607, -0.0199, +0.2971, +0.0390, +0.0895, -0.3088, +0.0169, -0.1333, +0.0738, +0.2161, -0.1207, -0.3352],
[ -0.0134, +0.3853, -0.2106, +0.1996, -0.2277, -0.0971, +0.0917, -0.2901, -0.2493, +0.0295, -0.1438, -0.1902, -0.0074, +0.2240, -0.0277, -0.4374, +0.0749, -0.1779, +0.2687, -0.4093, -0.0042, -0.5023, -0.1169, -0.3157, +0.0061, +0.0270, +0.0204, -0.4626, -0.1717, -0.2126, +0.1335, -0.5028],
[ -0.0813, +0.1958, -0.4203, +0.3027, -0.3896, -0.1201, -0.0383, -0.1807, -0.4834, -0.3672, -0.3664, +0.2401, -0.0114, -0.0852, -0.2220, -0.1953, +0.0773, -0.0048, +0.1560, -0.1524, +0.0772, -0.2740, +0.1346, -0.3171, -0.0648, +0.1633, +0.2050, -0.1560, +0.0270, +0.3009, -0.2798, -0.0756],
[ -0.1754, +0.1428, +0.2527, -0.2624, -0.1126, -0.0014, +0.1030, -0.2716, -0.2678, -0.0268, +0.0982, -0.0385, -0.0628, -0.0768, -0.2531, +0.2935, -0.0661, +0.0778, -0.1184, +0.0070, -0.1331, -0.1174, -0.1338, -0.1601, -0.0357, -0.1964, -0.0550, -0.1151, +0.2369, +0.1578, -0.0826, -0.1985],
[ -0.1724, -0.0328, +0.0090, -0.0564, +0.0876, -0.0607, +0.0060, -0.2330, +0.1137, -0.0771, -0.0774, +0.0727, -0.2037, +0.1521, +0.0666, +0.0258, -0.2189, -0.1417, +0.0276, -0.0387, -0.0747, -0.0214, -0.0793, -0.0520, +0.0918, -0.1276, -0.0877, +0.0309, -0.0630, -0.0149, -0.0197, -0.1755],
[ +0.1471, -0.1542, +0.1202, -0.2846, +0.1209, -0.0383, -0.2689, -0.0442, -0.1086, +0.3428, +0.0120, +0.0473, +0.0320, -0.2629, -0.0904, -0.3732, -0.2179, +0.2540, -0.1725, -0.4163, -0.0333, +0.0934, -0.3123, -0.1123, -0.2196, +0.1580, -0.6386, +0.0650, -0.0473, +0.0521, +0.0061, -0.2745],
[ +0.0064, -0.1054, -0.2054, -0.1706, +0.1626, +0.0895, +0.0571, -0.2639, +0.0269, +0.1943, +0.0687, -0.1510, -0.1987, +0.0784, -0.1774, -0.0242, +0.0519, -0.3330, +0.0364, +0.1868, -0.3204, +0.1106, +0.0456, -0.1627, -0.2792, +0.0017, +0.2943, +0.0481, -0.1523, -0.1656, -0.0222, -0.0239],
[ +0.0853, +0.2513, -0.1716, +0.0164, -0.1375, -0.0870, +0.2430, +0.2161, -0.4489, -0.3427, +0.0341, -0.0022, -0.1488, +0.2685, -0.2290, -0.2439, +0.1216, -0.1475, -0.0332, -0.1282, -0.1603, -0.1076, -0.1279, -0.1439, -0.2784, -0.4271, +0.1286, -0.1134, -0.1994, -0.1031, -0.0210, -0.2327],
[ +0.1303, -0.0463, +0.1797, -0.0939, +0.2427, -0.0791, -0.0735, -0.2248, +0.1545, -0.1325, -0.1812, -0.0896, +0.0695, +0.0225, -0.1880, +0.1619, -0.0468, +0.0904, +0.1570, -0.0206, +0.1266, -0.0148, +0.0305, +0.2494, +0.1687, -0.0774, -0.2693, +0.0449, +0.0040, -0.1319, +0.1513, -0.0410],
[ +0.0545, +0.0586, -0.0087, -0.1021, -0.1756, -0.0722, +0.0678, +0.0310, -0.1490, -0.2823, +0.1335, -0.0038, +0.0660, +0.0696, -0.2747, -0.3360, +0.1061, +0.3080, +0.1201, -0.3870, +0.2960, -0.4409, -0.0295, +0.0854, -0.0908, +0.1224, -0.4637, -0.4016, +0.0420, +0.0505, +0.0364, -0.2983],
[ -0.1218, +0.2787, -0.1838, -0.0315, -0.1590, -0.2840, +0.2845, +0.0601, -0.1741, -0.2363, -0.3620, -0.1355, +0.0943, +0.1343, -0.0346, -0.1135, +0.0327, -0.2982, +0.1805, -0.1483, +0.1698, -0.1056, -0.0257, +0.0580, -0.1921, +0.0863, +0.1439, -0.1360, +0.0468, +0.2411, -0.1872, +0.0329],
[ +0.0068, +0.1272, +0.0108, +0.0178, +0.2308, +0.0207, -0.0050, +0.0127, +0.1008, -0.2972, -0.2233, -0.1369, +0.0797, +0.0023, -0.0782, -0.4778, +0.1916, +0.1325, +0.0110, -0.2083, +0.2786, -0.2724, -0.1214, +0.0510, -0.1068, -0.1982, -0.4602, -0.1082, -0.1563, -0.0689, -0.0913, +0.0983],
[ +0.1631, +0.1356, -0.1882, +0.2125, -0.4817, -0.1368, +0.1216, -0.1032, -0.4494, -0.2093, -0.0110, +0.0402, -0.0097, +0.1575, -0.2447, -0.8683, +0.1860, -0.4305, +0.1405, -0.3244, +0.1927, -0.5331, +0.0910, -0.1750, -0.2639, -0.3461, -0.0655, -0.4643, -0.0272, +0.0600, +0.1538, -0.3951],
[ +0.0750, +0.0031, -0.1113, +0.0419, -0.0726, +0.1712, +0.1273, -0.0844, +0.0187, -0.1579, +0.0365, +0.1953, +0.0259, +0.1069, +0.1584, +0.0159, +0.1700, -0.0276, +0.0061, -0.1753, -0.0827, -0.0493, +0.0756, -0.1169, +0.0177, -0.2200, -0.0495, -0.0934, +0.1999, -0.0962, -0.0035, +0.1083],
[ -0.0754, -0.1933, +0.1219, -0.3622, -0.2560, +0.0829, -0.3323, +0.0923, -0.1712, +0.0494, +0.1063, +0.3118, +0.0088, -0.3756, -0.0977, +0.0160, -0.0817, +0.1595, -0.3452, +0.2652, +0.2646, +0.2833, -0.3530, +0.0805, -0.1736, +0.0675, -0.1320, -0.3568, +0.1824, -0.0068, +0.0391, -0.3348],
[ +0.0661, +0.1602, -0.0509, +0.0562, -0.1738, +0.0114, -0.0268, -0.0354, -0.2069, -0.0250, -0.1061, -0.1695, -0.0719, +0.2797, -0.2477, -0.2539, +0.1287, -0.2037, +0.2556, -0.1008, +0.1943, -0.1660, +0.2728, -0.2338, -0.0806, -0.2346, +0.0449, -0.4673, -0.0362, -0.1172, +0.1695, -0.2252],
[ +0.0348, -0.2188, +0.0041, -0.1818, +0.3175, -0.0947, -0.2779, -0.0764, +0.2407, -0.1541, +0.2586, -0.1852, -0.1379, -0.3336, +0.1402, -0.0446, +0.0584, +0.0994, -0.3633, +0.0636, -0.0156, -0.0767, -0.2649, +0.0149, +0.2484, +0.2916, +0.1928, -0.0036, +0.0696, -0.0935, +0.2752, +0.0187],
[ -0.2666, +0.0507, -0.1783, +0.2308, +0.3974, -0.0719, +0.0276, -0.0048, +0.1177, +0.0816, -0.2346, -0.2762, +0.1167, +0.0719, -0.1303, -0.0892, +0.0177, +0.0072, +0.0965, +0.2305, +0.0988, +0.1532, -0.1653, +0.0692, -0.0419, -0.1874, -0.0896, +0.0014, +0.0375, -0.0905, -0.3757, +0.3573],
[ +0.4116, -0.2717, +0.2356, -0.1943, +0.0575, +0.0379, -0.0606, -0.0819, +0.1179, +0.2377, -0.1506, +0.1710, +0.0912, -0.2922, +0.0898, +0.1814, +0.1221, +0.1917, -0.3906, +0.1684, +0.1638, +0.2434, -0.1656, +0.1352, +0.0744, -0.0942, -0.2128, +0.0767, +0.0628, +0.1426, +0.3458, -0.0437],
[ -0.1387, -0.5340, +0.2895, -0.5476, +0.5888, +0.1435, -0.4898, +0.0061, +0.6167, +0.1024, +0.1127, +0.2197, +0.0206, -0.4723, +0.1195, +0.6172, +0.0276, +0.3961, -0.5498, +0.4008, -0.2163, +0.3337, -0.2608, +0.1666, +0.3415, +0.0077, -0.1649, +0.2619, -0.1937, -0.1043, +0.1770, +0.4285],
[ -0.0167, +0.0725, +0.1501, +0.0806, -0.0904, -0.2287, +0.1906, -0.0706, -0.0861, -0.1585, -0.1175, -0.0603, -0.0193, +0.4876, -0.1954, -0.0463, -0.1083, +0.1297, -0.0301, +0.0312, +0.0755, +0.0648, -0.4867, -0.0645, +0.0074, +0.0624, -0.1972, -0.1996, -0.1207, -0.1015, +0.0720, +0.0260],
[ +0.0007, -0.1637, +0.1202, -0.1045, +0.2969, +0.1975, -0.1374, +0.1684, +0.0790, +0.2108, -0.0220, +0.0773, +0.0046, +0.0205, -0.1746, +0.3445, +0.0773, +0.0005, +0.0251, +0.3337, -0.3365, +0.3956, -0.2011, +0.2489, +0.1875, +0.0282, -0.4611, +0.2249, +0.0182, -0.1252, -0.1899, +0.1563],
[ -0.0142, +0.0174, +0.1562, +0.0763, +0.1314, -0.0686, +0.3657, -0.0132, -0.0737, +0.0247, +0.0431, -0.2967, +0.0002, +0.2221, +0.1011, +0.1039, -0.0503, -0.3926, +0.1014, -0.1349, -0.1005, +0.1254, +0.0250, -0.1482, -0.2554, +0.1027, +0.1661, -0.1071, -0.0521, -0.0568, +0.1508, +0.0668],
[ -0.1106, +0.1260, -0.3472, +0.2769, +0.0344, -0.0668, +0.2888, +0.1583, -0.2782, -0.1161, -0.2939, +0.1309, -0.0010, +0.4387, +0.1623, -0.2627, -0.1011, -0.3530, +0.0604, -0.2499, +0.2736, -0.2715, +0.2004, -0.5407, -0.4915, -0.1778, +0.1274, -0.1071, -0.0170, -0.1190, -0.1540, -0.0364],
[ -0.1767, +0.2753, +0.2479, -0.0753, -0.2057, -0.2379, -0.0411, -0.0945, -0.1757, +0.1752, +0.1322, +0.0548, -0.0980, +0.1753, -0.0510, +0.2050, -0.0246, +0.5660, -0.2124, +0.1708, -0.1779, +0.2125, -0.0143, +0.1992, +0.1330, -0.2561, -0.1304, +0.2212, -0.2898, +0.0983, -0.1803, +0.1087],
[ -0.0503, -0.3082, +0.1056, -0.1658, +0.3225, +0.0727, -0.4463, -0.0153, +0.0195, +0.0962, -0.0483, -0.0484, +0.2464, -0.5537, +0.1422, +0.1233, -0.1036, +0.0864, -0.2107, +0.1319, +0.2002, +0.3051, -0.2054, +0.3069, +0.2754, +0.1618, -0.0593, -0.0373, +0.2155, -0.1157, -0.1199, +0.2342],
[ -0.1789, -0.1216, +0.0442, -0.1111, +0.1411, -0.0572, -0.4238, +0.0134, -0.1511, +0.0625, -0.0139, -0.2257, -0.1143, -0.2315, +0.3597, -0.1227, +0.0240, +0.2061, -0.0474, +0.0561, -0.2806, -0.0939, -0.0608, +0.1852, -0.0210, -0.3526, +0.0992, -0.3513, -0.0787, +0.1074, -0.0475, -0.1759],
[ -0.0510, +0.0215, +0.1585, -0.0757, +0.0357, -0.0553, -0.1151, -0.1353, +0.1000, -0.2570, -0.0664, -0.1762, +0.0430, -0.0365, +0.0198, +0.1154, -0.5763, +0.0393, -0.0443, +0.0504, +0.0482, +0.1528, +0.1955, -0.0493, +0.2712, -0.0688, -0.1406, +0.1479, +0.0204, +0.0838, -0.2282, +0.2307],
[ -0.1682, -0.0467, -0.0758, +0.3832, -0.1471, +0.0612, +0.3901, +0.1065, +0.2009, -0.3104, -0.2998, -0.3175, -0.0722, +0.1549, -0.2472, -0.1729, +0.0841, -0.1691, +0.1407, -0.1969, -0.0491, +0.0103, +0.1179, -0.1327, -0.1275, +0.0368, +0.0953, -0.1660, -0.0245, -0.3851, +0.1340, -0.1417],
[ +0.0114, -0.0822, -0.2575, -0.0169, +0.1292, +0.0791, -0.0803, +0.0061, -0.0445, -0.2228, +0.0215, +0.1863, +0.2645, -0.0295, +0.0756, -0.2138, -0.1607, +0.0527, +0.0592, -0.1770, -0.0982, -0.1096, +0.0925, -0.0325, +0.0047, +0.1512, +0.0663, -0.1348, +0.0084, -0.1352, +0.0189, +0.1428],
[ +0.0052, +0.1124, +0.1083, +0.1163, +0.0787, +0.0839, +0.0839, +0.0506, +0.0537, +0.1066, +0.1034, -0.1299, -0.1434, +0.0188, +0.1823, +0.1403, -0.4525, +0.0949, -0.0981, +0.0722, -0.1085, -0.2382, +0.1028, +0.0664, +0.1976, +0.1073, -0.2736, +0.2433, -0.3520, -0.0386, -0.2319, -0.0724],
[ -0.3279, -0.1491, -0.1409, +0.2056, -0.1464, +0.0543, +0.1842, +0.1104, -0.2819, +0.0769, -0.1159, +0.0228, -0.0988, +0.0026, -0.1204, -0.0780, -0.2018, +0.1755, +0.1574, +0.0222, +0.1662, -0.2193, -0.0718, +0.0010, -0.0123, -0.0120, +0.2587, +0.0358, -0.1435, +0.0017, -0.2620, +0.0965],
[ -0.1144, -0.1048, +0.2211, -0.0726, -0.1721, -0.2475, -0.3226, +0.0120, +0.0908, +0.0375, -0.0974, +0.0490, -0.1180, -0.3155, -0.2565, -0.0092, -0.4400, +0.2027, -0.1459, +0.1043, +0.0771, +0.0825, -0.1541, -0.0713, -0.0437, -0.0249, -0.1757, -0.1115, +0.0457, +0.1141, -0.2567, +0.0405],
[ +0.0587, +0.1083, +0.0729, +0.2131, -0.1586, +0.2208, -0.1576, -0.0811, -0.0467, +0.2201, -0.1082, -0.2077, +0.0030, -0.1222, +0.2023, +0.1155, -0.1616, +0.0105, +0.1167, -0.1257, +0.4859, +0.1337, -0.0169, -0.0163, +0.2076, +0.0367, -0.0050, -0.2590, -0.0800, -0.2192, +0.0938, +0.1126],
[ -0.3834, -0.0180, -0.2714, +0.0303, +0.0784, -0.1242, +0.1105, +0.0237, -0.0085, +0.2615, +0.0189, -0.3734, +0.0088, +0.1211, -0.0838, +0.0067, +0.1956, +0.1577, +0.2132, -0.0044, -0.2748, +0.1417, +0.0201, +0.1002, +0.0311, -0.0052, -0.1695, -0.0750, +0.2200, -0.2848, +0.0438, -0.0442],
[ -0.1496, +0.1258, +0.1903, -0.0337, -0.1470, -0.0530, +0.0519, -0.0037, +0.0342, +0.0404, -0.0950, -0.0840, +0.1083, -0.0488, +0.0427, +0.1454, +0.0851, -0.0203, -0.2354, +0.1562, +0.1899, +0.3145, +0.0013, +0.1608, +0.0126, +0.2080, -0.1409, -0.0746, +0.0580, -0.1045, -0.1753, +0.1225],
[ -0.0349, +0.1354, -0.1052, -0.1189, +0.0288, -0.0257, +0.0813, -0.1559, +0.1267, +0.0664, +0.2004, +0.1232, +0.2557, -0.1729, -0.0666, +0.1644, +0.1043, -0.2672, +0.0537, +0.0566, -0.1738, +0.0036, +0.1406, -0.0574, -0.0556, +0.3336, -0.0328, -0.1624, +0.0132, -0.0627, -0.1523, +0.0552],
[ -0.3105, +0.2681, -0.5462, +0.2785, -0.2453, -0.2965, +0.1436, +0.0786, -0.3242, -0.3518, +0.1025, +0.2219, -0.1324, +0.1681, +0.0701, -0.0938, +0.1574, -0.5157, +0.3574, -0.1100, +0.2647, -0.1698, +0.2684, -0.3876, -0.6240, -0.1013, +0.2920, -0.3569, -0.0008, +0.0974, +0.1444, -0.3349],
[ +0.0848, -0.1191, +0.2283, +0.0922, +0.2880, -0.1747, -0.4457, +0.1013, +0.2494, +0.1487, +0.1013, -0.0403, -0.0236, -0.1965, -0.0655, +0.0818, +0.0493, -0.0605, -0.1889, +0.1772, -0.2826, +0.2783, -0.1653, +0.3505, +0.4192, -0.1048, -0.1459, +0.0779, -0.0154, -0.1573, -0.1254, -0.1118],
[ -0.1817, +0.0719, +0.1352, +0.3208, +0.2142, -0.1149, +0.0020, +0.1617, +0.1055, +0.0395, -0.1802, -0.0631, -0.3172, +0.1971, +0.0197, +0.1271, -0.2375, -0.1849, -0.0134, +0.1223, +0.2566, +0.0311, -0.2746, +0.0278, +0.1233, +0.0167, -0.0363, +0.2146, -0.0466, +0.0732, -0.1490, +0.1040],
[ +0.1008, -0.1501, +0.0264, -0.4661, -0.0553, +0.0431, -0.3076, -0.0461, +0.1393, -0.1225, +0.2811, -0.0363, -0.0403, -0.3370, -0.0865, -0.1179, +0.1106, +0.2035, -0.2432, -0.0859, +0.0600, -0.0890, -0.0749, +0.0483, +0.0615, -0.0239, -0.4674, +0.0199, +0.0669, +0.1410, +0.1846, +0.2626],
[ +0.0663, +0.1486, -0.3928, +0.3257, -0.0316, +0.1377, +0.0418, +0.1921, -0.1616, -0.2265, -0.0917, +0.1582, -0.0537, +0.0295, -0.2264, -0.1921, -0.0225, +0.0928, +0.0747, -0.5268, -0.0068, -0.3328, +0.0437, -0.2361, -0.1408, -0.1234, +0.2216, -0.1372, -0.0499, +0.1940, +0.0098, -0.2953],
[ +0.0290, -0.1583, -0.0172, -0.1748, -0.0042, -0.0725, -0.2227, -0.1366, -0.1771, +0.1987, +0.3142, +0.1889, +0.0195, -0.5461, +0.0921, +0.1407, -0.1656, +0.1985, +0.0113, +0.2613, +0.2925, +0.1166, -0.1286, +0.1031, -0.2228, -0.0605, -0.2151, +0.2477, +0.1602, -0.0109, +0.0207, +0.1257],
[ +0.0630, -0.1688, +0.1662, -0.2327, +0.2832, +0.1350, -0.1658, +0.0504, -0.0502, +0.1736, +0.1002, -0.0051, -0.0311, -0.0628, +0.0039, +0.5085, -0.2191, +0.5105, -0.0927, +0.2833, -0.2828, +0.1078, +0.0406, -0.0392, -0.2372, +0.1508, +0.0556, +0.0313, +0.1296, +0.1315, -0.1143, +0.1632]
])

weights_dense2_b = np.array([ -0.0655, +0.0020, +0.0358, -0.0192, +0.0570, +0.0000, +0.0711, -0.0145, +0.0294, +0.0139, -0.0215, -0.0952, +0.0000, +0.0526, -0.0585, +0.0633, -0.0332, +0.0030, +0.0107, +0.0830, +0.0140, +0.0888, -0.1115, -0.0722, +0.0240, +0.0476, -0.0807, -0.0421, +0.0000, -0.0557, -0.0403, +0.0034])

weights_final_w = np.array([
[ -0.0230],
[ +0.0730],
[ -0.2093],
[ +0.0463],
[ -0.1983],
[ -0.0031],
[ +0.2101],
[ -0.0066],
[ -0.1481],
[ -0.1615],
[ -0.1766],
[ +0.1332],
[ -0.0012],
[ +0.2332],
[ -0.0380],
[ -0.3066],
[ -0.1738],
[ -0.2982],
[ +0.0285],
[ -0.1548],
[ +0.2539],
[ -0.2544],
[ +0.2006],
[ -0.4121],
[ -0.2084],
[ -0.0381],
[ +0.2733],
[ -0.3076],
[ +0.0013],
[ +0.0957],
[ -0.1298],
[ -0.1112]
])

weights_final_b = np.array([ +0.0352])

if __name__=="__main__":
    main()
