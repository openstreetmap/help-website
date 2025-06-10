+++
type = "question"
title = "OSM arctoolbox uploaded polylines instead of polygons"
description = '''Hello! I tried a few hours ago to upload the urban cadastral parcel to OSM using the OSM arctoolbox of ArcMAP, but when I checked the result, all the polygons were uploaded as polylines. You can see the change in the following URL: https://www.openstreetmap.org/changeset/57752238 Do you know how to ...'''
date = "2018-04-03T18:28:00Z"
lastmod = "2018-04-03T20:14:00Z"
weight = 62891
keywords = [ "arcgis" ]
aliases = [ "/questions/62891" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM arctoolbox uploaded polylines instead of polygons](/questions/62891/osm-arctoolbox-uploaded-polylines-instead-of-polygons)

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
<span id="post-62891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62891-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I tried a few hours ago to upload the urban cadastral parcel to OSM using the OSM arctoolbox of ArcMAP, but when I checked the result, all the polygons were uploaded as polylines. You can see the change in the following URL: <a href="https://www.openstreetmap.org/changeset/57752238">https://www.openstreetmap.org/changeset/57752238</a></p>
<p>Do you know how to fix it? All the polylines are declared as buildings polygons.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Apr '18, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/6e4820013539b4b2508f25660d61af72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sadae&#39;s gravatar image" />
<p><span>sadae</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sadae has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62891" class="comments-container">
&#10;</div>
<div id="comment-tools-62891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62891-form-container" class="comment-form-container">
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

<span id="62894"></span>

<div id="answer-container-62894" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62894-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-62894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should not have run this "upload" (we call it a data import) without prior consultation. Please read the <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">import guidelines.</a> Among other things, these guidelines would have instructed you to</p>
<ul>
<li>discuss your plans in advance e.g. on the "imports" mailing list</li>
<li>when unsure, try things out first before importing a larger amount of data</li>
<li>make sure the source is license compatible, and document the license and the import properly</li>
</ul>
<p>In the discussion, you would have been told that parcel boundaries are usually not welcome in OSM because they are not generally observable on the ground.</p>
<p>I am now deleting the problematic data. Apart from the total lack of tagging, it is also suspicious that your changeset had exactly 10,000 elements which is the limit since a while; it is possible that the software wanted to upload more but was thwarted by the changeset size limit. Thankfully, in this case!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '18, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62894" class="comments-container">
&#10;</div>
<div id="comment-tools-62894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62894-form-container" class="comment-form-container">
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

