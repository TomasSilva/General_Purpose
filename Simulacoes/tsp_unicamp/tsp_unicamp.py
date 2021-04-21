import gmplot
import numpy as np
from python_tsp.distances import great_circle_distance_matrix
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.heuristics import solve_tsp_simulated_annealing

Institutos = [
    ('IA', -22.815233063553617, -47.07037078529995),
    ('IB', -22.820229531445353, -47.07000653565959),
    ('IC', -22.814926404943815, -47.064690333802474),
    ('IE', -22.81453903753336, -47.06592209701338),
    ('IEL', -22.814789980442555, -47.069399550953875),
    ('IFCH', -22.814931107741785, -47.06831653567905),
    ('IFGW', -22.81772913854128, -47.06727234920307),
    ('IG', -22.813207125332596, -47.06915680683303),
    ('IMECC', -22.815591089631496, -47.067618233877795),
    ('IQ', -22.81931511976706, -47.06753093568966),
    ('FCF', -22.82435135625503, -47.065082376116145),
    ('FENF', -22.830823892631756, -47.06286504789011),
    ('FEA', -22.82011420945329, -47.06720500489791),
    ('FEAGRI', -22.81929211200016, -47.06048277303011),
    ('FEC', -22.8163942433822, -47.0620745871537),
    ('FEEC', -22.820928941904636, -47.06640939315277),
    ('FEM', -22.81950719809562, -47.06591359333648),
    ('FEQ', -22.821173177149085, -47.06443992215571),
    ('FCM', -22.830104822784364, -47.0631423161313),
    ('FEF', -22.815141947517855, -47.07262756341806),
    ('FE', -22.816748564193414, -47.066048635644904)
]


# Create the map plotter:
apikey = ''  # (your API key here)
# PRACA DO CB
gmap = gmplot.GoogleMapPlotter(-22.81713425394216, -
                               47.06973932371405, 14, apikey=apikey)

# Mark a hidden gem:
for inst in Institutos:
    gmap.marker(inst[1], inst[2], color='cornflowerblue')

for inst1 in Institutos:
    for inst2 in Institutos:
        if inst1 != inst2:
            gmap.plot([inst1[1], inst2[1]], [
                      inst1[2], inst2[2]], 'green', edge_width=1)


# Draw the map to an HTML file:
gmap.draw('map.html')

# Solve TSP
matrix = [[-22.81713425394216, -47.06973932371405]]
for inst in Institutos:
    matrix.append([inst[1], inst[2]])

min = 100000000

distance_matrix = great_circle_distance_matrix(matrix)


# for i in range(1, 50):
permutation, distance = solve_tsp_simulated_annealing(distance_matrix)
# if distance < min:
#     min = distance
#     min_dist = distance
#     min_perm = permutation


print(distance)
print(permutation)
print(len(permutation))
for i in range(1, len(permutation)):
    print(Institutos[permutation[i]-1][0])
