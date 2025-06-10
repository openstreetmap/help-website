+++
type = "question"
title = "Setting up own map server for routing."
description = '''I want to build my own map server which users can use for routing, directions etc. Currently, I have only st up an OSRM server which can send back json response using this tutorial here and it works perfect for me. Now I want to take it to the next level and implement tiles like, users get to see th...'''
date = "2019-11-09T09:02:00Z"
lastmod = "2019-11-10T09:39:00Z"
weight = 71560
keywords = [ "openrouteservice", "osrm", "nominatim", "osm", "tileserver" ]
aliases = [ "/questions/71560" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Setting up own map server for routing.](/questions/71560/setting-up-own-map-server-for-routing)

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
<span id="post-71560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71560-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to build my own map server which users can use for routing, directions etc. Currently, I have only st up an OSRM server which can send back json response using this tutorial <a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-an-osrm-server-on-ubuntu-14-04">here</a> and it works perfect for me. Now I want to take it to the next level and implement tiles like, users get to see their route and maps. I also want to add an auto-complete address functionality. I have read a lot of articles like these <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">here</a> and its further links down. But I am not getting it together. Will following these steps help me achieve my goal. What tutorial should i look for auto-complete, is Nominatim or Pelias is required and how they can be integrated with OSM. Basically I want to build something similar to <a href="https://openrouteservice.org/">openrouteservice</a> o my own server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openrouteservice" rel="tag" title="see questions tagged &#39;openrouteservice&#39;">openrouteservice</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '19, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/45c1cced3ea049e72e23496b4715be45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vsaadnet&#39;s gravatar image" />
<p><span>vsaadnet</span><br />
<span class="score" title="45 reputation points">45</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vsaadnet has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Nov '19, 10:27</strong> </span></p>
</div>
</div>
<div id="comments-container-71560" class="comments-container">
&#10;</div>
<div id="comment-tools-71560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71560-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="71574"></span>

<div id="answer-container-71574" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71574-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vsaadnet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Photon is the easiest solution for autocomplete geocoding: <a href="http://photon.komoot.de">http://photon.komoot.de</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '19, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-71574" class="comments-container">
<span id="71576"></span>
<div id="comment-71576" class="comment">
<div id="post-71576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I learned about photon, but my problem is now that i have osrm backend set up how to have the front-end up and running that shows polyline/maps to users. should i have my own tile server for that, as OSRM front-end is not running on my system it says <code>localhost:9966 secure connection failed</code></p>
</div>
<div id="comment-71576-info" class="comment-info">
<span class="comment-age">(10 Nov '19, 09:39)</span> <span class="comment-user userinfo">vsaadnet</span>
</div>
</div>
</div>
<div id="comment-tools-71574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71574-form-container" class="comment-form-container">
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

