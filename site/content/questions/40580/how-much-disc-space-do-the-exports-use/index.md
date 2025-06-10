+++
type = "question"
title = "How much disc space do the exports use?"
description = '''I need to have a local tile server set up because you guys block MOBAC, and I need offline maps for geocaching. (These are for my consumption, and I don&#x27;t need uninterrupted service. But it&#x27;s also nice to be able to point Leaflet at them, and maybe tweak them. And I do need tiles for offline use, fo...'''
date = "2015-01-24T21:09:00Z"
lastmod = "2015-01-27T14:19:00Z"
weight = 40580
keywords = [ "planet", "extract", "osm2pgsql", "osmosis" ]
aliases = [ "/questions/40580" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How much disc space do the exports use?](/questions/40580/how-much-disc-space-do-the-exports-use)

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
<span id="post-40580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40580-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to have a local tile server set up because you guys block MOBAC, and I need offline maps for geocaching. (These are for my consumption, and I don't need uninterrupted service. But it's also nice to be able to point Leaflet at them, and maybe tweak them. And I <em>do</em> need tiles for offline use, for both Cachebox and Cachewolf.)</p>
<p>Now, I’ve imported Belgium, to try this out, and the entire disc use is about 8 GiB after installing everything needed, where /var/lib/postgresql is about 5½ GiB. I do not have unlimited space here, only about (currently) 16 GiB more. (I could possibly try to get this set up on another box though I'd need space estimates there too. It could probably do 400 GB.)</p>
<p>I have two ways I can go forward from here:</p>
<p>① drop DB, recreate DB, import Europe extract from Geofabrik</p>
<p>② combine NL/BE/LU/DE/AT/CH extracts where I need them</p>
<p>The problems here are:</p>
<p>osm2pgsql does not want to do ②; I’m being told to combine the extracts with osmosis before importing. However, how do I keep the combination up-to-date later?</p>
<p>How much disc space would I need for ① ? I assume I can then throw the files from <a href="http://download.geofabrik.de/europe-updates/000/000/">http://download.geofabrik.de/europe-updates/000/000/</a> to osm2pgsql to keep it updated?</p>
<p>Could I possibly import just the Europe changesets in the ② scenario, too?</p>
<p>osm2pgsql works. I didn’t use osmosis yet, and I don’t quite see what parts of its functionality I need for all this (GIS newbie here).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '15, 21:09</strong></p>
<img src="https://secure.gravatar.com/avatar/4a1f42a59e40446158ce872818a963a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mirabilos&#39;s gravatar image" />
<p><span>mirabilos</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mirabilos has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '15, 12:55</strong> </span></p>
</div>
</div>
<div id="comments-container-40580" class="comments-container">
<span id="40582"></span>
<div id="comment-40582" class="comment">
<div id="post-40582-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hm, <a href="http://www.grulic.org.ar/~mdione/glob/posts/osm-planet-importing-and-rendering-times/">this</a> sounds like I need 200-300 GiB total for Europe uncut, and to stay away from flat nodes due to lack of upgradability. Still, the question stays open, in case someone else has better figures, and (more importantly) instructions/recommendations.</p>
</div>
<div id="comment-40582-info" class="comment-info">
<span class="comment-age">(24 Jan '15, 22:02)</span> <span class="comment-user userinfo">mirabilos</span>
</div>
</div>
</div>
<div id="comment-tools-40580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40580-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="40586"></span>

<div id="answer-container-40586" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40586-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Flat nodes don't impact upgradability but their benefit is greatest for full planet imports.</p>
<p>Since you do not need a continuously running tile server - you can afford downtimes while updating - the most space-efficient way to do what you want is</p>
<ol>
<li>if your area of interest is rectangular, goto 2; else determine the area you want and create a "poly" file for it (e.g. draw polygon in josm, save as .osm, use osm2poly.pl - or use another method)</li>
<li>download europe-latest.osm.pbf from Geofabrik</li>
<li>use osmosis (or osmcut or osm-history-splitter) to cut out the area of interest from the Europe file</li>
<li>import the resulting file with osm2pgsql using the <code>--slim</code> and <code>--drop</code> options which leads to a non-updatable database and makes the database unusable during import</li>
<li>whenever you want to update, repeat steps 1-4.</li>
</ol>
<p>Alternatively, if you <em>do</em> want uninterrupted service, follow steps 1-3 above and then</p>
<ol>
<li>import the resulting file with osm2pgsql using <code>--slim</code></li>
<li>when you want to update, repeat steps 1-3 above and then</li>
<li>use osmosis with the <code>--derive-change</code> option to compute the difference between the new file of interest and the last one and save to an .osc file</li>
<li>use osm2pgsql with <code>--append</code> to load that .osc file</li>
</ol>
<p>There are other options, like consuming the Europe diffs from the Geofabrik site, but that would lead to unnecessary data in your database that you would have to remove from time to time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '15, 00:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '15, 09:04</strong> </span></p>
</div>
</div>
<div id="comments-container-40586" class="comments-container">
<span id="40592"></span>
<div id="comment-40592" class="comment">
<div id="post-40592-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you want to trim diffs to your poly of bounding box before applying, have a look at trim_osc.py in <a href="https://github.com/Zverik/regional">https://github.com/Zverik/regional</a> . That will greatly reduce database growth due to "out of area" updates.</p>
</div>
<div id="comment-40592-info" class="comment-info">
<span class="comment-age">(25 Jan '15, 09:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="40597"></span>
<div id="comment-40597" class="comment">
<div id="post-40597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, this mostly sounds like a plan. (Indeed, I don't need uninterrupted service.) But it seems I have no way to estimate the size? Also, “use osmosis to…” is still a bit hard to look through, I don't grok its documentation well. Mh. I'll wait a bit to see what other answers there are.</p>
</div>
<div id="comment-40597-info" class="comment-info">
<span class="comment-age">(25 Jan '15, 12:50)</span> <span class="comment-user userinfo">mirabilos</span>
</div>
</div>
<span id="40646"></span>
<div id="comment-40646" class="comment">
<div id="post-40646-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><code>osmosis --read-pbf in.osm.pbf --bbox left=a right=b top=c bottom=d --write-pbf out.pbf</code> is the command line for cutting out a rectangle, and <code>osmosis --read-pbf new.osm.pbf --read-pbf old.osm.pbf --derive-change --write-xml-change diff.osc.gz</code> is the command line for producing a diff.</p>
</div>
<div id="comment-40646-info" class="comment-info">
<span class="comment-age">(27 Jan '15, 09:11)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="40647"></span>
<div id="comment-40647" class="comment">
<div id="post-40647-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for this recipe. This was one of those recipes I was looking for actually :-)</p>
</div>
<div id="comment-40647-info" class="comment-info">
<span class="comment-age">(27 Jan '15, 14:19)</span> <span class="comment-user userinfo">nordie69</span>
</div>
</div>
</div>
<div id="comment-tools-40586" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40586-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40593"></span>

<div id="answer-container-40593" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40593-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In answer to "How much disc space would I need for ① ?", I suspect that 300Gb would be a bit low, currently. I don't have a Europe extract maintained currently, but when I last did (a couple of years ago) my recollection is that it needed 250-300Gb, so the requirement would be larger now.</p>
<p>However, I'm sure that someone must have more up to date figures.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '15, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-40593" class="comments-container">
<span id="40598"></span>
<div id="comment-40598" class="comment">
<div id="post-40598-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hm okay. Thanks for the estimate. (Maybe I'll just get another box to play mapserver.)</p>
</div>
<div id="comment-40598-info" class="comment-info">
<span class="comment-age">(25 Jan '15, 12:50)</span> <span class="comment-user userinfo">mirabilos</span>
</div>
</div>
<span id="40645"></span>
<div id="comment-40645" class="comment">
<div id="post-40645-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A world-wide planet needs about 450 GB in PostGIS, and the planet.osm.pbf is 27 GB. The europe.osm.pbf is about half that size so 250 GB will probably be sufficient. This is for an updatable <code>--slim</code> database; <code>--drop</code> should save quite a bit of that. All just a wild guess though since of course the relation between PBF size and database size is not necessarily constant.</p>
</div>
<div id="comment-40645-info" class="comment-info">
<span class="comment-age">(27 Jan '15, 09:09)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40593-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40594"></span>

<div id="answer-container-40594" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40594-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At the start of this you say "I need to have a local tile server set up because you guys block MOBAC, and I need offline maps for geocaching.".</p>
<p>I'm guessing that the issue here is lack of data coverage and cost of mobile data when you're out and about.</p>
<p>However, maybe it's worth taking a step back and asking if lots of individual map tiles is the best way to hold and display data? I don't know what you're displaying data on, but if it's a phone there are quite a few options (<a href="http://wiki.osm.org/wiki/OsmAnd">Osmand</a>'s offline layer may work for you if you're using an Android phone, and plenty of <a href="http://wiki.osm.org/wiki/Android#Android_software_supporting_OpenStreetMap">other options</a> are available).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '15, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-40594" class="comments-container">
<span id="40599"></span>
<div id="comment-40599" class="comment">
<div id="post-40599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The issue here is the price (and speed) of GPRS coverage in foreign countries, yes. I am using Cachebox for Windows Mobile which serves my Geocaching needs and also seems to be the best moving map application for Windows Mobile.</p>
</div>
<div id="comment-40599-info" class="comment-info">
<span class="comment-age">(25 Jan '15, 12:53)</span> <span class="comment-user userinfo">mirabilos</span>
</div>
</div>
</div>
<div id="comment-tools-40594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40594-form-container" class="comment-form-container">
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

