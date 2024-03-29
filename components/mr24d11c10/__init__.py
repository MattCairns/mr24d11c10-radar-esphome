import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

DEPENDENCIES = ["uart"]
CODEOWNERS = ["@TheRealTom", "@MattCairns"]
MULTI_CONF = True

mr24d11c10_ns = cg.esphome_ns.namespace("mr24d11c10")
Mr24d11c10Component= mr24d11c10_ns.class_(
    "Mr24d11c10Component", cg.Component, uart.UARTDevice
)
CONF_MR24D11C10_ID = "mr24d11c10_id"

CONFIG_SCHEMA = cv.Schema({
            cv.GenerateID(): cv.declare_id(Mr24d11c10Component),
}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
    "mr24d11c10",
    baud_rate=9600,
    require_tx=True,
    require_rx=True,
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
