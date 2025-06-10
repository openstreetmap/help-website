+++
type = "question"
title = "Basic commercial use"
description = '''Hi, as I understood, the project is available for commercial use, and we should make a donation if we should use it, am I right ? My needs are quite simple (only API calls from back office): - geocode European addresses (especially in France+DromCom) to get Lat/Long from a literal address - compute ...'''
date = "2020-06-23T14:57:00Z"
lastmod = "2020-06-23T15:34:00Z"
weight = 75417
keywords = [ "donation", "api", "howto", "basic" ]
aliases = [ "/questions/75417" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Basic commercial use](/questions/75417/basic-commercial-use)

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
<span id="post-75417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>as I understood, the project is available for commercial use, and we should make a donation if we should use it, am I right ?</p>
<p>My needs are quite simple (only API calls from back office): - geocode European addresses (especially in France+DromCom) to get Lat/Long from a literal address - compute the car route between two coordinates, regardless of the traffic</p>
<p>Does these API already exist ?</p>
<p>If I plan to use about up to 100k call a day, could you advice me on the best approach (ie : use openstreetmap on a OnPremise server, what about SLA etc ...)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-donation" rel="tag" title="see questions tagged &#39;donation&#39;">donation</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-howto" rel="tag" title="see questions tagged &#39;howto&#39;">howto</span> <span class="post-tag tag-link-basic" rel="tag" title="see questions tagged &#39;basic&#39;">basic</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jun '20, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/7d8487ab8b6f3779f5cf8c223710fedf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nico69330&#39;s gravatar image" />
<p><span>Nico69330</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nico69330 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75417" class="comments-container">
&#10;</div>
<div id="comment-tools-75417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75417-form-container" class="comment-form-container">
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

<span id="75418"></span>

<div id="answer-container-75418" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75418-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to differentiate between the use of the data (always free and under ODbL license) and the use of computing services (limited resource, funded through donations, operated by volunteers). 100k calls a day is definitely more than we can accept on the free computing services made available by the project, and we cannot take donations in exchange for more server use.</p>
<p>The services you want to use are Nominatim (for geocoding) and a routing service like OSRM or Graphhopper. The free, community-run versions of these services are nominatim.openstreetmap.org and routing.openstreetmap.de.</p>
<p>If you want to use these services with the intensity you mention, you should either install the software on your own systems (everything is Open Source and free of charge), or buy the service from a commercial provider. Our wiki has a list of companies in various regions offering these services: <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '20, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jun '20, 15:04</strong> </span></p>
</div>
</div>
<div id="comments-container-75418" class="comments-container">
&#10;</div>
<div id="comment-tools-75418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75418-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75420"></span>

<div id="answer-container-75420" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75420-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for your quick feedback I'll have a check on this</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '20, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7d8487ab8b6f3779f5cf8c223710fedf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nico69330&#39;s gravatar image" />
<p><span>Nico69330</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nico69330 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75420" class="comments-container">
&#10;</div>
<div id="comment-tools-75420" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75420-form-container" class="comment-form-container">
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

