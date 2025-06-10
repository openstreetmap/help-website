+++
type = "question"
title = "[closed] render kml 10mb KML file cordinates data on OSM map throws stop running script error in OpenLayer.js file"
description = '''I am trying to render the kml file having 18000 line string data on OSM map using openlayer HTTP strategy. To render OSM map i am using GeoExt.MapPanel and ExtJS 3.4 viewport. The problem is I am facing the stop running script error on page and in IE8 hang the PC and browser. Thanks...'''
date = "2013-04-15T08:15:00Z"
lastmod = "2013-04-15T08:39:00Z"
weight = 21539
keywords = [ "maps", "extract", "osm", "largekmlfiles" ]
aliases = [ "/questions/21539" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] render kml 10mb KML file cordinates data on OSM map throws stop running script error in OpenLayer.js file](/questions/21539/render-kml-10mb-kml-file-cordinates-data-on-osm-map-throws-stop-running-script-error-in-openlayerjs-file)

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
<span id="post-21539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21539-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to render the kml file having 18000 line string data on OSM map using openlayer HTTP strategy. To render OSM map i am using GeoExt.MapPanel and ExtJS 3.4 viewport.</p>
<p>The problem is I am facing the stop running script error on page and in IE8 hang the PC and browser.</p>
<p>Thanks...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-largekmlfiles" rel="tag" title="see questions tagged &#39;largekmlfiles&#39;">largekmlfiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '13, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/1bbfada2a55b8e61e7b81dd3cece8091?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bhavin%20Patel&#39;s gravatar image" />
<p><span>Bhavin Patel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bhavin Patel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>15 Apr '13, 08:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-21539" class="comments-container">
&#10;</div>
<div id="comment-tools-21539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21539-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Frederik Ramm 15 Apr '13, 08:40

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21540"></span>

<div id="answer-container-21540" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21540-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to set up a database on the server side and make it so that only data for the currently visible map extent is loaded from the database. Asking the browser to handle that amount of data is asking for trouble. Various options exist to do the database loading, one of the simplest probably being <a href="http://www.featureserver.org">FeatureServer</a>.<br />
</p>
<p>Your question is not OpenStreetMap related - the fact that you are using an OSM base map is not relevant to your problem. Check openlayers.org for OpenLayers help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '13, 08:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '13, 08:39</strong> </span></p>
</div>
</div>
<div id="comments-container-21540" class="comments-container">
&#10;</div>
<div id="comment-tools-21540" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21540-form-container" class="comment-form-container">
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

