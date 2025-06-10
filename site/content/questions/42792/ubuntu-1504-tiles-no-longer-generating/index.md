+++
type = "question"
title = "Ubuntu 15.04 - Tiles no longer generating"
description = '''I upgraded from Ubuntu 14.04 to 15.04 Friday (via 14.10 then 15.04) - and since my OSM tile server is not generating new tiles. Areas that already have had tiles generated work flawlessly, but if I &quot;pan&quot; around in Leaflet to areas I have not generated tiles for, no tiles are generated, and looking a...'''
date = "2015-05-01T19:11:00Z"
lastmod = "2015-05-04T16:52:00Z"
weight = 42792
keywords = [ "tileserver", "postgresql", "15.04", "postgis", "ubuntu" ]
aliases = [ "/questions/42792" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Ubuntu 15.04 - Tiles no longer generating](/questions/42792/ubuntu-1504-tiles-no-longer-generating)

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
<span id="post-42792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42792-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I upgraded from Ubuntu 14.04 to 15.04 Friday (via 14.10 then 15.04) - and since my OSM tile server is not generating new tiles. Areas that already have had tiles generated work flawlessly, but if I "pan" around in Leaflet to areas I have not generated tiles for, no tiles are generated, and looking at glances I do not see any of the tile generation services being kicked off. I would rather not do the 36 hour database rebuild for another 6 months as map data is still relatively current for most areas.</p>
<p>Had 2 questions:</p>
<ol>
<li>Ubuntu 15.04 uses systemd now for services called upon on boot. Could the instructions I followed to set up the tile server for 14.04 need updating to reflect systemd now being used instead of init.d?</li>
<li>When upgrading, Ubuntu "automatically removed no longer needed packages" including Boost, Mapnick, and some other actually needed packages. I re-downloaded all the packages in the steps listed <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a> - but also in the process I noticed my PostgreSQL was updated from 9.3 to 9.4 - thus I did a apt-get postgresql-9.4-postgis-2.1 - I recall somewhere mentioned I may have to do some extra steps due to upgrading PostgreSQL?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-15.04" rel="tag" title="see questions tagged &#39;15.04&#39;">15.04</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '15, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/1afe4bf83008befdcf7bdf5c6abfa195?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f00dl3a&#39;s gravatar image" />
<p><span>f00dl3a</span><br />
<span class="score" title="171 reputation points">171</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f00dl3a has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '15, 23:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42792" class="comments-container">
&#10;</div>
<div id="comment-tools-42792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42792-form-container" class="comment-form-container">
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

<span id="42877"></span>

<div id="answer-container-42877" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42877-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aseerel4c26 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>upgraded PostgreSQL by completely removing and re-installing the applicaiton. Re-created databases. Re-downloaded the PBF and re-built the tile server database. Resolved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '15, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/1afe4bf83008befdcf7bdf5c6abfa195?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f00dl3a&#39;s gravatar image" />
<p><span>f00dl3a</span><br />
<span class="score" title="171 reputation points">171</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f00dl3a has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-42877" class="comments-container">
&#10;</div>
<div id="comment-tools-42877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42877-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42794"></span>

<div id="answer-container-42794" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42794-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Upon a PostgreSQL upgrade, Ubuntu will normally run the new version in parallel to the old (e.g. 9.4 on port 5433, p.3 on port 5432 or so). Your message does not contain enough information to help you; "tiles not rendering" could be caused by a large variety of issues. Is renderd running? If not, start it by hand. Does it start? If not, check why and eliminate the problem. If renderd is running, check the Apache error log - can mod_tile successfully send its request to renderd? Can renderd successfully talk to the database? Check the PostgreSQL logs. Run renderd in foreground mode (-f flag) to see debug output and let that inform your further bug hunting. This kind of complicated debugging might be better suited to IRC.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '15, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42794" class="comments-container">
&#10;</div>
<div id="comment-tools-42794" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42794-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42797"></span>

<div id="answer-container-42797" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42797-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I need to at least recompile things as Boost is now a newer version. It appears like it was looking for an old version of Boost when I ran renderd -f. Doing that now, but found another issue.</p>
<p>I am following the instructions at <a href="http://stackoverflow.com/questions/28788653/migrating-from-postgresql-9-3-to-9-4-postgis">http://stackoverflow.com/questions/28788653/migrating-from-postgresql-9-3-to-9-4-postgis</a> as PostgreSQL on Ubuntu 15.04 is version 9.4. For some reason, when running pg_config --pkglibdir it returns /usr/lib/postgresql/9.3/lib, even though psql --version returns 9.4.1. I created a symbolic link, sudo ln -s /usr/lib/postgresql/9.4/lib/postgis-2.1.so /usr/lib/postgresql/9.3/lib , but now in rendered I am getting the error "incompatible library "/usr/lib/postgresql/9.3/lib/postgis-2.1.so" version mismatch DETAIL Server is version 9.3, library is version 9.4. This doesn't make sense as the --version returns 9.4.1.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '15, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/1afe4bf83008befdcf7bdf5c6abfa195?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f00dl3a&#39;s gravatar image" />
<p><span>f00dl3a</span><br />
<span class="score" title="171 reputation points">171</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f00dl3a has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '15, 11:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-42797" class="comments-container">
&#10;</div>
<div id="comment-tools-42797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42797-form-container" class="comment-form-container">
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

