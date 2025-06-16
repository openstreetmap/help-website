+++
type = "question"
title = "Is there a good tool to see why a polygon is not rendered?"
description = '''I have a few polygons (forrest) that I made a few years ago. They are rendered on some layers on mapnik. But in many layers they aren&#x27;t. So it is some problems with them. Is there a good tool to see what&#x27;s wrong with these polygons? The polygon is visible on level 8 and level 9 on osm.org (mapnik) b...'''
date = "2011-09-19T12:13:00Z"
lastmod = "2011-09-19T14:25:00Z"
weight = 8010
keywords = [ "rendering", "errors", "tools", "polygon", "mapnik" ]
aliases = [ "/questions/8010" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a good tool to see why a polygon is not rendered?](/questions/8010/is-there-a-good-tool-to-see-why-a-polygon-is-not-rendered)

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
<span id="post-8010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8010-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a few polygons (forrest) that I made a few years ago. They are rendered on some layers on mapnik. But in many layers they aren't. So it is some problems with them. Is there a good tool to see what's wrong with these polygons?</p>
<p>The polygon is visible on level 8 and level 9 on <a href="http://osm.org">osm.org</a> (mapnik) but not on level 10-18.</p>
<p>I discovered that it's visible on all levels with the Osmarender map. So maybe this is a Mapnik problem.</p>
<p>In this case I talk about the forrest on an island: <a href="https://www.openstreetmap.org/?lat=60.38138&amp;lon=17.20959&amp;zoom=15&amp;layers=M">https://www.openstreetmap.org/?lat=60.38138&amp;lon=17.20959&amp;zoom=15&amp;layers=M</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-tools" rel="tag" title="see questions tagged &#39;tools&#39;">tools</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Sep '11, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonas_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Sep '11, 12:52</strong> </span></p>
</div>
</div>
<div id="comments-container-8010" class="comments-container">
&#10;</div>
<div id="comment-tools-8010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8010-form-container" class="comment-form-container">
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

<span id="8018"></span>

<div id="answer-container-8018" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8018-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-8018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jonas_ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://tools.geofabrik.de/osmi/">OSM Inspector</a> and <a href="http://keepright.ipax.at/report_map.php?zoom=14&amp;lat=60.38773&amp;lon=17.23459&amp;layers=B00T&amp;ch=0%2C130&amp;show_ign=1&amp;show_tmpign=1">keep right</a> are both useful tools when checking for errors. These should flag any geometry errors.</p>
<p>In this case neither showed any problems, looking at the tagging I noticed that the island had natural=land and layer=0 both of which were not necessary since the island was part of a multipolygon. Removing the out of date tags has fixed the problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '11, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb4d30bb6d40cf9b3644ff4f453e5bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quantumstate&#39;s gravatar image" />
<p><span>quantumstate</span><br />
<span class="score" title="455 reputation points">455</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quantumstate has 3 accepted answers">30%</span></p>
</div>
</div>
<div id="comments-container-8018" class="comments-container">
&#10;</div>
<div id="comment-tools-8018" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8018-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8011"></span>

<div id="answer-container-8011" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8011-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mapnik have different rendering rules for different zoom levels. This helps to make the map clean and not cluttered. Osmarender does not do this and can therefore be more cluttered.</p>
<p>One example of this is Finland, "land of the thousand lakes", whitch is rendered the standard color in Mapnik but since Osmrender renderes all the lakes even at the low zoom levels it is almost blue in Osmrender.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '11, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8011" class="comments-container">
<span id="8012"></span>
<div id="comment-8012" class="comment">
<div id="post-8012-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, but then it should be the opposite, since level 10-18 contains more details than level 8 and 9 does.</p>
</div>
<div id="comment-8012-info" class="comment-info">
<span class="comment-age">(19 Sep '11, 12:44)</span> <span class="comment-user userinfo">Jonas_</span>
</div>
</div>
</div>
<div id="comment-tools-8011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8011-form-container" class="comment-form-container">
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

