+++
type = "question"
title = "Large map cropping issue"
description = '''I&#x27;m trying to export an image (ideally an SVG) of the entire Fiji region - which is quite large. Whenever I go to export the map, it&#x27;s cropped to a smaller region than what I&#x27;ve selected. I&#x27;ve tried other formats, scales and regions, but it seems to be unable to export the whole area. Are there any ...'''
date = "2015-12-03T06:30:00Z"
lastmod = "2015-12-07T20:40:00Z"
weight = 46942
keywords = [ "svg", "large_area" ]
aliases = [ "/questions/46942" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Large map cropping issue](/questions/46942/large-map-cropping-issue)

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
<span id="post-46942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46942-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to export an image (ideally an SVG) of the entire Fiji region - which is quite large.</p>
<p>Whenever I go to export the map, it's cropped to a smaller region than what I've selected. I've tried other formats, scales and regions, but it seems to be unable to export the whole area.</p>
<p>Are there any fixes or alternate ways of getting the full region?</p>
<p>This is what I'm selecting: <a href="http://i.imgur.com/Gj4O8Wv.png">http://i.imgur.com/Gj4O8Wv.png</a> This is what gets exported: <a href="http://imgur.com/5FHVe0D">http://imgur.com/5FHVe0D</a></p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-large_area" rel="tag" title="see questions tagged &#39;large_area&#39;">large_area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '15, 06:30</strong></p>
<img src="https://secure.gravatar.com/avatar/d36bfa98b24435f535da670ec36ba5ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="micjen0&#39;s gravatar image" />
<p><span>micjen0</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="micjen0 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46942" class="comments-container">
&#10;</div>
<div id="comment-tools-46942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46942-form-container" class="comment-form-container">
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

<span id="46945"></span>

<div id="answer-container-46945" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46945-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect you are seeing the problem because the area you select is spanning the 180° meridian. I would suggest, as a workaround, exporting two images, one for the area in the western hemisphere, and one for the part of Fiji in the eastern hemisphere.</p>
<p>There is likely a bug either in the area-selection code, or in the image export, that causes this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '15, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-46945" class="comments-container">
<span id="47041"></span>
<div id="comment-47041" class="comment">
<div id="post-47041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - good suggestion, but the bug seems to break the area directly adjacent to the meridian, giving me Invalid Bounding Box or server areas. In fact it's almost impossible to export the part of Fiji east of the line.</p>
</div>
<div id="comment-47041-info" class="comment-info">
<span class="comment-age">(07 Dec '15, 20:38)</span> <span class="comment-user userinfo">micjen0</span>
</div>
</div>
</div>
<div id="comment-tools-46945" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46945-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47036"></span>

<div id="answer-container-47036" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47036-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not sure whether that "error" also occurs in other OSM based tools.</p>
<p>So have a look at <a href="https://wiki.openstreetmap.org/wiki/OSM_on_Paper">OSM_on_Paper</a> or <a href="https://wiki.openstreetmap.org/wiki/SVG">SVG</a> in the OSM wiki and tell us about success or failure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '15, 17:04</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-47036" class="comments-container">
<span id="47042"></span>
<div id="comment-47042" class="comment">
<div id="post-47042-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried Mapbox earlier which had the same problem - but I'll give these a shot too, thanks.</p>
</div>
<div id="comment-47042-info" class="comment-info">
<span class="comment-age">(07 Dec '15, 20:40)</span> <span class="comment-user userinfo">micjen0</span>
</div>
</div>
</div>
<div id="comment-tools-47036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47036-form-container" class="comment-form-container">
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

