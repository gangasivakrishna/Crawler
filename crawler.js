var express = require('express');
var path = require('path');
var app = express();
var fs = require('fs');
var request = require('request');
var port = 8090;
var cheerio = require('cheerio'); 

var url = 'https://www.w3schools.com/html/html_forms.asp';




request(url,function(err,res,body){


var $ = cheerio.load(body);
var data = [];
  $('a').each(function(){

    console.log($(this).attr('href'));
});






  
});
