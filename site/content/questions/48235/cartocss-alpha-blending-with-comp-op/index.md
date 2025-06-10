+++
type = "question"
title = "CartoCSS: alpha blending with comp-op"
description = '''Using CartoCSS/Tilemill, I have one layer for the land polygons and one for urban areas, as follows: #zoomed-polygons[zoom&amp;gt;7] {  polygon-fill: white; }  #urban[zoom&amp;gt;=4] {  polygon-fill: #FFCC99;  polygon-opacity: 0.66;  polygon-smooth: 0.75; }  I would like the urban areas to be clipped inside...'''
date = "2016-02-20T11:02:00Z"
lastmod = "2016-02-22T12:21:00Z"
weight = 48235
keywords = [ "tilemill", "carto" ]
aliases = [ "/questions/48235" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [CartoCSS: alpha blending with comp-op](/questions/48235/cartocss-alpha-blending-with-comp-op)

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
<span id="post-48235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48235-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using CartoCSS/Tilemill, I have one layer for the land polygons and one for urban areas, as follows:</p>
<pre><code>#zoomed-polygons[zoom&gt;7] {
  polygon-fill: white;
}
&#10;#urban[zoom&gt;=4] {
  polygon-fill: #FFCC99;
  polygon-opacity: 0.66;
  polygon-smooth: 0.75;
}</code></pre>
<p>I would like the urban areas to be clipped inside the land mass so they do not extend to water areas, unlike on the following screenshot:</p>
<p><a href="http://i.stack.imgur.com/Dnpyn.jpg"><img src="http://i.stack.imgur.com/Dnpyn.jpg" alt="map example" /></a></p>
<p>I believe <code>comp-op: dst-in;</code> is the correct way to go, but regardless of the <code>comp-op</code> value I set, I can't get anywhere near the desired result, unfortunately.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '16, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ed9e2083fe20e8b4671e7ca94d76a16c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20T&#39;s gravatar image" />
<p><span>Vincent T</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent T has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-48235" class="comments-container">
&#10;</div>
<div id="comment-tools-48235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48235-form-container" class="comment-form-container">
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

<span id="48290"></span>

<div id="answer-container-48290" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48290-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vincent T has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bear in mind that when you set a map background-colour (i.e. the sea in your example) then every source image is fully opaque and most of the alpha-blending comp-ops become much less useful.</p>
<p>The <a href="https://www.mapbox.com/tilemill/docs/guides/comp-op/">tilemill comp-op documentation</a> states:</p>
<p>"The dst-in comp-op will only draw parts of the destination that intersect with parts of the sources. The colors of the source will not be drawn, only the alpha channel (the shapes). If your source is completely solid, this operation will effectively be the same as dst, since all parts of the destination will intersect with the source."</p>
<p>The last sentence here is the most important - your source is completely solid. The approach that I would recommend is to use ocean polygons, not land polygons, and then draw land(background colour), city polygons and then ocean polygons on top.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '16, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-48290" class="comments-container">
&#10;</div>
<div id="comment-tools-48290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48290-form-container" class="comment-form-container">
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

