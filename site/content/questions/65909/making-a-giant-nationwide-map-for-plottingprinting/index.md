+++
type = "question"
title = "Making a giant nationwide map for plotting/printing"
description = '''I&#x27;d like to produce a A1 or A0 map of Great Britain or the British Isles (or maybe just England and Wales) with a very simple presentation for most OSM data, but with all the waymarked hiking pathsin detail and maybe bike routes, waterways and a good selection of town names. I&#x27;ve done lots of medium...'''
date = "2018-09-15T18:22:00Z"
lastmod = "2018-10-16T22:58:00Z"
weight = 65909
keywords = [ "waymarked", "a0", "printing", "a1", "hiking" ]
aliases = [ "/questions/65909" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Making a giant nationwide map for plotting/printing](/questions/65909/making-a-giant-nationwide-map-for-plottingprinting)

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
<span id="post-65909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65909-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to produce a A1 or A0 map of Great Britain or the British Isles (or maybe just England and Wales) with a very simple presentation for most OSM data, but with all the waymarked hiking pathsin detail and maybe bike routes, waterways and a good selection of town names.</p>
<p>I've done lots of medium/long distance walks, and I'd like to print off the map and highlight (with a highlighter pen) the walks I've done.</p>
<p>None of the on-line map-making tools I've found will produce something at that size, and none will show the waymarked trails.</p>
<p>I'm reasonably comfortable with building software from packages on Linux, but there are so many packages and tools out there (some of which seem like abandonware) that I don't know where to start. Having a Mapnik install might not do the trick - because it would produce millions of tiny .png files. Perhaps there is a away to produce something in vector mode that could be converted to a PDF.</p>
<p>Are there off-the-shelf map styles that sort-of do what I'm looking for?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-waymarked" rel="tag" title="see questions tagged &#39;waymarked&#39;">waymarked</span> <span class="post-tag tag-link-a0" rel="tag" title="see questions tagged &#39;a0&#39;">a0</span> <span class="post-tag tag-link-printing" rel="tag" title="see questions tagged &#39;printing&#39;">printing</span> <span class="post-tag tag-link-a1" rel="tag" title="see questions tagged &#39;a1&#39;">a1</span> <span class="post-tag tag-link-hiking" rel="tag" title="see questions tagged &#39;hiking&#39;">hiking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '18, 18:22</strong></p>
<img src="https://secure.gravatar.com/avatar/b5c5070032df7883181003f187eacae0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spiregrain&#39;s gravatar image" />
<p><span>spiregrain</span><br />
<span class="score" title="183 reputation points">183</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spiregrain has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65909" class="comments-container">
<span id="65925"></span>
<div id="comment-65925" class="comment">
<div id="post-65925-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In case you missed it: <a href="https://wiki.openstreetmap.org/wiki/OSM_on_Paper">https://wiki.openstreetmap.org/wiki/OSM_on_Paper</a></p>
</div>
<div id="comment-65925-info" class="comment-info">
<span class="comment-age">(16 Sep '18, 21:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65909-form-container" class="comment-form-container">
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

<span id="65912"></span>

<div id="answer-container-65912" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65912-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-65912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This should be fairly easy to do using the relevant OSM vector data and QGIS.</p>
<p>At a minimum you need an extract of all route=hiking (perhaps with additional filters), and either a suitable tile layer as background or (more complex) build your own background using OSM vector data.</p>
<p>For an A4 size print with Orkney &amp; Shetland in cartouches I use a scale of 1:2.4M in OSGB projection (EPSG:27700). This would be 1:1.2M for A2 and 1:600k for A0 (if my maths is right). The latter is approximately the same as various synoptic OS maps usually billed as 10 miles to the inch. Using OSGB means that you may need your own background as names in Google projection are much less readable when raster tiles are re-projected. OS OpenData products may be an easier way to achieve a decent background rather than using OSM. In my experience I often start with OS OpenData and then move some features over to OSM because of things like having more attributes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '18, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-65912" class="comments-container">
<span id="66363"></span>
<div id="comment-66363" class="comment">
<div id="post-66363-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for this; I've finally got it working. It'll take a bit of tinkering until I'm totally happy to get it printed, but everything is working.</p>
</div>
<div id="comment-66363-info" class="comment-info">
<span class="comment-age">(16 Oct '18, 22:58)</span> <span class="comment-user userinfo">spiregrain</span>
</div>
</div>
</div>
<div id="comment-tools-65912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65912-form-container" class="comment-form-container">
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

