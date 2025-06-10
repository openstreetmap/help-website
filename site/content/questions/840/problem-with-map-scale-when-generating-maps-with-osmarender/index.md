+++
type = "question"
title = "Problem with map scale when generating maps with Osmarender"
description = '''I have to render custom and Osmarender maps for my University. At the moment I get it done by hand, but something doesn’t work properly when I’m generating the PNGs and the tiles from it. The tiles become bigger than they should. To be precise, they don’t become bigger, but they are scaled up and do...'''
date = "2010-09-17T16:00:00Z"
lastmod = "2010-09-18T15:33:00Z"
weight = 840
keywords = [ "rendering", "tiles", "scale", "osmarender", "tiles-home" ]
aliases = [ "/questions/840" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with map scale when generating maps with Osmarender](/questions/840/problem-with-map-scale-when-generating-maps-with-osmarender)

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
<span id="post-840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-840-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have to render custom and Osmarender maps for my University. At the moment I get it done by hand, but something doesn’t work properly when I’m generating the PNGs and the tiles from it. The tiles become bigger than they should. To be precise, they don’t become bigger, but they are scaled up and don’t have the exact scale of the ones used on OpenStreetMap.</p>
<p>I already tried to circumvent this error by using the Tiles@Home toolchain, but that’s not as easily manageble as I expected. I have to modify/rewrite the <code>tilesGen.pl</code> perl script, since I don’t want to upload the tiles to the OSM servers.</p>
<p>Is anybody aware of my problem? Maybe there is a better way for solving this. It would be great, if there was an solution.</p>
<p>I appreciate every hint that you give me. Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-scale" rel="tag" title="see questions tagged &#39;scale&#39;">scale</span> <span class="post-tag tag-link-osmarender" rel="tag" title="see questions tagged &#39;osmarender&#39;">osmarender</span> <span class="post-tag tag-link-tiles-home" rel="tag" title="see questions tagged &#39;tiles-home&#39;">tiles-home</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '10, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0eb3d00c9ec081fd0cf97aebe48d1e8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pvorb&#39;s gravatar image" />
<p><span>pvorb</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pvorb has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>18 Sep '10, 17:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-840" class="comments-container">
&#10;</div>
<div id="comment-tools-840" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-840-form-container" class="comment-form-container">
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

<span id="842"></span>

<div id="answer-container-842" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-842-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pvorb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My hint: try using <a href="http://maperitive.net">Maperitive</a>. It can generate bitmaps, SVGs and tiles and there are a lot options you can play with. And it's a desktop application and requires minimum set up.</p>
<p>Example: <a href="http://maperitive.net/docs/manual/Commands/ExportBitmap.html\">export-bitmap</a> command.</p>
<p>I'm the author, BTW.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '10, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-842" class="comments-container">
&#10;</div>
<div id="comment-tools-842" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-842-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="844"></span>

<div id="answer-container-844" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-844-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I tried some of the features of Maperitive already. It is pretty awesome and increadibly fast.</p>
<p>Now I have to learn how to write my own rendering rules for Maperitive and then I will port my Osmarender rules to Maperitive.</p>
<p>This is not exactly what I asked for, but it solves my problem. So I’ll mark your answer as accepted. Thank you very much for your help!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '10, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/0eb3d00c9ec081fd0cf97aebe48d1e8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pvorb&#39;s gravatar image" />
<p><span>pvorb</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pvorb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-844" class="comments-container">
&#10;</div>
<div id="comment-tools-844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-844-form-container" class="comment-form-container">
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

