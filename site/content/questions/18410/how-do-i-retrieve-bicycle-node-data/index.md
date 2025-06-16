+++
type = "question"
title = "How do I retrieve bicycle node data?"
description = '''For my bachelor project I&#x27;m working on a bicycle route planner and I&#x27;m trying to get, at the very least, the nodes and connections, with matching distance data for the bicycle route network in (a part of) the Netherlands. When I zoom in on The Netherlands the bicycle nodes and the conenctions betwee...'''
date = "2012-12-13T11:37:00Z"
lastmod = "2012-12-16T12:55:00Z"
weight = 18410
keywords = [ "nodes", "netherlands", "bicycle" ]
aliases = [ "/questions/18410" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I retrieve bicycle node data?](/questions/18410/how-do-i-retrieve-bicycle-node-data)

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
<span id="post-18410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18410-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For my bachelor project I'm working on a bicycle route planner and I'm trying to get, at the very least, the nodes and connections, with matching distance data for the bicycle route network in (a part of) the Netherlands.</p>
<p>When I zoom in on The Netherlands the bicycle nodes and the conenctions between them are numbered and listed in light blue, so I know the data is there, and I assume there is also distance data available. I have downloaded the .osm for the benelux, but now I have no idea how I can retrieve the data. I've been looking around but I haven't really found a tutorial or something. Can someone point me in the right direction?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-netherlands" rel="tag" title="see questions tagged &#39;netherlands&#39;">netherlands</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '12, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/eae8ee6cf28243e8986e0175081a1c65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoefschildpad&#39;s gravatar image" />
<p><span>Zoefschildpad</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoefschildpad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18410" class="comments-container">
&#10;</div>
<div id="comment-tools-18410" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18410-form-container" class="comment-form-container">
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

<span id="18412"></span>

<div id="answer-container-18412" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18412-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Zoefschildpad has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess you're not familiar with the OSM file format, so please read a bit about <a href="https://wiki.openstreetmap.org/wiki/Beginners_Guide_1.4.1">tagging</a> first.</p>
<p>I'll try to explain it on programmers level without a background in OSM, if this is wrong, please tell me what level you expect.</p>
<p>Basically, OSM data has 3 primitives: Nodes, Ways and Relations. Nodes just have single geographical coordinates, Ways are an ordered list of nodes, and Relations are a collection of other features (thus Nodes, Ways and other Relations).</p>
<p>Every primitive can have a number of tags to denote what type of feature it is.</p>
<p>For the case you're looking at, nodes have a tag rcn_ref=xx (regional cycling network reference), and the ways between those nodes are part of a relation. The relation is tagged as following:</p>
<pre><code>type=route
route=bicycle
network=rcn
note=xx-yy</code></pre>
<p>You can't trust on the correctness of the "note" tags, so you have to calculate the end nodes by getting all the ways in the relation, combining it to a single line and checking the end nodes of that line.</p>
<p>PS: Note that you don't have to download all data, there are services available where you can just download parts of the data (with the tags you want), see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a> or <a href="https://wiki.openstreetmap.org/wiki/Xapi">XAPI</a></p>
<p>PS2: the tags with rcn are also used in other countries, where they are normal (long) cycle routes, so no node-networks. So you do have to implement extra checks and provide bounding boxes to be sure you're working with node networks.</p>
<p>PS3: User <a href="https://www.openstreetmap.org/user/Polyglot">Polyglot</a> also made relations per cycle node network in Belgium, see this: <a href="https://www.openstreetmap.org/browse/relation/1726882">relation 1726882</a>, if you want information regarding cycle nodes you can also contact him.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '12, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-18412" class="comments-container">
<span id="18472"></span>
<div id="comment-18472" class="comment">
<div id="post-18472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That was really helpful, I think I got the nodes and ways now. One thing I noticed though is that there isn't a length-attribute in the ways, is there an easy way to calculate the length of a way?</p>
</div>
<div id="comment-18472-info" class="comment-info">
<span class="comment-age">(15 Dec '12, 17:20)</span> <span class="comment-user userinfo">Zoefschildpad</span>
</div>
</div>
<span id="18473"></span>
<div id="comment-18473" class="comment">
<div id="post-18473-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There are a bunch of links that might be useful <a href="http://en.wikipedia.org/wiki/Haversine_formula">here</a> and another explanation <a href="http://www.movable-type.co.uk/scripts/latlong.html">here</a>.</p>
</div>
<div id="comment-18473-info" class="comment-info">
<span class="comment-age">(15 Dec '12, 18:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="18485"></span>
<div id="comment-18485" class="comment">
<div id="post-18485-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OSM only has the raw data (including distances would be redundant as they can be calcualted), so you have to do the calculation yourself. The links given by SomeoneElse are indeed useful.</p>
</div>
<div id="comment-18485-info" class="comment-info">
<span class="comment-age">(16 Dec '12, 12:55)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-18412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18412-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18421"></span>

<div id="answer-container-18421" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18421-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In <a href="http://forum.openstreetmap.org/viewtopic.php?id=18951">this thread</a> on the Dutch language part of the OpenStreetMap forum. People talk about how they constructed <a href="http://mijndev.openstreetmap.nl/~ligfietser/fiets/?map=route&amp;zoom=13&amp;lat=52.03553&amp;lon=5.1682&amp;layers=0B0000FFTFFFFFFFF">this map</a>. Including examples of the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a> queries they used to get the bicycle network. You can find all the queries in the javascript files of the website.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '12, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-18421" class="comments-container">
&#10;</div>
<div id="comment-tools-18421" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18421-form-container" class="comment-form-container">
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

