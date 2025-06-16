+++
type = "question"
title = "Placement of labels and how to extract them?"
description = '''I was wondering if the labels for neighborhoods (areas) are pinned to a centroid or boundary or if they are free floating? Is it possible to extract these labels somehow? Ideally in the form of a shapefile or other geographically referenced file? It would help greatly with some Haiti mapping project...'''
date = "2011-02-15T21:08:00Z"
lastmod = "2011-02-16T19:13:00Z"
weight = 3088
keywords = [ "labels", "extracting" ]
aliases = [ "/questions/3088" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Placement of labels and how to extract them?](/questions/3088/placement-of-labels-and-how-to-extract-them)

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
<span id="post-3088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3088-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was wondering if the labels for neighborhoods (areas) are pinned to a centroid or boundary or if they are free floating? Is it possible to extract these labels somehow? Ideally in the form of a shapefile or other geographically referenced file? It would help greatly with some Haiti mapping projects my group is undertaking.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-extracting" rel="tag" title="see questions tagged &#39;extracting&#39;">extracting</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '11, 21:08</strong></p>
<img src="https://secure.gravatar.com/avatar/429f73c20b270c9cce35f7eca4cc645a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karinme&#39;s gravatar image" />
<p><span>karinme</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karinme has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3088" class="comments-container">
&#10;</div>
<div id="comment-tools-3088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3088-form-container" class="comment-form-container">
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

<span id="3095"></span>

<div id="answer-container-3095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3095-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-3095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Places in OSM are simply OSM objects tagged with <a href="https://wiki.openstreetmap.org/wiki/Place">place=*</a>. Thus they may be nodes located at a specific lat/long by a mapper, or they may be an area created with a closed way, or more complex shapes may be specified with a multipolygon. The answer to your first question is therefore dependant on the primitive used to map a place. Administrative areas are tagged differently and will usually be represented by closed ways or relations.</p>
<p>By 'label' I take it to mean the point at which the name tag is displayed on the slippy map on the OSM home page. The placement of the name is done by separate software (<a href="https://wiki.openstreetmap.org/wiki/Mapnik">mapnik</a>) and is independent of the how the data is stored in OSM. In practice it uses either the node or the centroid of the shape.</p>
<p>The primitive objects tagged with place are available in OSM XML format files from third-party sources, such as <a href="http://downloads.cloudmade.com/">Cloudmade</a> and <a href="http://www.geofabrik.de/data/download.html">Geofabrik</a>. Alternatively <a href="https://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> can be used to extract OSM data for a given bounding box using [place=*] as a <a href="https://wiki.openstreetmap.org/wiki/Xapi#Tag_Predicates">predicate</a>. The <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> tool is one convenient way of converting this data into other formats. Although this does discard some data, it does preserve all the data which you mention.</p>
<p>Shape files containing the data you require may also be provided by Cloudmade, Geofabrik and others. Certainly Geofabrik have been providing a rich set of resources for <a href="http://download.geofabrik.de/osm/central-america/">Haiti</a> for over a year.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '11, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-3095" class="comments-container">
&#10;</div>
<div id="comment-tools-3095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3095-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3116"></span>

<div id="answer-container-3116" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3116-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We appreciate your answer and the detailed information. With your help we were able to do what we had in mind. Thanks a lot for the support!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '11, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/429f73c20b270c9cce35f7eca4cc645a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karinme&#39;s gravatar image" />
<p><span>karinme</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karinme has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3116" class="comments-container">
&#10;</div>
<div id="comment-tools-3116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3116-form-container" class="comment-form-container">
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

