+++
type = "question"
title = "Load israel hiking map to qgis"
description = '''Hi, How can I load The Israel Hiking Map (osm project) To qgis? I did it once but I cant recall how. https://israelhiking.osm.org.il/'''
date = "2016-11-25T09:57:00Z"
lastmod = "2016-11-26T19:33:00Z"
weight = 53110
keywords = [ "qgis" ]
aliases = [ "/questions/53110" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Load israel hiking map to qgis](/questions/53110/load-israel-hiking-map-to-qgis)

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
<span id="post-53110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53110-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>How can I load The Israel Hiking Map (osm project) To qgis? I did it once but I cant recall how.</p>
<p><a href="https://israelhiking.osm.org.il/">https://israelhiking.osm.org.il/</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '16, 09:57</strong></p>
<img src="https://secure.gravatar.com/avatar/e9bb8068391f4abf60d01da116b97f03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nivkeren&#39;s gravatar image" />
<p><span>nivkeren</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nivkeren has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53110" class="comments-container">
&#10;</div>
<div id="comment-tools-53110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53110-form-container" class="comment-form-container">
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

<span id="53121"></span>

<div id="answer-container-53121" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53121-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>More of a QGIS than an OSM question, but I think what you need is something like the <a href="https://github.com/minorua/TileLayerPlugin/blob/master/README.md">tile layer plugin</a>. You can add custom tile layers. You can get the URL you need to add by right clicking a tile on the website you linked, and changing the numbers after /tiles/ with /{z}/{x}/{y}.png</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '16, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '16, 18:20</strong> </span></p>
</div>
</div>
<div id="comments-container-53121" class="comments-container">
<span id="53129"></span>
<div id="comment-53129" class="comment">
<div id="post-53129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>didn't work but thanks</p>
</div>
<div id="comment-53129-info" class="comment-info">
<span class="comment-age">(26 Nov '16, 19:33)</span> <span class="comment-user userinfo">nivkeren</span>
</div>
</div>
</div>
<div id="comment-tools-53121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53121-form-container" class="comment-form-container">
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

