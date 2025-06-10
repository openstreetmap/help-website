+++
type = "question"
title = "How do you use route_relations?"
description = '''OK, so assuming I&#x27;ve done all the relations for all variants of a route number, how exactly do I use the route_master option? The wiki doesn&#x27;t make it that clear for me.'''
date = "2013-10-18T02:28:00Z"
lastmod = "2015-01-03T11:48:00Z"
weight = 27291
keywords = [ "route_master", "bus", "route", "relation" ]
aliases = [ "/questions/27291" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you use route_relations?](/questions/27291/how-do-you-use-route_relations)

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
<span id="post-27291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27291-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OK, so assuming I've done all the relations for all variants of a route number, how exactly do I use the route_master option? The wiki doesn't make it that clear for me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route_master" rel="tag" title="see questions tagged &#39;route_master&#39;">route_master</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Oct '13, 02:28</strong></p>
<img src="https://secure.gravatar.com/avatar/6035647123b433de9d9aaa4259d07e8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheUltimateKoopa&#39;s gravatar image" />
<p><span>TheUltimateK...</span><br />
<span class="score" title="161 reputation points">161</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheUltimateKoopa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted <strong>25 Oct '13, 02:32</strong> </span></p>
</div>
</div>
<div id="comments-container-27291" class="comments-container">
&#10;</div>
<div id="comment-tools-27291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27291-form-container" class="comment-form-container">
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

<span id="27484"></span>

<div id="answer-container-27484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27484-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, you are perfectly allowed to just ignore the route_master relation. No software currently uses the route_master relations. They stem from the mindset of collection relations <a href="https://wiki.openstreetmap.org/wiki/Relations/Relations_are_not_Categories">which are deprecated</a> in other tagging domains of OpenStreetMap.</p>
<p>If you insist on making a route master, then do it as follows: Create a new relation. Add all routes that have the same value for the "ref" tag (e.g. "410") and for the "network" and/or "operator" tags as relation members in arbitrary order. Then tag the relation with the tags that have all collected members in common, i.e. at least "ref", "operator", and/or "network".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '13, 06:47</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-27484" class="comments-container">
&#10;</div>
<div id="comment-tools-27484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27484-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39990"></span>

<div id="answer-container-39990" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39990-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Public transport usually works with lines. The route master represents such a line. The route relations are all the different variations. It's nice to be able to tie them together. Line identifiers are reused all the time. Without route_master relations, how would one know which line 1 route variations belong together and which are in a different city? In Aalst there are 2x a line 91 and 92 for some odd reason. So it can happen within the same city as well.</p>
<p>As for the question. Just create a route master and add all the route relations for the same line to it.</p>
<p>Jo</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '15, 00:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a7dfce5853b949d2c4d04076890b4899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Polyglot&#39;s gravatar image" />
<p><span>Polyglot</span><br />
<span class="score" title="38 reputation points">38</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Polyglot has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '15, 17:12</strong> </span></p>
</div>
</div>
<div id="comments-container-39990" class="comments-container">
<span id="40000"></span>
<div id="comment-40000" class="comment">
<div id="post-40000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"how would one know which line 1 route variations belong together and which are in a different city"?</p>
<p>One of the great things about OpenStreetMap is that it's a spatial database and you can do spatial queries on it.</p>
</div>
<div id="comment-40000-info" class="comment-info">
<span class="comment-age">(03 Jan '15, 11:48)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-39990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39990-form-container" class="comment-form-container">
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

