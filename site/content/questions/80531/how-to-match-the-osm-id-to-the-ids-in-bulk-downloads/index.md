+++
type = "question"
title = "How to match the OSM ID to the ids in bulk downloads?"
description = '''Hi, I have a large number of OSM IDs such as the Relation 2172991 corresponding mostly to administrative boundaries.  I am now trying to match these against the ids in (for example) the bbbike bulk download but I am running into issues as the IDs do not match at all.  I know that relying on stable O...'''
date = "2021-06-11T13:55:00Z"
lastmod = "2021-06-11T14:01:00Z"
weight = 80531
keywords = [ "bulk", "nominatim", "id" ]
aliases = [ "/questions/80531" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to match the OSM ID to the ids in bulk downloads?](/questions/80531/how-to-match-the-osm-id-to-the-ids-in-bulk-downloads)

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
<span id="post-80531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80531-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have a large number of OSM IDs such as the <a href="https://www.openstreetmap.org/relation/29714">Relation 2172991</a> corresponding mostly to administrative boundaries.</p>
<p>I am now trying to match these against the ids in (for example) the <a href="https://download.bbbike.org/osm/bbbike/">bbbike bulk download</a> but I am running into issues as the IDs do not match at all.</p>
<p>I know that relying on stable OSM IDs is not advisable and I can always re-query the locations that have changed from nominatim but I am a bit lost on how to approach this issue.</p>
<p>If at all possible I do not want to use the lookup endpoint of nominatim in order to keep the load on the OSM servers as little as possible.</p>
<p>Best</p>
<p>Frederic</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bulk" rel="tag" title="see questions tagged &#39;bulk&#39;">bulk</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '21, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/608289a49f79fc0b01c186d197b8005c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FDenker&#39;s gravatar image" />
<p><span>FDenker</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FDenker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80531" class="comments-container">
<span id="80532"></span>
<div id="comment-80532" class="comment">
<div id="post-80532-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The IDs should certainly match any downloads from bbbike or Geofabrik. Have you considered that Nodes, Ways, and Relations each have an independent number range i.e. there is a way #2172991 and a node #2172991 in addition to your relation?</p>
</div>
<div id="comment-80532-info" class="comment-info">
<span class="comment-age">(11 Jun '21, 14:01)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80531-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

