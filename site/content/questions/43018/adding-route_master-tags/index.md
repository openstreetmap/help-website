+++
type = "question"
title = "Adding route_master tags?"
description = '''Am I reading this correctly? If a bus route is a single route that travels in a circle (i.e. in one direction, and loops), for example, route 526 in southeast England, has a circular route that travels between Crawley, Charlwood, Gatwick Airport, Horley, Smallfield, then back to Crawley, this route ...'''
date = "2015-05-11T15:24:00Z"
lastmod = "2015-05-11T15:27:00Z"
weight = 43018
keywords = [ "routes", "bus" ]
aliases = [ "/questions/43018" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding route_master tags?](/questions/43018/adding-route_master-tags)

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
<span id="post-43018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43018-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Am I reading this correctly? If a bus route is a single route that travels in a circle (i.e. in one direction, and loops), for example, route 526 in southeast England, has a circular route that travels between Crawley, Charlwood, Gatwick Airport, Horley, Smallfield, then back to Crawley, this route would be tagged as: type=route, route=bus, and ref=526?</p>
<p>However, if a route, is essentially a loop, but rather than going through areas, like A, B, C, D, A in a circle, it's more like A, B, C, D, C, B, A, should the full A to D to A route be treated as one route, or separate routes, for A to D, and D to A? And for routes that have variations (e.g. a route may serve a railways station on a Saturday, but not on any other day), how exactly does the route_master relation work? I.e. when adding a relation to a way, at the beginning of a route, do you add the relation, but tag it as route_master instead of just route? And when you finish one variation, for all other variations, do the parts of the route that are the same, have to be tagged again, for each variation?</p>
<p>And one final question (for now), for general route relations, do the ways have to be added in the exact order they are used? E.g. if a route starts on 1st Street, turns left into 3rd Street, then, does the route have to be added to 1st Street first, then 3rd Street? This may seem an obvious question, but I'm more confused about the route_master. The wiki doesn't really explain when, and how you add it, just what it is.</p>
<p>EDIT: Thanks for moving this to a separate question. I'm quite sure the last question should be "yes" (to the order of adding relations to ways). To expand on the question about route_master tags, I have another question, after reading some old questions about bus routes... am I correct in thinking the following?</p>
<p>Each variation of a route, has a separate relation (type=route, route=bus). Each of these relations, are itself, added to a relation (type=route_master, route_master=bus), such that: A route_master relation, contains, itself, multiple relations (for the variations of the route)?</p>
<p>Therefore, after adding the different route varations, how do you add "child relations", to a "parent relation"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routes" rel="tag" title="see questions tagged &#39;routes&#39;">routes</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '15, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/6035647123b433de9d9aaa4259d07e8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheUltimateKoopa&#39;s gravatar image" />
<p><span>TheUltimateK...</span><br />
<span class="score" title="161 reputation points">161</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheUltimateKoopa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '15, 15:39</strong> </span></p>
</div>
</div>
<div id="comments-container-43018" class="comments-container">
<span id="43019"></span>
<div id="comment-43019" class="comment">
<div id="post-43019-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Previously this question was added as an answer to this question:</p>
<p><a href="/questions/42928/how-do-i-add-bus-route-information-to-bus-stops">https://help.openstreetmap.org/questions/42928/how-do-i-add-bus-route-information-to-bus-stops</a></p>
</div>
<div id="comment-43019-info" class="comment-info">
<span class="comment-age">(11 May '15, 15:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43018" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43018-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

