+++
type = "question"
title = "How to extract partial data for large regions ?"
description = '''I&#x27;d like to greate an overview map of Europe, from Iceland to Greece, suitable for offline viewing. What are my options to get e.g.   all shoreline all national boundaries all big cities &amp;gt;100.000 inhabitants mayor waterways  mayor roads ?  The dataset is to be extracted once, it is intended as an...'''
date = "2010-08-27T17:21:00Z"
lastmod = "2010-09-08T07:14:00Z"
weight = 713
keywords = [ "download", "overview", "extract", "api", "export" ]
aliases = [ "/questions/713" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract partial data for large regions ?](/questions/713/how-to-extract-partial-data-for-large-regions)

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
<span id="post-713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-713-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to greate an overview map of Europe, from Iceland to Greece, suitable for offline viewing.</p>
<p>What are my options to get e.g.</p>
<ul>
<li>all shoreline</li>
<li>all national boundaries</li>
<li>all big cities &gt;100.000 inhabitants</li>
<li>mayor waterways</li>
<li>mayor roads ?</li>
</ul>
<p>The dataset is to be extracted once, it is intended as an overview, not as a current (up-to-date) map. Besides that, shorelines hopefully do not change as much as to warrant an update on a map of Europe-scale ;-)</p>
<p>I'd prefer to have tha map data in a vectorized form so that I can use e.g. mapnik to render this data for any desired screen size and resolution myself. That XML format that one can get from API/ROMA/TRAPI seems fine.</p>
<p>I learned that many such projects start with downloading planet.osm and extracting data, but I feel that planet.osm and its unpacking process uses more harddisk space than I am able to commit to this process.</p>
<p>I tried the API with bbox=???? and tile=??? but this sems to return all available data within the reach of the specified bounding box/tile. Further, using the API with tile=??? won't work with tiles of eg. zoomlevel 3 that would be needed to make a nice overview.</p>
<p>My problem is that I don't want all of the detail data if possible, but also that I want to cover large regions. Thus, even downloading all of the "regional" extracts from geofabrik.de or <a href="http://cloudmade.com">cloudmade.com</a> is overkill because I'd have to throw away most of the data.</p>
<p>Thank you for any hints</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-overview" rel="tag" title="see questions tagged &#39;overview&#39;">overview</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '10, 17:21</strong></p>
<img src="https://secure.gravatar.com/avatar/6cfb88a463b8a6a51176196f74a0de58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="uuser&#39;s gravatar image" />
<p><span>uuser</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="uuser has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '10, 07:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/278e1af65e82993efd0ba7bbbacf6435?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spaetz&#39;s gravatar image" />
<p><span>spaetz</span><br />
<span class="score" title="853 reputation points">853</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span></p>
</div>
</div>
<div id="comments-container-713" class="comments-container">
&#10;</div>
<div id="comment-tools-713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-713-form-container" class="comment-form-container">
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

<span id="715"></span>

<div id="answer-container-715" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-715-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Extracting data from a planet file does not require unpacking it first. Indeed you could download, unpack, and filter the planet file in one step like so:</p>
<pre><code>wget -O- http://planet.openstreetmap.org/planet-latest.osm.bz2 | bzcat | osmosis --rx - &lt;filter args here&gt; --wx my-compressed-output.osm.gz</code></pre>
<p>Your real problem is that not only do you want filtered data, you ideally want simplified data - for your purpose, having a country boundary in 100,000 points is a waste of space and processing time. Sadly there are no simple mechanisms for simplifying OSM data in that way.</p>
<p>Are you sure that you need OSM at all? Have a look at the <a href="http://naturalearthdata.com">Natural Earth</a> data set, which has administrative borders, populated places, and more, in different resolutions to choose from, and comes without any license restrictions (public domain).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '10, 18:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-715" class="comments-container">
&#10;</div>
<div id="comment-tools-715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-715-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="714"></span>

<div id="answer-container-714" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-714-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download data with specific tags using the <a href="http://wiki.openstreetmap.org/wiki/XAPI">Extended API (XAPI)</a>, which allows downloads covering a much larger area than the main API. XAPI only supports one set of filters per download, so you will need several XAPI queries to get all the data you're interested in. If you need all the data in a single file, you can merge the files using <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '10, 17:31</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-714" class="comments-container">
<span id="729"></span>
<div id="comment-729" class="comment">
<div id="post-729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I doubt XAPI is a practical way for downloading data for such large areas. There's limit of how much data you can download, so you'll be forced to split the download area into smaller tiles and then re-merge them into a single dataset. Use cases like the one described in the question is one of the thing sorely missing in the OSM. One way on how such problems would be easier to solve would be to provide smaler OSM extracts in a lat/long grid. You could then pick and choose which "tiles" you'd need and then merge them using tools like osmosis.</p>
</div>
<div id="comment-729-info" class="comment-info">
<span class="comment-age">(01 Sep '10, 18:59)</span> <span class="comment-user userinfo">Breki</span>
</div>
</div>
<span id="751"></span>
<div id="comment-751" class="comment">
<div id="post-751-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>XAPI can help to a large degree. For example, getting all city names within a lat/lon bounding box is pretty nice and easy with it. But what he wants will still require merging/filtering in any case...</p>
</div>
<div id="comment-751-info" class="comment-info">
<span class="comment-age">(08 Sep '10, 07:14)</span> <span class="comment-user userinfo">spaetz</span>
</div>
</div>
</div>
<div id="comment-tools-714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-714-form-container" class="comment-form-container">
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

