+++
type = "question"
title = "Layered Map renderer"
description = '''Hi, I am creating a Scenario for Open Transport Tycoon Deluxe which requires me to plot towns on a plain heightmap. The problem is is that on maps such as https://opentopomap.org and opencyclemap.org the town maps overlay the topology meaning that if a town is over certain geological features, those...'''
date = "2018-11-30T14:36:00Z"
lastmod = "2018-12-04T08:53:00Z"
weight = 67009
keywords = [ "layers", "renderer", "transparency" ]
aliases = [ "/questions/67009" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Layered Map renderer](/questions/67009/layered-map-renderer)

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
<span id="post-67009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67009-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am creating a Scenario for Open Transport Tycoon Deluxe which requires me to plot towns on a plain heightmap.</p>
<p>The problem is is that on maps such as <a href="https://opentopomap.org">https://opentopomap.org</a> and opencyclemap.org the town maps overlay the topology meaning that if a town is over certain geological features, those features are now hidden so I need to use features that surround the town in order to accurately plot it.</p>
<p>Is there something that would allow me to alter a certain layer's transparency in order to create the scenario as accurately as possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span> <span class="post-tag tag-link-transparency" rel="tag" title="see questions tagged &#39;transparency&#39;">transparency</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '18, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/e686473c1736c7bcbf5fdf9db6c7aec8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BenDragon81037&#39;s gravatar image" />
<p><span>BenDragon81037</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BenDragon81037 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67009" class="comments-container">
&#10;</div>
<div id="comment-tools-67009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67009-form-container" class="comment-form-container">
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

<span id="67013"></span>

<div id="answer-container-67013" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67013-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This sounds as if you are doing things the wrong way around.</p>
<p>You likely need to start with a DEM (digital elevation model) and then add whatever further info you need from OSM. Trying to extract the information out of one of the exiting map rendering would seemt to be fraught with issues.</p>
<p>For more information see for example <a href="https://wiki.openstreetmap.org/wiki/SRTM">https://wiki.openstreetmap.org/wiki/SRTM</a> and <a href="https://opendem.info/">https://opendem.info/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '18, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-67013" class="comments-container">
<span id="67017"></span>
<div id="comment-67017" class="comment">
<div id="post-67017-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's true that I have come extremely close to using DEMs, but that path also has its own set of issues; as I have never worked with them, and there seems to be nothing out there which is mainstream enough to support the native file types.</p>
<p>As for the image files which I can use with GIMP or paint.net, there's still the OSM data to obtain and extract it over the terrain via some program (Sure, direct greyscale DEM maps are nice, but it's not exactly clear to work with pixels which are nearly identical in shade).</p>
<p>I used the previous method due to its simplicity, but it's simply not good enough.</p>
</div>
<div id="comment-67017-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 20:11)</span> <span class="comment-user userinfo">BenDragon81037</span>
</div>
</div>
<span id="67058"></span>
<div id="comment-67058" class="comment">
<div id="post-67058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OSM doesn't have height information except for certain objects such as peaks. However for your scenario you will need an elevation profile. OpenTopoMap and OpenCycleMap <em>do</em> use a DEM which doesn't come from OSM but from a third-party source. OSM data is just rendered on top of it. You will have to do something similar.</p>
</div>
<div id="comment-67058-info" class="comment-info">
<span class="comment-age">(04 Dec '18, 08:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67013" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67013-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67053"></span>

<div id="answer-container-67053" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67053-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds like you want a way to get raster images or a pdf with just terrain contours for a certain town, and then another image that has the streets and buildings, without having to build your own tile server?</p>
<p>It may work to use "MyOSMatic" at <a href="https://print.get-map.org">https://print.get-map.org</a></p>
<p>This site will allow you to make png or pdf files from a certain area in a number of different styles. Contour lines are available as a separate overlay, so you can select "empty baseman for overlay testing" as the stylesheet, and then "contour lines at 10m resolution" as an overlay, to get a map with just the contour lines for a certain area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '18, 00:29</strong></p>
<img src="https://secure.gravatar.com/avatar/984eadc21cb77cb316db4ff21c94b869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joseph%20E&#39;s gravatar image" />
<p><span>Joseph E</span><br />
<span class="score" title="390 reputation points">390</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joseph E has 2 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-67053" class="comments-container">
&#10;</div>
<div id="comment-tools-67053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67053-form-container" class="comment-form-container">
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

