import OpenEXR
import other_imath as Imath
# import Imath

(w, h) = (1920, 1080)

data = ".." * w * h

for i in range(10):
    hdr = OpenEXR.Header(w, h)
    chan = Imath.Channel(Imath.PixelType(OpenEXR.HALF))
    hdr['channels'] = {'R' : chan, 'G' : chan, 'B' : chan, 'A' : chan}
    x = OpenEXR.OutputFile("/home/shrimo/lib/openexrpython-master/test_a.exr", hdr)
    x.writePixels({'R': data, 'G': data, 'B': data, 'A' : data})
    x.close()
