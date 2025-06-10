+++
type = "question"
title = "Open Garmin GPX in JOSM - &quot;Error occurred while parsing ..&quot;"
description = '''Hi all, I am using JOSM 4667 (Dec 2011) and GPX files sourced from a Garmin Nuvi 1440 system logging.  Trying to open some GPX track files I get an error &quot;Error occurred while parsing gpx file .. Only a part of the file will be available&quot;. The files are valid xml and I can use them in GPX editor. If...'''
date = "2012-01-08T02:06:00Z"
lastmod = "2012-01-12T10:15:00Z"
weight = 9842
keywords = [ "garmin", "josm", "gpx", "extensions" ]
aliases = [ "/questions/9842" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Open Garmin GPX in JOSM - "Error occurred while parsing .."](/questions/9842/open-garmin-gpx-in-josm-error-occurred-while-parsing)

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
<span id="post-9842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9842-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am using JOSM 4667 (Dec 2011) and GPX files sourced from a Garmin Nuvi 1440 system logging.<br />
</p>
<p>Trying to open some GPX track files I get an error "Error occurred while parsing gpx file .. Only a part of the file will be available". The files are valid xml and I can use them in GPX editor. If I remove the XML &lt;extensions&gt; .. &lt;/extensions&gt; data which contains some garmin specifc tags (see below), then the file works and loads into JOSM correctly.</p>
<p>Is this normal behaviour from JOSM? I would expect that it just ignores any XML tags that it does not like</p>
<p>How can I effectively work around this? What do others do to load GPX from Garmin and remove these tags before upload to OSM?</p>
<p>Example of one trkpt &lt;?xml version="1.0" encoding="UTF-8" standalone="no"?&gt;&lt;gpx version="1.1" creator="GPX Editor 1.3.56.1423" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemalocation="http://www.topografix.com/GPX/1/1 &amp;lt;a href=" http:="" www.topografix.com="" gpx="" 1="" 1="" gpx.xsd"=""&gt;"&gt;http://www.topografix.com/GPX/1/1/gpx.xsd"&gt;&lt;metadata&gt; &lt;link href="http://www.garmin.com"&gt;&lt;text&gt;Garmin International&lt;/text&gt; &lt;/link&gt;&lt;time&gt;2012-01-03T10:48:54Z&lt;/time&gt; &lt;bounds minlat="-37.638055" minlon="144.080658" maxlat="-37.546773" maxlon="144.260698"/&gt;&lt;/metadata&gt;&lt;trk&gt;&lt;name&gt;ACTIVE LOG: 30 Dec 2011 15:47&lt;/name&gt;</p>
&lt;trkseg&gt;&lt;trkpt lat="-37.630468" lon="144.081058"&gt;&lt;ele&gt;481.76&lt;/ele&gt;&lt;time&gt;2011-12-30T07:24:36Z&lt;/time&gt;&lt;extensions&gt;&lt;gpxtpx:trackpointextension&gt;&lt;gpxtpx:speed&gt;21.96&lt;/gpxtpx:speed&gt;&lt;gpxtpx:course&gt;94.59&lt;/gpxtpx:course&gt;&lt;/gpxtpx:trackpointextension&gt;&lt;/extensions&gt;&lt;/trkpt&gt; Thanks Andy
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-extensions" rel="tag" title="see questions tagged &#39;extensions&#39;">extensions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '12, 02:06</strong></p>
<img src="https://secure.gravatar.com/avatar/167b15c0b88e15fe2c5907f9c699dd9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20F&#39;s gravatar image" />
<p><span>Andy F</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy F has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-9842" class="comments-container">
&#10;</div>
<div id="comment-tools-9842" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9842-form-container" class="comment-form-container">
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

<span id="9843"></span>

<div id="answer-container-9843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9843-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A simple workaround is to use gpsbabel to translate the gpx file into another gpx file and loose all elements that are not in the standard.</p>
<p>The final solution is to submit a bug report at <a href="http://josm.openstreetmap.de/">JOSM</a> attach a sample file and propose a solution. if you know java you can edit the source of JOSM and submit a patch to the bug report. otherwise you have to wait for someone else to do it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '12, 07:14</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-9843" class="comments-container">
<span id="9907"></span>
<div id="comment-9907" class="comment">
<div id="post-9907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - good answer. I guess I was suprised that a native Garmin Nuvi GPX files would not go straight in JOSM, as I cannot be first to work using this combination of tools.</p>
<p>Andy</p>
</div>
<div id="comment-9907-info" class="comment-info">
<span class="comment-age">(12 Jan '12, 02:00)</span> <span class="comment-user userinfo">Andy F</span>
</div>
</div>
<span id="9916"></span>
<div id="comment-9916" class="comment">
<div id="post-9916-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I beleve [this][1] is the problem you are having.</p>
<p>[1]<a href="http://josm.openstreetmap.de/ticket/7247">http://josm.openstreetmap.de/ticket/7247</a></p>
</div>
<div id="comment-9916-info" class="comment-info">
<span class="comment-age">(12 Jan '12, 10:15)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
</div>
<div id="comment-tools-9843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9843-form-container" class="comment-form-container">
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

