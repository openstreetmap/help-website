+++
type = "question"
title = "calculating travel time between points using historical planet OSM"
description = '''I am planning to calculate annual trends in travel time between series of two points in my country of interest. I will be working with R using an &quot;osmdata&quot; package. I realized that historical OSM data are provided with the planet level only. So, I need to crop the huge planet level OSM to the countr...'''
date = "2020-07-08T19:58:00Z"
lastmod = "2020-07-09T19:29:00Z"
weight = 75606
keywords = [ "planet", "osmdata", "r", "traveltime", "openhistoricalmap" ]
aliases = [ "/questions/75606" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [calculating travel time between points using historical planet OSM](/questions/75606/calculating-travel-time-between-points-using-historical-planet-osm)

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
<span id="post-75606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75606-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am planning to calculate annual trends in travel time between series of two points in my country of interest. I will be working with R using an "osmdata" package. I realized that historical OSM data are provided with the planet level only. So, I need to crop the huge planet level OSM to the country size and import them into R. Now, I am following a useful post <a href="https://www.r-spatial.org/2017/07/14/large_scale_osm_in_r">link text</a>. But, it doesn't work, actually from executing SQL codes part in PgAdmin.</p>
<p>So, my first question is that there is anyone familiar with this issue, or know an easier or efficient way to utilize historical OSM via R.</p>
<p>Second, I am curious whether even if I can import the cropped OSM, "osmdata" package is applicable to the historical OSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-osmdata" rel="tag" title="see questions tagged &#39;osmdata&#39;">osmdata</span> <span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span> <span class="post-tag tag-link-traveltime" rel="tag" title="see questions tagged &#39;traveltime&#39;">traveltime</span> <span class="post-tag tag-link-openhistoricalmap" rel="tag" title="see questions tagged &#39;openhistoricalmap&#39;">openhistoricalmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '20, 19:58</strong></p>
<img src="https://secure.gravatar.com/avatar/54c0e607f76a604d86c3659668f31482?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KCKim&#39;s gravatar image" />
<p><span>KCKim</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KCKim has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75606" class="comments-container">
&#10;</div>
<div id="comment-tools-75606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75606-form-container" class="comment-form-container">
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

<span id="75607"></span>

<div id="answer-container-75607" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75607-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The download.geofabrik.de size typically has country extracts for the 1st Jan of each year going back to 2014 (but may vary by country).</p>
<p>For more flexibility, get the "history extract" for your country from download.geofabrik.de (requires OSM login), and use the "osmium" command line utility (requires Linux) to create snapshots from that for arbitrary points in time.</p>
<p>The link you posted does not seem to apply to history data at all, but to standard planet-wide imports. If you wanted to solve your issue without resorting to Geofabrik downloads, you would download the history planet file from <a href="https://planet.openstreetmap.org/pbf/full-history/history-latest.osm.pbf">https://planet.openstreetmap.org/pbf/full-history/history-latest.osm.pbf</a> and then first crop it with the osmium tool (not osmosis - it doesn't do history files) and then take a snapshot for a given point in time, again with the osmium utility.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '20, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-75607" class="comments-container">
<span id="75628"></span>
<div id="comment-75628" class="comment">
<div id="post-75628-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your quick reply Frederik.</p>
<p>For more clarity, the countries of my interest are India and Nepal. I have many point information (lat long) and so simply want to calculate travel times between the points hopefully via R. The time period is between 2013 and 2016 and I only need one travel time variable for each year. So, I might be able to use the travel time information as of the end of each year, considering the quality of OSM in Nepal in the earlier year (particularly the quality of 2013 information).</p>
<p>Do you still think that the history planet file is suitable for my work? (I already have downloaded it) And, do you mean that I can crop the file into the areas of the countries with the osmium tool, and take a snapshot at the time I need? And, then I can calculate the travel time, using which program?</p>
</div>
<div id="comment-75628-info" class="comment-info">
<span class="comment-age">(09 Jul '20, 19:17)</span> <span class="comment-user userinfo">KCKim</span>
</div>
</div>
<span id="75629"></span>
<div id="comment-75629" class="comment">
<div id="post-75629-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you want to compute routes from Nepal into India and vice versa, then you must use the history planet file. Use osmium to crop it to the area of interest (just once), and then use osmium again (once for each year) to create a snapshot for that year. Then use a routing engine, e.g. Graphhopper which is easy to install, let it load the file for one particular year, and compute all your travel times. Then delete the routing graph, and re-import with the next year, and so on.</p>
<p>PS I am informed that osmium does not require Linux, you can run it on Windows if you can manage to compile it.</p>
</div>
<div id="comment-75629-info" class="comment-info">
<span class="comment-age">(09 Jul '20, 19:29)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75607-form-container" class="comment-form-container">
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

