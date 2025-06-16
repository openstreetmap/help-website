+++
type = "question"
title = "Mississippi River riverbank problem"
description = '''The Mississippi River, just to the east of St Louis MO in the USA, is &quot;missing&quot; for part of its length. It appears as land, and an island in the river appears as water. This seems to indicate there is some problem with the relation used for the riverbank, but I can&#x27;t find it. In addition, there seem...'''
date = "2012-12-15T22:40:00Z"
lastmod = "2012-12-16T00:14:00Z"
weight = 18479
keywords = [ "river", "riverbank" ]
aliases = [ "/questions/18479" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mississippi River riverbank problem](/questions/18479/mississippi-river-riverbank-problem)

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
<span id="post-18479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18479-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The Mississippi River, just to the east of St Louis MO in the USA, is "missing" for part of its length. It appears as land, and an island in the river appears as water. This seems to indicate there is some problem with the relation used for the riverbank, but I can't find it. In addition, there seems to be a second "riverbank" shape on top of the relation (similar but not identical shape). Does anyone know how to debug this? I am new to OSM relations and don't know where to start...</p>
<p>Link: <a href="https://www.openstreetmap.org/?lat=38.7232&amp;lon=-90.1832&amp;zoom=13&amp;layers=M">https://www.openstreetmap.org/?lat=38.7232&amp;lon=-90.1832&amp;zoom=13&amp;layers=M</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-riverbank" rel="tag" title="see questions tagged &#39;riverbank&#39;">riverbank</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '12, 22:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ed0b2a6757c7515c4f9c529b2eb08ae3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eric22&#39;s gravatar image" />
<p><span>eric22</span><br />
<span class="score" title="401 reputation points">401</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eric22 has 2 accepted answers">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Dec '12, 22:42</strong> </span></p>
</div>
</div>
<div id="comments-container-18479" class="comments-container">
&#10;</div>
<div id="comment-tools-18479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18479-form-container" class="comment-form-container">
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

<span id="18480"></span>

<div id="answer-container-18480" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18480-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-18480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are right, there are several problems here - parts of the river are mapped twice, and one of these duplicates is a <a href="https://www.openstreetmap.org/?relation=1592433">very large and broken polygon</a> that includes (or tries to include) a couple of tributaries (among them the Meramec). It is probably hopeless to try and fix this so my suggestion would be to delete that large polygon (or cut it into smaller pieces and re-use those that aren't already covered by something else).</p>
<p>The OSM Inspector is a good tool to check multipolygons polygons for sanity, and it shows <a href="http://tools.geofabrik.de/osmi/?view=multipolygon&amp;lon=-90.40668&amp;lat=38.44305&amp;zoom=10">this polygon as having un-closed outer rings</a>:</p>
<p><img src="/upfiles/poly.png" alt="alt text" /></p>
<p>(Note however that OSM Inspector doesn't have live data - it is usually a day behind, so don't expect the display to change immediately after you've fixed something.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '12, 00:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-18480" class="comments-container">
&#10;</div>
<div id="comment-tools-18480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18480-form-container" class="comment-form-container">
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

