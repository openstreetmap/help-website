+++
type = "question"
title = "How to keep OSM maps updated?"
description = '''I have deployed a server on ubuntu for OSM. But it runs for only one countries or continent maps. My question is how we can setup our server that can run API calls for whole world. Also these maps are not updated, how to update these maps and automate the process. Is there a guide or tutorial which ...'''
date = "2019-10-23T20:47:00Z"
lastmod = "2019-10-24T06:48:00Z"
weight = 71290
keywords = [ "qgis", "gis", "osm", "josm" ]
aliases = [ "/questions/71290" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to keep OSM maps updated?](/questions/71290/how-to-keep-osm-maps-updated)

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
<span id="post-71290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71290-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have deployed a server on ubuntu for OSM. But it runs for only one countries or continent maps. My question is how we can setup our server that can run API calls for whole world. Also these maps are not updated, how to update these maps and automate the process. Is there a guide or tutorial which I can follow to setup a full equipped updated server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '19, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/45c1cced3ea049e72e23496b4715be45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vsaadnet&#39;s gravatar image" />
<p><span>vsaadnet</span><br />
<span class="score" title="45 reputation points">45</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vsaadnet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71290" class="comments-container">
<span id="71295"></span>
<div id="comment-71295" class="comment">
<div id="post-71295-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you explain what API calls you intend to make. You have tagged your question "JOSM" and "QGIS". Are you accessing your local server with JOSM, and is your intention to modify the data on the server?</p>
</div>
<div id="comment-71295-info" class="comment-info">
<span class="comment-age">(24 Oct '19, 06:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71290-form-container" class="comment-form-container">
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

<span id="71292"></span>

<div id="answer-container-71292" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71292-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vsaadnet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to serve the whole world then you are probably in the realms of downloading <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">planet.osm</a> and the associated <a href="https://wiki.openstreetmap.org/wiki/Planet.osm/diffs">diffs</a> for updates.</p>
<p>How to apply the updates and automate the process will probably depend on exactly what you are using for your server. The first link above has links to additional resources further down the page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '19, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-71292" class="comments-container">
&#10;</div>
<div id="comment-tools-71292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71292-form-container" class="comment-form-container">
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

