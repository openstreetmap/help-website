+++
type = "question"
title = "How to &quot;update&quot; GIS tile data?"
description = '''I previously had downloaded a metro extract from the OSM metro extracts page, and now found a site that offers individual state extract PBFs. I followed the instructions at http://switch2osm.org/loading-osm-data/ and for some reason the new data I imported, while it did not error out or anything and...'''
date = "2014-07-17T19:46:00Z"
lastmod = "2014-07-17T23:32:00Z"
weight = 34945
keywords = [ "osm", "postgis", "tileserver" ]
aliases = [ "/questions/34945" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to "update" GIS tile data?](/questions/34945/how-to-update-gis-tile-data)

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
<span id="post-34945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34945-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I previously had downloaded a metro extract from the OSM metro extracts page, and now found a site that offers individual state extract PBFs. I followed the instructions at <a href="http://switch2osm.org/loading-osm-data/">http://switch2osm.org/loading-osm-data/</a> and for some reason the new data I imported, while it did not error out or anything and is taking up the additional space - is not displaying when I view my tile server. I did a rm -fr /var/lib/tile as well as service restarts on apache2 &amp; renderd, and after that didn't work even fully rebooted the machine. It's still stuck looking like it's "cached" the old tiles and isn't displaying the new "larger area" of data. In psql, I did a \dt and it shows the same # of tables and table names. The size of the database, again, has increased - was ~270 MBs and is now ~862 MBs - so the data IS in there, just not displaying. Do I have to drop the gis database and re-create it from the templates? Or is there an easier way to update this data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '14, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/339a2b5537b6a2b5a653fec032d191f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f00dl3&#39;s gravatar image" />
<p><span>f00dl3</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f00dl3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34945" class="comments-container">
&#10;</div>
<div id="comment-tools-34945" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34945-form-container" class="comment-form-container">
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

<span id="34949"></span>

<div id="answer-container-34949" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34949-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you use osm2pgsql with default settings by default it'll replace the previous data, so the fact that you're still seeing it is odd (if it's not tile or browser cache).</p>
<p>A bit of a long shot, but is it possible that you used a different database name this time and are still pointing at the old one?</p>
<p>You could try looking in the database with psql to see if the data that you're expecting to be there actually is. For example, I recently made a change to a local database to include an "industrial" column, and to check that the data was actually there I did:</p>
<pre><code>psql -c &quot;select osm_id,industrial from planet_osm_polygon where industrial = &#39;warehouse&#39;&quot; gis</code></pre>
<p>which returned for me</p>
<pre><code>  osm_id   | industrial 
-----------+------------
 280982430 | warehouse
 280982431 | warehouse
(2 rows)</code></pre>
<p>The osm_ids above are the way IDs that of the features concerned. You might want to select something that exists in your old set of data, and your new one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '14, 23:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-34949" class="comments-container">
&#10;</div>
<div id="comment-tools-34949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34949-form-container" class="comment-form-container">
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

