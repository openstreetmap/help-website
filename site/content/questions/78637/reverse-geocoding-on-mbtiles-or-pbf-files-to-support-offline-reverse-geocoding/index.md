+++
type = "question"
title = "Reverse geocoding on mbtiles or pbf files to support offline reverse geocoding"
description = '''I know it seems this is an idiot idea, but I just want to find a way to support reverse geocoding on an offline map for mobile. Currently, I successfully load pbf files of a specific area that were got from a large mbtiles file on server (using xyz url, e.g. https://myserver.com/data/14/13047/7696.p...'''
date = "2021-02-03T10:20:00Z"
lastmod = "2021-02-04T08:43:00Z"
weight = 78637
keywords = [ "mbtiles", "reversegeocoding", "pbf", "offlinemaps" ]
aliases = [ "/questions/78637" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse geocoding on mbtiles or pbf files to support offline reverse geocoding](/questions/78637/reverse-geocoding-on-mbtiles-or-pbf-files-to-support-offline-reverse-geocoding)

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
<span id="post-78637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78637-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I know it seems this is an idiot idea, but I just want to find a way to support reverse geocoding on an offline map for mobile.</p>
<p>Currently, I successfully load pbf files of a specific area that were got from a large <strong>mbtiles</strong> file on server (using <strong>xyz</strong> url, e.g. <a href="https://myserver.com/data/14/13047/7696.pbf)">https://myserver.com/data/14/13047/7696.pbf)</a> and then able to render the offline map on a mobile device with these vector tiles.</p>
<p>Now, I want to find a way to allow user to save the POI of a specific coordinate which already showed on the map. But the POI was rendered by mapbox gl so I can't get data from it.</p>
<p>Is it possible to read information from mbtiles or pbf files? Because I think they have all needed information. Or may you advise some other way to achieve offline reverse geocoding?</p>
<p>I found that ArcGis have something similar (<a href="https://developers.arcgis.com/android/kotlin/sample-code/offline-geocode/)">https://developers.arcgis.com/android/kotlin/sample-code/offline-geocode/)</a> that they call <strong>locator files</strong>, but it seems I must use these tiles server instead of my own tiles server.</p>
<p>Thank you so much!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '21, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/611ff06dfd6b8165defd20ce36a68fab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bahung1221&#39;s gravatar image" />
<p><span>bahung1221</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bahung1221 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '21, 07:22</strong> </span></p>
</div>
</div>
<div id="comments-container-78637" class="comments-container">
&#10;</div>
<div id="comment-tools-78637" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78637-form-container" class="comment-form-container">
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

<span id="78639"></span>

<div id="answer-container-78639" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78639-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Is it possible to read information from mbtiles or pbf files?</p>
</blockquote>
<p>Yes, it is. Your favourite programming language will probably have a protobuf decoder, which you can use to extract data from the pbf vector tile (<a href="https://github.com/mapbox/vector-tile-spec).">https://github.com/mapbox/vector-tile-spec).</a> You can then reconstitute the geometries and the tags from here.</p>
<p>I've done this successfully in the past (in Swift for iOS) and it's reasonably easy. But you do need to know your way around the vector tile format.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '21, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-78639" class="comments-container">
<span id="78656"></span>
<div id="comment-78656" class="comment">
<div id="post-78656-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Glad to hear it's possible, so I just need to determine the pbf file that contain specific POI from coordinate, and then I will able to get all the tags from it.</p>
<p>I will try it, thank you so much!</p>
</div>
<div id="comment-78656-info" class="comment-info">
<span class="comment-age">(04 Feb '21, 07:54)</span> <span class="comment-user userinfo">bahung1221</span>
</div>
</div>
<span id="78658"></span>
<div id="comment-78658" class="comment">
<div id="post-78658-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No problem. Do come back here if you encounter any issues.</p>
</div>
<div id="comment-78658-info" class="comment-info">
<span class="comment-age">(04 Feb '21, 08:43)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78639-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78641"></span>

<div id="answer-container-78641" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78641-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/mapbox/carmen/">https://github.com/mapbox/carmen/</a> can index data from geojson or mbtiles and use mbtiles as storage. The backend has an abstraction and anything following the <a href="https://github.com/mapbox/tilelive#awesome-tilelive-modules">https://github.com/mapbox/tilelive#awesome-tilelive-modules</a> API standard can be used, e.g. locally stored mbtile files.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '21, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-78641" class="comments-container">
&#10;</div>
<div id="comment-tools-78641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78641-form-container" class="comment-form-container">
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

