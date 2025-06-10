+++
type = "question"
title = "Install nominatim with either valhalla or overpass indexed database"
description = '''Thanks for providing the platform to post queries. I have installed my own instances of valhalla and overpass using docker. The base OSM pbf file is same for both instances but underlying data model is different as they do different indexing using that pbf file. My question is, Can I use same underl...'''
date = "2023-11-09T07:37:00Z"
lastmod = "2023-11-10T07:04:00Z"
weight = 87981
keywords = [ "overpass", "nominatim", "valhalla" ]
aliases = [ "/questions/87981" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Install nominatim with either valhalla or overpass indexed database](/questions/87981/install-nominatim-with-either-valhalla-or-overpass-indexed-database)

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
<span id="post-87981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87981-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Thanks for providing the platform to post queries.</p>
<p>I have installed my own <strong>instances of valhalla and overpass using docker</strong>. The base OSM pbf file is same for both instances but underlying data model is different as they do different indexing using that pbf file. My question is, <strong>Can I use same underlying data structure of either valhalla or overpass to install nominatim instead of indexing different structure for nominatim?</strong>. It will save my hardware resources like RAM, disk space etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-valhalla" rel="tag" title="see questions tagged &#39;valhalla&#39;">valhalla</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '23, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/fccef35139e101c47c404c9f1ae8fbe9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akhil401&#39;s gravatar image" />
<p><span>akhil401</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akhil401 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87981" class="comments-container">
&#10;</div>
<div id="comment-tools-87981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87981-form-container" class="comment-form-container">
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

<span id="87982"></span>

<div id="answer-container-87982" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87982-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-87982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. Nominatim has its own data structure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '23, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-87982" class="comments-container">
<span id="87987"></span>
<div id="comment-87987" class="comment">
<div id="post-87987-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Jochen Topf. Correct me If I am wrong, I know that nominatim uses PostgreSQL database where as valhalla uses tile graph data structure and overpass uses indexed data structure. Is there any tool/mechanism to convert valhalla/overpass data structure to nominatim data structure? OR Is it possible can valhalla/overpass do geocoding and reverse geocoding instead of having nominatim?</p>
</div>
<div id="comment-87987-info" class="comment-info">
<span class="comment-age">(10 Nov '23, 07:04)</span> <span class="comment-user userinfo">akhil401</span>
</div>
</div>
</div>
<div id="comment-tools-87982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87982-form-container" class="comment-form-container">
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

