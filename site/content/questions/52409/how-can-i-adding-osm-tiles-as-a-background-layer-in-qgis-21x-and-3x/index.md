+++
type = "question"
title = "How can I adding OSM Tiles as a Background Layer in QGIS 2.1x and 3.x"
description = '''How can I bring in OpenStreetMap raster maps into QGIS? Meta: this is effectively asking an earlier question again, but restricted to QGIS versions from 2016 and later. '''
date = "2016-10-08T10:55:00Z"
lastmod = "2018-03-08T15:56:00Z"
weight = 52409
keywords = [ "qgis", "tiles" ]
aliases = [ "/questions/52409" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I adding OSM Tiles as a Background Layer in QGIS 2.1x and 3.x](/questions/52409/how-can-i-adding-osm-tiles-as-a-background-layer-in-qgis-21x-and-3x)

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
<span id="post-52409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52409-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I bring in OpenStreetMap raster maps into QGIS?</p>
<p>Meta: this is effectively asking an <a href="/questions/400/how-to-get-openstreetmap-as-a-raster-layer-in-qgis">earlier question</a> again, but restricted to QGIS versions from 2016 and later.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '16, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-52409" class="comments-container">
&#10;</div>
<div id="comment-tools-52409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52409-form-container" class="comment-form-container">
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

<span id="52410"></span>

<div id="answer-container-52410" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52410-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>QGIS (2.10 upwards) has two plugins available in the main repository which allow the addition of many raster tile layers, including those based on OSM:</p>
<ul>
<li><strong><a href="https://plugins.qgis.org/plugins/quick_map_services/">QuickMap Services</a></strong>. Accesses tiles directly allowing cacheing of tiles and reprojection. Eliminates some of the issues with:</li>
<li><strong><a href="https://plugins.qgis.org/plugins/openlayers_plugin/">OpenLayers Plugin</a></strong>. This is the plugin which has been recommended for a number of years. However it does not work well with QGIS composer, and one is forced to use Popular Mercator projection (ESPG:900913 /EPSG:3087).</li>
</ul>
<p>The former, QuickMap Services, is easy to use and is more flexible than the OpenLayers Plugin. Indeed, QuickMap Services was built upon the OpenLayers Plugin.</p>
<p>Both plugins can be installed directly from the Plugin menu in QGIS.</p>
<p>There may be differences in flexibility of adding specific layers to these plugins, but this topic merits a separate question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '16, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-52410" class="comments-container">
<span id="62586"></span>
<div id="comment-62586" class="comment">
<div id="post-62586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that neither of these plugins are available for QGIS 3.0 at present.</p>
</div>
<div id="comment-62586-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 15:56)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52410" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52410-form-container" class="comment-form-container">
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

