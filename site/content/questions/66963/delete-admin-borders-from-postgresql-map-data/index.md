+++
type = "question"
title = "Delete Admin borders from postgresql map data"
description = '''Hi, I have setup my own tile server and rendered India Map. I want to remove admin boundary. It was suggested in a post that you can achieve this by deleting admin borders from postgresql map database. Can somebody help and tell me what do I need to do to remove admin boundary from the map I am rend...'''
date = "2018-11-28T13:01:00Z"
lastmod = "2018-11-30T13:15:00Z"
weight = 66963
keywords = [ "boundaries" ]
aliases = [ "/questions/66963" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Delete Admin borders from postgresql map data](/questions/66963/delete-admin-borders-from-postgresql-map-data)

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
<span id="post-66963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66963-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have setup my own tile server and rendered India Map. I want to remove admin boundary. It was suggested in a post that you can achieve this by deleting admin borders from postgresql map database.</p>
<p>Can somebody help and tell me what do I need to do to remove admin boundary from the map I am rendering from my server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '18, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66963" class="comments-container">
&#10;</div>
<div id="comment-tools-66963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66963-form-container" class="comment-form-container">
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

<span id="67007"></span>

<div id="answer-container-67007" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67007-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should look at the corresponding layer configuration in the osm-carto style (see <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml#L1140">https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml#L1140</a> and <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/admin.mss)">https://github.com/gravitystorm/openstreetmap-carto/blob/master/admin.mss)</a> (if you are using that) and either remove the corresponding data from the database (not something that I would recommend), or simply remove/disable the corresponding layer configuration in the style (you could then add a border layer from another source for example).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '18, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '18, 13:18</strong> </span></p>
</div>
</div>
<div id="comments-container-67007" class="comments-container">
&#10;</div>
<div id="comment-tools-67007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67007-form-container" class="comment-form-container">
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

