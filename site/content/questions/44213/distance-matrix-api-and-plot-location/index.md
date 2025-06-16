+++
type = "question"
title = "Distance matrix api and plot location"
description = '''Hi there, I am trying to find a way to map 100 addresses on the openstreetmap. I have list of 100 addresses on excel file and i want to locate them on openstreetmap. Is there API to get this done? Apart from this I want to calculate driving distance between each of these locations and create a dista...'''
date = "2015-07-16T00:26:00Z"
lastmod = "2015-07-23T10:14:00Z"
weight = 44213
keywords = [ "api", "osm" ]
aliases = [ "/questions/44213" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Distance matrix api and plot location](/questions/44213/distance-matrix-api-and-plot-location)

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
<span id="post-44213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44213-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, I am trying to find a way to map 100 addresses on the openstreetmap. I have list of 100 addresses on excel file and i want to locate them on openstreetmap. Is there API to get this done?</p>
<p>Apart from this I want to calculate driving distance between each of these locations and create a distance matrix of 100X100.</p>
<p>Please advise me how this could be achieved?</p>
<p>hanks, Ashnav</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '15, 00:26</strong></p>
<img src="https://secure.gravatar.com/avatar/09bd09f31c49d237d773a26f0dc3b88d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashnav&#39;s gravatar image" />
<p><span>Ashnav</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashnav has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44213" class="comments-container">
&#10;</div>
<div id="comment-tools-44213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44213-form-container" class="comment-form-container">
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

<span id="44221"></span>

<div id="answer-container-44221" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44221-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please do not ask two questions in one.</p>
<p>You can use umap: umap.openstreetmap.fr for your first task. You will need to geocode the addresses first if they do not already have coordinate associated with them. You can do the later with nominatim see: <a href="https://wiki.openstreetmap.org/wiki/Nominatim">https://wiki.openstreetmap.org/wiki/Nominatim</a></p>
<p>OSRM has support for generating distance matrices see <a href="http://project-osrm.org/">http://project-osrm.org/</a> and <a href="https://github.com/Project-OSRM/osrm-backend/wiki/Server-api">https://github.com/Project-OSRM/osrm-backend/wiki/Server-api</a></p>
<p>Note: if you are using the public servers providing the above (instead of running them yourselve) you MUST conform to the respective acceptable use policies: <a href="https://wiki.openstreetmap.org/wiki/Acceptable_Use_Policy">https://wiki.openstreetmap.org/wiki/Acceptable_Use_Policy</a> and <a href="https://github.com/Project-OSRM/osrm-backend/wiki/Api-usage-policy">https://github.com/Project-OSRM/osrm-backend/wiki/Api-usage-policy</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '15, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '15, 15:03</strong> </span></p>
</div>
</div>
<div id="comments-container-44221" class="comments-container">
&#10;</div>
<div id="comment-tools-44221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44221-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44389"></span>

<div id="answer-container-44389" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44389-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Cannot comment, still the second question was already asked and <a href="/questions/37861/distance-matrix-api">answered here</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '15, 10:14</strong></p>
<img src="https://secure.gravatar.com/avatar/fec61c70a4cc98b1e84a5dfbde1e9a6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peatar&#39;s gravatar image" />
<p><span>peatar</span><br />
<span class="score" title="351 reputation points">351</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peatar has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-44389" class="comments-container">
&#10;</div>
<div id="comment-tools-44389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44389-form-container" class="comment-form-container">
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

