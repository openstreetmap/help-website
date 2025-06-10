+++
type = "question"
title = "How to change the display width of roads in JMapViewer?"
description = '''I am using JMapViewer to load the openstreetmap to display them in a frame. is there anyway to change the road/lane/street width displayed on the map through adjusting some parameter?? or can i custom the style of the openstreetview using java? and how? can anyone offer some links related to these i...'''
date = "2013-05-15T11:42:00Z"
lastmod = "2013-05-15T16:26:00Z"
weight = 22452
keywords = [ "width", "style", "jmapviewer", "road" ]
aliases = [ "/questions/22452" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to change the display width of roads in JMapViewer?](/questions/22452/how-to-change-the-display-width-of-roads-in-jmapviewer)

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
<span id="post-22452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22452-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using <span>JMapViewer</span> to load the openstreetmap to display them in a frame.</p>
<p>is there anyway to change the road/lane/street width displayed on the map through adjusting some parameter??</p>
<p>or can i custom the style of the openstreetview using java? and how?</p>
<p>can anyone offer some links related to these issues??</p>
<p>Thx.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-width" rel="tag" title="see questions tagged &#39;width&#39;">width</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-jmapviewer" rel="tag" title="see questions tagged &#39;jmapviewer&#39;">jmapviewer</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '13, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/438c2b44e9346a170c8303a98a62b539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="godoorsun&#39;s gravatar image" />
<p><span>godoorsun</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="godoorsun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 May '13, 16:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-22452" class="comments-container">
&#10;</div>
<div id="comment-tools-22452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22452-form-container" class="comment-form-container">
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

<span id="22453"></span>

<div id="answer-container-22453" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22453-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JMapViewer loads raster tiles that have been produced by the OpenStreetMap server (or another tile server) according to styling rules configured on that server; the tiles cannot be customised on the client.</p>
<p>You can set up your own tile server (see <a href="http://switch2osm.,org/">switch2osm.org</a> for good howtos), and then you can configure a different map style on your server. There are also commercial offerings for custom-styled tiles (e.g. Cloudmade, Mapbox).</p>
<p>Alternatively, you can change your client from loading and displaying raster tiles to working with vector data; in that case, the styling happens on the client and you can influence that at will. Check out <a href="http://wiki.openstreetmap.org/wiki/Mapsforge">MapsForge</a>, an open source vector rendering library for Java.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '13, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22453" class="comments-container">
<span id="22455"></span>
<div id="comment-22455" class="comment">
<div id="post-22455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks so much. I've tried cloudmade and it works, i can change the width of the road now, but it takes too much time to load tiles. I'll go to try to use the switch2osm and MapsForge now.</p>
</div>
<div id="comment-22455-info" class="comment-info">
<span class="comment-age">(15 May '13, 16:26)</span> <span class="comment-user userinfo">godoorsun</span>
</div>
</div>
</div>
<div id="comment-tools-22453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22453-form-container" class="comment-form-container">
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

