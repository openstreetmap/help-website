+++
type = "question"
title = "how to extract all address from PBF in exactly one city?"
description = '''I have PBF file from geofabrik with my country with many cities Now I want extract address names with building numbers and coordinates for autocompete service in one city I newbie in OSM and I have to learn many things ))'''
date = "2018-08-23T09:10:00Z"
lastmod = "2018-08-23T12:04:00Z"
weight = 65527
keywords = [ "openstreetmap", "pbf", "extract", "osmosis", "address" ]
aliases = [ "/questions/65527" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to extract all address from PBF in exactly one city?](/questions/65527/how-to-extract-all-address-from-pbf-in-exactly-one-city)

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
<span id="post-65527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65527-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have PBF file from geofabrik with my country with many cities Now I want extract address names with building numbers and coordinates for autocompete service in one city I newbie in OSM and I have to learn many things ))</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '18, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/876a2d7a65b56435df43e3ee4eb41d1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stremovskyy&#39;s gravatar image" />
<p><span>Stremovskyy</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stremovskyy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65527" class="comments-container">
&#10;</div>
<div id="comment-tools-65527" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65527-form-container" class="comment-form-container">
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

<span id="65530"></span>

<div id="answer-container-65530" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65530-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-65530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Stremovskyy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The basic outline is to use a tool like osmium to slice out the city and then to dump out the objects you are interested in.</p>
<p>The documentation has sections called "Creating geographic extracts" and "Filtering by tags" so I won't say more here:</p>
<p><a href="https://osmcode.org/osmium-tool/manual.html">https://osmcode.org/osmium-tool/manual.html</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Category:OSM_processing">There's a variety of similar tools</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '18, 12:04</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '18, 15:27</strong> </span></p>
</div>
</div>
<div id="comments-container-65530" class="comments-container">
&#10;</div>
<div id="comment-tools-65530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65530-form-container" class="comment-form-container">
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

