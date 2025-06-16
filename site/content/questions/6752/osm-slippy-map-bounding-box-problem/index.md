+++
type = "question"
title = "OSM Slippy Map Bounding Box problem"
description = '''Hi all, Can someone give me a reason to explain why this bounding box url zooms to the bounding box: https://www.openstreetmap.org/?minlon=22.3418234&amp;amp;minlat=57.5129102&amp;amp;maxlon=22.5739625&amp;amp;maxlat=57.6287332&amp;amp;box=yes  And this one doesn&#x27;t? https://www.openstreetmap.org/?minlon=-0.7600&amp;amp;m...'''
date = "2011-08-01T11:19:00Z"
lastmod = "2011-08-01T11:27:00Z"
weight = 6752
keywords = [ "openlayers", "bbox", "slippymap" ]
aliases = [ "/questions/6752" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM Slippy Map Bounding Box problem](/questions/6752/osm-slippy-map-bounding-box-problem)

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
<span id="post-6752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6752-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>Can someone give me a reason to explain why this bounding box url zooms to the bounding box:<br />
<a href="https://www.openstreetmap.org/?minlon=22.3418234&amp;minlat=57.5129102&amp;maxlon=22.5739625&amp;maxlat=57.6287332&amp;box=yes">https://www.openstreetmap.org/?minlon=22.3418234&amp;minlat=57.5129102&amp;maxlon=22.5739625&amp;maxlat=57.6287332&amp;box=yes</a><br />
And this one doesn't?<br />
<a href="https://www.openstreetmap.org/?minlon=-0.7600&amp;minlat=9.3500&amp;maxlon=-0.9200&amp;maxlat=9.4800&amp;box=yes">https://www.openstreetmap.org/?minlon=-0.7600&amp;minlat=9.3500&amp;maxlon=-0.9200&amp;maxlat=9.4800&amp;box=yes</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '11, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/7ced9ba139adb4087bbe8935b2eab74d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samlarsen1&#39;s gravatar image" />
<p><span>samlarsen1</span><br />
<span class="score" title="124 reputation points">124</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samlarsen1 has one accepted answer">50%</span> </br></br></p>
</div>
</div>
<div id="comments-container-6752" class="comments-container">
&#10;</div>
<div id="comment-tools-6752" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6752-form-container" class="comment-form-container">
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

<span id="6754"></span>

<div id="answer-container-6754" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6754-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-6754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="samlarsen1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It must be because your minlon is larger than your maxlon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '11, 11:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
</div>
<div id="comments-container-6754" class="comments-container">
<span id="6755"></span>
<div id="comment-6755" class="comment">
<div id="post-6755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks - stupid mistake</p>
</div>
<div id="comment-6755-info" class="comment-info">
<span class="comment-age">(01 Aug '11, 11:27)</span> <span class="comment-user userinfo">samlarsen1</span>
</div>
</div>
</div>
<div id="comment-tools-6754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6754-form-container" class="comment-form-container">
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

