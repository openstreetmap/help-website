+++
type = "question"
title = "Limits per day problem - supply chain optimization algorithm"
description = '''I am planning to do a PhD in supply chain optimization. I want to solve a warehouse localization problem. I have 120 long, alt addresses in West Europe. I need to calculate distances when using a clustering algorithm, then use a grid to locate the best option for the warehouse. For this purpose I wi...'''
date = "2015-11-28T18:08:00Z"
lastmod = "2015-12-01T06:09:00Z"
weight = 46873
keywords = [ "day", "limits", "algorithm", "per" ]
aliases = [ "/questions/46873" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Limits per day problem - supply chain optimization algorithm](/questions/46873/limits-per-day-problem-supply-chain-optimization-algorithm)

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
<span id="post-46873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46873-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am planning to do a PhD in supply chain optimization. I want to solve a warehouse localization problem. I have 120 long, alt addresses in West Europe. I need to calculate distances when using a clustering algorithm, then use a grid to locate the best option for the warehouse. For this purpose I will need to calculate the distances approximately 120 thousand times. I think opensteetmap is the best option for this problem.</p>
<ol>
<li><p>Can anybody provide some information from what to start? For now I have an algorithm made with Wolfram Mathematica, However I didn’t find any openstreetmap scripts that would work with this software.</p></li>
<li><p>Is there any finished application that I could use and communicate with it easily? E.g. googlemap api works, however it has a 2500 day limit and extra calculations would cost a lot.</p></li>
<li><p>Is it possible to use simply a web link, that wouldn’t have any limitations? Maybe someone could provide it and for a few days turn off the limits for my IP address?</p></li>
<li><p>If no, how should I use openstreetmap to solve this problem? Do I need to download the osm planet file and write the code to return the distance between A and B, or is there any completed solutions? I would need to remake the algorithm with another programming language in this case.</p></li>
</ol>
<p>I would be really grateful for any advice or help,</p>
<p>thank you in advanced</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-day" rel="tag" title="see questions tagged &#39;day&#39;">day</span> <span class="post-tag tag-link-limits" rel="tag" title="see questions tagged &#39;limits&#39;">limits</span> <span class="post-tag tag-link-algorithm" rel="tag" title="see questions tagged &#39;algorithm&#39;">algorithm</span> <span class="post-tag tag-link-per" rel="tag" title="see questions tagged &#39;per&#39;">per</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '15, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/61e048992e78d3ec65399605528e41a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ValentasG&#39;s gravatar image" />
<p><span>ValentasG</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ValentasG has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46873" class="comments-container">
<span id="46874"></span>
<div id="comment-46874" class="comment">
<div id="post-46874-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See also <a href="http://forum.openstreetmap.org/viewtopic.php?pid=563563#p563563">http://forum.openstreetmap.org/viewtopic.php?pid=563563#p563563</a> (crosspost)</p>
</div>
<div id="comment-46874-info" class="comment-info">
<span class="comment-age">(28 Nov '15, 20:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46873" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46873-form-container" class="comment-form-container">
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

<span id="46877"></span>

<div id="answer-container-46877" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46877-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There might be web routing algorithms that aren't protectd well enough to kick you out when you make 120k requests but you really shouldn't. It is much better - and it is the beauty of OSM that this is possible - to download the data and run your own routing software on it. There's Europe-only data extracts e.g. at download.geofabrik.de, and you can easily feed them into OSRM or Graphhopper - both free and open source routing engines that work with OSM data out of the box. Both have a HTTP API that you could use locally, but OSRM is in C++ with NodeJS bindings and Graphhopper is in Java, so it would probably be possible to integrate them into your application in a more direct fashion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '15, 20:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46877" class="comments-container">
<span id="46878"></span>
<div id="comment-46878" class="comment">
<div id="post-46878-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik for your replay.</p>
<p>When I used googlemaps API, I simply provided the long and alt coordinates and the API returned the distance. As I understand I can do the same thing by hosting a local map API on my own computer? Or I will need to rewrite my algorithm with C++ or Java?</p>
<p>I have checked graphhopper and it should be just the thing that I need, however as I understood I have still a query limit? "To increase your query limits for production you pay online within a few minutes via credit card or debit advice." As a free user I have the same amount as with googlemap api "500 per day". Or if I use a local computer the limits won't concern me?</p>
<p>I am downloading europe-latest.osm.pbf file, so thank you again for the tips :)</p>
</div>
<div id="comment-46878-info" class="comment-info">
<span class="comment-age">(28 Nov '15, 21:35)</span> <span class="comment-user userinfo">ValentasG</span>
</div>
</div>
<span id="46885"></span>
<div id="comment-46885" class="comment">
<div id="post-46885-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The limit doesn't apply for a local installation, of course.</p>
</div>
<div id="comment-46885-info" class="comment-info">
<span class="comment-age">(29 Nov '15, 09:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46893"></span>
<div id="comment-46893" class="comment">
<div id="post-46893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think there's one basic Graphhopper package and one API package, and if you install the API then you can access your own local Graphhopper through a web API just like you did with Google. And no, there won't be limits other than how fast your hardware can go ;)</p>
</div>
<div id="comment-46893-info" class="comment-info">
<span class="comment-age">(29 Nov '15, 14:55)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46877-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46910"></span>

<div id="answer-container-46910" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46910-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm assuming by distance, you're talking about road length distance or travel time. If you're after direct line distance, this can easily be calculated by simple math from the latitude and longitude.</p>
<p>OSRM offers a <a href="https://github.com/Project-OSRM/osrm-backend/wiki/Server-api#service-table">table</a> query which would probably reduce the number of calls you need to make. Their <a href="https://github.com/Project-OSRM/osrm-backend/wiki/API%20Usage%20Policy">usage policy</a> seems to allow you to do this with the publicly available server, but if you wanted to run your own server you could do it and you'd only need to load data for the part of Western Europe you need.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '15, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-46910" class="comments-container">
<span id="46911"></span>
<div id="comment-46911" class="comment">
<div id="post-46911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I am talking about the distance and travel time between. I am using now a simply, math formula, however for a correct optimization algorithm I need real distances between points. I understand that I need to do offline routing, because I will need to make requests about 120 thousand times. Otherwise, my IP should get blocked.</p>
<p>I have finished a algorithm with Wolfram Mathematica, I am working with googlemaps API distdata = Import["http://maps.googleapis.com/maps/api/directions/json?origin=" &lt;&gt; from &lt;&gt; "&amp;destination=" &lt;&gt; to &lt;&gt; "&amp;region=es&amp;sensor=false", {"HTML", "Source"}]; roadDistance = StringSplit[StringSplit[distdata, ":"][[13]],","][[1]] travelTime = StringSplit[StringSplit[distdata, ":"][[16]], ","][[1]]"</p>
<p>I would like similarly to googlemaps API provide longitude altitude coordinates for point A and B and receive back the distance and travel time for car/truck type vehicle. I have a recommendation to use GraphHopper with Java script. Launching a server would be difficult in this case. It is not necessary to rewrite my algorithm with Java script? Communication between Wolfram Mathematica and OSM should be possible? But how should I do it?</p>
</div>
<div id="comment-46911-info" class="comment-info">
<span class="comment-age">(30 Nov '15, 19:18)</span> <span class="comment-user userinfo">ValentasG</span>
</div>
</div>
<span id="46916"></span>
<div id="comment-46916" class="comment">
<div id="post-46916-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please note that there is no free solution based on OSM that allows you to make that many requests. It costs money to run a server with the whole planet dump and to provide bandwidth for so many requests. I think you either have to run your local server (and thus pay the cost) or pay for a geocoding solution.</p>
<p>See Frederiks comment on <a href="/questions/46914/nominatim-alternative">https://help.openstreetmap.org/questions/46914/nominatim-alternative</a> which states the same</p>
</div>
<div id="comment-46916-info" class="comment-info">
<span class="comment-age">(01 Dec '15, 06:09)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-46910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46910-form-container" class="comment-form-container">
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

