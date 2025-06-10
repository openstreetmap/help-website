+++
type = "question"
title = "Is there any possibility to draw an editable map using OSM data?"
description = '''Hi!, I am a newbie on openstreetmap related developments, I need to build a web application using PHP or Python frameworks, that could draw map using OSM data. It should also allows to edit attributes of nodes (ex: highway, signal lights, foot path, parking etc), edited data should not need to be up...'''
date = "2016-02-01T06:15:00Z"
lastmod = "2016-02-01T08:50:00Z"
weight = 47775
keywords = [ "openstreetmap", "rendering", "osm", "mapping" ]
aliases = [ "/questions/47775" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any possibility to draw an editable map using OSM data?](/questions/47775/is-there-any-possibility-to-draw-an-editable-map-using-osm-data)

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
<span id="post-47775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47775-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!,</p>
<p>I am a newbie on openstreetmap related developments, I need to build a web application using PHP or Python frameworks, that could draw map using OSM data. It should also allows to edit attributes of nodes (ex: highway, signal lights, foot path, parking etc), edited data should not need to be updated to OSM servers.</p>
<p>I couldn't find any proper guide. Let me know if there any guides or tutorials to do so.</p>
<p>Where should I start? Please help me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '16, 06:15</strong></p>
<img src="https://secure.gravatar.com/avatar/8658f3497c28b5b44f3871d4513a4639?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daniel1420&#39;s gravatar image" />
<p><span>Daniel1420</span><br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daniel1420 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47775" class="comments-container">
<span id="47783"></span>
<div id="comment-47783" class="comment">
<div id="post-47783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/178875/is-there-any-possibility-to-draw-an-editable-map-using-osm-data">https://gis.stackexchange.com/questions/178875/is-there-any-possibility-to-draw-an-editable-map-using-osm-data</a></p>
</div>
<div id="comment-47783-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 08:50)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47775-form-container" class="comment-form-container">
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

<span id="47782"></span>

<div id="answer-container-47782" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47782-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your questions are too broad. OpenStreetMap is just a tiny component of what you want to build; you're essentially after a WebGIS solution that uses OSM data but the fact that it uses OSM data is not important for the solution, it could use other data as well. Hence you're really not asking your questions in the right place! -- You might want to look into "umap" which allows you to draw the results of Overpass requests on top of an OSM map; since umap is Open Source you could modify that to meet your needs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '16, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47782" class="comments-container">
&#10;</div>
<div id="comment-tools-47782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47782-form-container" class="comment-form-container">
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

