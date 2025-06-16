+++
type = "question"
title = "Are the coordinates of places in African locations often wrong?"
description = '''I am currently working with map data from Nairobi,Kenya. I am using leaflet to place textboxes on places clicked on the map and have their coordinates returned. Sometimes the pattern I get suggests that the coordinates being returned are incorrect. For example, there is this instance where I clicked...'''
date = "2018-02-26T14:03:00Z"
lastmod = "2018-03-07T14:35:00Z"
weight = 62402
keywords = [ "leaflet" ]
aliases = [ "/questions/62402" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Are the coordinates of places in African locations often wrong?](/questions/62402/are-the-coordinates-of-places-in-african-locations-often-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62402-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="/upfiles/leaflet_coords.jpg" alt="Picture supposed to be here" />I am currently working with map data from Nairobi,Kenya. I am using leaflet to place textboxes on places clicked on the map and have their coordinates returned. Sometimes the pattern I get suggests that the coordinates being returned are incorrect. For example, there is this instance where I clicked and created 6 textboxes. The further east I went, the smaller the longitudes were getting. From my knowledge of geography, it should be the other way round. Is this a problem with the data or could it be coming from leaflet?</p>
<p>EDIT:</p>
<p>My code for creating textboxes looks like this:</p>
<pre><code>  var counter = 0;
  var coordinates = {};
&#10;      function onMapClick(e) {
     counter++;
     var order_box = &#39;&lt;input type=&quot;text&quot; id= &#39; + &#39;&quot;&#39; + counter + &#39;&quot;&#39; + &#39; size = &quot;5&quot;&gt;&#39;;
     alert(order_box);
&#10;     var myIcon = new L.divIcon({
        html:order_box
     });
&#10;     var marker = new L.marker(e.latlng, {icon: myIcon}).addTo(map);
     coordinates[counter] = e.latlng;
     str = JSON.stringify(coordinates);
     alert(str);
&#10;     document.getElementById(&#39;coord1&#39;).value = str;
  }</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '18, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c90b2bba1514cbd750b8fadf7e90b3da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="imonike&#39;s gravatar image" />
<p><span>imonike</span><br />
<span class="score" title="96 reputation points">96</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="imonike has one accepted answer">100%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '18, 22:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62402" class="comments-container">
<span id="62407"></span>
<div id="comment-62407" class="comment">
<div id="post-62407-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this related to OSM? For more general GIS questions, try <a href="https://gis.stackexchange.com/">GIS StackExchange</a>.</p>
</div>
<div id="comment-62407-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 15:06)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="62408"></span>
<div id="comment-62408" class="comment">
<div id="post-62408-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes it is.</p>
</div>
<div id="comment-62408-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 15:43)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62410"></span>
<div id="comment-62410" class="comment">
<div id="post-62410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you give an example - for example give a URL in OSM (like <a href="https://www.openstreetmap.org/#map=11/-1.3038/36.7637">https://www.openstreetmap.org/#map=11/-1.3038/36.7637</a> , but zoomed in much more) where the you have clicked on a map and got co-ordinates that you didn't expect?</p>
</div>
<div id="comment-62410-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 15:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62415"></span>
<div id="comment-62415" class="comment not_top_scorer">
<div id="post-62415-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a screen-shot that clearly shows the issue. Is there a way for attaching files?</p>
</div>
<div id="comment-62415-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 15:56)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62423"></span>
<div id="comment-62423" class="comment not_top_scorer">
<div id="post-62423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could upload a picture to an image host and link to that - I've used <a href="https://lut.im/">https://lut.im/</a> for that, but plenty of others are available.</p>
</div>
<div id="comment-62423-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 17:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62435"></span>
<div id="comment-62435" class="comment not_top_scorer">
<div id="post-62435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>. <a href="https://help.openstreetmap.org/users/1725/andy">@andy</a>-mackey has told me what to do. The screen-shot should be visible now.</p>
</div>
<div id="comment-62435-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 10:16)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62438"></span>
<div id="comment-62438" class="comment not_top_scorer">
<div id="post-62438-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is that a screen shot of? It's clearly something running on your PC on port 5000, but what?</p>
</div>
<div id="comment-62438-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 10:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62443"></span>
<div id="comment-62443" class="comment">
<div id="post-62443-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>. I am building a python based app using the flask framework. I make use of the leaflet library that sources its map data from OSM.</p>
</div>
<div id="comment-62443-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 12:14)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62444"></span>
<div id="comment-62444" class="comment">
<div id="post-62444-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>. I am trying to build an app that helps with deliveries, so I place textboxes at locations deliveries are to be made and place the size of the order in the textbox. I use javascript alert boxes to debug my code. In it are 6 entries for 6 orders. Each order entry contains serial number, size of order and location coordinates of order. The leaflet API provides functionality for getting the lat and lon of any point on the map clicked.</p>
</div>
<div id="comment-62444-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 12:25)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
</div>
<div id="comment-tools-62402" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-62402-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62511"></span>

