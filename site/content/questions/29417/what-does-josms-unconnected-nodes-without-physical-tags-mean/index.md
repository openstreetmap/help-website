+++
type = "question"
title = "What does JOSM&#x27;s &quot;Unconnected nodes without physical tags&quot; mean?"
description = '''In JOSM, what does the &quot;Unconnected nodes without physical tags&quot; warning mean? In this case, I am attempting to create a a POI.'''
date = "2013-12-29T00:35:00Z"
lastmod = "2013-12-29T07:09:00Z"
weight = 29417
keywords = [ "node", "josm", "validator", "warning", "poi" ]
aliases = [ "/questions/29417" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What does JOSM's "Unconnected nodes without physical tags" mean?](/questions/29417/what-does-josms-unconnected-nodes-without-physical-tags-mean)

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
<span id="post-29417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In JOSM, what does the "Unconnected nodes without physical tags" warning mean? In this case, I am attempting to create a a POI.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-validator" rel="tag" title="see questions tagged &#39;validator&#39;">validator</span> <span class="post-tag tag-link-warning" rel="tag" title="see questions tagged &#39;warning&#39;">warning</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '13, 00:35</strong></p>
<img src="https://secure.gravatar.com/avatar/e72946d7c81ee170b322f6e6abae3442?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattflaschen&#39;s gravatar image" />
<p><span>mattflaschen</span><br />
<span class="score" title="226 reputation points">226</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattflaschen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Dec '13, 02:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-29417" class="comments-container">
&#10;</div>
<div id="comment-tools-29417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29417-form-container" class="comment-form-container">
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

<span id="29419"></span>

<div id="answer-container-29419" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29419-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mattflaschen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I expect the full warning message is <em>"No Tags - Unconnected nodes without physical tags"</em>?</p>
<p>The warning means you've added a node somewhere without any tags set on it.</p>
<p>The warning comes from the JOSM "validator". You can read about the validator and different error messages on the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Validator">JOSM Validator wiki page</a>.</p>
<p>Note that the validator runs prior to upload. But you can also run it at any other time if you show the validator panel. This has the advantage that you and right-click and "zoom to problem" on any particular message, to help figure out what it's talking about.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '13, 01:49</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-29419" class="comments-container">
<span id="29418"></span>
<div id="comment-29418" class="comment">
<div id="post-29418-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>In this case, the issue was that I unintentionally created two nodes, one without any tags. JOSM caught it before saving.</p>
</div>
<div id="comment-29418-info" class="comment-info">
<span class="comment-age">(29 Dec '13, 00:38)</span> <span class="comment-user userinfo">mattflaschen</span>
</div>
</div>
<span id="29430"></span>
<div id="comment-29430" class="comment">
<div id="post-29430-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you do try to upload and the "Suspicious data found" box pops up just click the "Cancel" button and the validator panel opens as Harry says above. Make your corrections and try uploading again, on complicated issues it might take several corrections to get things right. Get really stuck then back out by deleting the "data layer" in the layers panel, that removes any chance of inadvertently uploading bad data.</p>
</div>
<div id="comment-29430-info" class="comment-info">
<span class="comment-age">(29 Dec '13, 07:09)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-29419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29419-form-container" class="comment-form-container">
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

