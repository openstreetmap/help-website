+++
type = "question"
title = "Correcting connectivity errors"
description = '''I&#x27;m running a connectivity verifier over a small portion of the OSM map (New Zealand, if you&#x27;re interested, but you&#x27;ll guess that from the examples below). Before I barge in and start fixing things I thought I&#x27;d better make sure that I&#x27;m going about it the right way, so here&#x27;s some example problems ...'''
date = "2013-06-19T00:45:00Z"
lastmod = "2013-06-20T10:36:00Z"
weight = 23506
keywords = [ "node", "connectivity", "intersection", "oneway" ]
aliases = [ "/questions/23506" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Correcting connectivity errors](/questions/23506/correcting-connectivity-errors)

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
<span id="post-23506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23506-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm running a connectivity verifier over a small portion of the OSM map (New Zealand, if you're interested, but you'll guess that from the examples below).</p>
<p>Before I barge in and start fixing things I thought I'd better make sure that I'm going about it the right way, so here's some example problems and what I think should be done to fix them. I should point out that I haven't visited most of the places I'm planning to correct, so my first question is: is that a legitimate thing to do? Fix stuff you haven't seen?</p>
<p>The questions are pretty uncontroversial, but I'd rather do this all correctly than muck things up.</p>
<p>First, <a href="https://www.openstreetmap.org/browse/way/117981891">here</a> is a one-way road that goes nowhere: you can't get out. Should the road continue through the carpark?</p>
<p><a href="https://www.openstreetmap.org/browse/way/87892754">Here</a> is another dead-end one-way. I assume I should connect it to the adjoining road?</p>
<p><a href="https://www.openstreetmap.org/browse/way/86818633">Here</a> is a road not connected to an adjoining road. There's a nearby node on Waimea road. If I understand correctly, I should connect Monaghan road to the node on Waimea (I'm guessing in this case by moving the end of Monoghan rather than by creating a short link), but I should not break Waimea Road at the intersection?</p>
<p>I guess my question is: what's the policy on intersections? For route-generation purposes, arcs must end at every intersection, but if I understand correctly, for OSM, there must be a shared node at every intersection, but not necessarily a break in either road. Is that right?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-connectivity" rel="tag" title="see questions tagged &#39;connectivity&#39;">connectivity</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '13, 00:45</strong></p>
<img src="https://secure.gravatar.com/avatar/e2b783689a83a2187923729774f6db19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeoffL&#39;s gravatar image" />
<p><span>GeoffL</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeoffL has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '13, 07:24</strong> </span></p>
</div>
</div>
<div id="comments-container-23506" class="comments-container">
&#10;</div>
<div id="comment-tools-23506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23506-form-container" class="comment-form-container">
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

<span id="23514"></span>

<div id="answer-container-23514" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23514-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GeoffL has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You appear to have fixed two of them which seem fine now. The car park seems to have three roads, one with a pay on exit. I don't think the in and out have to join although the out should be extended to reach the car park. Some car parks will have a route out, such as a foot path or cycle track from it which need connecting to the roads in so routers work. This one goes through the pay office so I wouldn't want to be routed through it. One other thing to do in cases of doubt it is contact the previous mapper who may have been "on the ground".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '13, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '13, 09:29</strong> </span></p>
</div>
</div>
<div id="comments-container-23514" class="comments-container">
<span id="23529"></span>
<div id="comment-23529" class="comment">
<div id="post-23529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I think I learned from reading the documentation that the right thing is to give it a go, so I did. There's plenty of carparks around and some are drawn as roads (see <a href="https://www.openstreetmap.org/browse/changeset/16613092)">https://www.openstreetmap.org/browse/changeset/16613092)</a> and some are areas. I'd prefer roads, but I guess you get what you get.</p>
</div>
<div id="comment-23529-info" class="comment-info">
<span class="comment-age">(19 Jun '13, 19:24)</span> <span class="comment-user userinfo">GeoffL</span>
</div>
</div>
<span id="23541"></span>
<div id="comment-23541" class="comment">
<div id="post-23541-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@GeoffL</span> actually the best thing is to do both. Create a parking area instead of a single node and tag it as <em>amenity=parking</em>. Draw all roads leading to/from and inside the parking area. The roads inside should be tagged as <em>highway=service</em> and <em>service=parking_aisle</em>. See <a href="https://www.openstreetmap.org/?lat=-36.992675&amp;lon=174.881433&amp;zoom=18&amp;layers=M">these examples</a>.</p>
</div>
<div id="comment-23541-info" class="comment-info">
<span class="comment-age">(20 Jun '13, 10:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23514-form-container" class="comment-form-container">
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

