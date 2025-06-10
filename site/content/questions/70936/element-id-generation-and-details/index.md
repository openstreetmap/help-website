+++
type = "question"
title = "Element ID generation and details"
description = '''As we know each element has element ID assigned to it. On what basis 64 bit element ID&#x27;s are assigned. Does element IDs have any structure. Where can i find more details about Element ID generation and its structure.'''
date = "2019-09-27T06:48:00Z"
lastmod = "2019-09-27T07:33:00Z"
weight = 70936
keywords = [ "identifier", "id", "structure", "element" ]
aliases = [ "/questions/70936" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Element ID generation and details](/questions/70936/element-id-generation-and-details)

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
<span id="post-70936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70936-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As we know each element has element ID assigned to it. On what basis 64 bit element ID's are assigned. Does element IDs have any structure. Where can i find more details about Element ID generation and its structure.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-identifier" rel="tag" title="see questions tagged &#39;identifier&#39;">identifier</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-structure" rel="tag" title="see questions tagged &#39;structure&#39;">structure</span> <span class="post-tag tag-link-element" rel="tag" title="see questions tagged &#39;element&#39;">element</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Sep '19, 06:48</strong></p>
<img src="https://secure.gravatar.com/avatar/3a9e601ec47c2494edc45f8c0e90a0aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amruthesha&#39;s gravatar image" />
<p><span>Amruthesha</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amruthesha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70936" class="comments-container">
&#10;</div>
<div id="comment-tools-70936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70936-form-container" class="comment-form-container">
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

<span id="70939"></span>

<div id="answer-container-70939" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70939-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-70939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Amruthesha has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The element IDs (node, way, relation IDs) are assigned by the PostgreSQL database on the central OpenStreetMap server. The API code merely tells the database to "save" a new object with an ID of NULL (e.g. for a new node, the relevant code line is <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/app/models/node.rb#L270)">https://github.com/openstreetmap/openstreetmap-website/blob/master/app/models/node.rb#L270)</a> and then the database assigns a new ID based on a PostgreSQL "sequence" (cf. <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/db/structure.sql#L1470).">https://github.com/openstreetmap/openstreetmap-website/blob/master/db/structure.sql#L1470).</a></p>
<p>These IDs have no structure or meaning altogether.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Sep '19, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Sep '19, 07:34</strong> </span></p>
</div>
</div>
<div id="comments-container-70939" class="comments-container">
&#10;</div>
<div id="comment-tools-70939" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70939-form-container" class="comment-form-container">
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

