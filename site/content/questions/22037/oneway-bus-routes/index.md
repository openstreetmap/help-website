+++
type = "question"
title = "Oneway bus routes"
description = '''I am trying to mark some bus routes which go only one way down two-way roads, but I can&#x27;t see how to check whether I&#x27;ve chosen the correct facing arrow. Unfortunately the Transport Map doesn&#x27;t show any oneway arrows, so I can&#x27;t check what I&#x27;ve done. Can anyone suggest what to do, please?'''
date = "2013-05-02T14:18:00Z"
lastmod = "2015-02-08T10:05:00Z"
weight = 22037
keywords = [ "bus", "route", "arrow", "oneway" ]
aliases = [ "/questions/22037" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Oneway bus routes](/questions/22037/oneway-bus-routes)

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
<span id="post-22037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22037-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to mark some bus routes which go only one way down two-way roads, but I can't see how to check whether I've chosen the correct facing arrow. Unfortunately the Transport Map doesn't show any oneway arrows, so I can't check what I've done. Can anyone suggest what to do, please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-arrow" rel="tag" title="see questions tagged &#39;arrow&#39;">arrow</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '13, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/b96c53807761fec6103da2fc2f003b26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonga&#39;s gravatar image" />
<p><span>Jonga</span><br />
<span class="score" title="101 reputation points">101</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonga has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22037" class="comments-container">
&#10;</div>
<div id="comment-tools-22037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22037-form-container" class="comment-form-container">
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

<span id="22050"></span>

