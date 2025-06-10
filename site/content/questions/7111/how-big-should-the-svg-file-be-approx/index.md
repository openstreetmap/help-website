+++
type = "question"
title = "How big should the svg file be approx.?"
description = '''Im running the xsltproc osm-map-features-z17.xml but I get errors in the beginning and it goes into a continuos &quot;area centre.....&quot; Is this correct? What should ideally be the file size?'''
date = "2011-08-16T09:44:00Z"
lastmod = "2011-08-16T11:10:00Z"
weight = 7111
keywords = [ "sreem" ]
aliases = [ "/questions/7111" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How big should the svg file be approx.?](/questions/7111/how-big-should-the-svg-file-be-approx)

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
<span id="post-7111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7111-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Im running the xsltproc osm-map-features-z17.xml but I get errors in the beginning and it goes into a continuos "area centre....." Is this correct? What should ideally be the file size?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sreem" rel="tag" title="see questions tagged &#39;sreem&#39;">sreem</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '11, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/805f974cf5a6cc0673fa25d1f3bcec3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sreemoyee%20Mitra&#39;s gravatar image" />
<p><span>Sreemoyee Mitra</span><br />
<span class="score" title="30 reputation points">30</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sreemoyee Mitra has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7111" class="comments-container">
<span id="7112"></span>
<div id="comment-7112" class="comment">
<div id="post-7112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you referring to <a href="http://wiki.openstreetmap.org/wiki/Osmarender/Howto#xsltproc">this step in using the osmarender?</a> Not clear from your question</p>
</div>
<div id="comment-7112-info" class="comment-info">
<span class="comment-age">(16 Aug '11, 09:58)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
</div>
<div id="comment-tools-7111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7111-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="7114"></span>

<div id="answer-container-7114" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7114-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Calculation of area centers takes quite a while, so be patient. Note that the perl implementation of osmarender is quite a bit faster than the XSLT version.</p>
<p>The size of the resulting SVG file depends a lot on the size and complexity of the area that you render. Files between 200kB and 5MB are quite common. If the file is significantely smaller something might be worng. Larger files can be perfectly valid but are hard on rasterizers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '11, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-7114" class="comments-container">
&#10;</div>
<div id="comment-tools-7114" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7114-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7115"></span>

<div id="answer-container-7115" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7115-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your experience is normal. Unfortunately, it can take a long time to render a SVG using xsltproc. I rendered a relatively large city several months ago with the z17 stylesheet (its bounding box was North 41.6000 West -81.85 South 41.4173 EAST -81.5323 ) and it had taken over 6 hours to render !</p>
<p>As petschge mentioned, the speed was much quicker with <a href="http://wiki.openstreetmap.org/wiki/Osmarender/orp">or/p</a> - the same bounding box and stylesheet had taken less than 10 minutes to render with or/p !</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '11, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-7115" class="comments-container">
&#10;</div>
<div id="comment-tools-7115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7115-form-container" class="comment-form-container">
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

