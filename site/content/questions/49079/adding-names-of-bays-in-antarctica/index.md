+++
type = "question"
title = "Adding names of bays in Antarctica"
description = '''I noticed that many of the bays and small islands off the coast of Antarctica don&#x27;t have their names applied yet. What is the best way to mark the names of bays and small islands? Do you have to select the entire (often oddly shaped) bay or just a part of it where the name should appear?'''
date = "2016-04-07T07:04:00Z"
lastmod = "2016-04-07T08:40:00Z"
weight = 49079
keywords = [ "island", "antarctica", "bay", "names", "ocean" ]
aliases = [ "/questions/49079" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding names of bays in Antarctica](/questions/49079/adding-names-of-bays-in-antarctica)

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
<span id="post-49079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49079-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I noticed that many of the bays and small islands off the coast of Antarctica don't have their names applied yet. What is the best way to mark the names of bays and small islands? Do you have to select the entire (often oddly shaped) bay or just a part of it where the name should appear?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span> <span class="post-tag tag-link-antarctica" rel="tag" title="see questions tagged &#39;antarctica&#39;">antarctica</span> <span class="post-tag tag-link-bay" rel="tag" title="see questions tagged &#39;bay&#39;">bay</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-ocean" rel="tag" title="see questions tagged &#39;ocean&#39;">ocean</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '16, 07:04</strong></p>
<img src="https://secure.gravatar.com/avatar/79ce95460505b93e1ce8d3cb1a225eea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JennyPenny&#39;s gravatar image" />
<p><span>JennyPenny</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JennyPenny has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49079" class="comments-container">
&#10;</div>
<div id="comment-tools-49079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49079-form-container" class="comment-form-container">
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

<span id="49080"></span>

<div id="answer-container-49080" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49080-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-49080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For small islands, a node with place=island, name=* will do the trick. You can also just add those tags to the encircling coastline if one is present. For bays and coves, points and capes, I add a node and tag it with natural=bay or natural=cape, add a name and source and call it good. I've experimented with adding bays as a long closed way but it's tricky to know where the "boundaries" are.</p>
<p>Here is an area I've worked on: <a href="https://www.openstreetmap.org/query?lat=59.50353&amp;lon=-151.37398#map=13/59.4967/-151.4152">https://www.openstreetmap.org/query?lat=59.50353&amp;lon=-151.37398#map=13/59.4967/-151.4152</a></p>
<p>Sadie Cove is a bay (SE in the window) that I defined as an area by making a copy of the coastline, closing the way at the "mouth", adjusting it and then retagging it as above. It's certainly much harder to do than merely adding a node. It doesn't supply much more information either because the bay is still pretty obvious when seen on a larger scale map.</p>
<p>There are a few islands on the screen in that URL that are tagged using both conventions. Look at those lying due south of Hesketh Island.</p>
<p>Cheers, Dave</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '16, 08:40</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-49080" class="comments-container">
&#10;</div>
<div id="comment-tools-49080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49080-form-container" class="comment-form-container">
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

