+++
type = "question"
title = "How to map a small area from a precise survey"
description = '''I want to map the objects in a small pedestrian area (say, 20x20 meters). I have a pretty precise survey done on paper, down to centimeters. JOSM has a bar at the bottom which displays useful info when drawing polygons - angle to the last segment, current segment length... but the segment length&#x27;s p...'''
date = "2015-09-28T03:29:00Z"
lastmod = "2015-09-28T23:17:00Z"
weight = 45624
keywords = [ "josm", "survey", "mapping" ]
aliases = [ "/questions/45624" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to map a small area from a precise survey](/questions/45624/how-to-map-a-small-area-from-a-precise-survey)

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
<span id="post-45624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45624-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to map the objects in a small pedestrian area (say, 20x20 meters). I have a pretty precise survey done on paper, down to centimeters.</p>
<p>JOSM has a bar at the bottom which displays useful info when drawing polygons - angle to the last segment, current segment length... but the segment length's precision is only displayed in decimeters (e.g. it shows "5.6 meters" with a single digit after the decimal point). I'd like one more digit of precision to get centimeters. This would make my mapping quite simple.</p>
<p>Is there a way to change that in JOSM, or another tool I can use to map this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-survey" rel="tag" title="see questions tagged &#39;survey&#39;">survey</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '15, 03:29</strong></p>
<img src="https://secure.gravatar.com/avatar/e81394b007264247f2acb0e57e596301?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Federico%20Mena%20Quintero&#39;s gravatar image" />
<p><span>Federico Men...</span><br />
<span class="score" title="471 reputation points">471</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Federico Mena Quintero has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45624" class="comments-container">
&#10;</div>
<div id="comment-tools-45624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45624-form-container" class="comment-form-container">
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

<span id="45633"></span>

<div id="answer-container-45633" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45633-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-45633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Federico Mena Quintero has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use JOSM's measurement plugin, or hack JOSM source to let you zoom closer. But there wouldn't be much point to it:</p>
<ul>
<li>The OSM database stores coordinates in <a href="https://wiki.openstreetmap.org/wiki/Rails_port/Database_schema">a format that has a 1.7cm granularity</a> depending on where you are on earth (longitude granularity does get finer near the poles). So you can't store anything more precise in OSM.</li>
<li>Plate tectonics cause movements of <a href="https://en.wikipedia.org/wiki/File:Global_plate_motion_2008-04-17.jpg">more than 1cm/year in most places of the world</a>, so while you can map something with cm accuracy relative to itself, the absolute position (which is what OSM stores) would need to be updated every year.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '15, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-45633" class="comments-container">
<span id="45639"></span>
<div id="comment-45639" class="comment">
<div id="post-45639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll try the measurement plugin :)</p>
<p>I'm fine with 1.7 cm granularity. I'm pretty sure my little area lies completely within a tectonic plate; if it cracks in two during an earthquake, I'll have bigger problems.</p>
</div>
<div id="comment-45639-info" class="comment-info">
<span class="comment-age">(28 Sep '15, 17:43)</span> <span class="comment-user userinfo">Federico Men...</span>
</div>
</div>
<span id="45649"></span>
<div id="comment-45649" class="comment">
<div id="post-45649-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederico, you’re able to get any length by zooming and some arithmetic + - up to 0.04 m using JOSM, suitable for a building with the aid of the original building drawings or a survey locally. Since the measurement at 0.04 m is divided into 4 sections you got 0.01 m. The mode of your GPS is much lower for instance between 2.00 and 10.00 m, so don’t use the trick for open spaces like you’ve mentioned, as Vincent mentioned the accuracy of OSM is not that good.</p>
</div>
<div id="comment-45649-info" class="comment-info">
<span class="comment-age">(28 Sep '15, 23:17)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-45633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45633-form-container" class="comment-form-container">
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

