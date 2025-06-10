+++
type = "question"
title = "which WGS84 datum?"
description = '''HI- a few general quesitons:   all of the information about OSM references WGS84 as the datum, is this meant to be the WGS84(G1150) datum? which is the current realization of WGS84 or some older version?    What happens if a user uploads data into OSM having collected it in another datum, say NAD83 ...'''
date = "2012-01-11T19:42:00Z"
lastmod = "2012-01-20T03:17:00Z"
weight = 9901
keywords = [ "datum", "wgs84" ]
aliases = [ "/questions/9901" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [which WGS84 datum?](/questions/9901/which-wgs84-datum)

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
<span id="post-9901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9901-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>HI- a few general quesitons:</p>
<ol>
<li><p>all of the information about OSM references WGS84 as the datum, is this meant to be the WGS84(G1150) datum? which is the current realization of WGS84 or some older version?<br />
</p></li>
<li><p>What happens if a user uploads data into OSM having collected it in another datum, say NAD83 for example. Does OSM automatically convert that to WGS84?</p></li>
<li><p>Is there any information available about how OSM computes/stores positional information for vectors when multiple users measure the same road or building?<br />
</p></li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-datum" rel="tag" title="see questions tagged &#39;datum&#39;">datum</span> <span class="post-tag tag-link-wgs84" rel="tag" title="see questions tagged &#39;wgs84&#39;">wgs84</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '12, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a9d82fc316a7dceaa56056fdf9a66110?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rockfordz&#39;s gravatar image" />
<p><span>rockfordz</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rockfordz has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-9901" class="comments-container">
&#10;</div>
<div id="comment-tools-9901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9901-form-container" class="comment-form-container">
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

<span id="9904"></span>

<div id="answer-container-9904" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9904-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-9904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>If you like. The different versions are not that different. Normally you lose more precision in the quantification of the coordinates then by using the wrong version of the datum. (And way more by using inaccurate measuring devices like a GPS.)</li>
<li>The API does not have an option of specifying a datum and any coordinates will be interpreted as WGS84. If a user uploads in the wrong datum it will not be converted. This is normally not a problem since any format the API supports (GPX, OSM) uses WGS84 and the error will therefore be in the converters.</li>
<li>The database stores GPX traces separately from vector data and all conversion between them is done by hand. The traces are a guide to the user when entering vector data and there are no automatic computation of vector data from the traces.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '12, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jan '12, 03:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f075add936ab95d2d368f2e48f5ddc22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ebenezer&#39;s gravatar image" />
<p><span>Ebenezer</span><br />
<span class="score" title="948 reputation points">948</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span></p>
</div>
</div>
<div id="comments-container-9904" class="comments-container">
&#10;</div>
<div id="comment-tools-9904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9904-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9929"></span>

<div id="answer-container-9929" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9929-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-9929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please anyone feel free to correct me if I am wrong, but this is my understanding.</p>
<p>The WGS-84 datum is supposed to be centred at the earth's centre of mass and aligned with its axis of rotation. Satellite-based systems can determine those parameters to an accuracy of millimetres. It is also necessary to define, arbitrarily, the location of 0° of longitude (the Greenwich meridian). Since WGS-84 was defined (in 1984), the thing that has most affected its accuracy is tectonic plate movement (continental drift), which has altered the position of some major land masses by a significant fraction of a metre. That has resulted in several derived datums being specified, tied to significant land masses (North America, Europe, etc.). The re-specification of WGS-84 itself has, I think, resulted in changes of only fractions of a millimetre.</p>
<p>A good hand-held GPS receiver, operating under ideal conditions, can fix its position to within one or two metres. Under trees or near tall buildings, they are nowhere near that good. I have not heard of anyone using anything more accurate to add data to OSM, so it would appear that the consequences of the movement of the land relative to WGS-84 (away from major earthquakes) are about one order of magnitude smaller than the accuracy that can be expected from most OSM data, and the consequences of the re-specification of the WGS-84 datum are trivial. That is to say, we don't need to worry just yet.</p>
<p>As far as I know, positions in GPX files are always referred to WGS-84, and any device that writes a GPX file should convert locations to that datum, even if the device holds the information internally in some other form.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '12, 22:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-9929" class="comments-container">
<span id="9939"></span>
<div id="comment-9939" class="comment">
<div id="post-9939-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The horizontal difference between WGS84(transit or original) and WGS84(G1150) is 1.6 meters on the east coast of the US, computed using HTDP from the National Geodetic Survey. So, when using coordinate data from OSM it would be helpful to know exactly what datum the data is tied to so this bias could be accounted for.</p>
</div>
<div id="comment-9939-info" class="comment-info">
<span class="comment-age">(13 Jan '12, 15:21)</span> <span class="comment-user userinfo">rockfordz</span>
</div>
</div>
<span id="10049"></span>
<div id="comment-10049" class="comment">
<div id="post-10049-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I suppose the pragmatic answer is that OSM uses whatever datum the GPS currently uses, as I suspect that few contributors have access to a more accurate source of information. I don't really have the knowlege to take this discussion much further, but I would be grateful if anyone could tell me whether G1150 is a re-specification of the WGS84 datum itself or of a reference frame derived from it.</p>
</div>
<div id="comment-10049-info" class="comment-info">
<span class="comment-age">(18 Jan '12, 20:14)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="10082"></span>
<div id="comment-10082" class="comment">
<div id="post-10082-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See <a href="http://www.sxbluegps.com/world-about-datum.html">http://www.sxbluegps.com/world-about-datum.html</a> - GPS currently uses WGS84(G1150), so a GPS receiver with no differential correction will use WGS84(G1150). This version of WGS84 is the latest, and started in 2002, so I think it is fair to say that OSM probably uses it. :)</p>
</div>
<div id="comment-10082-info" class="comment-info">
<span class="comment-age">(20 Jan '12, 03:17)</span> <span class="comment-user userinfo">Ebenezer</span>
</div>
</div>
</div>
<div id="comment-tools-9929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9929-form-container" class="comment-form-container">
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

