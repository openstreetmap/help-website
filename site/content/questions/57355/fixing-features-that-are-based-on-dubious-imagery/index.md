+++
type = "question"
title = "Fixing features that are based on dubious imagery"
description = '''I have a couple of related questions about the area around the Tolmie Peak Trail area in Mount Rainier National Park. Bing imagery significantly disagrees with Mapbox and the USGS topo map on the shape of nearby Lake Eunice and its position relative to the trail. A number of OSM GPS tracks of people...'''
date = "2017-07-30T19:26:00Z"
lastmod = "2017-07-30T20:40:00Z"
weight = 57355
keywords = [ "correction", "imagery", "imagerydifferences" ]
aliases = [ "/questions/57355" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Fixing features that are based on dubious imagery](/questions/57355/fixing-features-that-are-based-on-dubious-imagery)

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
<span id="post-57355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57355-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a couple of related questions about the area around the <a href="https://www.openstreetmap.org/way/129536770">Tolmie Peak Trail</a> area in Mount Rainier National Park.</p>
<p><a href="https://binged.it/2uOxXsm">Bing imagery</a> <em>significantly</em> disagrees with <a href="https://tinyurl.com/yd9spoq2">Mapbox</a> and the USGS topo map on the shape of nearby Lake Eunice and its position relative to the trail. A number of OSM GPS tracks of people who have walked up to the lake shore seem to agree with the Mapbox/USGS information. Overall, the Bing imagery for that area looks warped, and aligning some parts of the map with it causes others to misalign. (As a side note, large trees are clearly visible at the edges of the lake on all imagery so the issue probably isn't the lake water level changing).</p>
<p>The problem is that the OSM shape for Lake Eunice is clearly based on Bing imagery: it has the same strange shape and is placed too close to the trail (many GPS traces go straight through the lake). (<a href="https://imgur.com/a/IZXop">screenshot</a>)</p>
<p>In this situation, it appropriate to redraw the lake based on Mapbox/USGS data, or, since there is a disagreement, should we wait until someone collects GPS data on the lake's shape and position? If I redraw the lake, where can I document the reason I did it, and if not, can the lake be marked as dubious?</p>
<p>And as a bonus question, what can cause such large distortion in satellite imagery?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-correction" rel="tag" title="see questions tagged &#39;correction&#39;">correction</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-imagerydifferences" rel="tag" title="see questions tagged &#39;imagerydifferences&#39;">imagerydifferences</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '17, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/84ed409c844cbf6608f2e74e69412571?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattX&#39;s gravatar image" />
<p><span>MattX</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattX has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57355" class="comments-container">
&#10;</div>
<div id="comment-tools-57355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57355-form-container" class="comment-form-container">
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

<span id="57356"></span>

<div id="answer-container-57356" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57356-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-57356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MattX has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think there is any answer other than simply to adjust the lake to fit current imagery (please do not delete), given that this is potentially a larger object and will require many changes you would be best off using JOSM.</p>
<p>Add a note that the Bing imagery was off and you are done (note you can check against both digital globe sources too).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '17, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-57356" class="comments-container">
&#10;</div>
<div id="comment-tools-57356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57356-form-container" class="comment-form-container">
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

