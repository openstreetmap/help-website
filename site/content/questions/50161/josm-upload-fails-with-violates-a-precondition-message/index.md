+++
type = "question"
title = "JOSM upload fails with &quot;violates a precondition&quot; message"
description = '''I have a large changeset that JOSM refuses to upload because of a &quot;precondition error&quot;. It tells me there is a problem with &quot;way id:230281711 because the node with id:4226001328 either does not exist or is not visible&quot;. The node does exist and is visible but nevertheless JOSM will not accept the upl...'''
date = "2016-06-12T16:02:00Z"
lastmod = "2016-06-12T23:27:00Z"
weight = 50161
keywords = [ "josm", "precondition_failed", "error" ]
aliases = [ "/questions/50161" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM upload fails with "violates a precondition" message](/questions/50161/josm-upload-fails-with-violates-a-precondition-message)

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
<span id="post-50161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50161-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a large changeset that JOSM refuses to upload because of a "precondition error". It tells me there is a problem with "way id:230281711 because the node with id:4226001328 either does not exist or is not visible". The node does exist and is visible but nevertheless JOSM will not accept the upload. I have quite a bit of work invested in that changeset and would really like to salvage it if possible.</p>
<p>However, I got frustrated the other night and saved my work in an OSM file to work on it the next day. But now the individual changes are no longer available in the command window or anywhere else that I can see. Is there any way to dissect an OSM file to see what changes might be there? And why oh why didn't JOSM present me with a conflict resolution dialog?</p>
<p>I have a feeling nobody knows these answers but I remain hopeful I can resurrect my work somehow.</p>
<p>Thanks,</p>
<p>Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-precondition_failed" rel="tag" title="see questions tagged &#39;precondition_failed&#39;">precondition_failed</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '16, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-50161" class="comments-container">
&#10;</div>
<div id="comment-tools-50161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50161-form-container" class="comment-form-container">
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

<span id="50163"></span>

<div id="answer-container-50163" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50163-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think File-&gt;Update data should trigger JOSM to generate the conflicts. Don't have a broken changeset to test with at the moment.</p>
<p>If that doesn't work, I think searching for the way using the id and purging it should allow the upload to proceed. Purge is under the edit menu, select the way before selecting the menu item.</p>
<p>Since you have the edits saved to a file, it's "safe" to try both things. Just delete the layer and reopen if it seems things have gone further sideways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '16, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-50163" class="comments-container">
<span id="50165"></span>
<div id="comment-50165" class="comment">
<div id="post-50165-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Wow, you are a lifesaver Max.</p>
<p>After updating my data as you suggested a conflict dialog resulted with only one conflict listed. It still wouldn't accept my upload after that but, grabbing at straws, I selected &amp; updated a few of the important individual objects I had worked on and then tried another upload. Finally JOSM accepted it and my work was saved.</p>
<p>Usually I hate seeing the Conflict Dialog box appear but this time it was most welcome. I'm still wondering why JOSM did not generate a Conflict when it encountered this error. Without that one has no way to fix the error.</p>
<p>Thanks a ton for your insight. It saved a ton of work for me.</p>
<p>Dave</p>
</div>
<div id="comment-50165-info" class="comment-info">
<span class="comment-age">(12 Jun '16, 23:27)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-50163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50163-form-container" class="comment-form-container">
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

