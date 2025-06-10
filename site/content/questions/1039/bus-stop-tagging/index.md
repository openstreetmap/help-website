+++
type = "question"
title = "Bus stop tagging"
description = '''I live in Vancouver, British Columbia, Canada. The bus stops here are tagged in differing ways. They seem to be tagged with the bus numbers or bay numbers for the name field. I am wondering how they should be tagged. Briefly, each bus stop has a number of ways to identify it.  Bus stop number. This ...'''
date = "2010-10-07T05:09:00Z"
lastmod = "2010-10-07T09:52:00Z"
weight = 1039
keywords = [ "bus", "stop", "tagging" ]
aliases = [ "/questions/1039" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bus stop tagging](/questions/1039/bus-stop-tagging)

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
<span id="post-1039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1039-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I live in Vancouver, British Columbia, Canada. The bus stops here are tagged in differing ways. They seem to be tagged with the bus numbers or bay numbers for the name field. I am wondering how they should be tagged.</p>
<p>Briefly, each bus stop has a number of ways to identify it.</p>
<ol>
<li>Bus stop number. This is a unique 5 digit number (e.g. 53174) that identifies the bus stop and can be used to request the details of the next buses coming to the stop by an automated service. It may be possible that some of the longer bus stops have two poles with the same number.</li>
<li>Bus stop location. This is the location of the bus stop as documented by the Translink website (e.g SB MARINE DRIVE AT KERR ST, 900S BLOCK 8 AVE NEW WESTMINSTER)and I believe is also unique but may not be for larger stops.</li>
<li>Bus stop name. Not all bus stops have this, but some of the larger ones have names (e.g. Granville, Bridgeport, Sasmat). These are not unique.</li>
<li>Buses that use the stop. This is subject to change as scheduling changes and is definitely not unique. Bus routes are numbers from 1-999, but the route number does not uniquely describe the route (e.g. some routes may go via a side street but share the same route number, and buses going both ways on a route have the same number)</li>
</ol>
<p>How should I tag the stops?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-stop" rel="tag" title="see questions tagged &#39;stop&#39;">stop</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '10, 05:09</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-1039" class="comments-container">
&#10;</div>
<div id="comment-tools-1039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1039-form-container" class="comment-form-container">
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

<span id="1047"></span>

<div id="answer-container-1047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1047-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't have to put all information on the stop itself. Specify what describes the bus stop with the tags described on <a href="http://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop">the wiki page about bus_stop</a>. Tag the name of the station and/or its reference on the node. You can add more details if you wish (shelter, bench, wheelchair). The location is really optional since the node is self descriptive.<br />
Describe the buses lines separately with <a href="http://wiki.openstreetmap.org/wiki/Relation:route">relations of type 'route'</a>.<br />
There is a portal about buses on the wiki : <a href="http://wiki.openstreetmap.org/wiki/Buses"></a><a href="http://wiki.openstreetmap.org/wiki/Buses"></a><a href="http://wiki.openstreetmap.org/wiki/Buses">http://wiki.openstreetmap.org/wiki/Buses</a><br />
For more complex cases (lines changing during the day/the week, routes depending on direction, etc) where we don't have a consensus on the wiki, you can subscribe to the active mailing-list dedicated for public transportation in OSM at '<a href="http://lists.openstreetmap.org/listinfo/talk-transit">talk-transit</a>'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '10, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '10, 16:43</strong> </span></p>
</div>
</div>
<div id="comments-container-1047" class="comments-container">
&#10;</div>
<div id="comment-tools-1047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1047-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1043"></span>

<div id="answer-container-1043" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1043-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Bus stop number looks like a ref=</li>
<li>Bus stop location looks like an address, this could be an alternative to storing the location as a position. This should be tagged with addr:*= on the coresponding addresses and not on the bus stop.</li>
<li>Bus stop name should be tagged as name=</li>
<li>Bus routes can be tagged using a relation. See <a href="http://wiki.openstreetmap.org/wiki/Relation:route#Bus_Routes_.28also_trolley_bus.29">the wiki</a></li>
</ol>
<p>I hope this was helpfull.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '10, 08:56</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-1043" class="comments-container">
&#10;</div>
<div id="comment-tools-1043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1043-form-container" class="comment-form-container">
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

