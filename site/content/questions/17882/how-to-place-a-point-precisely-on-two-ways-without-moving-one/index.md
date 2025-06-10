+++
type = "question"
title = "How to place a point precisely on two ways without moving one?"
description = '''Say that I have two ways that cross but do not have a shared point (an intersection). In Potlatch, how can I create a point that is on both ways without moving either one? It seems like no matter how I try to do this I end up creating a junction between the two ways but moving one of them. This is p...'''
date = "2012-11-22T03:28:00Z"
lastmod = "2012-11-26T10:48:00Z"
weight = 17882
keywords = [ "potlatch", "construction", "intersection", "tracing" ]
aliases = [ "/questions/17882" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to place a point precisely on two ways without moving one?](/questions/17882/how-to-place-a-point-precisely-on-two-ways-without-moving-one)

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
<span id="post-17882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17882-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Say that I have two ways that cross but do not have a shared point (an intersection). In Potlatch, how can I create a point that is on both ways without moving either one? It seems like no matter how I try to do this I end up creating a junction between the two ways but moving one of them.</p>
<p>This is particularly of interest to me at the moment as I am trying to use the technique described on the <a href="http://wiki.openstreetmap.org/wiki/Roof_modelling">http://wiki.openstreetmap.org/wiki/Roof_modelling</a> page in the wiki to make my roof and parking lot outlines a bit more exact; and I can use "make parallel way" to create a nice grid to work with, but when I try to trace it I have no points to snap to, and when I create the points I end up moving my construction lines. Which then negates the point of doing all that work in the first place.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch" rel="tag" title="see questions tagged &#39;potlatch&#39;">potlatch</span> <span class="post-tag tag-link-construction" rel="tag" title="see questions tagged &#39;construction&#39;">construction</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-tracing" rel="tag" title="see questions tagged &#39;tracing&#39;">tracing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '12, 03:28</strong></p>
<img src="https://secure.gravatar.com/avatar/4a4c8a91603aa21e05f5a441d5c13f26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blahedo&#39;s gravatar image" />
<p><span>blahedo</span><br />
<span class="score" title="736 reputation points">736</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blahedo has 2 accepted answers">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '12, 03:29</strong> </span></p>
</div>
</div>
<div id="comments-container-17882" class="comments-container">
&#10;</div>
<div id="comment-tools-17882" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17882-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="17906"></span>

<div id="answer-container-17906" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17906-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you can imagine to try the editor JOSM:</p>
<p>There is a plugin called <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/utilsplugin2">utilsplugin2</a> that gives you the feature to select two ways that cross eachother, and it automatically adds a new node where the lines cut.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '12, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-17906" class="comments-container">
<span id="17938"></span>
<div id="comment-17938" class="comment">
<div id="post-17938-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm aware of JOSM and will probably learn to use it at some point, but Java issues prevent me from using it right now, so this question was specifically about Potlatch. (Your answer may be useful for <em>other</em> people who have this question, of course. :)</p>
</div>
<div id="comment-17938-info" class="comment-info">
<span class="comment-age">(23 Nov '12, 19:48)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
</div>
<div id="comment-tools-17906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17906-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17883"></span>

<div id="answer-container-17883" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17883-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Does "shift click" work for you? If it doesn't, what does happen?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '12, 03:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-17883" class="comments-container">
<span id="17884"></span>
<div id="comment-17884" class="comment">
<div id="post-17884-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Shift-click is how you add a node to an existing way, yes; and if that click is on the selected way and in the vicinity of another way, the node gets added to both ways; but one (or both?) of the ways may move as a result of this. I'm asking if there's any way to do this without moving either way. (There will be slight adjustment due to rounding error, inevitably, but not nearly as much as I'm currently seeing.)</p>
</div>
<div id="comment-17884-info" class="comment-info">
<span class="comment-age">(22 Nov '12, 04:05)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
<span id="17886"></span>
<div id="comment-17886" class="comment">
<div id="post-17886-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The closer you zoom in, the greater precision you should be able to place the node with.</p>
</div>
<div id="comment-17886-info" class="comment-info">
<span class="comment-age">(22 Nov '12, 08:13)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="17908"></span>
<div id="comment-17908" class="comment">
<div id="post-17908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you zoom further in after you have started P2, and are accurate the point will not move see this question <a href="https://help.openstreetmap.org/questions/15374/how-to-join-existing-paths">https://help.openstreetmap.org/questions/15374/how-to-join-existing-paths</a></p>
</div>
<div id="comment-17908-info" class="comment-info">
<span class="comment-age">(23 Nov '12, 00:26)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="17939"></span>
<div id="comment-17939" class="comment">
<div id="post-17939-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, I can zoom in (and I do), but it's frustrating that the precision of computing an intersection, between two lines that are already in the system, is dependent on the stability of my mouse-clicking hand. I'd vastly prefer to do this computationally, but what I'm hearing is that the answer to my question is "you can't."</p>
</div>
<div id="comment-17939-info" class="comment-info">
<span class="comment-age">(23 Nov '12, 19:50)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
<span id="17945"></span>
<div id="comment-17945" class="comment">
<div id="post-17945-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The code in question is at <a href="https://github.com/systemed/potlatch2/blob/master/net/systemeD/halcyon/connection/Way.as#L209">https://github.com/systemed/potlatch2/blob/master/net/systemeD/halcyon/connection/Way.as#L209</a> . If you think there's an issue with the calculations, you're welcome to submit a ticket or a pull request as to how it could be improved.</p>
</div>
<div id="comment-17945-info" class="comment-info">
<span class="comment-age">(24 Nov '12, 00:20)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="17981"></span>
<div id="comment-17981" class="comment not_top_scorer">
<div id="post-17981-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Or, if you are not a software programmer, switch to JOSM editor ;-)</p>
</div>
<div id="comment-17981-info" class="comment-info">
<span class="comment-age">(26 Nov '12, 10:48)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-17883" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-17883-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17957"></span>

<div id="answer-container-17957" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17957-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi excuse, a bit late but in P2 you could try zoom max, like stated, mouse pointer at 'needed node connection', dont move your mouse pointer and shift and click with left mouse button and theres IMHO no movement at all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '12, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-17957" class="comments-container">
&#10;</div>
<div id="comment-tools-17957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17957-form-container" class="comment-form-container">
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

