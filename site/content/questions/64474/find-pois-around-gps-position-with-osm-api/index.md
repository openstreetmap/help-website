+++
type = "question"
title = "Find POIs around GPS position with OSM API"
description = '''Hello, First of all, thank you for your work on OSM, it&#x27;s awesome ! I want to use OpenStreetMap API to be able from my mobile app to find POIs like for instance supermarkets around a GPS position. I am not really sure how to do and I could not find in the Wiki the section talking about POIs (or anyt...'''
date = "2018-07-01T17:34:00Z"
lastmod = "2018-07-02T17:48:00Z"
weight = 64474
keywords = [ "api", "osm", "gps" ]
aliases = [ "/questions/64474" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Find POIs around GPS position with OSM API](/questions/64474/find-pois-around-gps-position-with-osm-api)

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
<span id="post-64474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64474-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>First of all, thank you for your work on OSM, it's awesome !</p>
<p>I want to use OpenStreetMap API to be able from my mobile app to find POIs like for instance supermarkets around a GPS position. I am not really sure how to do and I could not find in the Wiki the section talking about POIs (or anything that could solve my problem). Do you have any idea or example of an API request which would give such result ?</p>
<p>Thank you !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '18, 17:34</strong></p>
<img src="https://secure.gravatar.com/avatar/317eb4ff95d621c752550f54d4212a6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Howls&#39;s gravatar image" />
<p><span>Howls</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Howls has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64474" class="comments-container">
&#10;</div>
<div id="comment-tools-64474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64474-form-container" class="comment-form-container">
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

<span id="64475"></span>

<div id="answer-container-64475" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64475-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OSM API is for editing, not a general purpose API.</p>
<p>You should be looking at the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">overpass API</a> or offline solutions on device.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '18, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '18, 18:42</strong> </span></p>
</div>
</div>
<div id="comments-container-64475" class="comments-container">
&#10;</div>
<div id="comment-tools-64475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64475-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64481"></span>

<div id="answer-container-64481" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64481-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The app may work for you. <a href="https://wiki.openstreetmap.org/wiki/MAPS.ME">https://wiki.openstreetmap.org/wiki/MAPS.ME</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '18, 17:48</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-64481" class="comments-container">
&#10;</div>
<div id="comment-tools-64481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64481-form-container" class="comment-form-container">
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

