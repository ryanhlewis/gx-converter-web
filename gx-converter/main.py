from g_code_property_extractor import GCodePropertyExtractor
from g_code_transformer import GCodeTransformer
from header import Header


with open("../scratch/calibration-cube.gcode", "r") as f:
    code = f.read()

hotbed_temp = GCodePropertyExtractor.get_hotbed_temperature(code)
nozzle_temp = GCodePropertyExtractor.get_nozzle_temperature(code)
print_time = GCodePropertyExtractor.get_print_time(code)
filament_usage = GCodePropertyExtractor.get_filament_usage(code)
layer_height = GCodePropertyExtractor.get_layer_height(code)
shell_count = 3
print_speed = 60

code = GCodeTransformer.convert(code)

header = Header(
    print_time, filament_usage, layer_height, 1, print_speed, hotbed_temp, nozzle_temp
)

gx = header.assembled_header + code.encode("utf-8")

with open("../scratch/cube-test.gx", "wb") as f:
    f.write(gx)
