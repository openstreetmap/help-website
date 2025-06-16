+++
type = "question"
title = "Why am i missing polygons/features from OSM data when importing to ESRI"
description = '''Hi All, I have been importing OSM data into ESRI ArcGIS and I am noticing in some places features are missing (mainly Polygons). I am importing data from geofabrik Bulgaria.osm.pbf but comparing the attached image in ESRI to the osm data, there appears to be a lot of the wood or forest areas missing...'''
date = "2015-11-03T12:39:00Z"
lastmod = "2015-11-04T16:06:00Z"
weight = 46363
keywords = [ "shapefile", "esri", "data", "missing" ]
aliases = [ "/questions/46363" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why am i missing polygons/features from OSM data when importing to ESRI](/questions/46363/why-am-i-missing-polygonsfeatures-from-osm-data-when-importing-to-esri)

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
<span id="post-46363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46363-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I have been importing OSM data into ESRI ArcGIS and I am noticing in some places features are missing (mainly Polygons).</p>
<p>I am importing data from geofabrik Bulgaria.osm.pbf but comparing the attached image in ESRI to the osm data, there appears to be a lot of the wood or forest areas missing in the south of Bulgaria. Also looking at the raw polygon files imported there are no polygons present, but there are linear features which seem to match the wood boundaries.</p>
<p>Are there possible issues that the Areas features are not being imported or created from the nodes and can this be fixed?</p>
<p>Many thanks</p>
<p>Jon</p>
<p><img src="/upfiles/OSM_Bulgaria_ESRI_Import.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-esri" rel="tag" title="see questions tagged &#39;esri&#39;">esri</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '15, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ad7df450e9cbc9f0133014ef50c8bcf0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jon2709&#39;s gravatar image" />
<p><span>Jon2709</span><br />
<span class="score" title="36 reputation points">36</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jon2709 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-46363" class="comments-container">
&#10;</div>
<div id="comment-tools-46363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46363-form-container" class="comment-form-container">
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

<span id="46364"></span>

<div id="answer-container-46364" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46364-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi All,</p>
<p>It seems that I have identified the possible problem,</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Area/The_Future_of_Areas">https://wiki.openstreetmap.org/wiki/Area/The_Future_of_Areas</a></p>
<p>I will have a look at the Tag area=yes and see if these ways are closed or multipolygons</p>
<p>If anyone has further info, please share.</p>
<p>Thanks</p>
<p>Jon</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '15, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/ad7df450e9cbc9f0133014ef50c8bcf0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jon2709&#39;s gravatar image" />
<p><span>Jon2709</span><br />
<span class="score" title="36 reputation points">36</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jon2709 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46364" class="comments-container">
<span id="46366"></span>
<div id="comment-46366" class="comment">
<div id="post-46366-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>I wouldn't read too much into "the future of areas" - it doesn't really have much bearing on OSM as it is now. There is no area datatype, and you can't rely on closed ways having an "area=yes" tag.</p>
</div>
<div id="comment-46366-info" class="comment-info">
<span class="comment-age">(03 Nov '15, 13:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46386"></span>
<div id="comment-46386" class="comment">
<div id="post-46386-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have now noticed that the majority of these issues have now been resolved since I posted. The Bulgaria.osm has been updated and now all forests are importing into ESRI.</p>
<p>Thank you for the updates!!</p>
<p>I am working on Eastern Europe and would be very glad to share any issues that I come across to help improve the quality of the data.</p>
<p>Please let me know how I should post these issues.</p>
<p>Best</p>
<p>Jon</p>
</div>
<div id="comment-46386-info" class="comment-info">
<span class="comment-age">(04 Nov '15, 15:56)</span> <span class="comment-user userinfo">Jon2709</span>
</div>
</div>
<span id="46387"></span>
<div id="comment-46387" class="comment">
<div id="post-46387-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That depends on the kind of issue. If you spot a specific mistake, you're best of making a "Note" (available on the main website, right hand side of the map) describing the problem. If it is something more general, a good plpace to start might be the country specific mailing list <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists#Country-Specific_Lists">https://wiki.openstreetmap.org/wiki/Mailing_lists#Country-Specific_Lists</a> or forum <a href="http://forum.openstreetmap.org/">http://forum.openstreetmap.org/</a></p>
</div>
<div id="comment-46387-info" class="comment-info">
<span class="comment-age">(04 Nov '15, 16:06)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-46364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46364-form-container" class="comment-form-container">
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

