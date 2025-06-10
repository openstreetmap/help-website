+++
type = "question"
title = "convert REGCAN95 coordinates to OpenStreetMap coordinates (WGS84-Form in lat/long)"
description = '''I have some coordinates in datum REGCAN95, and I want to know how to convert them to something usable in OpenStreetMap. I have found that REGCAN95 uses the EPSG codes as follows:  4082 REGCAN95 for UTM 27 4083 REGCAN95 for UTM 28  For example I have the coordinate 28BR205306 or 28BR067530, which I w...'''
date = "2016-03-15T19:51:00Z"
lastmod = "2016-03-17T13:10:00Z"
weight = 48683
keywords = [ "wgs84", "transformation", "utm" ]
aliases = [ "/questions/48683" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [convert REGCAN95 coordinates to OpenStreetMap coordinates (WGS84-Form in lat/long)](/questions/48683/convert-regcan95-coordinates-to-openstreetmap-coordinates-wgs84-form-in-latlong)

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
<span id="post-48683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48683-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-48683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some coordinates in datum REGCAN95, and I want to know how to convert them to something usable in OpenStreetMap.</p>
<p>I have found that REGCAN95 uses the EPSG codes as follows:</p>
<ul>
<li>4082 REGCAN95 for UTM 27</li>
<li>4083 REGCAN95 for UTM 28</li>
</ul>
<p>For example I have the coordinate 28BR205306 or 28BR067530, which I want to find in OpenStreetMap or other webmaps. How can I convert them?</p>
<p>PS: I have also asked this on GIS.stackexchange.com and got some comments with hints, <strong>but no answer.</strong> I answered it myself, as I have found a solution via the <a href="https://en.wikipedia.org/wiki/Military_grid_reference_system">Wikipedia page abouth the MGRS reference system</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wgs84" rel="tag" title="see questions tagged &#39;wgs84&#39;">wgs84</span> <span class="post-tag tag-link-transformation" rel="tag" title="see questions tagged &#39;transformation&#39;">transformation</span> <span class="post-tag tag-link-utm" rel="tag" title="see questions tagged &#39;utm&#39;">utm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '16, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '16, 15:31</strong> </span></p>
</div>
</div>
<div id="comments-container-48683" class="comments-container">
<span id="48707"></span>
<div id="comment-48707" class="comment">
<div id="post-48707-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please dont duplicate questions here &amp; on GIS Stack Exchange. Or if you do, say so; and certainly take the trouble to update the query when it's already answered. It's very frustrating to start writing an answer &amp; find the query has already been answered. I like to help, NOT HAVE MY TIME WASTED.</p>
</div>
<div id="comment-48707-info" class="comment-info">
<span class="comment-age">(16 Mar '16, 13:50)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48683-form-container" class="comment-form-container">
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

<span id="48706"></span>

<div id="answer-container-48706" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48706-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Conversion to &amp; from various co-ordinate systems is usually done using the Proj4 library. This projection occurs in proj4 with the following parameters: "+proj=utm +zone=27 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs", which appears to be identical to EPSG:3187 shown <a href="http://spatialreference.org/ref/epsg/3187/">here</a> on Spatial Reference.</p>
<p>This site allows on-line conversions between many reference systems. Otherwise you will have to make use of tools provided by OSGeo.</p>
<p>This question has been asked &amp; answered on <a href="http://gis.stackexchange.com/questions/185122/convert-regcan95-coordinates-to-openstreetmap-coordinates-wgs84-form-in-lat-lon">GIS Stack Exchange</a> also. The OP did not provide this information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '16, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-48706" class="comments-container">
<span id="48710"></span>
<div id="comment-48710" class="comment">
<div id="post-48710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. I like this proj4 tool, because you can convert many coordinates per script at once. Well, theoretically.</p>
<p>I tried it with your command: <code>cs2cs +proj=utm +zone=28 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs &lt;(echo 28RBR205306)</code> <strong>but didn’t get a coordinate.</strong> The result was <code>19d29'18.575"W 0dN 0.000RBR205306</code>. Something must be wrong, but I don’t know what. I tried it both with <code>28BR205306</code> and <code>28RBR205306</code>. Same, false result. :-(</p>
</div>
<div id="comment-48710-info" class="comment-info">
<span class="comment-age">(16 Mar '16, 15:26)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
<span id="48711"></span>
<div id="comment-48711" class="comment">
<div id="post-48711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have searched on spatialreference.org and there seems <strong>no data about <a href="http://spatialreference.org/ref/epsg/?page=38">EPSG:4083</a></strong>.</p>
</div>
<div id="comment-48711-info" class="comment-info">
<span class="comment-age">(16 Mar '16, 15:36)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
<span id="48713"></span>
<div id="comment-48713" class="comment">
<div id="post-48713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To use cs2cs/proj4 to convert the locations, you would first need to translate the MGRS representation to a UTM representation. proj4 doesn't understand the MGRS representation.</p>
</div>
<div id="comment-48713-info" class="comment-info">
<span class="comment-age">(16 Mar '16, 16:10)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="48717"></span>
<div id="comment-48717" class="comment">
<div id="post-48717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5517/erik">@erik</a> Re: EPSG:4082. Yes I'd have told you that but thought I was wasting my time with my answer. However I thought what I had written might be of some use to someone else.</p>
</div>
<div id="comment-48717-info" class="comment-info">
<span class="comment-age">(16 Mar '16, 21:37)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="48718"></span>
<div id="comment-48718" class="comment">
<div id="post-48718-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> Would you mind telling me how to do so? I mean, how to translate MGRS to UTM with cs2cs? Or is that impossible? Maybe another commandline tool?</p>
</div>
<div id="comment-48718-info" class="comment-info">
<span class="comment-age">(17 Mar '16, 00:56)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
<span id="48722"></span>
<div id="comment-48722" class="comment not_top_scorer">
<div id="post-48722-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is no support for MGRS in cs2cs so you would need to use another tool.</p>
</div>
<div id="comment-48722-info" class="comment-info">
<span class="comment-age">(17 Mar '16, 13:10)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-48706" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-48706-form-container" class="comment-form-container">
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

