+++
type = "question"
title = "Which router does Maps.me use?"
description = '''I&#x27;ve noticed a few odd routing decisions in the Maps.me navigation algorithm and would like to find out whether it&#x27;s their router problem or just an outdated map (e.g. someone corrected the problem in the meantime). Which router do they use? If it&#x27;s Graphopper or OSMR, then it&#x27;s easy to test online....'''
date = "2020-01-31T05:22:00Z"
lastmod = "2020-02-02T16:42:00Z"
weight = 72791
keywords = [ "maps.me", "debugging", "navigation" ]
aliases = [ "/questions/72791" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Which router does Maps.me use?](/questions/72791/which-router-does-mapsme-use)

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
<span id="post-72791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72791-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've noticed a few odd routing decisions in the Maps.me navigation algorithm and would like to find out whether it's their router problem or just an outdated map (e.g. someone corrected the problem in the meantime).</p>
<p>Which router do they use?</p>
<p>If it's Graphopper or OSMR, then it's easy to test online. If not, is their router available for testing elsewhere?</p>
<p>Examples of problems include extreme detours for bikes, when there's an obvious direct bike route, ignoring the fact bikes have no turn restriction at a given crossroad and routing them as if they were cars and directing cars off a straight highway for no reason only to make them return to the highway at first opportunity.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps.me" rel="tag" title="see questions tagged &#39;maps.me&#39;">maps.me</span> <span class="post-tag tag-link-debugging" rel="tag" title="see questions tagged &#39;debugging&#39;">debugging</span> <span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '20, 05:22</strong></p>
<img src="https://secure.gravatar.com/avatar/7894b2a54e5989db2e91cf2a6009286b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aneleutheroi&#39;s gravatar image" />
<p><span>aneleutheroi</span><br />
<span class="score" title="191 reputation points">191</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aneleutheroi has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-72791" class="comments-container">
&#10;</div>
<div id="comment-tools-72791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72791-form-container" class="comment-form-container">
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

<span id="72797"></span>

<div id="answer-container-72797" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72797-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-72797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aneleutheroi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>maps.me routes on device and doesn't use any of the hosted routing services. AFAIK there is no "online" version of their algorithm, so IMHO the best course of action would be to report the problems on the maps.me issue tracker <a href="https://github.com/mapsme/omim">https://github.com/mapsme/omim</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '20, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-72797" class="comments-container">
<span id="72812"></span>
<div id="comment-72812" class="comment">
<div id="post-72812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for pointing to the issue tracker! I'll wait for the map update (to exclude the problems have been fixed by edits) and let them know.</p>
</div>
<div id="comment-72812-info" class="comment-info">
<span class="comment-age">(01 Feb '20, 21:45)</span> <span class="comment-user userinfo">aneleutheroi</span>
</div>
</div>
</div>
<div id="comment-tools-72797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72797-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72815"></span>

<div id="answer-container-72815" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72815-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://weekly-geekly.github.io/articles/262185/index.html">https://weekly-geekly.github.io/articles/262185/index.html</a> gives some background to their routing engine choice. As <a href="https://help.openstreetmap.org/users/2053/simonpoole">@simonpoole</a> explains it's their own on-device algorithm.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '20, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-72815" class="comments-container">
&#10;</div>
<div id="comment-tools-72815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72815-form-container" class="comment-form-container">
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

