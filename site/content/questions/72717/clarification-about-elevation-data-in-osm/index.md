+++
type = "question"
title = "Clarification about elevation data in OSM"
description = '''Hi There,  I&#x27;ve come across some mixed documentation and wanted to check with the community regarding standards. OSM defines the &quot;ele&quot; tag as elevation above mean sea level. This other OSM wiki page that defines &quot;Altitude&quot; mentions the use of the WGS84 Ellipsoid. Also, the GPX 1.1 Standard uses WGS8...'''
date = "2020-01-27T16:06:00Z"
lastmod = "2020-01-28T15:28:00Z"
weight = 72717
keywords = [ "wgs84", "elevation", "height" ]
aliases = [ "/questions/72717" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Clarification about elevation data in OSM](/questions/72717/clarification-about-elevation-data-in-osm)

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
<span id="post-72717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72717-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi There,</p>
<p>I've come across some mixed documentation and wanted to check with the community regarding standards.</p>
<p>OSM defines the <a href="https://wiki.openstreetmap.org/wiki/Key:ele">"ele"</a> tag as elevation above mean sea level.<br />
<a href="https://wiki.openstreetmap.org/wiki/Altitude">This other OSM wiki page that defines "Altitude"</a> mentions the use of the WGS84 Ellipsoid.<br />
Also, the <a href="http://www.topografix.com/GPX/1/1/gpx.xsd">GPX 1.1 Standard</a> uses WGS84 heights for its "ele" tags.</p>
<p>Based on the above information, are the following assumptions correct?</p>
<ul>
<li>Any "ele" tags in OSM are MSL (mean sea level) heights in meters.</li>
<li>Any "ele" tags in GPX files are WGS84 heights in meters.</li>
<li>GPX files also contain and optional "geoidheight" tag that describes the undulation in meters at that point.</li>
</ul>
<p>I'm trying to sort this out to ensure the height information in the GPX files that I upload are correct.<br />
Also, is the "ele" tag even used much in OSM? do most editors ignore/avoid it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wgs84" rel="tag" title="see questions tagged &#39;wgs84&#39;">wgs84</span> <span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-height" rel="tag" title="see questions tagged &#39;height&#39;">height</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '20, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/85838baa8f5fccb9aa8cd5ed15aca300?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ian%20Colwell&#39;s gravatar image" />
<p><span>Ian Colwell</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ian Colwell has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-72717" class="comments-container">
&#10;</div>
<div id="comment-tools-72717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72717-form-container" class="comment-form-container">
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

<span id="72730"></span>

<div id="answer-container-72730" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72730-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>I use ele only if it's written on site. On a sign or some kind of marker.</p>
<p>GPS altitude is usually most unreliable (to be polite), except if you have dedicated hardware.</p>
<p>And data consumers usually use SRTM or suchlike to have global coverage.</p>
<p>The "Altitude" page you refer to seems deprecated : "there was also a proposal (on this page) to use Key:alt for this purpose. This was never explained properly. Please see ele=*".</p>
<p>Hope this helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '20, 02:00</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span> </br></p>
</div>
</div>
<div id="comments-container-72730" class="comments-container">
<span id="72740"></span>
<div id="comment-72740" class="comment">
<div id="post-72740-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I'll assume my 3 assumptions are correct then.</p>
</div>
<div id="comment-72740-info" class="comment-info">
<span class="comment-age">(28 Jan '20, 15:28)</span> <span class="comment-user userinfo">Ian Colwell</span>
</div>
</div>
</div>
<div id="comment-tools-72730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72730-form-container" class="comment-form-container">
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

