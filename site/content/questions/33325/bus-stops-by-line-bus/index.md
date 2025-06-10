+++
type = "question"
title = "Bus stops by line bus"
description = '''Hi, How I can to take a bus stops with coordinates using line of bus?  Like this link http://www.overpass-api.de/api/sketch-line?ref=409&amp;amp;network=ATAC&amp;amp;style=wuppertal I tried using this query but the ref (number of bus) is different by number of bus of company http://overpass-api.de/api/xapi?...'''
date = "2014-05-20T14:28:00Z"
lastmod = "2014-12-19T23:09:00Z"
weight = 33325
keywords = [ "overpass", "bus", "ref", "busstops", "network" ]
aliases = [ "/questions/33325" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bus stops by line bus](/questions/33325/bus-stops-by-line-bus)

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
<span id="post-33325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33325-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>How I can to take a bus stops with coordinates using line of bus? Like this link <a href="http://www.overpass-api.de/api/sketch-line?ref=409&amp;network=ATAC&amp;style=wuppertal">http://www.overpass-api.de/api/sketch-line?ref=409&amp;network=ATAC&amp;style=wuppertal</a></p>
<p>I tried using this query but the ref (number of bus) is different by number of bus of company <a href="http://overpass-api.de/api/xapi?*%5Bhighway=bus_stop%5D%5Boperator=ATAC%5D">http://overpass-api.de/api/xapi?*[highway=bus_stop][operator=ATAC]</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-ref" rel="tag" title="see questions tagged &#39;ref&#39;">ref</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '14, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/14a5ca3b780dbd33a047f3d3eb426963?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alessandro%20Borelli&#39;s gravatar image" />
<p><span>Alessandro B...</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alessandro Borelli has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33325" class="comments-container">
&#10;</div>
<div id="comment-tools-33325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33325-form-container" class="comment-form-container">
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

<span id="33345"></span>

<div id="answer-container-33345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33345-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This depends on how your bus route has been mapped into OSM. Some contributors use the old tagging "highway=bus_stop" for the bus stops but others use the new "<a href="http://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport">public transport</a>" scheme with "<a href="http://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dplatform">public_transport=platform</a>" (where transit users are waiting) and/or "<a href="http://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dstop_position">public_transport=stop_position</a>" (where the bus itselfs stops on the highway). But in both cases, the "ref" is not always provided on hte stop position or is concatenated (like "1;2;5") which is not very useful. The best is to take the "ref" from the <a href="http://wiki.openstreetmap.org/wiki/Relation:route#Bus_routes_.28also_trolley_bus.29">bus route (relation) itself</a>. And of course, a bus stop may belong to several bus routes/relations.</p>
<p>So you should retrieve the expected bus relation first with the "operator" and "ref" and then walk through the relation members to find the elements representing the bus stops (either with "highway=bus_stop" or "public_transport=*"), then get the coordinates (be careful, some of theses elements are nodes which is easy but some others can be theoritically polygons (closed ways) then the coordinates should be calculated (centroid)).<br />
If the relation doesn't exist for your bus route, then create it (it's fast when all bus stops are already mapped).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '14, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
</div>
<div id="comments-container-33345" class="comments-container">
<span id="33346"></span>
<div id="comment-33346" class="comment">
<div id="post-33346-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi, thank you for your answer. I took the node of bus with this call <a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;rel%5Bref=409%5D%5Bnetwork=ATAC%5D;out;">http://overpass-api.de/api/interpreter?data=[out:json];rel[ref=409][network=ATAC];out;</a></p>
<p>Now I have a node of any bus stops with coordinates. :)</p>
</div>
<div id="comment-33346-info" class="comment-info">
<span class="comment-age">(21 May '14, 11:07)</span> <span class="comment-user userinfo">Alessandro B...</span>
</div>
</div>
</div>
<div id="comment-tools-33345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33345-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39733"></span>

<div id="answer-container-39733" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39733-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>ref should be used for the identifier of the stop. route_ref can contain a semicolon separated list of lines which serve this bus stop.</p>
<p>Since public_transport=platform/bus=yes is still not rendered after 3 years, it's safe to assume all bus stops are still marked highway=bus_stop.</p>
<p>Apparently it's indeed allowed nowadays to use ways, or multipolygon relations nowadays for the platforms. Where I map in Belgium, you will only find nodes for public_transport=platform/bus=yes/highway=bus_stop. If there is an actual platform, then there will be a way or an area with public_transport=platform/highway=platform (to get it rendered) in addition to that node. It's the public_transport=platform/bus=yes/highway=bus_stop node which contains all the juicy details. No need to duplicate those to all bus stop related objects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '14, 23:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a7dfce5853b949d2c4d04076890b4899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Polyglot&#39;s gravatar image" />
<p><span>Polyglot</span><br />
<span class="score" title="38 reputation points">38</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Polyglot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39733" class="comments-container">
&#10;</div>
<div id="comment-tools-39733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39733-form-container" class="comment-form-container">
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

