class·Solution:
····def·hammingDistance(self,·x:·int,·y:·int)·->·int:
········x_bin·=·bin(x)[2:]··#·[2:]·to·remove·'0b'·prefix
········y_bin·=·bin(y)[2:]
········hamming_distance·=·0
········max_length·=·max(len(x_bin),·len(y_bin))
········x_bin·=·x_bin.zfill(max_length)
········y_bin·=·y_bin.zfill(max_length)
········for·i·in·range(max_length):
············if·x_bin[i]·!=·y_bin[i]:
················hamming_distance·+=·1

········return·hamming_distance


1
