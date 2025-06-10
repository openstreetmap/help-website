+++
type = "question"
title = "Previous versions of the map"
description = '''Is there a way to access and export previous versions of the map, for a specific country and date? '''
date = "2021-06-14T12:49:00Z"
lastmod = "2022-08-02T12:37:00Z"
weight = 80572
keywords = [ "export", "retroactive" ]
aliases = [ "/questions/80572" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Previous versions of the map](/questions/80572/previous-versions-of-the-map)

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
<span id="post-80572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to access and export previous versions of the map, for a specific country and date?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-retroactive" rel="tag" title="see questions tagged &#39;retroactive&#39;">retroactive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jun '21, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e48827c9be2e2c65528c7b2ec8651abc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mert%20Su&#39;s gravatar image" />
<p><span>Mert Su</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mert Su has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80572" class="comments-container">
&#10;</div>
<div id="comment-tools-80572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80572-form-container" class="comment-form-container">
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

<span id="80573"></span>

<div id="answer-container-80573" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80573-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Previous versions of the <em>data</em>, yes; previous versions of the <em>map</em>, no.</p>
<p>This means you can get the data but making it into a map is your own responsibility. For getting the data for a specific point in time,</p>
<ol>
<li>download "history planet" file from <a href="https://planet.openstreetmap.org/pbf/full-history/">https://planet.openstreetmap.org/pbf/full-history/</a> or alternatively download a regional history file from download.geofabrik.de (that server has history files for individual countries but you need to log in with your OSM account to access them)</li>
<li>use the <code>osmium</code> command line tool (see <a href="https://docs.osmcode.org/osmium/latest/osmium-time-filter.html)">https://docs.osmcode.org/osmium/latest/osmium-time-filter.html)</a> to extract the data for one specific point in time from the history file</li>
</ol>
<p>If you then want to make a map from the resulting file, you'd basically follow standard instructions for a tile server setup e.g. switch2osm.org.</p>
<p>If you want to generate a map that looks exactly like the map on OSM looked at the time, you will want to check out a suitable older version of the <code>openstreetmap-carto</code> map style.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '21, 12:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-80573" class="comments-container">
<span id="80574"></span>
<div id="comment-80574" class="comment">
<div id="post-80574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, have a nice day.</p>
</div>
<div id="comment-80574-info" class="comment-info">
<span class="comment-age">(14 Jun '21, 14:24)</span> <span class="comment-user userinfo">Mert Su</span>
</div>
</div>
</div>
<div id="comment-tools-80573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80573-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85276"></span>

<div id="answer-container-85276" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85276-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use overpass turbo (<a href="https://overpass-turbo.eu/).">https://overpass-turbo.eu/).</a> Create a bounding box over your desired area, then use the following code and/or use the examples and resources on the webpage to tailor the code to isolate the data that you want (the below code loads all drinking water objects as they existed on 2016-01-01). Export the data to kml and upload to qgis!</p>
<p>[date:"2016-01-01T00:00:00Z"]; ( node [amenity=drinking_water] ({{bbox}}); way [amenity=drinking_water] ({{bbox}}); relation [amenity=drinking_water] ({{bbox}}); ); out body;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '22, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/8eaf4372b3a04e79d9701a75f36c383f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lee1234566666&#39;s gravatar image" />
<p><span>lee1234566666</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lee1234566666 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85276" class="comments-container">
&#10;</div>
<div id="comment-tools-85276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85276-form-container" class="comment-form-container">
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

