+++
type = "question"
title = "Error on image stream using ojw.dev.openstreetmap.org"
description = '''Hi! I&#x27;m Gabriel, an Argentinian programmer (please excuse my english). I&#x27;m using the service published on http://ojw.dev.openstreetmap.org/ to get maps for an application, on regular time intervals. From some days i&#x27;ve been detecting some errors in my log when loading the image data, on a .NET compo...'''
date = "2013-09-11T18:54:00Z"
lastmod = "2014-12-28T22:15:00Z"
weight = 26293
keywords = [ "map", "image", "stream", "error" ]
aliases = [ "/questions/26293" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error on image stream using ojw.dev.openstreetmap.org](/questions/26293/error-on-image-stream-using-ojwdevopenstreetmaporg)

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
<span id="post-26293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26293-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I'm Gabriel, an Argentinian programmer (please excuse my english).</p>
<p>I'm using the service published on <a href="http://ojw.dev.openstreetmap.org/">http://ojw.dev.openstreetmap.org/</a> to get maps for an application, on regular time intervals. From some days i've been detecting some errors in my log when loading the image data, on a .NET component designed to such end. These errors are related to the info on the downloaded stream (the image). After some hours of debugging, i've noticed that if i call this url:</p>
<p><a href="http://ojw.dev.openstreetmap.org/StaticMap/?lat=-38.033819065207&amp;lon=-57.570014370957&amp;z=15&amp;mlat0=-38.033819065207&amp;mlon0=-57.570014370957&amp;layer=mapnik&amp;w=350&amp;h=250&amp;filter=grey&amp;show=1">http://ojw.dev.openstreetmap.org/StaticMap/?lat=-38.033819065207&amp;lon=-57.570014370957&amp;z=15&amp;mlat0=-38.033819065207&amp;mlon0=-57.570014370957&amp;layer=mapnik&amp;w=350&amp;h=250&amp;filter=grey&amp;show=1</a></p>
<p>... i've got an incorrect response, in terms of image data. If I change the zoom parameter (the z=15 part of the url) from 15 to 16, the service works as expected.</p>
<p>After looking the raw data of the image in an hex editor, i've notice this error at the firsts lines of the stream:</p>
<p>Warning: imagecreatefrompng(): '../../data/tiles/mapnik151114420132.png' is not a valid PNG file in /home/ojw/publichtml/StaticMap/map.php.inc on line 49</p>
<p>If i remove this bytes from the stream, i got a "correct" image data. When open it from a image browser, the image appears correct but with a grey block at the lower right part of it.</p>
<p>What can i do to fix it?</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '13, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/b4ed5f57ec80b4fcb776f39a3a53fc7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kaleb&#39;s gravatar image" />
<p><span>Kaleb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kaleb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26293" class="comments-container">
&#10;</div>
<div id="comment-tools-26293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26293-form-container" class="comment-form-container">
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

<span id="26297"></span>

<div id="answer-container-26297" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26297-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-26297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This (and indeed anything on <code>dev.openstreetmap.org</code>) is not a production service. Our dev machines are predominantly provided to help developers of OSM mapping software, rather than offering APIs to third-party clients. In particular, 'static map APIs' such as this have often caused very high load on the dev machines and have had to be shut down.</p>
<p>I'd recommend instead that you use the <a href="http://open.mapquestapi.com/staticmap/">MapQuest Open Static Maps API</a>. These maps are made from OSM data just the same, but are likely to offer a more reliable service. Make sure to read MapQuest Open's terms of service and any attribution requirements before deploying it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '13, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-26297" class="comments-container">
<span id="39902"></span>
<div id="comment-39902" class="comment">
<div id="post-39902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also take a look at <a href="http://wiki.openstreetmap.org/wiki/Static_map_images">static map images</a> in the wiki for alternative solutions, such as <a href="http://wiki.openstreetmap.org/wiki/Bigmap">Bigmap</a>. And please make sure to read the <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a> first.</p>
</div>
<div id="comment-39902-info" class="comment-info">
<span class="comment-age">(28 Dec '14, 22:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26297" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26297-form-container" class="comment-form-container">
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

