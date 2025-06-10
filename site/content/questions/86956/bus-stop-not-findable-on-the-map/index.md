+++
type = "question"
title = "Bus Stop not findable on the map"
description = '''There is a bus line and on the bus line I see there is a Bus stop but when searching on the map i don&quot;t find it because the tag bus_stop is missing... And there are A LOT og such bus stops around here. What could be done? https://www.openstreetmap.org/#map=19/46.72443/8.19056 '''
date = "2023-03-21T10:35:00Z"
lastmod = "2023-04-02T16:36:00Z"
weight = 86956
keywords = [ "busstops" ]
aliases = [ "/questions/86956" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bus Stop not findable on the map](/questions/86956/bus-stop-not-findable-on-the-map)

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
<span id="post-86956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86956-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a bus line and on the bus line I see there is a Bus stop but when searching on the map i don"t find it because the tag bus_stop is missing... And there are A LOT og such bus stops around here. What could be done? <a href="https://www.openstreetmap.org/#map=19/46.72443/8.19056">https://www.openstreetmap.org/#map=19/46.72443/8.19056</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '23, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/e75c2867710eacd4aa83145aa2113555?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tschugga&#39;s gravatar image" />
<p><span>Tschugga</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tschugga has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86956" class="comments-container">
&#10;</div>
<div id="comment-tools-86956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86956-form-container" class="comment-form-container">
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

<span id="86957"></span>

<div id="answer-container-86957" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86957-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My guess is because the stops have been mapped as ways, e.g. <a href="https://www.openstreetmap.org/way/319580098">https://www.openstreetmap.org/way/319580098</a>, which I suspect is uncommon for bus stops. They are more visible on this layer: <a href="https://www.openstreetmap.org/#map=19/46.72447/8.19039&amp;layers=T">https://www.openstreetmap.org/#map=19/46.72447/8.19039&amp;layers=T</a></p>
<p>I think often</p>
<pre><code>public_transport=stop_position 
bus=yes</code></pre>
<p>gets translated to a bus stop, but maybe less so for ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Mar '23, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-86957" class="comments-container">
<span id="86958"></span>
<div id="comment-86958" class="comment">
<div id="post-86958-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Moreover, the example given is actually a line rather than an area.</p>
<blockquote>
<p>I suspect is uncommon for bus stops</p>
</blockquote>
<p>It is - as an example, there are no bus stops mapped as lines in Britain or Ireland.</p>
<p>Even the "standard" OSM style can handle bus stops mapped as areas, although users have needed to force them to be treated as areas:</p>
<pre><code>   osm_id   | building | area
------------+----------+------
  397855454 | yes      |
 1106583542 | yes      |
 1044292687 | yes      |
  411672747 | yes      |
  411670814 | yes      |
  882894545 | yes      |
 1109987879 |          | yes
  438154268 | roof     |
  319441627 |          | yes
  413108425 | yes      |
  360798659 | yes      |
(11 rows)</code></pre>
</div>
<div id="comment-86958-info" class="comment-info">
<span class="comment-age">(21 Mar '23, 11:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="86964"></span>
<div id="comment-86964" class="comment">
<div id="post-86964-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, yes most are mapped as lines and therefor are not findable which is a shame since somebody clearly put work in to mapping the lines.</p>
<p>So what ca be done in this case?</p>
</div>
<div id="comment-86964-info" class="comment-info">
<span class="comment-age">(22 Mar '23, 07:37)</span> <span class="comment-user userinfo">Tschugga</span>
</div>
</div>
<span id="86999"></span>
<div id="comment-86999" class="comment">
<div id="post-86999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Changing the mapping from "line" to "area" wouldn't lose any information (actually, it'd be a better representation of what was there). That's one option.</p>
<p>When mapping bus stops myself I only ever map them as nodes.</p>
</div>
<div id="comment-86999-info" class="comment-info">
<span class="comment-age">(29 Mar '23, 01:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86957-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87050"></span>

<div id="answer-container-87050" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87050-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem is mostly about rendering, and I presume most people will be talking about osm-carto, which is the standard layer, i.e. most people who use OSM for the first time will exclusively use this one. The Transport Layer and ÖPNVKarte are normally suited for public transport and will render stops properly.</p>
<p>We are talking about "Alpbach Parkplatz" bus stops here:</p>
<p>On the western side of the road, the bus stop is tagged as a node: <a href="https://www.openstreetmap.org/node/3260069022">https://www.openstreetmap.org/node/3260069022</a></p>
<p>On the eastern side of the road, the bus stop is tagged as a way: <a href="https://www.openstreetmap.org/way/319580110">https://www.openstreetmap.org/way/319580110</a></p>
<p>highway=bus_stop should not be used on a way → highway=platform would be a better choice. Adding a footway to make it routable would be even better.</p>
<p>If rendering on OSM-carto is a concern, you may think about the following course of action:</p>
<ul>
<li>Add a node on the eastern side of the road, roughly where the stop post is supposed to be. Tag it as highway=bus_stop. Add it to the stop_area relation. Add it into every northbound route relation, replacing the platform way. (It is recommended to use JOSM to edit bus route relations, especially to preserve the order of members; it is very difficult to do it correctly with iD).</li>
<li>Add names to bus stop nodes. This might imply a degree of data duplication, which goes against the "One feature"-principle but it seems to be standard practice in your country (e.g. <a href="https://www.openstreetmap.org/relation/4219619">https://www.openstreetmap.org/relation/4219619</a> ).</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '23, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/53ebd409ff25d999fe0cb1c69adfc781?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bxl-forever&#39;s gravatar image" />
<p><span>bxl-forever</span><br />
<span class="score" title="210 reputation points">210</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bxl-forever has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '23, 16:38</strong> </span></p>
</div>
</div>
<div id="comments-container-87050" class="comments-container">
&#10;</div>
<div id="comment-tools-87050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87050-form-container" class="comment-form-container">
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

