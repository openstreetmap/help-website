+++
type = "question"
title = "［Building Lane Model for OSM］How can I get multiple gpx from osm for repeated roads?"
description = '''Hi all: I&#x27;m thinking to build the lane model for OSM using machine learning techniques. How can I get multiple gpx files from osm database for certain roads? Thanks in advance for any advice or feedback. Best D. Below are my half-baked ideas: 1) Motivation: a) According to Sebastian Thrun, in order ...'''
date = "2011-11-17T16:47:00Z"
lastmod = "2011-11-18T11:23:00Z"
weight = 9085
keywords = [ "multiple", "lane", "gpx" ]
aliases = [ "/questions/9085" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [［Building Lane Model for OSM］How can I get multiple gpx from osm for repeated roads?](/questions/9085/building-lane-model-for-osmhow-can-i-get-multiple-gpx-from-osm-for-repeated-roads)

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
<span id="post-9085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9085-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all:</p>
<p>I'm thinking to build the lane model for OSM using machine learning techniques. How can I get multiple gpx files from osm database for certain roads?</p>
<p>Thanks in advance for any advice or feedback. Best D.</p>
<p>Below are my half-baked ideas:</p>
<p>1) Motivation:</p>
<p>a) According to Sebastian Thrun, in order to build the autonomous driving car, they push google map to 15cm accuracy with lane models !!! (I guess they do it in an expensive way, maybe only for part of CA to test their car) <a href="http://www.youtube.com/watch?v=bp9KBrH8H04">http://www.youtube.com/watch?v=bp9KBrH8H04</a></p>
<p>b) Also, several OSM members have already proposed the lane tag for the map. However, it'll be a pain for our dear brave volunteers to track and mark the lane they were in.</p>
<p>2) One possible way out: a) the bottleneck is that gpx files uploaded by users are often too noisy to figure out the lane assignment. But we have the "turn constraint" (change to inner/outer lane before turning left/right) and relative geometry shape of the route.</p>
<p>b) Given multiple gpx files for one road segment, we can have a robust estimation of the lane model using machine learning techniques.</p>
<p>c) Also, such technique may be useful for map refinement instead of asking users to correct by their own where the accuracy is in meters.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-lane" rel="tag" title="see questions tagged &#39;lane&#39;">lane</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Nov '11, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a24fb83b1a0f9b1915be072d2c42762d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eminemya&#39;s gravatar image" />
<p><span>eminemya</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eminemya has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '11, 16:47</strong> </span></p>
</div>
</div>
<div id="comments-container-9085" class="comments-container">
&#10;</div>
<div id="comment-tools-9085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9085-form-container" class="comment-form-container">
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

<span id="9087"></span>

<div id="answer-container-9087" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The gpx dataset is not linked to the main dataset at all. You can try to find som algorithms that can match traces to roads based on their direction, tags and date. The database was not designed with this in mind. It might be better to crowdsource theese types of tasks.</p>
<p>You are mentioning 15cm of accuracy. This is a rich mans dream. It requires an absurd amount of traces with 15m accuracy to confidently reduce it to 15cm accuracy. And there are a lot of chalanges if you want to derrive the lanes as well.</p>
<p>May I ask what research department are funding you?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '11, 18:25</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-9087" class="comments-container">
&#10;</div>
<div id="comment-tools-9087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9087-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9104"></span>

<div id="answer-container-9104" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9104-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>15cm accuracy gps is not affordable yet (althoughit seems this is more for market reasons than technical ones, and city workers are pushing for it, so we might get there someday).</p>
<p>If you download gpx traces from OSM for a multi-lane motorway, you'll see a fuzzy cloud of traces. I find it hard to imagine that even with a huge number of those you could filter out individual lanes.</p>
<p>I think the best you can do with current tools is using very well-calibrated very hi-res statellite imagery. Getting good-enough calibration via gps is probably possible but will be a lot of boring repetitive work.</p>
<p>Say (hypothetically) you get to this point, there are a few OSMers (myself included) who would frown uppon storing motorway lanes as separate ways in the main osm db, as your project seem to require. Tagging one way as "lanes=3, width=10" is great and usefull, but adding multiple ways will cause a lot of trouble for routing and rendering engines, and arguably bloat the database.</p>
<p>All that said, I dont want to put you off such an exciting project, and OSM is surely a good place to start, even if only for the tools and the wealth of knowledge. But realize it might be a bit harder than you had hoped :p</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '11, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-9104" class="comments-container">
&#10;</div>
<div id="comment-tools-9104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9104-form-container" class="comment-form-container">
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

