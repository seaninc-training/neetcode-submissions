import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        k_points = []
        i = 0

        while i < k:
            min_distance = None
            closest_point = None
            for point in points:
                distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)

                if min_distance is None or distance < min_distance:
                    min_distance = distance
                    closest_point = point

            k_points.append(closest_point)
            points.remove(closest_point)
            i += 1
        
        return k_points

