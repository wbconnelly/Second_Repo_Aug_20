//jQuery(function($) {
//  function changeCAT() {
//    $('#avg_scores').replaceWith('<iframe id = "avg_scores" width="100%" title="State Scores for Efficiency All Years" height="425px" src="https://opendata.socrata.com/w/e7v3-dykt/y34g-bnf3?cur=-O_5jDmfgMG&from=root" frameborder="5"scrolling="no"><a href="https://opendata.socrata.com/dataset/State-Scores-for-Efficiency-All-Years/e7v3-dykt" title="State Scores for Efficiency All Years" target="_blank">"State Scores for Efficiency All Years"</a></iframe>');
 // };
 // $('#btn1').click(changeCAT);
//});


// next link: <iframe id = "avg_scores" width="500px" title="State Scores for Effectiveness" height="425px" src="https://opendata.socrata.com/w/fcf5-3ncu/y34g-bnf3?cur=wyPLO4ia5CS&from=root" frameborder="0"scrolling="no"><a href="https://opendata.socrata.com/dataset/State-Scores-for-Effectiveness/fcf5-3ncu" title="State Scores for Effectiveness" target="_blank">""State Scores for Effectiveness"</a></iframe>

jQuery(function($) {
  function changeCAT() {
  var choice = $('#choice').val() 
  if(choice == "effectiveness" ){$('#avg_scores').replaceWith('<iframe id = "avg_scores" width="100%" title="State Scores for Effectiveness" height="425px" src="https://opendata.socrata.com/w/fcf5-3ncu/y34g-bnf3?cur=wyPLO4ia5CS&from=root" frameborder="0"scrolling="no"><a href="https://opendata.socrata.com/dataset/State-Scores-for-Effectiveness/fcf5-3ncu" title="State Scores for Effectiveness" target="_blank">""State Scores for Effectiveness"</a></iframe>');}
   else if (choice == "safety"){$('#avg_scores').replaceWith('<iframe id = "avg_scores" width="100%" title="State Scores for Safety All Years" height="425px" src="https://opendata.socrata.com/w/8tjz-p37i/y34g-bnf3?cur=La5O1pRe-4N&from=root" frameborder="0"scrolling="no"><a href="https://opendata.socrata.com/dataset/State-Scores-for-Safety-All-Years/8tjz-p37i" title="State Scores for Safety All Years" target="_blank">"State Scores for Safety All Years"</a></iframe>');}
   else if (choice == "efficiency"){$('#avg_scores').replaceWith('<iframe id = "avg_scores" width="100%" title="State Scores for Efficiency All Years" height="425px" src="https://opendata.socrata.com/w/e7v3-dykt/y34g-bnf3?cur=-O_5jDmfgMG&from=root" frameborder="5"scrolling="no"><a href="https://opendata.socrata.com/dataset/State-Scores-for-Efficiency-All-Years/e7v3-dykt" title="State Scores for Efficiency All Years" target="_blank">"State Scores for Efficiency All Years"</a></iframe>');}
   else {alert('Please make a valid choice');}
   };
  $('#btn1').click(changeCAT);
});
