+++
type = "question"
title = "How does one identify GPX speed in JOSM?"
description = '''I haven&#x27;t been able to locate a speed key for JOSM&#x27;s color coding when using &quot;Car&quot; mode for coloring GPX tracks by speed. Where can I find what color corresponds to what speed?'''
date = "2012-01-08T07:51:00Z"
lastmod = "2020-10-16T17:32:00Z"
weight = 9844
keywords = [ "josm", "gpx" ]
aliases = [ "/questions/9844" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How does one identify GPX speed in JOSM?](/questions/9844/how-does-one-identify-gpx-speed-in-josm)

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
<span id="post-9844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9844-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I haven't been able to locate a speed key for JOSM's color coding when using "Car" mode for coloring GPX tracks by speed. Where can I find what color corresponds to what speed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '12, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-9844" class="comments-container">
<span id="9845"></span>
<div id="comment-9845" class="comment">
<div id="post-9845-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Rationale: I'm looking to update the "maxspeed" rendering style for JOSM to support the full range of US speed limits, and to get color consistency with GPX rendering.</p>
</div>
<div id="comment-9845-info" class="comment-info">
<span class="comment-age">(08 Jan '12, 07:52)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-9844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9844-form-container" class="comment-form-container">
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

<span id="9847"></span>

<div id="answer-container-9847" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9847-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Baloo Uriza has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You find the relevant section of code <a href="https://josm.openstreetmap.de/browser/josm/trunk/src/org/openstreetmap/josm/gui/layer/GpxLayer.java">here</a>.</p>
<p>The default color is HSB((v / 45 * 300), 1, 1) where <em>v</em> is the speed in m/s.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '12, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '12, 04:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span></p>
</div>
</div>
<div id="comments-container-9847" class="comments-container">
<span id="9864"></span>
<div id="comment-9864" class="comment">
<div id="post-9864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, could I get an example of how to calculate that? I definitely appreciate the comprehensive answer, but not sure how to use it.</p>
</div>
<div id="comment-9864-info" class="comment-info">
<span class="comment-age">(09 Jan '12, 14:52)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="10012"></span>
<div id="comment-10012" class="comment">
<div id="post-10012-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>OK, I stumbled into what the HSB is by accident. For others trying to find how to figure this out, it's at <a href="http://www.tomjewett.com/colors/hsb.html">http://www.tomjewett.com/colors/hsb.html</a></p>
</div>
<div id="comment-10012-info" class="comment-info">
<span class="comment-age">(17 Jan '12, 04:28)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="77121"></span>
<div id="comment-77121" class="comment">
<div id="post-77121-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The last referenced URL seems to be down now, the most recent internet archive link is <a href="https://web.archive.org/web/20190407225549/http://www.tomjewett.com/colors/hsb.html">https://web.archive.org/web/20190407225549/http://www.tomjewett.com/colors/hsb.html</a> .</p>
</div>
<div id="comment-77121-info" class="comment-info">
<span class="comment-age">(16 Oct '20, 17:32)</span> <span class="comment-user userinfo">Richlv</span>
</div>
</div>
</div>
<div id="comment-tools-9847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9847-form-container" class="comment-form-container">
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

