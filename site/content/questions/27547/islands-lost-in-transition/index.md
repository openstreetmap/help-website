+++
type = "question"
title = "Islands lost in transition"
description = '''There were some islands in this channel some weeks ago. Assume they have disappeared in the transition process while moving objects from coastline to other data layers. http://www.openstreetmap.org/#map=11/-8.0263/138.7951 Thanks for the answer.'''
date = "2013-10-28T08:44:00Z"
lastmod = "2013-10-30T20:56:00Z"
weight = 27547
keywords = [ "islands", "channel", "missing" ]
aliases = [ "/questions/27547" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Islands lost in transition](/questions/27547/islands-lost-in-transition)

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
<span id="post-27547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27547-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There were some islands in this channel some weeks ago. Assume they have disappeared in the transition process while moving objects from coastline to other data layers.<br />
<a href="http://www.openstreetmap.org/#map=11/-8.0263/138.7951">http://www.openstreetmap.org/#map=11/-8.0263/138.7951</a></p>
<p>Thanks for the answer.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-islands" rel="tag" title="see questions tagged &#39;islands&#39;">islands</span> <span class="post-tag tag-link-channel" rel="tag" title="see questions tagged &#39;channel&#39;">channel</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '13, 08:44</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></p>
</div>
</div>
<div id="comments-container-27547" class="comments-container">
<span id="27556"></span>
<div id="comment-27556" class="comment">
<div id="post-27556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Shouldn't the question be: "What happened to the islands?" or "How to recover these islands?". What is the question after all?</p>
</div>
<div id="comment-27556-info" class="comment-info">
<span class="comment-age">(28 Oct '13, 11:04)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-27547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27547-form-container" class="comment-form-container">
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

<span id="27559"></span>

<div id="answer-container-27559" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27559-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Opened a part of the area and saw that the former islands still retain only the "natural=coastline" tag, and the riverbank's ways are now part of a multipolygon relation with "waterway=riverbank".</p>
<p>What has to be done is:</p>
<ol>
<li>Remove the natural=coastline from the islands;</li>
<li>Add the island's ways to the multipolygon relation;</li>
<li>Add the role "inner" to the islands;</li>
<li>Optionally add the "place=island", mainly when the island has a name.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '13, 11:12</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '13, 10:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-27559" class="comments-container">
<span id="27669"></span>
<div id="comment-27669" class="comment">
<div id="post-27669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the (edited) answer. The described case is just an illustration of a systematic error source when people are moving objects from class to class (missing objects and wrong class). These errors are never detected by any OSM error or change detectors today. My intention was to bring this situation to the OSM experts' attention. Maybe I did this on a wrong place.</p>
</div>
<div id="comment-27669-info" class="comment-info">
<span class="comment-age">(30 Oct '13, 20:56)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-27559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27559-form-container" class="comment-form-container">
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

