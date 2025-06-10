+++
type = "question"
title = "JOSM revert nodes within closed polygon."
description = '''Hi While editing someone unintentionally quantized a polygon that&#x27;s part of a multi polygon. https://www.openstreetmap.org/way/481782771 I&#x27;m still registered as the last amender, but if you select a node you&#x27;ll see they&#x27;ve been moved since. I don&#x27;t want to revert the whole changeset if possible, but...'''
date = "2018-05-29T15:19:00Z"
lastmod = "2018-05-30T20:06:00Z"
weight = 63848
keywords = [ "josm", "revert", "polygon" ]
aliases = [ "/questions/63848" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM revert nodes within closed polygon.](/questions/63848/josm-revert-nodes-within-closed-polygon)

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
<span id="post-63848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63848-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi While editing someone unintentionally quantized a polygon that's part of a multi polygon.</p>
<p><a href="https://www.openstreetmap.org/way/481782771">https://www.openstreetmap.org/way/481782771</a></p>
<p>I'm still registered as the last amender, but if you select a node you'll see they've been moved since.</p>
<p>I don't want to revert the whole changeset if possible, but I'm struggling to see how to revert just the nodes. I've downloaded just the polygon way into JOSM, selected that way &gt; Data &gt; Revert Changeset &gt; Revert selection only, but nothing changes to upload.</p>
<p>Could someone provide instruction how to select the nodes plaes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '18, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63848" class="comments-container">
<span id="63849"></span>
<div id="comment-63849" class="comment">
<div id="post-63849-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Should be OK now. I used Potlatch1 (but then had to move a node slightly to persuade it to upload the data). I'm unclear why the residential areas are added as a relation rather than individual polygons though.</p>
</div>
<div id="comment-63849-info" class="comment-info">
<span class="comment-age">(29 May '18, 15:27)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="63850"></span>
<div id="comment-63850" class="comment">
<div id="post-63850-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for that, but I was hoping for instructions so I, &amp; others, can learn how to do it for ourselves in the future.</p>
<p>They're MPs as they have 'inners'.</p>
</div>
<div id="comment-63850-info" class="comment-info">
<span class="comment-age">(29 May '18, 15:35)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="63851"></span>
<div id="comment-63851" class="comment">
<div id="post-63851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a> if memory serves Potlatch 1 is still mentioned in the wiki as a "way to revert particular sorts of things".</p>
</div>
<div id="comment-63851-info" class="comment-info">
<span class="comment-age">(29 May '18, 15:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63852"></span>
<div id="comment-63852" class="comment">
<div id="post-63852-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ta. So it can't be done in JOSM?</p>
</div>
<div id="comment-63852-info" class="comment-info">
<span class="comment-age">(29 May '18, 15:47)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="63853"></span>
<div id="comment-63853" class="comment">
<div id="post-63853-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd expect not until someone writes some "consolidated history" code in there, no.</p>
<p>That said, there are an awful lot of plugins for JOSM and someone might step forward with an answer using JOSM. If you want to create an "example error" for someone to try and fix with JOSM you can always do that on the dev server.</p>
</div>
<div id="comment-63853-info" class="comment-info">
<span class="comment-age">(29 May '18, 15:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63848-form-container" class="comment-form-container">
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

<span id="63856"></span>

<div id="answer-container-63856" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63856-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To revert it in JOSM, you'd need to select the nodes constituting the way, since those are what had been changed. Selecting only the way will attempt to revert the way, but that in itself hadn't been changed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '18, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-63856" class="comments-container">
<span id="63887"></span>
<div id="comment-63887" class="comment">
<div id="post-63887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is what's stumped me. I'm only an occasional JOSM user. This is what I tried using a test: JOSM &gt; 'Open Location' using the changeset URL. It only loaded the nodes. Drew a rectangle to select all required nodes. Data &gt; Revert Changeset &gt; Revert Selection only Clicked 'Upload Changes' &amp; went through the usual procedures.</p>
<p>It didn't revert.</p>
</div>
<div id="comment-63887-info" class="comment-info">
<span class="comment-age">(30 May '18, 20:06)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-63856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63856-form-container" class="comment-form-container">
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

