+++
type = "question"
title = "How to get all the editing history for POI"
description = '''Hello everyone,  We are conducting a research by using OSM, and We would like to get all editing history ( changesets ) of all POI&#x27;s names in a particular area, such as a city or state. However, we were able to get the history of only one node, way, or relation. https://www.openstreetmap.org/api/0.6...'''
date = "2017-06-30T17:28:00Z"
lastmod = "2017-07-04T03:11:00Z"
weight = 56819
keywords = [ "api", "overpass", "editing", "osm", "poi" ]
aliases = [ "/questions/56819" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get all the editing history for POI](/questions/56819/how-to-get-all-the-editing-history-for-poi)

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
<span id="post-56819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56819-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>We are conducting a research by using OSM, and We would like to get all editing history ( changesets ) of all POI's names in a particular area, such as a city or state. However, we were able to get the history of only one node, way, or relation. <a href="https://www.openstreetmap.org/api/0.6/node/708866092/history">https://www.openstreetmap.org/api/0.6/node/708866092/history</a> This link shows an example. " We are focusing just on the POI's names, the user who did create the POI or the change, AND the category of the POI."</p>
<p>We searched on the Internet and found that getting what we want could be through downloading "Latest Weekly Changesets" in <a href="http://planet.openstreetmap.org/">http://planet.openstreetmap.org/</a> Could you please help us if there is an easier way to get all editing history of a specific area? such as OSM API, overpass-turbo.eu, Overpass API .. etc</p>
<p>*We are using Python as a programming language, any recommended tutorial?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '17, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/38959e012175f9594b4628cef77ea6c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aaabuabat&#39;s gravatar image" />
<p><span>aaabuabat</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aaabuabat has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56819" class="comments-container">
&#10;</div>
<div id="comment-tools-56819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56819-form-container" class="comment-form-container">
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

<span id="56826"></span>

<div id="answer-container-56826" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56826-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download the full history data from <a href="http://planet.osm.org/planet/full-history/">http://planet.osm.org/planet/full-history/</a> . You can use the Osmium tool to extract an area from this history file using the <a href="http://docs.osmcode.org/osmium/latest/osmium-extract.html">extract</a> command. You can then use <a href="http://osmcode.org/pyosmium/">pyosmium</a> to read that data from Python and get the data out in any way you like. Just be aware that OSM history data is messy and difficult to understand. You really have to understand the OSM data model in detail to interpret this data correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '17, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-56826" class="comments-container">
<span id="56867"></span>
<div id="comment-56867" class="comment">
<div id="post-56867-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your help and cooperation.</p>
</div>
<div id="comment-56867-info" class="comment-info">
<span class="comment-age">(04 Jul '17, 03:11)</span> <span class="comment-user userinfo">aaabuabat</span>
</div>
</div>
</div>
<div id="comment-tools-56826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56826-form-container" class="comment-form-container">
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

