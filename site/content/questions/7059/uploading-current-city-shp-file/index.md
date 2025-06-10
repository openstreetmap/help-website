+++
type = "question"
title = "uploading Current City .shp file"
description = '''I have a current .shp file that the city uses for it&#x27;s mapping. Is it okay to delete the current boundary in OSM and upload the new one? I&#x27;ve been moving nodes to bring the current OSM boundary into conformance with this updated one. Thank goodness the City is a small one. If moving nodes is the saf...'''
date = "2011-08-13T03:29:00Z"
lastmod = "2011-08-13T06:53:00Z"
weight = 7059
keywords = [ "shapefile", "boundary", "update" ]
aliases = [ "/questions/7059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [uploading Current City .shp file](/questions/7059/uploading-current-city-shp-file)

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
<span id="post-7059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7059-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a current .shp file that the city uses for it's mapping. Is it okay to delete the current boundary in OSM and upload the new one? I've been moving nodes to bring the current OSM boundary into conformance with this updated one. Thank goodness the City is a small one. If moving nodes is the safest way to update date, I will continue. But I would like to know if I would cause problems or would be crossing some kind of policy line by deleting the old boundary and just uploading the new one. I realize I would have to detach nodes to avoid ripping out whole streets.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '11, 03:29</strong></p>
<img src="https://secure.gravatar.com/avatar/58d4df87085eb9305e01437cd231fb93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="QBL&#39;s gravatar image" />
<p><span>QBL</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="QBL has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7059" class="comments-container">
&#10;</div>
<div id="comment-tools-7059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7059-form-container" class="comment-form-container">
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

<span id="7060"></span>

<div id="answer-container-7060" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7060-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When your shapefile has more details or is more exact then the already existing boundary, there is no reason to delete the old one to achieve better data.</p>
<p>Because the old boundary is possibly an element of one ore more relations, or even streets and ways are elements of the boundary.</p>
<p>And: As a matter of data amount, especially of the whole raw OSM data covering the planet, it can be always better not do delete old data and replace it with new, but to edit the existing ones. Because old Data is still stored in the history data.</p>
<p>A proper way to benefit from your new shapefile can be to load it into any editor that can handle shapefiles, but there in an extra layer. Then you can use this layer as a transparent overlay to adjust the already existing one.</p>
<p>Have a look at <a href="http://wiki.openstreetmap.org/wiki/Shapefile">shapefile</a> to see which editors or GIS programs can do that.</p>
<p>PS: do you really have the permission to use that shapefile for OSM purposes, according to the license that we are using and that is to come (ODBL)? (Please edit your question and add information if you have)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '11, 06:53</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '11, 08:19</strong> </span></p>
</div>
</div>
<div id="comments-container-7060" class="comments-container">
&#10;</div>
<div id="comment-tools-7060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7060-form-container" class="comment-form-container">
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

