+++
type = "question"
title = "How to find out if a person has entered a train station"
description = '''I am trying to create a mobile app for train delays, need to identify if the user is in a train station how can i do this? any ideas? Using POSTCODE, GPS, Open data or anything else, POSTCODE just identifies a exact gps location but the person can be in any of the point around the station Any way to...'''
date = "2016-10-07T23:06:00Z"
lastmod = "2016-10-17T08:54:00Z"
weight = 52402
keywords = [ "opendata", "station", "train" ]
aliases = [ "/questions/52402" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to find out if a person has entered a train station](/questions/52402/how-to-find-out-if-a-person-has-entered-a-train-station)

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
<span id="post-52402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52402-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-52402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to create a mobile app for train delays, need to identify if the user is in a train station how can i do this? any ideas?</p>
<p>Using POSTCODE, GPS, Open data or anything else, POSTCODE just identifies a exact gps location but the person can be in any of the point around the station</p>
<p>Any way to identify this plz?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opendata" rel="tag" title="see questions tagged &#39;opendata&#39;">opendata</span> <span class="post-tag tag-link-station" rel="tag" title="see questions tagged &#39;station&#39;">station</span> <span class="post-tag tag-link-train" rel="tag" title="see questions tagged &#39;train&#39;">train</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '16, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/24f9ddfbc116657dafd9c60b67801a4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brightnlight&#39;s gravatar image" />
<p><span>brightnlight</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brightnlight has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52402" class="comments-container">
<span id="52503"></span>
<div id="comment-52503" class="comment">
<div id="post-52503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am still waiting for any simple reply for my query, Couple of people have suggested me to go through the API and I have done my work and i need help, but here there is no one to say a simple request, I have posted my effort and asked for some kind help,</p>
<p>Would appreciate if someone comes up with a simple answer on how to question of how to find out if the person is in station or not as I am stuck and not able to find the answer myself!</p>
<p>Please</p>
</div>
<div id="comment-52503-info" class="comment-info">
<span class="comment-age">(12 Oct '16, 22:44)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52528"></span>
<div id="comment-52528" class="comment">
<div id="post-52528-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>It isn't a simple question so there won't be a simple reply, I'm afraid. If you're having difficulty with the information provided then I suggest you employ a developer to help. People do try to help on this site but they can only point you in the right direction, not build the entire solution for you.</p>
</div>
<div id="comment-52528-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 12:21)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52402" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52402-form-container" class="comment-form-container">
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

<span id="52403"></span>

<div id="answer-container-52403" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52403-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="brightnlight has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Tag:railway%3Dstation">railway=station</a> or <a href="https://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dstation">public_transport=station</a> tags define the area of a station, so you could check to see if the user's position is within one of those areas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '16, 23:36</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-52403" class="comments-container">
<span id="52405"></span>
<div id="comment-52405" class="comment">
<div id="post-52405-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Alester</p>
<p>Thanks for your answer very much appreciated,</p>
<p>What I have is the users GPS coordinates of the user on a particular location (x,y) -from location finder of the mobile app</p>
<p>What i need is Inside which station is this person in currently?</p>
<p>Now from what I infer from you kind reply is that there is a API call I can make to openstreetmap to find out if the person is within the area of the station?</p>
<p>Can you provide me an example for this call please using my gps location of the user?</p>
</div>
<div id="comment-52405-info" class="comment-info">
<span class="comment-age">(08 Oct '16, 08:22)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52406"></span>
<div id="comment-52406" class="comment">
<div id="post-52406-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>OSM does not provide an API for this type of query. You should look at something like Overpass instead (see multiple queries on this site).</p>
</div>
<div id="comment-52406-info" class="comment-info">
<span class="comment-age">(08 Oct '16, 09:53)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="52430"></span>
<div id="comment-52430" class="comment not_top_scorer">
<div id="post-52430-score" class="comment-score">
-3
</div>
<div class="comment-text">
<p>Hello Friend</p>
<p>I went with your help trying to find out examples of overpass, unable to get anything much</p>
<p>Please can you give me an example of the query view OSM or OPEN PASS to find given a input as x,y coordinates, if this coordinate is within the area of east croydon railway station</p>
<p>East croydon reference: <a href="http://geobrit.uk/302042289-east-croydon-station-railway-station-croydon-tq328658#data">http://geobrit.uk/302042289-east-croydon-station-railway-station-croydon-tq328658#data</a></p>
</div>
<div id="comment-52430-info" class="comment-info">
<span class="comment-age">(09 Oct '16, 21:58)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52435"></span>
<div id="comment-52435" class="comment">
<div id="post-52435-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You didn't look very far: try typing overpass into the search on this site or on the OSM Wiki. There are pages of documentation and nearly 500 questions with answers on this site alone. You will also find many answers about overpass on GIS StackInfo.</p>
</div>
<div id="comment-52435-info" class="comment-info">
<span class="comment-age">(10 Oct '16, 09:34)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="52438"></span>
<div id="comment-52438" class="comment">
<div id="post-52438-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, had a good look and found the following query helped me to get the result for the train station EAST CROYDON. node["name"="East Croydon"]<a href="%7B%7Bbbox%7D%7D">"train"="yes"</a>; "type": "node", "id": 302042289, "lat": 51.3758448, "lon": -0.0927317, "tags": { "name": "East Croydon", "naptan:AtcoCode": "9100ECROYDN", "network": "National Rail", "platforms": "6", "postal_code": "CR0 1LF", "public_transport": "station", "railway": "station", "ref": "ECR", "source_ref": "train": "yes", "wheelchair": "yes", } }, { "type": "node", "id": 676877753, "lat": 51.3760143, "lon": -0.0923223, "tags": { "name": "East Croydon", "public_transport": "stop_position", "train": "yes" } }, + 4 more stop_position sections this had 6 records which includes different platform points (log and lat) with in the station But for me to identify the user within the railway station I need to cover the area of the whole east croydon station (land and building) the person can be anywhere here, how can i find the bounding box of the whole station so that i can then check if the person with X and Y is within the station?</p>
<p>Please help</p>
</div>
<div id="comment-52438-info" class="comment-info">
<span class="comment-age">(10 Oct '16, 12:07)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52460"></span>
<div id="comment-52460" class="comment not_top_scorer">
<div id="post-52460-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please can you help?</p>
</div>
<div id="comment-52460-info" class="comment-info">
<span class="comment-age">(11 Oct '16, 04:04)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52517"></span>
<div id="comment-52517" class="comment">
<div id="post-52517-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is no "area of the whole east croydon station (land and building)" in OSM. So you have to perform some estimations based on the buildings, stops, platforms and similar elements. Read about <a href="https://wiki.openstreetmap.org/wiki/Railway_stations">railway stations</a> in OSM.</p>
</div>
<div id="comment-52517-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 07:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52403" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-52403-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52439"></span>

<div id="answer-container-52439" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52439-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Before even thinking about stations, I'd take a step back and find out a bit about OpenStreetMap. The wiki has a link from the <a href="https://wiki.openstreetmap.org/wiki/Main_Page">main page</a> that talks about <a href="https://wiki.openstreetmap.org/wiki/Develop">software development</a>. In particular I'd read <a href="https://wiki.openstreetmap.org/wiki/Elements">this page</a> that shows what elements OpenStreetMap data is composed of, and I'd use <a href="http://taginfo.openstreetmap.org/">taginfo</a> to search for railway stations and explore the various elements.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '16, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-52439" class="comments-container">
<span id="52447"></span>
<div id="comment-52447" class="comment">
<div id="post-52447-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Friend Thanks, I did learn node, way and relation but the thing is In the api for railway it says <a href="https://wiki.openstreetmap.org/wiki/Key:railway#Other_railways">https://wiki.openstreetmap.org/wiki/Key:railway#Other_railways</a> railway station Node Area Railway station. whole area But then when i run this query in the turbo node["name"="East Croydon"]<a href="%7B%7Bbbox%7D%7D">"railway"="station"</a>; it returns one point, Please can you help? I am unable to proceed, Any clues otherwise plz</p>
</div>
<div id="comment-52447-info" class="comment-info">
<span class="comment-age">(10 Oct '16, 17:17)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52506"></span>
<div id="comment-52506" class="comment">
<div id="post-52506-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The reason that no-one's given you a simple answer is because there isn't one. Stop thinking about JSON for a second and think about geography. Your "one point" is this node:</p>
<p><a href="https://www.openstreetmap.org/node/302042289">https://www.openstreetmap.org/node/302042289</a></p>
<p>but near it are other places that you might think are "in the station". There are 3 platforms, such as this one:</p>
<p><a href="https://www.openstreetmap.org/way/200673484">https://www.openstreetmap.org/way/200673484</a></p>
<p>There's a railway station building:</p>
<p><a href="https://www.openstreetmap.org/way/27297689">https://www.openstreetmap.org/way/27297689</a></p>
<p>There's a tram stop:</p>
<p><a href="https://www.openstreetmap.org/node/83701432">https://www.openstreetmap.org/node/83701432</a></p>
<p>(and there are tram platforms too). There is an adjacent bus station:</p>
<p><a href="https://www.openstreetmap.org/way/215645188">https://www.openstreetmap.org/way/215645188</a></p>
<p>with bus stops, and there are some stops just outside the rail station such as:</p>
<p><a href="https://www.openstreetmap.org/node/469761252">https://www.openstreetmap.org/node/469761252</a></p>
<p>So take a step back and define yourself by what you mean by "within the station". Does it mean "within an area defined by any object that might reasonably be considered part of East Croyden Station"? If so, that's what you'll need to define and use.</p>
</div>
<div id="comment-52506-info" class="comment-info">
<span class="comment-age">(12 Oct '16, 23:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52507"></span>
<div id="comment-52507" class="comment">
<div id="post-52507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well worded SomeoneElse. I was trying to say the same thing but wasn't sure how to phrase it. Basically, East Croydon Station isn't defined as a specific area which someone could 'be in'.</p>
</div>
<div id="comment-52507-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 00:04)</span> <span class="comment-user userinfo">NZGraham</span>
</div>
</div>
<span id="52525"></span>
<div id="comment-52525" class="comment">
<div id="post-52525-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks so much for your detailed explanation very much appreciated 1. Yes I realized that node is a point in space, so I need to define a area of a station to find out if the user has entered in to this space of area. 2. All the queries you provided is very interesting and again thats what I need (turbo queries to find out the best way to define what is the right way to define an area) 3. Please if you can provide me the turbo queries for the above then I would be able to find out and investigate more on defining the area of a station and then carry on more with my project work.</p>
<p>Much much appreciated for your help</p>
</div>
<div id="comment-52525-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 10:01)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52527"></span>
<div id="comment-52527" class="comment not_top_scorer">
<div id="post-52527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately I really can't help you define your own problem, much less provide a solution to it. There will be no one simple API/Overpass query that returns exactly the results that you need; you'll need to write some code to do that. Perhaps you need to engage with someone commercially and let them do it for you? There's one list at <a href="https://switch2osm.org/providers/">https://switch2osm.org/providers/</a> ; there are others in the OSM wiki.</p>
</div>
<div id="comment-52527-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 12:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52529"></span>
<div id="comment-52529" class="comment not_top_scorer">
<div id="post-52529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thz but all i asked is the overpass equivalent for this url u posted for railway station building plz <a href="https://www.openstreetmap.org/way/27297689">https://www.openstreetmap.org/way/27297689</a></p>
</div>
<div id="comment-52529-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 12:51)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52530"></span>
<div id="comment-52530" class="comment not_top_scorer">
<div id="post-52530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As SK53 said above, overpass is pretty well documented in the wiki (and has been discussed at length in other questions). Are you allergic to reading documentation? :)</p>
</div>
<div id="comment-52530-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 13:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52541"></span>
<div id="comment-52541" class="comment not_top_scorer">
<div id="post-52541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Friend i understand i went through the documentation and tried many different way to get the overpass query <a href="https://www.openstreetmap.org/way/27297689">https://www.openstreetmap.org/way/27297689</a> but unable to do so, wish you spend plz 2 mins to post the over pass query so i can carry on twiking it to get my area, plz help sorry to toruble</p>
</div>
<div id="comment-52541-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 18:22)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52554"></span>
<div id="comment-52554" class="comment not_top_scorer">
<div id="post-52554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Someone else</p>
<p>Please can you tell me how to get the overpass query for the following map query <a href="https://www.openstreetmap.org/way/27297689">https://www.openstreetmap.org/way/27297689</a></p>
</div>
<div id="comment-52554-info" class="comment-info">
<span class="comment-age">(15 Oct '16, 07:10)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
<span id="52555"></span>
<div id="comment-52555" class="comment">
<div id="post-52555-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Go to <a href="https://overpass-turbo.eu/,">https://overpass-turbo.eu/,</a> open the wizard and run a query for <code>building=train_station around "Croydon, London"</code> -&gt; <a href="http://overpass-turbo.eu/s/jmw">http://overpass-turbo.eu/s/jmw</a></p>
</div>
<div id="comment-52555-info" class="comment-info">
<span class="comment-age">(15 Oct '16, 08:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="52564"></span>
<div id="comment-52564" class="comment not_top_scorer">
<div id="post-52564-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Scai , looks like i can now work from here much appreciated</p>
</div>
<div id="comment-52564-info" class="comment-info">
<span class="comment-age">(17 Oct '16, 08:54)</span> <span class="comment-user userinfo">brightnlight</span>
</div>
</div>
</div>
<div id="comment-tools-52439" class="comment-tools">
<span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-52439-form-container" class="comment-form-container">
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

