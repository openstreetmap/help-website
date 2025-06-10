+++
type = "question"
title = "Export airport taxiways"
description = '''I would like to know how to export airport taxiways in .osm format. When I try to export the area where the airport is located, I just get the map of the roads for cars and other vehicles around the airport, but not the taxiways within the airport where the aircraft taxi on ground prior to its depar...'''
date = "2021-06-01T16:55:00Z"
lastmod = "2021-06-01T17:48:00Z"
weight = 80385
keywords = [ "airport", "export", "aircraft", "taxiway", "aerodrome" ]
aliases = [ "/questions/80385" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Export airport taxiways](/questions/80385/export-airport-taxiways)

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
<span id="post-80385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80385-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to know how to export airport taxiways in .osm format. When I try to export the area where the airport is located, I just get the map of the roads for cars and other vehicles around the airport, but not the taxiways within the airport where the aircraft taxi on ground prior to its departure.</p>
<p>Any hint on how to export the aerodrome layout?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-airport" rel="tag" title="see questions tagged &#39;airport&#39;">airport</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-aircraft" rel="tag" title="see questions tagged &#39;aircraft&#39;">aircraft</span> <span class="post-tag tag-link-taxiway" rel="tag" title="see questions tagged &#39;taxiway&#39;">taxiway</span> <span class="post-tag tag-link-aerodrome" rel="tag" title="see questions tagged &#39;aerodrome&#39;">aerodrome</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '21, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/f2c1b9639ce80a175c177b1f97b3c79e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PabloFuentesdf&#39;s gravatar image" />
<p><span>PabloFuentesdf</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PabloFuentesdf has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80385" class="comments-container">
<span id="80386"></span>
<div id="comment-80386" class="comment">
<div id="post-80386-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you explain how you tried to export the data, and what software you then used to look at the result? And which airport did you test this with?</p>
</div>
<div id="comment-80386-info" class="comment-info">
<span class="comment-age">(01 Jun '21, 16:57)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="80387"></span>
<div id="comment-80387" class="comment">
<div id="post-80387-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just tried the basic Export functionality offered by OpenStreetMap.org in the web browser. Then I converted this .osm file into a network for Eclipse SUMO (Simulator of Urban Mobility). The airport I tested is LEMD (Madrid Barajas Airport).</p>
<p>I want to simulate the movement of the aircrafts on the surface of the airport, in order to assess taxi times.</p>
</div>
<div id="comment-80387-info" class="comment-info">
<span class="comment-age">(01 Jun '21, 17:05)</span> <span class="comment-user userinfo">PabloFuentesdf</span>
</div>
</div>
</div>
<div id="comment-tools-80385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80385-form-container" class="comment-form-container">
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

<span id="80389"></span>

<div id="answer-container-80389" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80389-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PabloFuentesdf has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The most likely explanation is that the software you have used to process the data was not considering taxiways when building the routing graph (since exporting OSM data from the web site will definitely include them, and the LEMD airport definitely has them mapped in OSM).</p>
<p>You will have to reconfigure the software to process taxiways in addition to (or instead of) roads which I assume is what the software normally does.</p>
<p>If you cannot do that, then there is another option; you can modify the OSM file and make it look like all the taxiways were service roads. Then the graph building will likely consider them. This change can either be achieved with the "tag transform" functionality of the "Osmosis" software, or you can also try a simple text search&amp;replace on the .osm file you have exported (look for something like <code>&lt;tag k="aeroway" v="taxiway" /&gt;</code> and replace it with <code>&lt;tag k="highway" v="service" /&gt;</code>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '21, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jun '21, 17:20</strong> </span></p>
</div>
</div>
<div id="comments-container-80389" class="comments-container">
<span id="80390"></span>
<div id="comment-80390" class="comment">
<div id="post-80390-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I followed your manually replacing method and indeed it worked! Many thanks, Frederik.</p>
</div>
<div id="comment-80390-info" class="comment-info">
<span class="comment-age">(01 Jun '21, 17:48)</span> <span class="comment-user userinfo">PabloFuentesdf</span>
</div>
</div>
</div>
<div id="comment-tools-80389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80389-form-container" class="comment-form-container">
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

