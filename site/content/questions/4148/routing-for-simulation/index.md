+++
type = "question"
title = "Routing for simulation?"
description = '''Hi, I&#x27;m doing a school project- my goal is to simulate some of the city buses driving around in my town. I was just wondering if this was possible with some combination of open source projects related to osm.  I&#x27;d essentially like to just draw a number of bus routes on the map (I have lat/long coord...'''
date = "2011-03-28T10:54:00Z"
lastmod = "2011-03-28T13:02:00Z"
weight = 4148
keywords = [ "routing", "simulation" ]
aliases = [ "/questions/4148" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Routing for simulation?](/questions/4148/routing-for-simulation)

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
<span id="post-4148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4148-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm doing a school project- my goal is to simulate some of the city buses driving around in my town. I was just wondering if this was possible with some combination of open source projects related to osm.</p>
<p>I'd essentially like to just draw a number of bus routes on the map (I have lat/long coordinates of all the bus stops), and then I'd like to simulate buses moving along these routes.</p>
<p>It seems like something best done offline- but then the question is, given the info I have (lat/long), is it possible to do the routing offline? If so, what sort of file format should I work in?</p>
<p>Any pointers on how I could get started would be immensely helpful :)</p>
<p>Cheers, Heather</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-simulation" rel="tag" title="see questions tagged &#39;simulation&#39;">simulation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '11, 10:54</strong></p>
<img src="https://secure.gravatar.com/avatar/54d0b6494927c0040b96ed327202e8dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="heathermiller&#39;s gravatar image" />
<p><span>heathermiller</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="heathermiller has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4148" class="comments-container">
&#10;</div>
<div id="comment-tools-4148" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4148-form-container" class="comment-form-container">
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

<span id="4153"></span>

<div id="answer-container-4153" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4153-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Actually I am not sure if you really need "routing" (which would be calculate a route from start to end using a road graph). Your request sounds as if you already knew the routes the busses will take, so you probably want to display these bus routes on a map? Have a look here how bus routes work in OSM: <a href="https://wiki.openstreetmap.org/wiki/Bus_routes">https://wiki.openstreetmap.org/wiki/Bus_routes</a></p>
<p>If I am wrong, this is how you could bring routing to work: You will have to download an osm-extract of the area you are interested in (or download the planet-file and extract it yourself with osmosis). Then you will usually load the data into a database or convert it otherwise to optimize it for the scope. There is projects which offer styles optimized for routing on OSM as well as software to do the routing, e.g. <a href="https://wiki.openstreetmap.org/wiki/Gosmore">gosmore</a>, <a href="https://wiki.openstreetmap.org/wiki/MoNav">monav</a> and others. An introduction to routing and related software can be found <a href="https://wiki.openstreetmap.org/wiki/Routing">here in the wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '11, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '11, 13:09</strong> </span></p>
</div>
</div>
<div id="comments-container-4153" class="comments-container">
&#10;</div>
<div id="comment-tools-4153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4153-form-container" class="comment-form-container">
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

