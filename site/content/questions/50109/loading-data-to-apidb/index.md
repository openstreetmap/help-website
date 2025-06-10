+++
type = "question"
title = "Loading data to APIdb"
description = '''Im trying to upload 8GB osm file into API db, i truncated it before so its empty but as it appears its not. Postres throws error duplicated key. What is the best way to add new region to map, or how to clear data, so that configuration remains unchanged? Here is my osmosis command:  nohup osmosis --...'''
date = "2016-06-09T15:53:00Z"
lastmod = "2016-06-10T09:18:00Z"
weight = 50109
keywords = [ "api", "osmosis" ]
aliases = [ "/questions/50109" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Loading data to APIdb](/questions/50109/loading-data-to-apidb)

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
<span id="post-50109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50109-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Im trying to upload 8GB osm file into API db, i truncated it before so its empty but as it appears its not. Postres throws error duplicated key. What is the best way to add new region to map, or how to clear data, so that configuration remains unchanged?</p>
<p>Here is my osmosis command: nohup osmosis --read-xml file.osm --write-apidb authFile=Auth.txt validateSchemaVersion=no 2&gt; errorOutput.txt &gt; output.txt &amp;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '16, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/016ab1463a1f9187246270165f1a0a25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorax&#39;s gravatar image" />
<p><span>jorax</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorax has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50109" class="comments-container">
<span id="50112"></span>
<div id="comment-50112" class="comment">
<div id="post-50112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Without seeing the data we can only speculate...</p>
<p>Assuming that the API db was really empty, maybe you're somehow trying to load the same thing twice?</p>
</div>
<div id="comment-50112-info" class="comment-info">
<span class="comment-age">(09 Jun '16, 19:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50117"></span>
<div id="comment-50117" class="comment">
<div id="post-50117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded 3 countries from geofabrik and merged them with osmosis. I dont think geofabrik files overlap with each other. Besides i used grep to scan for this duplicated id. It was found only once. I used --truncate-apidb before, but my guess is it doesnt work as it should. Is there any other way to append missing data? Somthing that will ignore duplicated data?</p>
</div>
<div id="comment-50117-info" class="comment-info">
<span class="comment-age">(09 Jun '16, 21:07)</span> <span class="comment-user userinfo">jorax</span>
</div>
</div>
</div>
<div id="comment-tools-50109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50109-form-container" class="comment-form-container">
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

<span id="50118"></span>

<div id="answer-container-50118" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50118-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://help.openstreetmap.org/questions/45930/osmosis-import-duplicate-key-value-violates-unique-constraint">https://help.openstreetmap.org/questions/45930/osmosis-import-duplicate-key-value-violates-unique-constraint</a></p>
<p>outdated osmosis was the reason. Im using updated version right now. I'll post if this solved the problem but im pretty sure it will. Kinda sad that apt-get update doesn't work here, i had to install it manually.</p>
<p>EDIT: confirmed, remember always to use updated tools</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '16, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/016ab1463a1f9187246270165f1a0a25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorax&#39;s gravatar image" />
<p><span>jorax</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorax has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '16, 11:30</strong> </span></p>
</div>
</div>
<div id="comments-container-50118" class="comments-container">
&#10;</div>
<div id="comment-tools-50118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50118-form-container" class="comment-form-container">
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