<div id="answer-container-62511" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62511-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello all. Sorry I am just getting back to this. I have been caught up attending to job-related tasks. <a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a>, turns out you were right. I had a line of code with one wrong operand in a subtraction operation that causing the coordinates to be reversed and mapped to the wrong textbox. Thank you all for all the help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '18, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c90b2bba1514cbd750b8fadf7e90b3da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="imonike&#39;s gravatar image" />
<p><span>imonike</span><br />
<span class="score" title="96 reputation points">96</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="imonike has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-62511" class="comments-container">
<span id="62512"></span>
<div id="comment-62512" class="comment">
<div id="post-62512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've made this ths accepted answer - hope you don't mind!</p>
</div>
<div id="comment-62512-info" class="comment-info">
<span class="comment-age">(05 Mar '18, 14:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62513"></span>
<div id="comment-62513" class="comment">
<div id="post-62513-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> Please, be my guest! :-) Thank you</p>
</div>
<div id="comment-62513-info" class="comment-info">
<span class="comment-age">(05 Mar '18, 14:14)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62514"></span>
<div id="comment-62514" class="comment">
<div id="post-62514-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>BTW (didn't want to add this before to not make the confusion all too large as it was clear that you had a technical issue), the REAL answer is: YES</p>
<p>Lots of place coordinates in Africa have been imported from catastrophically bad data sources and are very often simply nonsense.</p>
</div>
<div id="comment-62514-info" class="comment-info">
<span class="comment-age">(05 Mar '18, 15:17)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="62521"></span>
<div id="comment-62521" class="comment">
<div id="post-62521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>. Would care to enumerate these data sources? Also would you know where the map data for Kenya and Nigeria are sourced from?</p>
</div>
<div id="comment-62521-info" class="comment-info">
<span class="comment-age">(06 Mar '18, 08:13)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62524"></span>
<div id="comment-62524" class="comment not_top_scorer">
<div id="post-62524-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Larger places are probably OK, but there multiple imports of GNIS data and other such sources by HOT multiple years back that were never cleaned up AFAIK. Essentially you simply need to check the source, likely the original changeset when the data was added. I suspect recent stuff should be a lot better.</p>
</div>
<div id="comment-62524-info" class="comment-info">
<span class="comment-age">(06 Mar '18, 13:33)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="62526"></span>
<div id="comment-62526" class="comment">
<div id="post-62526-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have to admit SimonPoole's comment above was the first thing that I thought of too. GNIS data has been used in a number of places and is mostly rubbish. There are some attempts to clean it up in e.g. Maproulette (not sure there's a current challenge for this data in Africa, but it would surely be a good candidate).</p>
<p>To find other examples of problem data sources in rural Africa, search for named place=village in Overpass <a href="https://overpass-turbo.eu/s/wKR">https://overpass-turbo.eu/s/wKR</a> and examine a few to see if they actually match any imagery. An example problem changeset is <a href="https://www.openstreetmap.org/changeset/376211">https://www.openstreetmap.org/changeset/376211</a> (there's no source on any data there unfortunately).</p>
</div>
<div id="comment-62526-info" class="comment-info">
<span class="comment-age">(06 Mar '18, 13:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62549"></span>
<div id="comment-62549" class="comment not_top_scorer">
<div id="post-62549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>, <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, many thanks for your helpful comments. Will keep all this in mind as I go along. Cheers!!!</p>
</div>
<div id="comment-62549-info" class="comment-info">
<span class="comment-age">(07 Mar '18, 14:35)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
</div>
<div id="comment-tools-62511" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-62511-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62411"></span>

<div id="answer-container-62411" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62411-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not so much an answer more a theory. When i open an editor over a some African countries, and choose to see all traces i find that there are very, very few GPX traces available. Although most Backgrounds that i have used ( in Europe) seem to be accurately aligned we can check them as we fortunately have lots traces available. There may be several reasons for Europe having lots of traces, The main one guess being disposable income as GPSes are/were expensive. OSM started in Europe and it was a few years before Bing and other Aerial backgrounds became available, perhaps because of this we had to use GPSes as the main source. Now smartphones are available, with good gps chips, and in use worldwide I would suggest if mappers upload GPX enough traces to give a good world wide coverage OSM's accuracy could improve everywhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '18, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '18, 14:54</strong> </span></p>
</div>
</div>
<div id="comments-container-62411" class="comments-container">
<span id="62412"></span>
<div id="comment-62412" class="comment not_top_scorer">
<div id="post-62412-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nairobi's substantially east of Greenwich and slightly south of the equator, so I'm guessing "lat and long being mixed up" rather than "actually asking about west of Greenwich".</p>
</div>
<div id="comment-62412-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 15:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62413"></span>
<div id="comment-62413" class="comment not_top_scorer">
<div id="post-62413-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok wrong again:)</p>
</div>
<div id="comment-62413-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 15:53)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="62414"></span>
<div id="comment-62414" class="comment">
<div id="post-62414-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am dealing with Kenya, so all my degrees are east of zero.</p>
</div>
<div id="comment-62414-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 15:54)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62416"></span>
<div id="comment-62416" class="comment not_top_scorer">
<div id="post-62416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It doesn't look like the lat and long are being mixed up. Isn't there a way that I can upload or send the screen-shot? It would really save all the back and forth</p>
</div>
<div id="comment-62416-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 16:04)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62417"></span>
<div id="comment-62417" class="comment">
<div id="post-62417-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes see this <a href="/questions/11589/how-do-i-put-a-screen-image-into-a-question">https://help.openstreetmap.org/questions/11589/how-do-i-put-a-screen-image-into-a-question</a></p>
</div>
<div id="comment-62417-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 16:14)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="62418"></span>
<div id="comment-62418" class="comment not_top_scorer">
<div id="post-62418-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You may be able to edit your question and add the jpeg.</p>
</div>
<div id="comment-62418-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 16:22)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="62420"></span>
<div id="comment-62420" class="comment not_top_scorer">
<div id="post-62420-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to give the long and lat of the 6 textboxes spread over Nairobi and surrounding regions, starting from the most westerly to the most easterly. A box near Riruta lat: -1.29 lon:36.89, a box near Kawangware lat: -1.30 lon: 36.86, south of Nairobi lat: -1.27 lon: 36.83, close to Eastleigh lat: -1.29 lon:36.79, close to Buru Buru lat:-1.28 lon:36.76 and close to Donholm lat: -1.29 lon 36.73. You would notice that the longitudes are decreasing moving from west to east. It ought to be the other way round. It also doesn't look like the lon and lat values are being mixed up.</p>
</div>
<div id="comment-62420-info" class="comment-info">
<span class="comment-age">(26 Feb '18, 17:03)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62436"></span>
<div id="comment-62436" class="comment">
<div id="post-62436-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/1725/andy">@andy</a>-mackey. I have added the screen-shot. It should be visible now.</p>
</div>
<div id="comment-62436-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 10:18)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62437"></span>
<div id="comment-62437" class="comment not_top_scorer">
<div id="post-62437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>From the screen-shot, it can be clearly seen that the longitudes are getting smaller as we move from west to east. It should be the other way around.</p>
</div>
<div id="comment-62437-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 10:21)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62441"></span>
<div id="comment-62441" class="comment">
<div id="post-62441-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The position and your lat lon are displayed here over the OpenStreetMap and something clearly wrong somewhere <a href="http://www.gpsvisualizer.com/display/20180227005526-48148-map.html">http://www.gpsvisualizer.com/display/20180227005526-48148-map.html</a><br />
Your Dunholm position is located over Riruta and your Riruta located over Dunholm. Similarly with Kawangware and Buru Baru.</p>
<p>On Imgur here <a href="https://imgur.com/NXyLCfd">https://imgur.com/NXyLCfd</a></p>
</div>
<div id="comment-62441-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 10:31)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="62442"></span>
<div id="comment-62442" class="comment not_top_scorer">
<div id="post-62442-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a>. Yeah, I am hoping we can figure out where the problems are coming from. I hadn't heard of the GPSVisualizer before. I am new to mapping.You overlaid the map with the coordinates I supplied?</p>
</div>
<div id="comment-62442-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 12:10)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62445"></span>
<div id="comment-62445" class="comment not_top_scorer">
<div id="post-62445-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Using <a href="http://www.gpsvisualizer.com/map_input?bg_map=google_openstreetmap&amp;form=google&amp;width=1200">http://www.gpsvisualizer.com/map_input?bg_map=google_openstreetmap&amp;form=google&amp;width=1200</a><br />
I pasted the following in the box on the right side and selected "Draw the map"<br />
I think I changed the waypoint options on the left side to permanent labels too.<br />
name,desc,latitude,longitude<br />
Riruta,at,-1.29,36.89<br />
Kawangware,near,-1.30,36.86<br />
Nairobi,south,-1.27,36.83<br />
Eastleigh,close,-1.29,36.79<br />
Buru Buru,close,-1.28,36.76<br />
Donholm,close,-1.29,36.73</p>
</div>
<div id="comment-62445-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 12:27)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="62447"></span>
<div id="comment-62447" class="comment not_top_scorer">
<div id="post-62447-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a>. Now I can't be sure whether the error is from the data, the leaflet API or my handling of the API.</p>
</div>
<div id="comment-62447-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 12:41)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62448"></span>
<div id="comment-62448" class="comment not_top_scorer">
<div id="post-62448-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your coordinates are either wrong or in a different format. How did you obtain them?</p>
</div>
<div id="comment-62448-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 13:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="62449"></span>
<div id="comment-62449" class="comment">
<div id="post-62449-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The names may have been sorted to the wrong set of coordinates?</p>
</div>
<div id="comment-62449-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 13:14)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="62455"></span>
<div id="comment-62455" class="comment not_top_scorer">
<div id="post-62455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> I obtain them programmatically. Each time I double-click to create a textbox, I save the coordinates in a javascript variable. The method for getting the lat and long values is functionality provided by the leaflet API.</p>
</div>
<div id="comment-62455-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 14:45)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62457"></span>
<div id="comment-62457" class="comment not_top_scorer">
<div id="post-62457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/7380/nevw"></a><a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a> I don't think so. You see I wasn't clicking on the places named per se. I just used them to give a visual idea of the situation since those places are places whose names showed up on the map and were close to the places I actually clicked. I gave that information before <a href="https://help.openstreetmap.org/users/644/andy-mackey"></a><a href="https://help.openstreetmap.org/users/644/andy-mackey">@andy mackey</a> showed me how to upload my screen-shot.</p>
</div>
<div id="comment-62457-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 14:50)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62461"></span>
<div id="comment-62461" class="comment not_top_scorer">
<div id="post-62461-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Show us the code your are using to obtain/show these coordinates. This isn't a feature provided by Leaflet out of the box, is it? Also, try a different browser.</p>
</div>
<div id="comment-62461-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 15:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="62464"></span>
<div id="comment-62464" class="comment not_top_scorer">
<div id="post-62464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> I have edited the question to show the relevant part of the code.</p>
</div>
<div id="comment-62464-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 15:53)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62465"></span>
<div id="comment-62465" class="comment not_top_scorer">
<div id="post-62465-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/644/andy-mackey">@andy mackey</a>.I had thought along similar lines but wanted other opinions since I know so little about mapping. It is hardly to be expected that the quality of gps receivers used for Africa to match those used in Europe and used to the same extent. Assuming that this is indeed the reason for my problems, is there anything I can do in the meantime? Like maybe implementing error-correction algorithms to deal with problematic data, or techniques from cartography or computational geometry that could help ameliorate the situation?</p>
</div>
<div id="comment-62465-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 16:03)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="62467"></span>
<div id="comment-62467" class="comment not_top_scorer">
<div id="post-62467-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have used Garmin Etrex Vista HCX and Oregon 450 GPSes so not professional equipment. Judging from my experience ( I have uploaded about a 1000 traces) with a clear view I would say better than 4 meter accuracy. Mapping ways, or aligning Aerial with a mass of traces I think 2 metres is achievable, My android Moto G3 is just about as good but won't do points every second. So pass the word, "upload those traces".</p>
</div>
<div id="comment-62467-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 19:43)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="62469"></span>
<div id="comment-62469" class="comment not_top_scorer">
<div id="post-62469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If averaged waypoints, that is when a gps records for a time at a fixed known point, for better accuracy could maybe be used to fix points that are identifiable on background may be worth a try.</p>
</div>
<div id="comment-62469-info" class="comment-info">
<span class="comment-age">(27 Feb '18, 19:52)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="62485"></span>
<div id="comment-62485" class="comment not_top_scorer">
<div id="post-62485-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks <a href="https://help.openstreetmap.org/users/644/andy-mackey">@andy mackey</a>. I was hoping for something that could deal with the data as is. While clearly uploading traces is the ultimate solution, I am afraid I don't think that would happen quick enough for my project. Thanks a lot for the help.</p>
</div>
<div id="comment-62485-info" class="comment-info">
<span class="comment-age">(28 Feb '18, 14:06)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
</div>
<div id="comment-tools-62411" class="comment-tools">
<span class="comments-showing"> showing 5 of 23 </span> <a href="#" class="show-all-comments-link">show 18 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-62411-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

