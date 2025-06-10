+++
type = "question"
title = "show all ways between two points"
description = '''I want to write an offline app that read my country&#x27;s map and the end user can select two points on the map and the app must calculate all ways between these points and based on some other condition show the best  way to the user '''
date = "2016-06-28T06:28:00Z"
lastmod = "2016-07-01T15:16:00Z"
weight = 50499
keywords = [ "ways", "maps", "distance" ]
aliases = [ "/questions/50499" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [show all ways between two points](/questions/50499/show-all-ways-between-two-points)

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
<span id="post-50499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50499-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to write an offline app that read my country's map and the end user can select two points on the map and the app must calculate all ways between these points and based on some other condition show the best way to the user</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '16, 06:28</strong></p>
<img src="https://secure.gravatar.com/avatar/5356ea00133edec322c345d3c8efc3a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Moolerian&#39;s gravatar image" />
<p><span>Moolerian</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Moolerian has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50499" class="comments-container">
&#10;</div>
<div id="comment-tools-50499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50499-form-container" class="comment-form-container">
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

<span id="50500"></span>

<div id="answer-container-50500" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50500-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-50500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Moolerian has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You almost certainly do not want <em>all</em> ways since that would be a very large number (including all detours). What you are looking for is a routing algorithm; you don't want to compute all ways first and then select the best, but instead apply an algorithm that finds the best right away. There are ready-made routing engines for OSM that you could use (e.g. GraphHopper), or building blocks that you can somehow call from your application (e.g. libosmscout). Of course you can also choose to write everything yourself; search for the terms "routing" and "graph" on this help site for more pointers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '16, 06:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '16, 06:52</strong> </span></p>
</div>
</div>
<div id="comments-container-50500" class="comments-container">
<span id="50501"></span>
<div id="comment-50501" class="comment">
<div id="post-50501-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you , i know that i don't want ALL ways i want sth like google direction in it's map but mine is offline and suggested direction based on some manual conditions</p>
</div>
<div id="comment-50501-info" class="comment-info">
<span class="comment-age">(28 Jun '16, 07:11)</span> <span class="comment-user userinfo">Moolerian</span>
</div>
</div>
<span id="50544"></span>
<div id="comment-50544" class="comment">
<div id="post-50544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Moolerian, I assume that you have already seen the OSM wiki page <a href="http://wiki.openstreetmap.org/wiki/Routing">http://wiki.openstreetmap.org/wiki/Routing</a> ... also with its sub pages about online and offline routing ... What solution comes near your aim? IIRC graphhopper has now a feature implemented about alternative routes.</p>
</div>
<div id="comment-50544-info" class="comment-info">
<span class="comment-age">(01 Jul '16, 15:16)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-50500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50500-form-container" class="comment-form-container">
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

