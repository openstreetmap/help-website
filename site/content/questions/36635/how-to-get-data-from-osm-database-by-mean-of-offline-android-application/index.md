+++
type = "question"
title = "how to get data from OSM database by mean of  offline android application"
description = '''I&#x27;am planing to create an offline android application , i&#x27;am wondring how to get data from the openstreetmap database also how to show the map on the smartphone . any links for android api will help .'''
date = "2014-09-05T19:42:00Z"
lastmod = "2014-09-05T22:17:00Z"
weight = 36635
keywords = [ "android", "osmdroid", "osm" ]
aliases = [ "/questions/36635" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to get data from OSM database by mean of offline android application](/questions/36635/how-to-get-data-from-osm-database-by-mean-of-offline-android-application)

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
<span id="post-36635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36635-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'am planing to create an offline android application , i'am wondring how to get data from the openstreetmap database also how to show the map on the smartphone . any links for android api will help .</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '14, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/26ceead6052b5d3807baaa723b9fa7a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abogaseem&#39;s gravatar image" />
<p><span>abogaseem</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abogaseem has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Sep '14, 19:43</strong> </span></p>
</div>
</div>
<div id="comments-container-36635" class="comments-container">
<span id="36640"></span>
<div id="comment-36640" class="comment">
<div id="post-36640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here are a <a href="https://help.openstreetmap.org/search/?q=create+android&amp;Submit=search&amp;t=question">bunch of previous similar questions</a> - some of the answers might be relevant.</p>
<p>As ever the best way to solve the problem depends on what you want to do (Vector or Raster? Based on pre-rendered tiles or drawn on the fly? With overlaid points of interest or not?). Without more information about that it's difficult to give a more specific answer.</p>
</div>
<div id="comment-36640-info" class="comment-info">
<span class="comment-age">(05 Sep '14, 22:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36635-form-container" class="comment-form-container">
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

<span id="36639"></span>

<div id="answer-container-36639" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36639-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Two nearly identical questions from you: <a href="https://help.openstreetmap.org/questions/36638/how-do-i-create-my-region-database-by-mean-of-osm-for-my-android-application">https://help.openstreetmap.org/questions/36638/how-do-i-create-my-region-database-by-mean-of-osm-for-my-android-application</a></p>
<p>The way that you can get your own OSM data into the OsmAnd app is to download the extract file for your region from <a href="http://download.geofabrik.de">http://download.geofabrik.de</a> These files are generated daily from the OSM database.</p>
<p>Then convert/process the data as your app needs to work well. OsmAnd uses a program they created called OsmAndMapCreator which you can download from their home page at <a href="http://osmand.net">http://osmand.net</a></p>
<p>For you own app you'll have to decide what data from OSM you want and what schema your on phone database will use and then create that from the extract file for your region(s) of interest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '14, 20:48</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-36639" class="comments-container">
&#10;</div>
<div id="comment-tools-36639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36639-form-container" class="comment-form-container">
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

