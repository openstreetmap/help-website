+++
type = "question"
title = "I need this way to be a closed polygon but it&#x27;s downloading as an outline"
description = '''This man_made: pier should be a closed polygon but I can&#x27;t figure out where the error is. If I use QuickOSM plugin in QGIS, it downloads as an outline.  https://www.openstreetmap.org/way/406477559#map=18/57.05036/-135.32801 Edit: my main problem is that it&#x27;s rendering as an outline in Mapbox. I reac...'''
date = "2020-10-26T23:36:00Z"
lastmod = "2020-10-28T21:19:00Z"
weight = 77258
keywords = [ "qgis", "quickosm", "pier", "bounding-polygon" ]
aliases = [ "/questions/77258" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [I need this way to be a closed polygon but it's downloading as an outline](/questions/77258/i-need-this-way-to-be-a-closed-polygon-but-its-downloading-as-an-outline)

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
<span id="post-77258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77258-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This <code>man_made: pier</code> should be a closed polygon but I can't figure out where the error is. If I use QuickOSM plugin in QGIS, it downloads as an outline.</p>
<p><a href="https://www.openstreetmap.org/way/406477559#map=18/57.05036/-135.32801">https://www.openstreetmap.org/way/406477559#map=18/57.05036/-135.32801</a></p>
<p>Edit: my main problem is that it's rendering as an outline in Mapbox. I reached out to them and they said it's probably not closed in OSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-quickosm" rel="tag" title="see questions tagged &#39;quickosm&#39;">quickosm</span> <span class="post-tag tag-link-pier" rel="tag" title="see questions tagged &#39;pier&#39;">pier</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '20, 23:36</strong></p>
<img src="https://secure.gravatar.com/avatar/efa2bd232d1bfd0540fe303e6cba5f64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jfact0ry&#39;s gravatar image" />
<p><span>Jfact0ry</span><br />
<span class="score" title="366 reputation points">366</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jfact0ry has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '20, 08:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-77258" class="comments-container">
&#10;</div>
<div id="comment-tools-77258" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77258-form-container" class="comment-form-container">
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

<span id="77261"></span>

<div id="answer-container-77261" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77261-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jfact0ry has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>QuickOSM is using GDAL/OGR to convert the OSM data into geometries. From somewhere it is reading an osmconf.ini:</p>
<p><a href="https://github.com/OSGeo/gdal/blob/master/gdal/data/osmconf.ini">https://github.com/OSGeo/gdal/blob/master/gdal/data/osmconf.ini</a></p>
<p>On <a href="https://github.com/OSGeo/gdal/blob/36ebdf2e4834dba7d1b466ddf86c3625f672ba99/gdal/data/osmconf.ini#L7">line 7</a> there is a list of tags that will cause a closed OSM object to be treated as a polygon. Neither <code>man_made</code> or <code>man_made=pier</code> is on it.</p>
<p>There should be some way to feed QuickOSM a customized version of osmconf.ini.</p>
<p>I looked at the object in JOSM, it's currently a closed way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '20, 02:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-77261" class="comments-container">
<span id="77265"></span>
<div id="comment-77265" class="comment">
<div id="post-77265-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are piers not ambiguous enough to require <code>area=yes</code>?</p>
</div>
<div id="comment-77265-info" class="comment-info">
<span class="comment-age">(27 Oct '20, 08:33)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-77261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77261-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77264"></span>

<div id="answer-container-77264" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77264-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tag <code>man_made=pier</code> is somewhat special. Most tags clearly either signify that a way is to be interpreted as a line (<code>highway</code>) or as a polygon (<code>landuse</code>). You can use the <code>area=yes/no</code> tag to overwrite this, but there is a clear either/or decision here. But <code>man_made=pier</code> is different, it is to be understood as a polygon if it is a closed way and as a line if it is not closed. There is probably software out there that can't handle this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '20, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-77264" class="comments-container">
<span id="77295"></span>
<div id="comment-77295" class="comment">
<div id="post-77295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The OSM wiki doesn't really clarify how a closed way is to be treated when it comes to man_made=pier. Based on my own data usage, I get the sense that many systems treat a closed way as a loop of pier, not an area. I always add area=yes if a closed way pier is an area.</p>
</div>
<div id="comment-77295-info" class="comment-info">
<span class="comment-age">(28 Oct '20, 21:19)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-77264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77264-form-container" class="comment-form-container">
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

