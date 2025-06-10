+++
type = "question"
title = "How can I export an section of map as an image using Overpass API?"
description = '''Hello. I have a coordinates of a place and I want to get a corresponding section of map as an image. I know that it possible in Overpass Turbo (&quot;Export&quot; button), but can I do this from my code using Overpass API for Python?'''
date = "2021-11-20T12:19:00Z"
lastmod = "2021-11-21T14:16:00Z"
weight = 82626
keywords = [ "overpassapi", "export" ]
aliases = [ "/questions/82626" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I export an section of map as an image using Overpass API?](/questions/82626/how-can-i-export-an-section-of-map-as-an-image-using-overpass-api)

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
<span id="post-82626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82626-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I have a coordinates of a place and I want to get a corresponding section of map as an image. I know that it possible in Overpass Turbo ("Export" button), but can I do this from my code using Overpass API for Python?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '21, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/fd6cb10eddbcafaab334ca88ca024cc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sertyhopss&#39;s gravatar image" />
<p><span>Sertyhopss</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sertyhopss has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '21, 12:20</strong> </span></p>
</div>
</div>
<div id="comments-container-82626" class="comments-container">
&#10;</div>
<div id="comment-tools-82626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82626-form-container" class="comment-form-container">
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

<span id="82637"></span>

<div id="answer-container-82637" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82637-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sertyhopss has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What overpass does when you export to an image, is to download individual tiles and place your query result on top. Since you do not seem to even need to export data, Overpass is the wrong tool. You can either download the individual tiles with Python and paste them together - see e.g. <a href="https://github.com/zverik/bigmap2">https://github.com/zverik/bigmap2</a> or <a href="https://github.com/geofabrik/GfStaticmap">https://github.com/geofabrik/GfStaticmap</a> for inspiration in PHP - or you can use a hosted "Static map" service (<a href="https://wiki.openstreetmap.org/wiki/Static_map_images).">https://wiki.openstreetmap.org/wiki/Static_map_images).</a> Whichever you choose, understand that you are using someone else's computing resources for this, and that you cannot use this massively without causing harm. So before you publish something that you expect to be very widely used, check with the operators of the respective servers you are relying on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '21, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82637" class="comments-container">
<span id="82639"></span>
<div id="comment-82639" class="comment">
<div id="post-82639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. I want to use this for my bachelor's thesis and for only one city, without publishing the program. It contains a factor analysis of traffic accidents at intersections. I have the database which include coordinates of crashes, time, weather, information about cars etc. Also I want to add information about road: tile, priorities, traffic lights, max speed and maybe something else. Most of this information i can get using queries to Overpass API, but not tiles. Thanks for links, I'll see it.</p>
</div>
<div id="comment-82639-info" class="comment-info">
<span class="comment-age">(21 Nov '21, 08:50)</span> <span class="comment-user userinfo">Sertyhopss</span>
</div>
</div>
<span id="82642"></span>
<div id="comment-82642" class="comment">
<div id="post-82642-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>@Serlyhopss I'd look at QGIS which can show tiles in the background (XYZ Tile layers) and pull data from OSM via Overpass-like queries (or just save the geojson from the queries). I do this all the time.</p>
</div>
<div id="comment-82642-info" class="comment-info">
<span class="comment-age">(21 Nov '21, 14:16)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82637" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82637-form-container" class="comment-form-container">
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

