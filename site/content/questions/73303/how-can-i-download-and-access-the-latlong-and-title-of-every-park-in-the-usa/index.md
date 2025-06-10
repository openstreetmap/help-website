+++
type = "question"
title = "How can I download and access the lat/long and title of every park in the USA?"
description = '''I am interested in building a database table of as many city parks as I can. Looking through the docs of Open Street Map, it looks like there are lots of big hammers, but the operation I want to accomplish is quite simple: I just want to get the name, city/state, and lat/long of as many city parks a...'''
date = "2020-03-02T05:47:00Z"
lastmod = "2020-03-02T21:33:00Z"
weight = 73303
keywords = [ "world", "database", "parks", "sql" ]
aliases = [ "/questions/73303" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I download and access the lat/long and title of every park in the USA?](/questions/73303/how-can-i-download-and-access-the-latlong-and-title-of-every-park-in-the-usa)

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
<span id="post-73303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73303-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am interested in building a database table of as many city parks as I can. Looking through the docs of Open Street Map, it looks like there are lots of big hammers, but the operation I want to accomplish is quite simple: I just want to get the name, city/state, and lat/long of as many city parks as I can.</p>
<p>How can I accomplish this with OSM data? Do I need to download the 40GB world and start filtering from there? I am comfortable working with SQL databases, if I could get it into that format I could perhaps query and trim down the extra data from there.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-world" rel="tag" title="see questions tagged &#39;world&#39;">world</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-parks" rel="tag" title="see questions tagged &#39;parks&#39;">parks</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '20, 05:47</strong></p>
<img src="https://secure.gravatar.com/avatar/4f974589b0cfe91a6b445dcf605cc176?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="broderick99&#39;s gravatar image" />
<p><span>broderick99</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="broderick99 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73303" class="comments-container">
<span id="73312"></span>
<div id="comment-73312" class="comment">
<div id="post-73312-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is not an answer to your question because you specified "with OSM data" but... you can query the USGS geonames server for features of class "park" and download the results per state. (I don't know of any way to do a single query for the whole country.)</p>
<p><a href="https://geonames.usgs.gov/apex/f?p=138:1:0:::::">https://geonames.usgs.gov/apex/f?p=138:1:0:::::</a></p>
<p>This query will likely only return a fraction of what OSM has, because all of the USGS parks were imported into OSM but many more parks have been manually mapped by OSM users.</p>
<p>Be aware that 1) coordinates are sometimes approximate 2) some info is out of date 3) the definition of "park" is quite inconsistent, as Frederik mentioned.</p>
</div>
<div id="comment-73312-info" class="comment-info">
<span class="comment-age">(02 Mar '20, 19:48)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="73315"></span>
<div id="comment-73315" class="comment">
<div id="post-73315-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's not got all the data for each entry, but there are bulk downloads for GNIS:</p>
<p><a href="https://www.usgs.gov/core-science-systems/ngp/board-on-geographic-names/download-gnis-data">https://www.usgs.gov/core-science-systems/ngp/board-on-geographic-names/download-gnis-data</a></p>
</div>
<div id="comment-73315-info" class="comment-info">
<span class="comment-age">(02 Mar '20, 21:33)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-73303" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73303-form-container" class="comment-form-container">
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

<span id="73304"></span>

<div id="answer-container-73304" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73304-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can start with this 7 GB file <a href="http://download.geofabrik.de/north-america/us-latest.osm.pbf">http://download.geofabrik.de/north-america/us-latest.osm.pbf</a> and then import that into a PostGIS database with the <code>osm2pgsql</code> utility. On import, you can provide a "style file" that says which objects you are interested in; if you use this to limit the import to features of interest - at first guess, probably "boundary" polygons you you can find out which city or state something is in, and "leisure" polygons so get the parks - then you should end up with a relatively slim database. Be sure to use the options <code>--slim</code> and <code>--drop</code> on import to save space, and use <code>--hstore</code> to ensure you have access to all tags you need. An even more surgical option would be pre-filtering the PBF file with the <code>osmosis</code> utility where you can not only specify keys but also key-value combinations that you want to import, yielding a much smaller PBF file to feed to <code>osm2pgsql</code>.</p>
<p>Be aware that the word "park" means many different things - anything between "a patch of green in the city" and "a state-sized highly protected natural reserve", and you might have to invest a little time to get the queries right. See the discussion starting at <a href="https://lists.openstreetmap.org/pipermail/talk-us/2018-January/018263.html">https://lists.openstreetmap.org/pipermail/talk-us/2018-January/018263.html</a> for some background.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '20, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73304" class="comments-container">
&#10;</div>
<div id="comment-tools-73304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73304-form-container" class="comment-form-container">
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

