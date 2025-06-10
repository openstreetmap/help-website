+++
type = "question"
title = "Multiple questions about relations / routes"
description = '''I&#x27;m trying to learn how to properly create relations for MTB way routes and have the following questions:  Is it possible to create a relation route by just designating the relation for a subset of way segment nodes instead of entire way segments? This would allow route creation without having to sp...'''
date = "2016-04-23T03:14:00Z"
lastmod = "2022-01-21T07:53:00Z"
weight = 49370
keywords = [ "mtb", "route", "relation" ]
aliases = [ "/questions/49370" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple questions about relations / routes](/questions/49370/multiple-questions-about-relations-routes)

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
<span id="post-49370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49370-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to learn how to properly create relations for MTB way routes and have the following questions:</p>
<ol>
<li>Is it possible to create a relation route by just designating the relation for a subset of way segment nodes instead of entire way segments? This would allow route creation without having to split ways into segments at all intersections where the route turns onto a new way. There would be no direction to the route but that is not a problem for the routes I want to create (they can be ridden either direction).</li>
<li>(Assuming routes must consist of way segments with direction specified correctly), how do you handle a single route that passes over the same way segment twice but in opposite directions?</li>
<li>Related to 2., how do you handle multiple routes that use the same way segment but in opposite directions? I have read that you can duplicate the way segment so you have two spatially identical way segments "on top of each other" but with opposite directions. Is that the correct way to do this? I worry that subsequent tag or other edits to the "top" way segment might miss the duplicate "bottom" segment. Also whether that would foul up name rendering if there are two identical segments with the same name rendered twice.</li>
<li>Are there any detailed tutorials / info sources explaining how to create relations to designate routes for ways? Please reference if so.</li>
</ol>
<p>Thanks for the assistance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mtb" rel="tag" title="see questions tagged &#39;mtb&#39;">mtb</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '16, 03:14</strong></p>
<img src="https://secure.gravatar.com/avatar/efc638db6236b1d5523fb3e1c58a5ac5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hdmtb&#39;s gravatar image" />
<p><span>hdmtb</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hdmtb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49370" class="comments-container">
<span id="49383"></span>
<div id="comment-49383" class="comment">
<div id="post-49383-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: here <span>on this site</span> please ask one question only in one "question" entry. That makes it more helpful for other people in the future.</p>
</div>
<div id="comment-49383-info" class="comment-info">
<span class="comment-age">(23 Apr '16, 21:42)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="83130"></span>
<div id="comment-83130" class="comment">
<div id="post-83130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>re: route with nodes instead of ways I asked myself exactly the same question while mapping foot route in the city. Splitting many ways absolutely makes future maintenance way more complicated. Have you found any interesting feedback regarding this topic?</p>
</div>
<div id="comment-83130-info" class="comment-info">
<span class="comment-age">(20 Jan '22, 23:52)</span> <span class="comment-user userinfo">yrtimiD</span>
</div>
</div>
<span id="83137"></span>
<div id="comment-83137" class="comment">
<div id="post-83137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>maxerickson's answer below is still valid. You need to split the way.</p>
</div>
<div id="comment-83137-info" class="comment-info">
<span class="comment-age">(21 Jan '22, 07:53)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-49370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49370-form-container" class="comment-form-container">
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

<span id="49372"></span>

<div id="answer-container-49372" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49372-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Routes don't have to have a direction. It's fine to split ways where needed for modeling something. Alternative ways of modeling the difference reflected in the split would anyway be just as complicated.</p>
<p>If a way can have traffic in both directions, there's no problem using it for routes that traverse it in one direction or the other. Ways should not overlap.</p>
<p>So a route can have a direction, in which case the ways would be marked as forward or backward, but it is not necessary, many ways just have a blank role, with no info about direction. The is some indication of this on the wiki page for routes:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Relation:route#Members">http://wiki.openstreetmap.org/wiki/Relation:route#Members</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '16, 05:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-49372" class="comments-container">
<span id="49378"></span>
<div id="comment-49378" class="comment">
<div id="post-49378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for input. Still wondering about renderings that for example include arrows alongside routes to indicate intended direction. If all segments are not using the "correct" direction for a given route, those arrows will be confusing.</p>
<p>Also - should I include just the ways without nodes in the relations, or include ways and their nodes?</p>
<p>Thanks.</p>
</div>
<div id="comment-49378-info" class="comment-info">
<span class="comment-age">(23 Apr '16, 14:45)</span> <span class="comment-user userinfo">hdmtb</span>
</div>
</div>
<span id="49379"></span>
<div id="comment-49379" class="comment">
<div id="post-49379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't include nodes of ways. They can and should be automatically derived from ways. Also it just makes it way more difficult to keep the relation up to date since nodes can be added and removed from ways.</p>
</div>
<div id="comment-49379-info" class="comment-info">
<span class="comment-age">(23 Apr '16, 18:01)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49372-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49375"></span>

<div id="answer-container-49375" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49375-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>2&amp;3 : Add the way twice in the relation, and ensure that all the ways come in the proper order in the relation. You can add roles forward and backward but it is not mandatory : usually routes can be used in both directions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '16, 06:46</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-49375" class="comments-container">
&#10;</div>
<div id="comment-tools-49375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49375-form-container" class="comment-form-container">
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

