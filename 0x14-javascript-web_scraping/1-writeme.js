#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(`An error occurred: ${err}`);
  } else {
    console.log('Content has been written to the file successfully.');
  }
});
