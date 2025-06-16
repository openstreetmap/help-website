+++
type = "question"
title = "How to remove a repeated (not duplicate) node present in a same way?"
description = '''I am working on importing a number of ways obtained as a result of vectorizing of a raster map. Because of the nature of the source data and as a result of chosen curve smoothing algorithm there are many cases when a single way intersects itself. In general, self-intersection has no automatic resolu...'''
date = "2019-04-04T09:40:00Z"
lastmod = "2019-04-04T11:16:00Z"
weight = 68631
keywords = [ "josm", "self-intersection" ]
aliases = [ "/questions/68631" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to remove a repeated (not duplicate) node present in a same way?](/questions/68631/how-to-remove-a-repeated-not-duplicate-node-present-in-a-same-way)

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
<span id="post-68631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68631-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on importing a number of ways obtained as a result of vectorizing of a raster map. Because of the nature of the source data and as a result of chosen curve smoothing algorithm there are many cases when a single way intersects itself. In general, self-intersection has no automatic resolution in e.g. JOSM and requires human intervention, which in my case would be many hundreds of edits.</p>
<p>However, in my case it is always a very specific type of self-intersection that should rather be described as a "self-touching way". Let me illustrate it.</p>
<p><img src="/upfiles/self-touching.JPG" alt="intersection" /></p>
<p>On the image above pay attention that there is a node an the intersection point, at direction of individual segments make it so that the right part of the "eight"-like figure touches the left part of it in that point. So it is not two duplicate notes (different IDs but same coordinates) but rather a single node (the same ID) that is present two times in a same way. Inspecting the OSM XML confirms this observation.</p>
<p>An algorithmic solution that is possible in this case is to remove one occurrence of that repeating node from the way. The result of such transformation for my example is below:</p>
<p><img src="/upfiles/split.JPG" alt="split" /></p>
<p>This transformation reaches the goal of preserving a "waistline" in the eight-shaped polygon, only making it slightly "thicker". This is an acceptable approximation given the resolution of the original raster data and noise already present in it.</p>
<p>The same effect can be achieved manually: a) duplicate the node, b) delete one of the copied nodes.</p>
<p>Such a solution is fine for my application and is guaranteed to create no new self-intersections because of the way the polygon is oriented (orientation of the top circle and the bottom circle always match).</p>
<p>I can come up with a solution that involves scripted editing of the underlying OSM-XML (see my own answer below). But I wonder <strong>if there are solutions to do it automatically without the need to export to OSM format, e.g. directly in the JOSM editor.</strong></p>
<p><em>P.S.</em> An alternative solution is to create two independent ways touching each other at the central node (upper circle and a lower circle). It is a bit harder to do when editing an XML in a sense that new ways have to be allocated, but is also acceptable for me if there are ready tools to do that.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-self-intersection" rel="tag" title="see questions tagged &#39;self-intersection&#39;">self-intersection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '19, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0b00a1d4f3b4a6a9ce38c875c482aba1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Atakua&#39;s gravatar image" />
<p><span>Atakua</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Atakua has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-68631" class="comments-container">
&#10;</div>
<div id="comment-tools-68631" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68631-form-container" class="comment-form-container">
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

<span id="68632"></span>

<div id="answer-container-68632" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68632-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My own solution so far is to export the JOSM layer into an OSM XML file. Then to use a scripted language capable of processing XML (Python or any other really) to open the file and do the following.</p>
<ul>
<li>For each way check if there are repeating node IDs ("ref" tag) included into it.</li>
<li>If there are such repetitions, keep only one of them</li>
<li>Make an exception for the first and the last node reference in the way. For closed ways their IDs are the same.</li>
</ul>
<p>As I mentioned already, applying such script requires exporting data from JOSM, processing it and then reopening it in JOSM for further processing and uploading to the database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '19, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0b00a1d4f3b4a6a9ce38c875c482aba1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Atakua&#39;s gravatar image" />
<p><span>Atakua</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Atakua has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-68632" class="comments-container">
<span id="68637"></span>
<div id="comment-68637" class="comment">
<div id="post-68637-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Has your import actually gone through this process <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">https://wiki.openstreetmap.org/wiki/Import/Guidelines</a> ?</p>
</div>
<div id="comment-68637-info" class="comment-info">
<span class="comment-age">(04 Apr '19, 10:50)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="68639"></span>
<div id="comment-68639" class="comment">
<div id="post-68639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> Steps 1 to 3 of that processes are done, now at step 4 "Documentation". Tracked by me and others here: <a href="https://wiki.openstreetmap.org/wiki/WikiProject_Sweden/naturvardsverket_import">https://wiki.openstreetmap.org/wiki/WikiProject_Sweden/naturvardsverket_import</a> . Resolution of technical issues to understand if it is at all doable, which this question is actually about, is being done in parallel.</p>
</div>
<div id="comment-68639-info" class="comment-info">
<span class="comment-age">(04 Apr '19, 11:16)</span> <span class="comment-user userinfo">Atakua</span>
</div>
</div>
</div>
<div id="comment-tools-68632" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68632-form-container" class="comment-form-container">
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

