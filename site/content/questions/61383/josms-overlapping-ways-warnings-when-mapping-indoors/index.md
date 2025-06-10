+++
type = "question"
title = "JOSM&#x27;s overlapping ways warnings when mapping indoors"
description = '''I&#x27;m preparing a building for indoor mapping, and while doing so, I&#x27;m merging adjacent walls from two rooms (which were drawn separately). Thus many pairs of nodes end up containing two ways, each of them part of one of the rooms sharing the wall. I thought this was the standard way to do things (it ...'''
date = "2017-12-27T15:33:00Z"
lastmod = "2017-12-27T17:52:00Z"
weight = 61383
keywords = [ "indoor", "josm", "validation", "warning" ]
aliases = [ "/questions/61383" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM's overlapping ways warnings when mapping indoors](/questions/61383/josms-overlapping-ways-warnings-when-mapping-indoors)

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
<span id="post-61383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61383-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm preparing a building for indoor mapping, and while doing so, I'm merging adjacent walls from two rooms (which were drawn separately). Thus many pairs of nodes end up containing two ways, each of them part of one of the rooms sharing the wall.</p>
<p>I thought this was the standard way to do things (it seemed to work without issues for outdoor mapping, e.g. for adjacent buildings), but on upload, JOSM emits warnings about "Overlapping ways" everywhere. I then tried looking for other buildings already mapped for indoors, such as the Louvre, but it also has the same validation issues, so I don't know where to find a "correct" example of indoor mapping that gets no warnings.</p>
<p>I'm supposing that such warnings mean that there should be a way to do it without getting them. If so, how to do it? Otherwise, should I just ignore them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-validation" rel="tag" title="see questions tagged &#39;validation&#39;">validation</span> <span class="post-tag tag-link-warning" rel="tag" title="see questions tagged &#39;warning&#39;">warning</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '17, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/395b52b769f88f777174aeadaaf4be12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voyageant&#39;s gravatar image" />
<p><span>voyageant</span><br />
<span class="score" title="181 reputation points">181</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voyageant has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61383" class="comments-container">
<span id="61385"></span>
<div id="comment-61385" class="comment">
<div id="post-61385-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you just send us the osm code of a set of objects like the one you mention, or upload the .osm file somewhere (Dropbox...) so we can check?</p>
</div>
<div id="comment-61385-info" class="comment-info">
<span class="comment-age">(27 Dec '17, 16:13)</span> <span class="comment-user userinfo">edvac</span>
</div>
</div>
</div>
<div id="comment-tools-61383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61383-form-container" class="comment-form-container">
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

<span id="61386"></span>

<div id="answer-container-61386" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61386-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="voyageant has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can confirm that correctly mapped rooms (<code>indoor=room</code>) with shared nodes will trigger validation warnings in JOSM. There are other incorrect validation results related to indoor mapping, too, such as warnings about duplicated nodes for features located above each other on different levels.</p>
<p>Keep in mind that the validator warnings in JOSM are merely an indicator that something <em>might</em> be wrong – but the validator may very well be mistaken, as in this case. Seeing how indoor mapping is still a rather niche topic in OSM, it's quite likely that JOSM has simply not yet been updated to know about the relevant tags.</p>
<p>For your particular issue, you could theoretically work around the limitation by adding <code>area=yes</code> tags to your rooms. However, I don't recommend that. Instead, it's best to just ignore this warning for the time being – there's an "ignore" button in the validator dialog for such situations – and <a href="https://josm.openstreetmap.de/newticket">report</a> the issue to the JOSM developers so they can improve the validator.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '17, 17:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-61386" class="comments-container">
&#10;</div>
<div id="comment-tools-61386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61386-form-container" class="comment-form-container">
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

