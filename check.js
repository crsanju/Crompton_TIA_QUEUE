const fs = require('fs');
const path = 'c:/Users/Sanju/OneDrive - CromptonConcepts/Sharepoint - Documents/Clients/Application development/Apps/TIA+QUEUE/Crompton_TIA_QUEUE/Crompton_TIA_Queue.html';
const content = fs.readFileSync(path, 'utf8');
const match = content.match(/<script>([\s\S]*)<\/script>/);
if(!match) {
  console.log('no script');
  process.exit(1);
}
const code = match[1];
try {
  new Function(code);
  console.log('parsed ok');
} catch(e) {
  console.log('parse error');
  console.log(e);
  console.log('error at', e.stack.split('\n')[0]);
}
