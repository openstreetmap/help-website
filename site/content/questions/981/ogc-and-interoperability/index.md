+++
type = "question"
title = "OGC and interoperability"
description = '''I understand that OSM holds geospatial information. Browsing through the documentation (e.g. the API) I found no reference to terms and concepts from the OGC. Is the conclusion correct that OSM can never act as a OGC compliant service provider? If so, why?'''
date = "2010-10-01T16:23:00Z"
lastmod = "2010-10-01T19:43:00Z"
weight = 981
keywords = [ "interoperabilty", "ogc", "standards" ]
aliases = [ "/questions/981" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OGC and interoperability](/questions/981/ogc-and-interoperability)

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
<span id="post-981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-981-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I understand that OSM holds geospatial information. Browsing through the documentation (e.g. the API) I found no reference to terms and concepts from the OGC.<br />
Is the conclusion correct that OSM can never act as a OGC compliant service provider? If so, why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-interoperabilty" rel="tag" title="see questions tagged &#39;interoperabilty&#39;">interoperabilty</span> <span class="post-tag tag-link-ogc" rel="tag" title="see questions tagged &#39;ogc&#39;">ogc</span> <span class="post-tag tag-link-standards" rel="tag" title="see questions tagged &#39;standards&#39;">standards</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '10, 16:23</strong></p>
<img src="https://secure.gravatar.com/avatar/000bf25a2e14bb74dfef9e465e9e3002?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qw%C3%A4rtz&#39;s gravatar image" />
<p><span>qwärtz</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qwärtz has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Oct '10, 18:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-981" class="comments-container">
&#10;</div>
<div id="comment-tools-981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-981-form-container" class="comment-form-container">
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

<span id="990"></span>

<div id="answer-container-990" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-990-score" class="post-score" title="current number of votes">
11
</div>
<span id="post-990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unlike the business world, OSM does not view standards compliance as a goal in itself; i.e. if we are to use a standard, it must have clear an direct benefits for the project - otherwise nobody will code it or assign resources to it. While this does not apply to each and every OGC standard, on the whole they range from "cumbersome" to "useless" for OSM and thus are disregarded.</p>
<p>It is unlikely that the OSM server infrastructure itself should become "OCG compliant" in any way in the near future because the above mentioned benefits are unlikely to outweigh the cost in terms of implementation work and server load.</p>
<p>This does not, however, mean that you cannot use OSM in an OGC-compliant world - it just means that OSM is not going to provide OGC compliance for you on a silver platter. You can, for example, access several third-party WMS servers (see <a href="http://wiki.openstreetmap.org/wiki/WMS">Wiki</a>) serving OSM data, or you can install software to convert osm to shape files and vice versa. There's also an ogr2osm utility. The <a href="http://openrouteservice.org"></a><a href="http://openrouteservice.org"></a><a href="http://openrouteservice.org">openrouteservice.org</a> web site offers OpenLS-based geocoding and routing, and many more.</p>
<p>All these have in common that you either have to write/install software yourself, or use a - sometimes paid-for - service provided by a third party. If, for example, you wanted a WFS server serving OpenStreetMap data, you could import OSM data into a PostGIS database (see <a href="http://wiki.openstreetmap.org/wiki/osm2pgsql">Wiki</a>) and run an UMN map server off it, and so on. You are right in that the project doesn't provide that and is unlikely to do so any time soon, but any third party can do with our data what they want, including setting up OGC compliant services. (However, OSM has a very good history of accepting contributions of all kind - so if you think you can add OGC services to the OSM core infrastructure without any ill effects then step forward on the <a href="http://lists.openstreetmap.org/listinfo/dev">developers list</a> and start coding!)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '10, 19:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Oct '10, 09:42</strong> </span></p>
</div>
</div>
<div id="comments-container-990" class="comments-container">
&#10;</div>
<div id="comment-tools-990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-990-form-container" class="comment-form-container">
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

