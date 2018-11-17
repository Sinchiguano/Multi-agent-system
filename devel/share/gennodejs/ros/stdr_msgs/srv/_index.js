
"use strict";

let AddCO2Source = require('./AddCO2Source.js')
let DeleteSoundSource = require('./DeleteSoundSource.js')
let AddSoundSource = require('./AddSoundSource.js')
let AddThermalSource = require('./AddThermalSource.js')
let LoadMap = require('./LoadMap.js')
let DeleteThermalSource = require('./DeleteThermalSource.js')
let DeleteCO2Source = require('./DeleteCO2Source.js')
let MoveRobot = require('./MoveRobot.js')
let RegisterGui = require('./RegisterGui.js')
let LoadExternalMap = require('./LoadExternalMap.js')
let DeleteRfidTag = require('./DeleteRfidTag.js')
let AddRfidTag = require('./AddRfidTag.js')

module.exports = {
  AddCO2Source: AddCO2Source,
  DeleteSoundSource: DeleteSoundSource,
  AddSoundSource: AddSoundSource,
  AddThermalSource: AddThermalSource,
  LoadMap: LoadMap,
  DeleteThermalSource: DeleteThermalSource,
  DeleteCO2Source: DeleteCO2Source,
  MoveRobot: MoveRobot,
  RegisterGui: RegisterGui,
  LoadExternalMap: LoadExternalMap,
  DeleteRfidTag: DeleteRfidTag,
  AddRfidTag: AddRfidTag,
};
