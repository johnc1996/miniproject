var express = require('express');
var server = express(); // better instead
server.configure(function(){
  server.use('/media', express.static(__dirname + '/media'));
  server.use(express.static(templates + '/public'));
});

server.listen(3000);