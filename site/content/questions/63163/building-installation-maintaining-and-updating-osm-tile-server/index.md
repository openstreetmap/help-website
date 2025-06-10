+++
type = "question"
title = "Building, Installation, Maintaining and Updating OSM Tile Server"
description = '''Hi Guys, So before I start - I have done a lot of research into this, but I always seem to get stuck at the same issue. Firstly, the setup: Hardware: Xeon D-1520 - 32GB - Hybrid SoftRaid 2x2tb + 2x480GB SSD  Software: Ubuntu Server 16.04 &quot;Xenial Xerus&quot; LTS The Problem: So - I&#x27;ve managed to get a OSM...'''
date = "2018-04-26T11:58:00Z"
lastmod = "2018-04-26T17:07:00Z"
weight = 63163
keywords = [ "rendering", "installation", "updating", "tileserver" ]
aliases = [ "/questions/63163" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Building, Installation, Maintaining and Updating OSM Tile Server](/questions/63163/building-installation-maintaining-and-updating-osm-tile-server)

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
<span id="post-63163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63163-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Guys, So before I start - I have done a lot of research into this, but I always seem to get stuck at the same issue.</p>
<p>Firstly, the setup:</p>
<p>Hardware: Xeon D-1520 - 32GB - Hybrid SoftRaid 2x2tb + 2x480GB SSD</p>
<p>Software: Ubuntu Server 16.04 "Xenial Xerus" LTS</p>
<p>The Problem:</p>
<p>So - I've managed to get a OSM tile server running by importing europe.osm.pbf by following an article here: <a href="https://www.linuxbabe.com/linux-server/openstreetmap-tile-server-ubuntu-16-04">https://www.linuxbabe.com/linux-server/openstreetmap-tile-server-ubuntu-16-04</a></p>
<p>Which got me as far as being able to render tiles and display them via a leaflet map, however, the problem is, that map is now out of date and i cant for the life of me figure out how to go about updating what is in the database currently.</p>
<p>So, 2 questions</p>
<ol>
<li>Is that guide linked above the recommended way to setup a tile server, if not, what would be the best guide?</li>
<li>If that guide is fine - how would one go about updating my current europe tiles to a more up to date version</li>
</ol>
<p>Please try to be as descriptive as possible as this is still a relatively new thing to me.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-updating" rel="tag" title="see questions tagged &#39;updating&#39;">updating</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '18, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/fa4e6fbb05a1a2a9d8ab31540b4ee391?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaza1994&#39;s gravatar image" />
<p><span>gaza1994</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaza1994 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63163" class="comments-container">
<span id="63178"></span>
<div id="comment-63178" class="comment">
<div id="post-63178-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just out of interest, how long did it take to do an "initial load" of Europe on that hardware?</p>
</div>
<div id="comment-63178-info" class="comment-info">
<span class="comment-age">(26 Apr '18, 15:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63179"></span>
<div id="comment-63179" class="comment">
<div id="post-63179-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>around 3-4 days (ish)</p>
</div>
<div id="comment-63179-info" class="comment-info">
<span class="comment-age">(26 Apr '18, 15:26)</span> <span class="comment-user userinfo">gaza1994</span>
</div>
</div>
<span id="63180"></span>
<div id="comment-63180" class="comment">
<div id="post-63180-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was worried about that - that's going to rule out "overnight updates" then, I think. "diff" based updates should be possible, but you'll want to start with an up to date server, though.</p>
</div>
<div id="comment-63180-info" class="comment-info">
<span class="comment-age">(26 Apr '18, 15:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63181"></span>
<div id="comment-63181" class="comment">
<div id="post-63181-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>starting fresh isnt an issue!</p>
<p>Is there a good guide on how the "diff updates" work and how it could be scheduled to do it?</p>
</div>
<div id="comment-63181-info" class="comment-info">
<span class="comment-age">(26 Apr '18, 15:38)</span> <span class="comment-user userinfo">gaza1994</span>
</div>
</div>
<span id="63182"></span>
<div id="comment-63182" class="comment">
<div id="post-63182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know of a good "how they work" guide but <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">this section</a> should tell you <em>what</em> you need to do.</p>
<p>I guess that there ought to be a page at switch2osm.org about it, but no-one has written that yet. Feel free to volunteer :)</p>
</div>
<div id="comment-63182-info" class="comment-info">
<span class="comment-age">(26 Apr '18, 15:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63163-form-container" class="comment-form-container">
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

<span id="63164"></span>

<div id="answer-container-63164" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63164-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd suggest doing applying updates as described <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">here</a> for 16.04 (or <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">here</a> for 18.04). Those use the same software as the switch2osm guides for <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">16.04</a> and <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">18.04</a>, which is mostly similar to the <a href="https://www.linuxbabe.com/linux-server/openstreetmap-tile-server-ubuntu-16-04">LinuxBabe</a> notes, with some default user acount changes. Some repositories are using forked versions to avoid user typing and editing where possible.</p>
<p>One thing to look out for - the forked version of <code>mod_tile</code> (which contains <code>openstreetmap-tiles-update-expire</code>) has been modified to use https destinations only for openstreetmap.org. The version you have installed may not do this. It's a one-line change in the code though, so easy to apply.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '18, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63164" class="comments-container">
&#10;</div>
<div id="comment-tools-63164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63164-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63165"></span>

<div id="answer-container-63165" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63165-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want a one-off update only, and not set up continuous updates, then you could also do the following:</p>
<ul>
<li>repeat your "osm2pgsql" step with a more recent data file, and then</li>
<li>(optionally) run render_list again to re-generate tiles</li>
</ul>
<p>While the update is running, you won't be able to generate tiles since the database is empty, but existing tiles will still display. If this is not acceptable to you, you could also import into a new database (say, "gis_new"), and when the import is complete, drop your old database and rename the new. If your disk space is not sufficient for two parallel databases, you can "drop table planet_osm_ways; drop table planet_osm_nodes; drop table planet_osm_rels;" on the old databases before you start, this will free over 50% of the disk space and make your old database still-working-but-un-updatable - not a problem since you plan to get rid of it anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '18, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63165" class="comments-container">
<span id="63174"></span>
<div id="comment-63174" class="comment">
<div id="post-63174-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>what would be a good method if i wanted to update often, say once a month?</p>
</div>
<div id="comment-63174-info" class="comment-info">
<span class="comment-age">(26 Apr '18, 14:48)</span> <span class="comment-user userinfo">gaza1994</span>
</div>
</div>
<span id="63177"></span>
<div id="comment-63177" class="comment">
<div id="post-63177-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"Once a month" is about the worst thing that you can do because it's already too seldom for using the "diff" based updates (updating a database with all the diffs for one month will likely take more time than loading the whole thing anew) and at the same time a bit frequent for doing full data loads. But still I'd go for the full data load - should just about be doable over night on your platform.</p>
</div>
<div id="comment-63177-info" class="comment-info">
<span class="comment-age">(26 Apr '18, 15:04)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="63183"></span>
<div id="comment-63183" class="comment">
<div id="post-63183-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so basically, Load EU - render the tiles, then when updating, nuke the database, re-import EU and force a re-render of all the tiles?</p>
</div>
<div id="comment-63183-info" class="comment-info">
<span class="comment-age">(26 Apr '18, 17:07)</span> <span class="comment-user userinfo">gaza1994</span>
</div>
</div>
</div>
<div id="comment-tools-63165" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63165-form-container" class="comment-form-container">
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

