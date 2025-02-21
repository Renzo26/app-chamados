const fs = require('fs');
const path = require('path');

const dataFile = path.join(__dirname, 'data', 'contadores.json');

function readData() {
  try {
    const data = fs.readFileSync(dataFile, 'utf8');
    return JSON.parse(data);
  } catch (err) {
    return {};
  }
}

function writeData(data) {
  fs.writeFileSync(dataFile, JSON.stringify(data));
}

module.exports = { readData, writeData };