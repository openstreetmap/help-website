+++
type = "question"
title = "Errors when downloading a large OSM file from Overpass API"
description = '''I have been experiencing difficulty when trying to download a 2 GB OSM file from the slippy map at https://www.openstreetmap.org. The usual link message appears in the bottom left-hand side of the screen after I make a selection but when I browse to a location to save the file, the download finishes...'''
date = "2021-12-13T11:35:00Z"
lastmod = "2021-12-13T12:15:00Z"
weight = 82821
keywords = [ "fails", "downloading", "slippymap", "overpass-api" ]
aliases = [ "/questions/82821" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Errors when downloading a large OSM file from Overpass API](/questions/82821/errors-when-downloading-a-large-osm-file-from-overpass-api)

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
<span id="post-82821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82821-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been experiencing difficulty when trying to download a 2 GB OSM file from the slippy map at <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a>. The usual link message appears in the bottom left-hand side of the screen after I make a selection but when I browse to a location to save the file, the download finishes in a few seconds and results in a 1 KB file containing the following lines.</p>
<p>&lt;bounds minlat="12.0720000" minlon="97.7010000" maxlat="20.4890000" maxlon="103.1950000"/&gt;</p>
<p>&lt;remark&gt; runtime error: Query ran out of memory in "recurse" at line 1. It would need at least 524 MB of RAM to continue. &lt;/remark&gt;</p>
<p>I do get a download some of the time so I know the server has this capability.</p>
<p>My questions are, what ran out of memory and why?</p>
<p>I could get my OSM data elsewhere but it seems this method should work all the time. It does work maybe one out of 5 times but mostly I get this error. I've used this method for years for compilations of Garmin-compatible maps with mkgmap but never with an area this large.</p>
<p>Is there a solution for this issue? Is it a server loading problem that occurs during busy times of day? Is 2 GB too much to ask for from this server?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fails" rel="tag" title="see questions tagged &#39;fails&#39;">fails</span> <span class="post-tag tag-link-downloading" rel="tag" title="see questions tagged &#39;downloading&#39;">downloading</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '21, 11:35</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82821" class="comments-container">
&#10;</div>
<div id="comment-tools-82821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82821-form-container" class="comment-form-container">
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

<span id="82822"></span>

<div id="answer-container-82822" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82822-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, 2 GB is too much to ask from this server. Try requesting a custom .osm.pbf extract from extract.bbbike.org or from protomaps.com, or download a signle-country .osm.pbf from download.geofabrik.de.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '21, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82822" class="comments-container">
<span id="82823"></span>
<div id="comment-82823" class="comment">
<div id="post-82823-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, thanks.</p>
<p>I'll do that.</p>
</div>
<div id="comment-82823-info" class="comment-info">
<span class="comment-age">(13 Dec '21, 12:15)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-82822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82822-form-container" class="comment-form-container">
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

