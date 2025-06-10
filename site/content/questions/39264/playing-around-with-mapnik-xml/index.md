+++
type = "question"
title = "playing around with mapnik xml"
description = '''I&#x27;m trying to get OSM-carto to finally include paved/unpaved roads. They are asking for a proposal, rendered with real data. I&#x27;ve got the OSM history renderer already running, which uses this mapnik .xml stylesheet to render data. To avoid having to install a lot more software, I&#x27;d like to play arou...'''
date = "2014-12-13T15:33:00Z"
lastmod = "2014-12-18T11:10:00Z"
weight = 39264
keywords = [ "mapnik" ]
aliases = [ "/questions/39264" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [playing around with mapnik xml](/questions/39264/playing-around-with-mapnik-xml)

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
<span id="post-39264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39264-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get OSM-carto to finally include paved/unpaved roads. <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/110">They are asking for a proposal, rendered with real data</a>.</p>
<p>I've got the OSM history renderer already running, which uses <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/">this mapnik .xml stylesheet</a> to render data. To avoid having to install a lot more software, I'd like to play around with this xml file. But is there any software a I can use to make understanding and editing the xml easier? I tried Quantumnik but <a href="https://github.com/springmeyer/quantumnik/issues/9">couldn't get it installed</a>. In Tilemill it looks complicated to get the real OSM data entered. I can't seem to find a description of the tags used either.</p>
<p>The XML itself looks kind of human readable, so maybe I'm best off just playing around with the code itself...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '14, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-39264" class="comments-container">
<span id="39268"></span>
<div id="comment-39268" class="comment">
<div id="post-39268-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I would highly recommend Andy Allan's cool OSM carto workshop at sotm 2014: <a href="http://blog.gravitystorm.co.uk/2014/07/07/openstreetmap-carto-workshop/">http://blog.gravitystorm.co.uk/2014/07/07/openstreetmap-carto-workshop/</a></p>
<p>Lots of helpful detail to get you started with TileMill and carto style.</p>
</div>
<div id="comment-39268-info" class="comment-info">
<span class="comment-age">(13 Dec '14, 20:25)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-39264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39264-form-container" class="comment-form-container">
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

<span id="39683"></span>

<div id="answer-container-39683" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39683-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-39683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The map style on the openstreetmap.org website is available here <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> in carto format. That's easier to read than the XML file. It uses mapnik in the background. It should be usable with TileMill.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '14, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-39683" class="comments-container">
<span id="39687"></span>
<div id="comment-39687" class="comment">
<div id="post-39687-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>In particular, note that a patch in XML will almost certainly not be accepted. The stylesheet is maintained in CartoCSS.</p>
</div>
<div id="comment-39687-info" class="comment-info">
<span class="comment-age">(18 Dec '14, 11:10)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-39683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39683-form-container" class="comment-form-container">
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

