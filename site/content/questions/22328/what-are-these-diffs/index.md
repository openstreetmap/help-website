+++
type = "question"
title = "What are these diffs?"
description = '''Are these differences errors or there are formal reason for them? Look at the extract in the permalink: http://www.openstreetmap.org/?lat=49.0032&amp;amp;lon=-120.498&amp;amp;zoom=12&amp;amp;layers=M As an experienced mapper, I can understand the sharp cut on the white holes, displaced country border... but I d...'''
date = "2013-05-12T10:59:00Z"
lastmod = "2013-05-14T11:04:00Z"
weight = 22328
keywords = [ "rendering", "colors", "contrast" ]
aliases = [ "/questions/22328" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What are these diffs?](/questions/22328/what-are-these-diffs)

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
<span id="post-22328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22328-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Are these differences errors or there are formal reason for them? Look at the extract in the permalink:</p>
<p><a href="http://www.openstreetmap.org/?lat=49.0032&amp;lon=-120.498&amp;zoom=12&amp;layers=M">http://www.openstreetmap.org/?lat=49.0032&amp;lon=-120.498&amp;zoom=12&amp;layers=M</a></p>
<p>As an experienced mapper, I can understand the sharp cut on the white holes, displaced country border... but I dont understan the color differences for the (obviously) same area object types (light and dark green), the horizontal/vertical tile/grid lines, the very weak contrast between the light-green and light-blue... As I undestand, the SlippyMap is OSM's reference map and should be (among) the best maps created on the most recen/valid OSM source data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-colors" rel="tag" title="see questions tagged &#39;colors&#39;">colors</span> <span class="post-tag tag-link-contrast" rel="tag" title="see questions tagged &#39;contrast&#39;">contrast</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '13, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-22328" class="comments-container">
&#10;</div>
<div id="comment-tools-22328" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22328-form-container" class="comment-form-container">
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

<span id="22330"></span>

<div id="answer-container-22330" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22330-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-22330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The darker green comes from a <a href="http://www.openstreetmap.org/browse/relation/2421485">landuse=forest</a> relation and the lighter green from a <a href="http://www.openstreetmap.org/browse/relation/1209319">natural=wood</a> relation. Additionally there is a <a href="http://www.openstreetmap.org/browse/relation/2230176">boundary=national_park / leisure=nature_reserve</a> combination rendered as an area with many "NR" labels and to the west there is a <a href="http://www.openstreetmap.org/browse/relation/2421484">boundary=national_park</a> without the <em>leisure=nature_reserve</em> tag but with a <em>leisure=park</em> tag resulting in an even lighter green. Somewhat confusing but that's what you get if you want to render many different tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '13, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '13, 20:13</strong> </span></p>
</div>
</div>
<div id="comments-container-22330" class="comments-container">
<span id="22416"></span>
<div id="comment-22416" class="comment">
<div id="post-22416-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This comes back to the conflicting interpretations of landuse=forest vs natural=wood. In this case they really should be tagged the same on each side of the border, but different mappers follow different conventions.</p>
<p>I keep pushing for the "landuse=forest is for forestry activity" interpretation, but some people use another interpreation, many people dont know/care, and many areas are hard to judge either way. Sigh...</p>
</div>
<div id="comment-22416-info" class="comment-info">
<span class="comment-age">(14 May '13, 10:46)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="22417"></span>
<div id="comment-22417" class="comment">
<div id="post-22417-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It's worse than you think: a lot of US forests are just land which is designated National Forest and run by the Forest Service. In many cases there is nary a tree in sight, although this area is mainly forested, but there are gaps <a href="http://mc.bbbike.org/mc/?lon=-121.78925&amp;lat=48.93702&amp;zoom=15&amp;num=4&amp;mt0=mapnik-german&amp;mt1=bing-satellite&amp;mt2=hike_bike&amp;mt3=mapquest-satellite.">http://mc.bbbike.org/mc/?lon=-121.78925&amp;lat=48.93702&amp;zoom=15&amp;num=4&amp;mt0=mapnik-german&amp;mt1=bing-satellite&amp;mt2=hike_bike&amp;mt3=mapquest-satellite.</a> Note the miasalignment of US/Canadian border. North Cascades National Park was also tagged leisure=park (I removed it).</p>
</div>
<div id="comment-22417-info" class="comment-info">
<span class="comment-age">(14 May '13, 11:04)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22330-form-container" class="comment-form-container">
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

