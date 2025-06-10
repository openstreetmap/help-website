+++
type = "question"
title = "Processed coastline projection ?"
description = '''I&#x27;ve downloaded the processed_p coastline in shp format. Assigning Mercator at import seems to produce the &quot;nearest&quot; result, but I have still around 8&#x27; South (latitude) difference and longitude is OK, compared to the other OSM layers witch comes with good position. My region is 166E 22S.'''
date = "2013-08-08T06:48:00Z"
lastmod = "2013-08-09T12:05:00Z"
weight = 25059
keywords = [ "coastline" ]
aliases = [ "/questions/25059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Processed coastline projection ?](/questions/25059/processed-coastline-projection)

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
<span id="post-25059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25059-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've downloaded the processed_p coastline in shp format. Assigning Mercator at import seems to produce the "nearest" result, but I have still around 8' South (latitude) difference and longitude is OK, compared to the other OSM layers witch comes with good position. My region is 166E 22S.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '13, 06:48</strong></p>
<img src="https://secure.gravatar.com/avatar/eb72ffe09501ab600bf1a807e6bc787a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nubernc&#39;s gravatar image" />
<p><span>nubernc</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nubernc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25059" class="comments-container">
&#10;</div>
<div id="comment-tools-25059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25059-form-container" class="comment-form-container">
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

<span id="25063"></span>

<div id="answer-container-25063" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25063-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are different types of Mercator projections. You may have grabbed the wrong one. processed_p is in EPSG:3857. But if you're reprojecting anyway then don't bother with processed_p, get the EPSG:4326 file that Jochen Topf makes available at <a href="http://openstreetmapdata.com/">http://openstreetmapdata.com/</a> and load that. This has the additional benefit of including data north of 85°N and south of 85°S.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '13, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-25063" class="comments-container">
<span id="25119"></span>
<div id="comment-25119" class="comment">
<div id="post-25119-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Fine, I found a land-polygons-split-4326 file wich is perfect, thanks. I'am newbe (first post) on this list, what do you mean with "cast your vote"</p>
</div>
<div id="comment-25119-info" class="comment-info">
<span class="comment-age">(09 Aug '13, 12:05)</span> <span class="comment-user userinfo">nubernc</span>
</div>
</div>
</div>
<div id="comment-tools-25063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25063-form-container" class="comment-form-container">
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

