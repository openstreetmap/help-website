+++
type = "question"
title = "Topology and wayfinding"
description = '''Being rather new in OSM.... I am wondering how node/edge topology is handled internally in OSM networks. Apparently - in the network that can be down loaded straight away - major roads are continues, i.e. not &#x27;broken up&#x27; where minor roads are joining. Accordingly nodes are missing at these &#x27;tributar...'''
date = "2011-09-24T21:25:00Z"
lastmod = "2011-10-03T13:02:00Z"
weight = 8126
keywords = [ "topology" ]
aliases = [ "/questions/8126" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Topology and wayfinding](/questions/8126/topology-and-wayfinding)

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
<span id="post-8126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8126-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Being rather new in OSM.... I am wondering how node/edge topology is handled internally in OSM networks. Apparently - in the network that can be down loaded straight away - major roads are continues, i.e. not 'broken up' where minor roads are joining. Accordingly nodes are missing at these 'tributary' locations. How does e.g. shortest path analysis take place, when full node/edge topology is missing? Do OSM apply an alternative algorithm that - in some clever way - can work without topology, or is there a version of the network with all edges split up at junctions? If the latter is the case, can such a data set be downloaded? And if so, how? Cheers Hans Skov-Petersen, Uni. of Copenhagen, DK</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-topology" rel="tag" title="see questions tagged &#39;topology&#39;">topology</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '11, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/7ee16a181aada217a5742f7ac4d1df55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hans%20SP&#39;s gravatar image" />
<p><span>Hans SP</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hans SP has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8126" class="comments-container">
&#10;</div>
<div id="comment-tools-8126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8126-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="8127"></span>

<div id="answer-container-8127" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8127-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-8127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are to look at the OSM data as a formal graph then a <em>node</em> in OSM is a node in the graph and the OSM <em>way</em> is a path. This is the most logical way to store information about the roads. To find the edges you have to splitt the paths into the edges. Routing software does this when reading the OSM data.</p>
<p>When you think about it the road network is not a planar graph. Roads can cross without there being an intersection. This can happen if one or boath ways is a bridge or a tunnel. Routing engies should not route between ways that cross without a node.</p>
<p>If you find two ways that does not share a node at the intersection in OSM, but there is an intersection there, then this is an error in the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '11, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8127" class="comments-container">
&#10;</div>
<div id="comment-tools-8127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8127-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8159"></span>

<div id="answer-container-8159" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8159-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Gnonthgol has given a good answer. But on a broader point, you should bear in mind: OSM data is not optimised for any single use, whether that be routing or rendering or whatever. Rather, you are expected to preprocess it into a form that suits your application's needs.</p>
<p>So, for example, the Mapnik rendering on <a href="http://osm.org">osm.org</a> does not use OSM data directly; rather, it uses an optimised version produced by the program osm2pgsql. Similarly, as Gnonthgol says, you will need to create a graph to route effectively, and there are several pieces of software that do that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '11, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-8159" class="comments-container">
&#10;</div>
<div id="comment-tools-8159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8159-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8248"></span>

<div id="answer-container-8248" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8248-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hans, for the specific issue of reconnecting minor roads to major ones, you have at least two tools that allow you to do just this (e. g. simply point them to Copenhagen in your above case): <a href="http://tools.geofabrik.de/osmi">http://tools.geofabrik.de/osmi</a> and <a href="http://keepright.ipax.at/report_map.php">http://keepright.ipax.at/report_map.php</a></p>
<p>They are even capable to detect "suspicious node proximities" and show you the potential "culprits" automatically</p>
<p>Hervé</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Oct '11, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/63a3d001d166921b51b1bd82b2865726?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Herve5&#39;s gravatar image" />
<p><span>Herve5</span><br />
<span class="score" title="568 reputation points">568</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Herve5 has 3 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Oct '11, 13:05</strong> </span></p>
</div>
</div>
<div id="comments-container-8248" class="comments-container">
&#10;</div>
<div id="comment-tools-8248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8248-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8229"></span>

<div id="answer-container-8229" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8229-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks, both of you. I continue with a local version, where I can build the full topology my self. For sure I finde many places (e.g. i Copenhagen) where nodes are not present, where minor meets major roads. I would regard route finding a rather generic application, not 'any single use'. I agree that route finding can take place with only nodes (with node/edge topology build in), but rendering resulting routes will be problematic, without edges being clipped at junctions/nodes. Cheers Hans</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '11, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/7ee16a181aada217a5742f7ac4d1df55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hans%20SP&#39;s gravatar image" />
<p><span>Hans SP</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hans SP has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8229" class="comments-container">
&#10;</div>
<div id="comment-tools-8229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8229-form-container" class="comment-form-container">
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

