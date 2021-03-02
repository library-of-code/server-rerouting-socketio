const express = require("express");
const http = require("http");
const socket = require("socket.io")(http);
const path = require("path");
const smartAttendanceServer = require("socket.io-client")('http://localhost:5000', {reconnectionDelayMax: 10000,});

const app = express();

// PORT = process.env.PORT || "8000"
app.set("port", process.env.PORT || "8080");
const server = http.createServer(app);
const io = socket.listen(server);

io.on("connection", socket => {
  smartAttendanceServer.emit('foo',
  {
    number_of_popups: 4,
    repeat_popup: 10,
  })
  smartAttendanceServer.on("flask event", function (data) {
    socket.emit("message", data);
  })
  console.log("React App connected")
  socket.on("react event", body => {
    console.log(body)
  })
})




smartAttendanceServer.on("flask event", function (data) {
  console.log(data);
})
smartAttendanceServer.on("empty event", function (data) {
  // console.log(data);
})

// console.log("server started at port", { PORT });
// server.listen(app.get(PORT));

server.listen(app.get("port"));
module.exports = server;