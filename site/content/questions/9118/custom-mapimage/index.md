+++
type = "question"
title = "Custom Map/Image"
description = '''I work with a GPS tracking applications for companies to track their fleets, and they can toggle from Bing to OSM(which I prefer to use). Basically, they have a large junk yard and want to track trucks within the yard going from dock to dock. What they have requested is a custom map of the yard to b...'''
date = "2011-11-18T20:49:00Z"
lastmod = "2011-11-18T22:40:00Z"
weight = 9118
keywords = [ "shapes", "images", "mapping", "customization" ]
aliases = [ "/questions/9118" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Custom Map/Image](/questions/9118/custom-mapimage)

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
<span id="post-9118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9118-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I work with a GPS tracking applications for companies to track their fleets, and they can toggle from Bing to OSM(which I prefer to use). Basically, they have a large junk yard and want to track trucks within the yard going from dock to dock. What they have requested is a custom map of the yard to be uploaded into the GPS application.</p>
<p>What we want to do is "overlay" either an actual satellite image, or a vectorized/ESRI drawing over OSM that is to scale, and then input the lats and longs of each dock to ensure accuracy.</p>
<p>How can this be done? Can we find an image and "paste" it overtop? Can we draw the outlines of the image and place it over the accurate lats and longs?</p>
<p>Any help is greatly appreciated.</p>
<p>Thanks,</p>
<p>Chris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapes" rel="tag" title="see questions tagged &#39;shapes&#39;">shapes</span> <span class="post-tag tag-link-images" rel="tag" title="see questions tagged &#39;images&#39;">images</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '11, 20:49</strong></p>
<img src="https://secure.gravatar.com/avatar/882085e719325c7bb8ad98d5251e7f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CWIBBY&#39;s gravatar image" />
<p><span>CWIBBY</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CWIBBY has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9118" class="comments-container">
&#10;</div>
<div id="comment-tools-9118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9118-form-container" class="comment-form-container">
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

<span id="9120"></span>

<div id="answer-container-9120" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9120-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use an editor like <a href="https://josm.openstreetmap.de/">JOSM</a> to load satelite images from a WMS service. The Bing satelite image are already configured because we have permission from them to use the satelite images to generate maps. You do not have to upload the changes and can save them as a .osm file.</p>
<p>You have not mentioned what "GPS application" you are using. Since it apperantly have support for multiple tile layers I assume you can add a new layer.</p>
<p>You can set up a render server like <a href="https://wiki.openstreetmap.org/wiki/TileMill">TileMill</a> and add the custom data and style to render a layer with transparent background. Then add this layer as an overlay over the base layers in your application.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '11, 22:40</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-9120" class="comments-container">
&#10;</div>
<div id="comment-tools-9120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9120-form-container" class="comment-form-container">
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

