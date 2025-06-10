+++
type = "question"
title = "runtime error"
description = '''Hi, I want to create a global electricity transmission and distribution map. It works well with the overpass turbo for smaller countries like Austria with the code type:way &amp;amp; (power=line | power=cable | power=minor_line) in Germany. Unfortunately,if I do it with Germany, a runtime error occurs a...'''
date = "2019-08-08T23:17:00Z"
lastmod = "2019-08-09T11:24:00Z"
weight = 70349
keywords = [ "overpass", "extracts" ]
aliases = [ "/questions/70349" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [runtime error](/questions/70349/runtime-error)

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
<span id="post-70349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70349-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to create a global electricity transmission and distribution map. It works well with the overpass turbo for smaller countries like Austria with the code type:way &amp; (power=line | power=cable | power=minor_line) in Germany. Unfortunately,if I do it with Germany, a runtime error occurs after 25 seconds saying "runtime error: Query timed out in "query" at line 12 after 26 seconds." indicating that it´s too big and there´s not enough processing time.<br />
Can anybody help me to also load the power line network for bigger countries? best regards, Philipp</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-extracts" rel="tag" title="see questions tagged &#39;extracts&#39;">extracts</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '19, 23:17</strong></p>
<img src="https://secure.gravatar.com/avatar/90b2ffbaa008a4ded152e03dc96fd4e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philipp&#39;s gravatar image" />
<p><span>Philipp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philipp has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '19, 11:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-70349" class="comments-container">
&#10;</div>
<div id="comment-tools-70349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70349-form-container" class="comment-form-container">
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

<span id="70355"></span>

<div id="answer-container-70355" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70355-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While you can increase the timeout (change [timeout:25] to something larger), that will only help a bit as the problem with larger countries is that they are larger and queries will take longer to the point that they will always fail.</p>
<p>You could try to use a dedicated extract service, for example: <a href="https://osmaxx.hsr.ch/">https://osmaxx.hsr.ch/</a></p>
<p>Or download "raw" OSM data and filter it to contain objects that you are interested in and then split it in to regions (or the other ways around). You probably will also need to convert OSM data to a format that actually has instantiated geometries, for example GeoJSON.</p>
<p>Download sites: <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts</a></p>
<p>Tools: <a href="https://wiki.openstreetmap.org/wiki/Osmium">osmium tool</a>, <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> and many more</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '19, 11:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '19, 11:32</strong> </span></p>
</div>
</div>
<div id="comments-container-70355" class="comments-container">
&#10;</div>
<div id="comment-tools-70355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70355-form-container" class="comment-form-container">
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

