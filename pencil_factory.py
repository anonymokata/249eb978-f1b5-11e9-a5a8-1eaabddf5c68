from pencil import Pencil
from eraser import Eraser
class PencilFactory:
    NO2_HB_POINT_DURABILITY = 4860
    NO2_HB_LENGTH = 44
    NO2_HB_ERASER_DURABILITY = NO2_HB_LENGTH*NO2_HB_POINT_DURABILITY

    def get_no2_hb():
        return Pencil(point_durability=PencilFactory.NO2_HB_POINT_DURABILITY, length=PencilFactory.NO2_HB_LENGTH, eraser=Eraser(PencilFactory.NO2_HB_ERASER_DURABILITY))