<div id="answer-container-22050" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22050-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-22050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The following assumes you are mapping your bus route with a route relation.</p>
<p>On the sections of the route which are only travelled by the bus in one direction, add in the role either forward or backward depending whether the bus travels with or against the direction of the way.</p>
<p>In Potlatch 2 the role is set using the 3 little arrow logos next to the route in the Simple View or the third field in the relations view in Advanced mode. You can see the direction of the way by the orientation of the arrow in the tool panel (usually lower-right corner), or you can choose the Enhanced view from the MapStyle drop down and this will draw arrows on a way when it is selected to make it's direction more obvious.</p>
<p>In JOSM you choose for the direction of all ways to be shown by setting an option. JOSM also has more features for adding bus routes, but I suspect these might be overly complex for what you want to do right now.</p>
<p>Here are example ways with this type of tagging on bus routes (you could open them in an editor to inspect how they appear:</p>
<ul>
<li><a href="http://osm.org/go/eu8Y~y39?layers=T">City Loop, Nottingham</a> (many buses do a one way loop around the city centre for instance on <a href="http://www.openstreetmap.org/browse/way/16202048">Middle Hill</a> ),</li>
<li><a href="http://osm.org/go/eu8Sp2w9?layers=T">Inham Nook, Chilwell</a> (final part of route is a <a href="http://www.openstreetmap.org/browse/way/12355557">loop</a>),</li>
<li><a href="http://osm.org/go/eus6a41Z--?layers=T">Maidenhead</a> (a number of buses go only one way on roads at the NW side of town, including <a href="http://www.openstreetmap.org/browse/way/4261323">Cranbrook Drive</a>).</li>
</ul>
<p>Here are links to each of these sites on OePNV Map another visualisation of public transport which does show one direction segments : <a href="http://www.öpnvkarte.de/?zoom=17&amp;lat=52.95081&amp;lon=-1.14637&amp;layers=TBTTT">Middle Hill</a>, <a href="http://www.öpnvkarte.de/?zoom=18&amp;lat=52.92275&amp;lon=-1.24838&amp;layers=TBTTT">Inham Nook</a>, <a href="http://www.öpnvkarte.de/?zoom=17&amp;lat=51.53396&amp;lon=-0.74806&amp;layers=TBTTT">Cranbrook Drive</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '13, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 May '13, 14:35</strong> </span></p>
</div>
</div>
<div id="comments-container-22050" class="comments-container">
<span id="22051"></span>
<div id="comment-22051" class="comment">
<div id="post-22051-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Multiple examples used in case any bus routes change (not unknown in Maidenhead)</p>
</div>
<div id="comment-22051-info" class="comment-info">
<span class="comment-age">(02 May '13, 19:00)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="22057"></span>
<div id="comment-22057" class="comment">
<div id="post-22057-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, thanks, that's answered it.</p>
</div>
<div id="comment-22057-info" class="comment-info">
<span class="comment-age">(02 May '13, 21:28)</span> <span class="comment-user userinfo">Jonga</span>
</div>
</div>
<span id="22061"></span>
<div id="comment-22061" class="comment">
<div id="post-22061-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can accept the answer, then others can see that this helped</p>
</div>
<div id="comment-22061-info" class="comment-info">
<span class="comment-age">(02 May '13, 23:27)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="22077"></span>
<div id="comment-22077" class="comment">
<div id="post-22077-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SK53</span> Your first and third link are broken.</p>
</div>
<div id="comment-22077-info" class="comment-info">
<span class="comment-age">(03 May '13, 14:03)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22081"></span>
<div id="comment-22081" class="comment">
<div id="post-22081-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can edit the answer too!</p>
</div>
<div id="comment-22081-info" class="comment-info">
<span class="comment-age">(03 May '13, 14:33)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22050-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22042"></span>

<div id="answer-container-22042" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22042-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bus routes are mapped using a relation to link together the ways that make up the route. It is usual to create a relation for each direction (and each variant) of the route. These can then be linked together using the Route Master relation. See <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport#Route">Public Transport Route</a> for more information. However the way Transport Map and other renderers display the route may be an issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '13, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/6edb4957e57770118c3b8022cfce68a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srbrook&#39;s gravatar image" />
<p><span>srbrook</span><br />
<span class="score" title="993 reputation points">993</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srbrook has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '13, 18:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-22042" class="comments-container">
<span id="22043"></span>
<div id="comment-22043" class="comment">
<div id="post-22043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but that doesn't seem to answer the specific point. When I've added a route, there are three direction options on the drop down: &gt;&gt;, &lt;&lt;, &lt;&gt;. The trouble is, I don't know which direction &gt;&gt; and &lt;&lt; are pointing along the road. The road itself is two-way so the bus route could theoretically be in either direction, although where there are stops, these are placed on the correct side.</p>
</div>
<div id="comment-22043-info" class="comment-info">
<span class="comment-age">(02 May '13, 15:11)</span> <span class="comment-user userinfo">Jonga</span>
</div>
</div>
<span id="22074"></span>
<div id="comment-22074" class="comment">
<div id="post-22074-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>left to right arrow sign (&gt;&gt;) means forward(node direction of the road).</p>
</div>
<div id="comment-22074-info" class="comment-info">
<span class="comment-age">(03 May '13, 12:32)</span> <span class="comment-user userinfo">erkinalp</span>
</div>
</div>
</div>
<div id="comment-tools-22042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22042-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39991"></span>

<div id="answer-container-39991" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39991-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-39991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't add roles to the ways of your route. Simply add all ways in the correct order.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '15, 00:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a7dfce5853b949d2c4d04076890b4899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Polyglot&#39;s gravatar image" />
<p><span>Polyglot</span><br />
<span class="score" title="38 reputation points">38</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Polyglot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39991" class="comments-container">
<span id="40576"></span>
<div id="comment-40576" class="comment">
<div id="post-40576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Fun thing is this likes to break, and quite badly, on routes that backtrack or loop. The 105 Peoria in north Tulsa and pretty much any route hitting Denver Avenue Station has this issue.</p>
</div>
<div id="comment-40576-info" class="comment-info">
<span class="comment-age">(24 Jan '15, 09:28)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="40852"></span>
<div id="comment-40852" class="comment">
<div id="post-40852-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's why I'm creating scripts to check whether those routes are still continuous and report the ones which aren't anymore.</p>
<p>Hopefully, one day, iD will be rewritten in such a way that route and other relations aren't broken anymore.</p>
</div>
<div id="comment-40852-info" class="comment-info">
<span class="comment-age">(08 Feb '15, 10:05)</span> <span class="comment-user userinfo">Polyglot</span>
</div>
</div>
</div>
<div id="comment-tools-39991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39991-form-container" class="comment-form-container">
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

