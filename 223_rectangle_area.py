class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        jointArea = 0;
        if not (H <= B or C <= E or D <= F or G <= A):
            #Not disjoint
            sideY = abs(max(B, F) - min(D, H))
            sideX = abs(max(E, A) - min(G, C))
            jointArea = sideX * sideY

            areaA = (C-A)*(D-B)
            areaB = (G-E)*(H-F)

            return areaA + areaB - jointArea

