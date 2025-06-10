+++
type = "question"
title = "Extracting roadvector data and plotting on the image"
description = '''I want to download an aerial image containing roads from OSM and also download the corresponding road vectors for all the roads in the image from OSM and plot the roadvectors superimposed on the image to highlight the roads. Can somebody help me how to do it?'''
date = "2015-01-23T10:08:00Z"
lastmod = "2015-01-23T16:49:00Z"
weight = 40553
keywords = [ "aerialimage", "roadvector", "road", "overlay" ]
aliases = [ "/questions/40553" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting roadvector data and plotting on the image](/questions/40553/extracting-roadvector-data-and-plotting-on-the-image)

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
<span id="post-40553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40553-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to download an aerial image containing roads from OSM and also download the corresponding road vectors for all the roads in the image from OSM and plot the roadvectors superimposed on the image to highlight the roads. Can somebody help me how to do it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-aerialimage" rel="tag" title="see questions tagged &#39;aerialimage&#39;">aerialimage</span> <span class="post-tag tag-link-roadvector" rel="tag" title="see questions tagged &#39;roadvector&#39;">roadvector</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '15, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/6119d99a48db7aeac5af6dc47af10798?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssbals&#39;s gravatar image" />
<p><span>ssbals</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssbals has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40553" class="comments-container">
&#10;</div>
<div id="comment-tools-40553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40553-form-container" class="comment-form-container">
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

<span id="40569"></span>

<div id="answer-container-40569" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40569-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM does not have aerial images, but suppose you find a provider for such images. Libraries such as <a href="http://leafletjs.com/">Leaflet</a> or <a href="http://openlayers.org/">OpenLayers</a> allow you to show tiles within a bounding box. You program needs to be aware of this bounding box. Then the program can e.g. create an <a href="http://overpass-api.de/">Overpass query</a> to retrieve all ways and place them over the tiles with the aerial images.</p>
<p>An <a href="http://dev.openlayers.org/examples/lite.html">example</a> how to retrieve WMS tiles with OpenLayers, this could be used to load the aerial images, provided they are available as WMS.</p>
<p><a href="http://overpass-api.de/open_layers_mashup.html">Here</a> is a post describing how to combine Overpass with OpenLayers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '15, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-40569" class="comments-container">
&#10;</div>
<div id="comment-tools-40569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40569-form-container" class="comment-form-container">
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

