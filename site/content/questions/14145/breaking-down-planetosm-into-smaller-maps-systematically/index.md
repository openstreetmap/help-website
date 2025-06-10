+++
type = "question"
title = "Breaking down planet.osm into smaller maps systematically"
description = '''I have downloaded the planet.osm as XML and am looking to break this down into smaller maps so that my computer may process them. I think that I will be able to handle at least 1 degree by 1 degree (i.e. W160 to W159 &amp;amp; N89 to N90 and so forth), but it is very tedious to do this in osmosis with c...'''
date = "2012-07-10T18:47:00Z"
lastmod = "2012-07-10T23:14:00Z"
weight = 14145
keywords = [ "osmosis" ]
aliases = [ "/questions/14145" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Breaking down planet.osm into smaller maps systematically](/questions/14145/breaking-down-planetosm-into-smaller-maps-systematically)

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
<span id="post-14145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14145-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded the planet.osm as XML and am looking to break this down into smaller maps so that my computer may process them. I think that I will be able to handle at least 1 degree by 1 degree (i.e. W160 to W159 &amp; N89 to N90 and so forth), but it is very tedious to do this in osmosis with command line. Can anyone think of a method through which I could automate the process?</p>
<p>Thank you,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '12, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/60f88b68b05449060d0744671d8cf758?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="somedude&#39;s gravatar image" />
<p><span>somedude</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="somedude has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '12, 14:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6edb4957e57770118c3b8022cfce68a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srbrook&#39;s gravatar image" />
<p><span>srbrook</span><br />
<span class="score" title="993 reputation points">993</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span></p>
</div>
</div>
<div id="comments-container-14145" class="comments-container">
&#10;</div>
<div id="comment-tools-14145" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14145-form-container" class="comment-form-container">
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

<span id="14149"></span>

<div id="answer-container-14149" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14149-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-14149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="somedude has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are several special-use programs that will split the planet into many small bits at the same time. One of them is <a href="http://svn.openstreetmap.org/applications/utils/osm-extract/osmcut/">http://svn.openstreetmap.org/applications/utils/osm-extract/osmcut/</a> (reads XML only, makes equal-sized squares, no support for relations); another is <a href="http://www.mkgmap.org.uk/page/tile-splitter">http://www.mkgmap.org.uk/page/tile-splitter</a> (reads PBF as well, makes variable-sizes squares based on how much data is in them).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '12, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14149" class="comments-container">
&#10;</div>
<div id="comment-tools-14149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14149-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14156"></span>

<div id="answer-container-14156" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14156-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not a direct answer to your question, but just in case you're not aware - there are a number of places where regularly updated planet <a href="http://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">extracts</a> are available. Depending on what you want to do with the data, it might be easier using one or more of those than trying to process the whole planet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '12, 23:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-14156" class="comments-container">
&#10;</div>
<div id="comment-tools-14156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14156-form-container" class="comment-form-container">
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

