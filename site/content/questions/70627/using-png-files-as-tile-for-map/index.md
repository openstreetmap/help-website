+++
type = "question"
title = "Using PNG files as tile for map"
description = '''I created a tile server (with this tutorial). Everything works great, but now I want to use only PNG files to show map on server which I generated with generate_tiles.py. The problem is that I have to create server at Windows and I would like to have only PNG files of map on server and use OpenLayer...'''
date = "2019-09-05T09:22:00Z"
lastmod = "2019-09-05T09:35:00Z"
weight = 70627
keywords = [ "windows", "generate_tiles", "tiles", "openlayers", "png" ]
aliases = [ "/questions/70627" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using PNG files as tile for map](/questions/70627/using-png-files-as-tile-for-map)

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
<span id="post-70627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70627-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I created a tile server (with this <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">tutorial</a>). Everything works great, but now I want to use only PNG files to show map on server which I generated with <a href="https://github.com/openstreetmap/mapnik-stylesheets/blob/master/generate_tiles.py">generate_tiles.py</a>.</p>
<p>The problem is that I have to create server at Windows and I would like to have only PNG files of map on server and use OpenLayers to show them. And my main question is how to do that and is it possible?</p>
<p>I am beginner at this and detailed description would be awesome. If you think that I misunderstood anything, please correct me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-png" rel="tag" title="see questions tagged &#39;png&#39;">png</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '19, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a0669c8940488f844fb4c72e9a87d36a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LukashArts&#39;s gravatar image" />
<p><span>LukashArts</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LukashArts has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70627" class="comments-container">
&#10;</div>
<div id="comment-tools-70627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70627-form-container" class="comment-form-container">
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

<span id="70630"></span>

<div id="answer-container-70630" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70630-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LukashArts has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>generate PNG tiles with generate_tiles.py</li>
<li>install simple web server on Windows (can be IIS, Apache, anything)</li>
<li>copy PNG files from Linux box into the web server's root directory on Windows</li>
<li>done!</li>
</ol>
<p>However, note that there are limits to this procedure if you want a large area and high detail - for example, if you wanted to do this for all of Germany you'd have to compute 80 million tiles of a total size of about 300 GB (or even more if the file system used on Windows has a large cluster size - see also <a href="https://blog.geofabrik.de/?p=268).">https://blog.geofabrik.de/?p=268).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '19, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70630" class="comments-container">
<span id="70631"></span>
<div id="comment-70631" class="comment">
<div id="post-70631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is that simple? I'll try it out then. I generated tiles for Croatia from zoom 0 - 15 (~500MB), so that should be enough for first testing. Thank you!</p>
</div>
<div id="comment-70631-info" class="comment-info">
<span class="comment-age">(05 Sep '19, 09:35)</span> <span class="comment-user userinfo">LukashArts</span>
</div>
</div>
</div>
<div id="comment-tools-70630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70630-form-container" class="comment-form-container">
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

