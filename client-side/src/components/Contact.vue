<template>
    <div>
      <section class="container">
          <div class="call-us"></div>
          <div class="txt">
              <h1>Contact Us</h1>
              <p>
                  We are here to help you with any queries you may have. 
                  Please feel free to contact us and we will get back to you 
                  as soon as possible.
              </p>
              <span class="socials">
                  <a href="https://www.facebook.com" target="_blank">
                      <img src="../assets/fbook.svg" alt="facebook">
                  </a>
                  <a href="https://www.twitter.com" target="_blank">
                      <img src="../assets/twitter.png" alt="twitter">
                  </a>
                  <a href="https://www.instagram.com" target="_blank">
                      <img src="../assets/insta.png" alt="instagram">
                  </a>
                  <a href="https://www.github.com/" target="_blank">
                      <img src="../assets/github.webp" alt="github">
                  </a>
              </span><br><br>
              <span class="ftr">© 2024 <router-link to="/">Event Ease</router-link> | All Rights Reserved | <router-link to="/register">List Your Service</router-link></span>
          </div>
      </section>
    </div>
  </template>
  
  <script setup>
  
  </script>
  
  <style scoped>
  .container {
      background-color: #1f1818;
      display: flex;
  }
  
  .call-us {
      background-image: url('../assets/contact.jpg');
      height: 60vh;
      background-size: cover;
      background-position: bottom;
      width: 80%;
  }
  
  .txt {
      margin: 50px 50px auto 50px;
      padding: 0 0 0 50px;
  }
  
  .txt h1 {
      font-size: 90px;
      text-transform: uppercase;
      font-family: "Truculenta", sans-serif;
      color: #fff;
  }
  
  .txt p {
      width: 60%;
      text-align: justify;
      color: #666;
  }
  
  .socials {
      display: flex;
      margin-top: 25px;
      img {
          width: 30px;
          margin: 20px 20px 0 0;
          filter: invert(100%);
          transition: all ease 0.5s;
      }
  }
  
  .socials img:hover {
      filter: invert(55%);
      transition: all ease 0.5s;
  }
  
  .ftr {
      color: #444;
      font-size: 12px;
      a {
          text-decoration: none;
          color: #444;
      }
  }
  
  .ftr a:hover {
      text-decoration: underline;
      color: #555;
  }
  </style>