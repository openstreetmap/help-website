+++
type = "question"
title = "Why are some pedestrian areas not rendering"
description = '''highway=pedestrian area=yes renders in OSM area:highway=pedestrian area=yes does not render in OSM I&#x27;m asking because a few years ago a bot changed all the former to the latter in Massachusetts.'''
date = "2017-10-11T16:34:00Z"
lastmod = "2017-10-19T20:29:00Z"
weight = 60067
keywords = [ "pedestrian", "tagging", "css", "area" ]
aliases = [ "/questions/60067" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why are some pedestrian areas not rendering](/questions/60067/why-are-some-pedestrian-areas-not-rendering)

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
<span id="post-60067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60067-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>highway=pedestrian area=yes renders in OSM</p>
<p>area:highway=pedestrian area=yes does not render in OSM</p>
<p>I'm asking because a few years ago a bot changed all the former to the latter in Massachusetts.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-css" rel="tag" title="see questions tagged &#39;css&#39;">css</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '17, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/75cc9956f060892f585352e9011cd26e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan01730&#39;s gravatar image" />
<p><span>Alan01730</span><br />
<span class="score" title="464 reputation points">464</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan01730 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60067" class="comments-container">
<span id="60075"></span>
<div id="comment-60075" class="comment">
<div id="post-60075-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>ask the maintainer of the bot why they made the change. Ask them whether this was discussed with the community. And after discussion, you can ask to revert the change. There is a Polish map that renders area:highway, but there is no reason AFAIK to change the former tagging.</p>
</div>
<div id="comment-60075-info" class="comment-info">
<span class="comment-age">(12 Oct '17, 04:14)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="60186"></span>
<div id="comment-60186" class="comment">
<div id="post-60186-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It should be noted that mappers have sometimes incorrectly used highway=pedestrian + area=yes in situations where area:highway=pedestrian should have been used instead: For the area covered by a pedestrian road, as opposed to a plaza. In those cases, replacing these tags would have been justified (although still subject to the usual rules for bot edits). Just something to keep in mind in general, I'm not aware of the specifics of this case.</p>
</div>
<div id="comment-60186-info" class="comment-info">
<span class="comment-age">(19 Oct '17, 20:29)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-60067" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60067-form-container" class="comment-form-container">
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

<span id="60078"></span>

<div id="answer-container-60078" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60078-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-60078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alan01730 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There might be some OSM renderers that show the <a href="https://wiki.openstreetmap.org/wiki/Key:area:highway"><code>area:highway</code></a> key. The renderer for the standard layer at <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a> doesn't at the moment. This has several reasons (still a low although rising usage, and it needs a re-import of the whole database because of the new key, as far as I know) but I'm confident that this will change in the future.</p>
<p>However <code>area:highway=pedestrian</code> is very different from <code>highway=pedestrian</code>! The <code>area:highway=pedestrian</code> tag is solely meant for <em>rendering</em>, not for <em>routing</em>. <code>area:highway=pedestrian</code> should not be connected to ways with a <code>highway</code> tag. Also this tag is and should be completely ignored by routers since it serves only a visual purpose.</p>
<p>Therefore replacing <code>highway=pedestrian</code> with <code>area:highway=pedestrian</code> is certainly wrong and breaks pedestrian routing.</p>
<p>As already mentioned by escada try to get into contact with the mapper / bot author. Try to comment in the changesets or send him/her a private message. If they remain unanswered then get into contact with the <a href="https://wiki.osmfoundation.org/wiki/Data_Working_Group">Data Working Group</a>. This should be the last option, though, since the DWG is usually very busy and should only be contacted for serious issues. If the mapper doesn't respond and there are only a few things to fix then go ahead and fix them yourself. Or get into contact with the local community and ask for some help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Oct '17, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60078" class="comments-container">
&#10;</div>
<div id="comment-tools-60078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60078-form-container" class="comment-form-container">
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

