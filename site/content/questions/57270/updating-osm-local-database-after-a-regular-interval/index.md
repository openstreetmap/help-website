+++
type = "question"
title = "Updating OSM local database after a regular interval"
description = '''I have setup a local version of OSM database using osm2pgsql in slim mode. Now I have the following tables planet_osm_lines planet_osm_nodes planet_osm_point planter_osm_roads planet_osm_ways I used the following command to migrate the database osm2pgsql -c -d DATABASE_NAME --slim planet.osm.pbf Eve...'''
date = "2017-07-25T16:33:00Z"
lastmod = "2017-07-26T07:45:00Z"
weight = 57270
keywords = [ "openstreetmap", "regions", "osm", "osm2pgsql", "planet_osm" ]
aliases = [ "/questions/57270" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Updating OSM local database after a regular interval](/questions/57270/updating-osm-local-database-after-a-regular-interval)

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
<span id="post-57270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57270-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have setup a local version of OSM database using osm2pgsql in slim mode. Now I have the following tables</p>
<p><code>planet_osm_lines</code></p>
<p><code>planet_osm_nodes</code></p>
<p><code>planet_osm_point</code></p>
<p><code>planter_osm_roads</code></p>
<p><code>planet_osm_ways</code></p>
<p>I used the following command to migrate the database</p>
<p><code>osm2pgsql -c -d DATABASE_NAME --slim planet.osm.pbf</code></p>
<p>Every thing is working fine. now I want to update these regularly and stay up to date with latest changes.</p>
<p>-- Since I am using rails is there a way to update these tables programatically? I mean I can run a schedulized job and it will update it with latest changes without having to download entire osm files?</p>
<p>-- Secondly since I am only interested in US, Canada and Mexico is there a way to fetch only these countries data?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-regions" rel="tag" title="see questions tagged &#39;regions&#39;">regions</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '17, 16:33</strong></p>
<img src="https://secure.gravatar.com/avatar/24fb9e633cb135d94e6a9b4cc4fc6d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aitizazk&#39;s gravatar image" />
<p><span>aitizazk</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aitizazk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57270" class="comments-container">
<span id="57279"></span>
<div id="comment-57279" class="comment">
<div id="post-57279-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://stackoverflow.com/questions/45310508/updating-osm-local-database-after-a-regular-interval-in-rails">https://stackoverflow.com/questions/45310508/updating-osm-local-database-after-a-regular-interval-in-rails</a></p>
</div>
<div id="comment-57279-info" class="comment-info">
<span class="comment-age">(26 Jul '17, 07:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57270-form-container" class="comment-form-container">
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

<span id="57271"></span>

<div id="answer-container-57271" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57271-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you've got a rendering server (which I'm assuming that you have) and are using mod_tile (which you may not be) then <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">this wiki page</a> might be useful. Even if you're not then you should be able to adapt the link to Zverik's "regional" scripts from there to cut down the updates that you apply to only North America.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '17, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-57271" class="comments-container">
&#10;</div>
<div id="comment-tools-57271" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57271-form-container" class="comment-form-container">
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

