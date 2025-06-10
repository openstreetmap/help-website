+++
type = "question"
title = "CRS for OSM import?"
description = '''I&#x27;m preparing to do an import. I&#x27;ve been following the guidelines, emailing the osm import lists, etc. I don&#x27;t want to clutter the email however with what I think is a simple question. What Coordinate Reference System do I want my data to be in before I convert from ogr to osm? I&#x27;m preparing to conv...'''
date = "2016-05-02T20:10:00Z"
lastmod = "2016-05-02T21:54:00Z"
weight = 49547
keywords = [ "crs", "import" ]
aliases = [ "/questions/49547" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [CRS for OSM import?](/questions/49547/crs-for-osm-import)

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
<span id="post-49547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49547-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm preparing to do an import. I've been following the guidelines, emailing the osm import lists, etc. I don't want to clutter the email however with what I think is a simple question.</p>
<p>What Coordinate Reference System do I want my data to be in before I convert from ogr to osm?</p>
<p>I'm preparing to convert my data in shapefile format to a PostGIS database. It's currently in WGS 84: 4326. Do I change it to the Web Mercator 3857?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crs" rel="tag" title="see questions tagged &#39;crs&#39;">crs</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '16, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/efa2bd232d1bfd0540fe303e6cba5f64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jfact0ry&#39;s gravatar image" />
<p><span>Jfact0ry</span><br />
<span class="score" title="366 reputation points">366</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jfact0ry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49547" class="comments-container">
&#10;</div>
<div id="comment-tools-49547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49547-form-container" class="comment-form-container">
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

<span id="49549"></span>

<div id="answer-container-49549" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49549-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are in a dialogue with the community on the import mailing list as you say, then that would have been a good opportunity to ask such a question! Also the people will likely want to see at least a sample of the .osm files you plan to upload. OSM stores its data in EPSG:4326 units.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '16, 21:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-49549" class="comments-container">
&#10;</div>
<div id="comment-tools-49549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49549-form-container" class="comment-form-container">
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

