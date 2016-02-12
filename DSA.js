jQuery(function($) {
  function changeCAT2() {
  var choice = $('#choice2').val() 
  if(choice == "effectiveness" ){$('#avg_improvement').replaceWith('<iframe id = "avg_improvement" width="100%" title="Improvement Effectiveness" height="425px" src="https://opendata.socrata.com/w/2zj4-gkct/y34g-bnf3?cur=GzimJB9mK-h&from=root" frameborder="0"scrolling="no"><a href="https://opendata.socrata.com/dataset/Improvement-Effectiveness/2zj4-gkct" title="Improvement Effectiveness" target="_blank">"Improvement Effectiveness"</a></iframe>');}
   else if (choice == "safety"){$('#avg_improvement').replaceWith('<iframe id = "avg_improvement" width="100%" title="Improvement in Safety" height="425px" src="https://opendata.socrata.com/w/dtbn-94bu/y34g-bnf3?cur=DSZT_y-PvOb&from=root" frameborder="5"scrolling="no"><a href="https://opendata.socrata.com/dataset/Improvement-in-Safety/dtbn-94bu" title="Improvement in Safety" target="_blank">"Improvement in Safety"</a></iframe>');}
   else if (choice == "efficiency"){$('#avg_improvement').replaceWith('<iframe id = "avg_improvement" width="100%" title="Improvement in Efficiency" height="425px" src="https://opendata.socrata.com/w/fiyv-6hpq/y34g-bnf3?cur=izKG9jQrv-S&from=root" frameborder="5"scrolling="no"><a href="https://opendata.socrata.com/dataset/Improvement-in-Efficiency/fiyv-6hpq" title="Improvement in Efficiency" target="_blank">"Improvement in Efficiency"</a></iframe>');}
   else {alert('Please make a valid choice');}
   };
  $('#btn2').click(changeCAT2);
});


