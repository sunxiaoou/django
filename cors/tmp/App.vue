<template>
  <div id="app">
    <img src="./assets/logo.png" />
    <router-view />
  </div>
</template>

<script>
import axios from "axios";

var config = {
  method: "get",
  url: "http://127.0.0.1:8090/api/token/",
};

axios(config)
  .then(function (response) {
    console.log(response.data);
    var token = window.document.cookie.match(
      new RegExp("csrftoken=([^;]+);")
    )[1];
    console.log(token);

    var FormData = require("form-data");
    var data = new FormData();
    data.append("title", "夜晚的潜水艇");
    data.append("price", "52.00");
    data.append("pub_date", "2020-09-17");

    var config = {
      method: "put",
      url: "http://127.0.0.1:8090/api/book/3",
      headers: {
        "Response-type": "application/json",
        "X-CSRFToken": token
      },
      data: data,
    };

    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
  })
  .catch(function (error) {
    console.log(error);
  });
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;

  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
