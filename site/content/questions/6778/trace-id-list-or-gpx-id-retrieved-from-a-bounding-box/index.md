+++
type = "question"
title = "Trace id list or (gpx id) retrieved from a bounding box"
description = '''I&#x27;d like the same thing than what&#x27;s here (more a less) : http://wiki.openstreetmap.org/wiki/API_v0.6#GPS_Traces 1/ but in XAPI I don&#x27;t want to log in just for retrieving gps traces. 2/ and I just need the IDs Here what I have from your exemple with api v0.6  &amp;lt;trk&amp;gt;  &amp;lt;name&amp;gt;20110625.gpx&amp;lt;...'''
date = "2011-08-02T13:49:00Z"
lastmod = "2011-08-02T18:47:00Z"
weight = 6778
keywords = [ "traces", "api", "gpx", "xapi" ]
aliases = [ "/questions/6778" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trace id list or (gpx id) retrieved from a bounding box](/questions/6778/trace-id-list-or-gpx-id-retrieved-from-a-bounding-box)

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
<span id="post-6778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6778-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like the same thing than what's here (more a less) : <a href="http://wiki.openstreetmap.org/wiki/API_v0.6#GPS_Traces">http://wiki.openstreetmap.org/wiki/API_v0.6#GPS_Traces</a></p>
<p>1/ but in XAPI I don't want to log in just for retrieving gps traces.</p>
<p>2/ and I just need the IDs Here what I have from your exemple with api v0.6<br />
&lt;trk&gt;<br />
&lt;name&gt;20110625.gpx&lt;/name&gt;<br />
&lt;desc&gt; support ride&lt;/desc&gt;<br />
&lt;url&gt;<a href="http://api.openstreetmap.org/trace/1040543/view%3C/url%3E">api.openstreetmap.org/trace/1040543/view&lt;/url&gt;</a><br />
<br />
&lt;trkpt lat="51.631283" lon="3.3e-05"&gt;<br />
&lt;time&gt;2011-06-25T08:57:54Z&lt;/time&gt;<br />
&lt;/trkpt&gt;<br />
<br />
&lt;trkpt lat="51.631257" lon="9.6e-05"&gt;<br />
&lt;time&gt;2011-06-25T08:57:55Z&lt;/time&gt;<br />
&lt;/trkpt&gt;<br />
<br />
...<br />
...<br />
&lt;/trk&gt;<br />
</p>
<p>here is what I wish (more or less) ... I fact I don't need to overload your server with long resquest when I just need the ID.<br />
&lt;trk&gt;<br />
&lt;name&gt;20110625.gpx&lt;/name&gt;<br />
&lt;desc&gt; support ride&lt;/desc&gt;<br />
&lt;url&gt;<a href="http://api.openstreetmap.org/trace/">api.openstreetmap.org/trace/</a><strong>1040543</strong>/view&lt;/url&gt;<br />
&lt;/trk&gt;<br />
</p>
<p>or even better<br />
&lt;trk&gt;<br />
&lt;name&gt;20110625.gpx&lt;/name&gt;<br />
&lt;desc&gt; support ride&lt;/desc&gt;<br />
&lt;url&gt;<a href="http://api.openstreetmap.org/trace/1040543/view%3C/url%3E">api.openstreetmap.org/trace/1040543/view&lt;/url&gt;</a><br />
<strong>&lt;id&gt;1040543&lt;/id&gt;</strong><br />
&lt;/trk&gt;<br />
</p>
<p>Why ? because I am developing a small tool for android named "Osm Mapper Helper", and I'd like to spot roads, streets already having good traces (not too old, with small point interval ). I'd like to filter traces younger than 12months, 18months, 24months.... why ? (again) because where I live (for the moment) every thing's changing quickly. Most of the atlas you buy are wrong !!! With an Id list, I can easily detect what's already available and what's new a bounding box.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '11, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0348ab36fbb79434173c38691b3fe41a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fabyen&#39;s gravatar image" />
<p><span>Fabyen</span><br />
<span class="score" title="216 reputation points">216</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fabyen has 2 accepted answers">100%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '11, 16:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span></br></p>
</div>
</div>
<div id="comments-container-6778" class="comments-container">
&#10;</div>
<div id="comment-tools-6778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6778-form-container" class="comment-form-container">
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

<span id="6803"></span>

<div id="answer-container-6803" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6803-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Neither <a href="http://wiki.openstreetmap.org/wiki/XAPI">XAPI</a> nor the new <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> seem to support GPS traces. Hence you have to get them through the OSM API.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '11, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-6803" class="comments-container">
&#10;</div>
<div id="comment-tools-6803" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6803-form-container" class="comment-form-container">
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

