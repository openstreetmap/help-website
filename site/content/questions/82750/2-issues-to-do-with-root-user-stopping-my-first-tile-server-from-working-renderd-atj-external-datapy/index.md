+++
type = "question"
title = "2 issues to do with &#x27;root&#x27; user stopping my first tile server from working (renderd atj external-data.py))"
description = '''Hi - I&#x27;ve been following good tutorials on switch2osm, linuxbabe on a clean ubuntu 18.04 build.  https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/ Help massively appreciated:  Issue 1 - &#x27;root&#x27; error when running scripts/get-external-data.py Issue 2 - &#x27;root&#x27; error when r...'''
date = "2021-12-04T10:28:00Z"
lastmod = "2021-12-05T12:08:00Z"
weight = 82750
keywords = [ "renderd" ]
aliases = [ "/questions/82750" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [2 issues to do with 'root' user stopping my first tile server from working (renderd atj external-data.py))](/questions/82750/2-issues-to-do-with-root-user-stopping-my-first-tile-server-from-working-renderd-atj-external-datapy)

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
<span id="post-82750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82750-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi - I've been following good tutorials on switch2osm, linuxbabe on a clean ubuntu 18.04 build. <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/</a></p>
<p>Help massively appreciated:</p>
<p>Issue 1 - 'root' error when running scripts/get-external-data.py Issue 2 - 'root' error when running sudo renderd -f -c /usr/local/etc/renderd.conf</p>
<p>error logs for 2 issues: <a href="https://pastebin.com/15gck0Pu">https://pastebin.com/15gck0Pu</a></p>
<p>my renderd config file:</p>
<pre><code>[renderd]
num_threads=2
tile_dir=/var/lib/mod_tile
stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input
font_dir=/usr/share/fonts
font_dir_recurse=true
&#10;[ajt]
URI=/hot/
TILEDIR=/home/renderaccount/src/mod_tile
XML=/home/renderaccount/src/openstreetmap-carto/mapnik.xml
HOST=MYPUBLICIPADRESS
TILESIZE=256
MAXZOOM=20</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '21, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/20e950eb7a5f2c52377f26a49dd71e06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kieran&#39;s gravatar image" />
<p><span>kieran</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kieran has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Dec '21, 10:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-82750" class="comments-container">
&#10;</div>
<div id="comment-tools-82750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82750-form-container" class="comment-form-container">
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

<span id="82751"></span>

<div id="answer-container-82751" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82751-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't run "<code>renderd -f -c /usr/local/etc/renderd.conf</code>" as root. Use the non-root username that you chose earlier in the instructions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '21, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82751" class="comments-container">
&#10;</div>
<div id="comment-tools-82751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82751-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82752"></span>

<div id="answer-container-82752" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82752-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for helping although I have this issue when I try that. E.g. I switch user to 'renderaccount' (my non-root username) and run without sudo:</p>
<p>renderd[18191]: An error occurred while loading the map layer 'ajt': Postgis Plugin: ERROR: permission denied for relation planet_osm_polygon</p>
<p>UPDATE: I gave superuser priviledgers to my 'renderaccount' in postgres... this is the error now, which I think relates to issue 1: renderd[18942]: An error occurred while loading the map layer 'ajt': Postgis Plugin: ERROR: relation "icesheet_polygons" does not exist LINE 1: SELECT ST_SRID("way") AS srid FROM icesheet_polygons WHERE "...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '21, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/20e950eb7a5f2c52377f26a49dd71e06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kieran&#39;s gravatar image" />
<p><span>kieran</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kieran has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Dec '21, 10:57</strong> </span></p>
</div>
</div>
<div id="comments-container-82752" class="comments-container">
<span id="82753"></span>
<div id="comment-82753" class="comment">
<div id="post-82753-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That probably means that you carried out some earlier steps as root rather than the non-root username that you chose earlier.</p>
</div>
<div id="comment-82753-info" class="comment-info">
<span class="comment-age">(04 Dec '21, 10:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82755"></span>
<div id="comment-82755" class="comment">
<div id="post-82755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another clean install I try... cry.</p>
</div>
<div id="comment-82755-info" class="comment-info">
<span class="comment-age">(04 Dec '21, 11:07)</span> <span class="comment-user userinfo">kieran</span>
</div>
</div>
<span id="82756"></span>
<div id="comment-82756" class="comment">
<div id="post-82756-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you get any questions as you go you could try asking on IRC in #osm - there might be someone there who can help. See <a href="https://wiki.openstreetmap.org/wiki/IRC#How_to_use_IRC">https://wiki.openstreetmap.org/wiki/IRC#How_to_use_IRC</a> .</p>
</div>
<div id="comment-82756-info" class="comment-info">
<span class="comment-age">(04 Dec '21, 11:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82757"></span>
<div id="comment-82757" class="comment">
<div id="post-82757-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>LEGEND - worked perfectly (in under an hour!). tutorial excellent except for maybe run all as non-root user (i know this is probably a no-brainer to people who get security etc...), and you need to give sudo privs to the non-root user and make postgres user superuser as well!</p>
</div>
<div id="comment-82757-info" class="comment-info">
<span class="comment-age">(04 Dec '21, 12:02)</span> <span class="comment-user userinfo">kieran</span>
</div>
</div>
<span id="82758"></span>
<div id="comment-82758" class="comment">
<div id="post-82758-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've added <a href="https://github.com/switch2osm/switch2osm.github.io/pull/175">https://github.com/switch2osm/switch2osm.github.io/pull/175</a> - does anything else need saying?</p>
</div>
<div id="comment-82758-info" class="comment-info">
<span class="comment-age">(04 Dec '21, 12:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82763"></span>
<div id="comment-82763" class="comment not_top_scorer">
<div id="post-82763-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ul>
<li><p>The validation/tips in brackets I found REALLY helpful</p></li>
<li><p>Do the the user and permissions at the beginning and include validation in brackets (something like: su renderaccount - you are now in your ‘renderaccount’ - run all commands form here). As the set up a user instruction was like instruction 10</p></li>
<li><p>You could say tested Dec 2021 now at the beginning</p></li>
<li><p>The switcher redirector link broken (I used jupyter)</p></li>
</ul>
<p>Thanks again</p>
</div>
<div id="comment-82763-info" class="comment-info">
<span class="comment-age">(05 Dec '21, 11:08)</span> <span class="comment-user userinfo">kieran</span>
</div>
</div>
<span id="82764"></span>
<div id="comment-82764" class="comment not_top_scorer">
<div id="post-82764-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just for completeness, future "Ubuntu" setup guides will be like <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-21/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-21/</a> since most of the software is built-into Ubuntu itself now. With new versions of Ubuntu you don't need to create a new non-root account yourself; the installation does it for you.</p>
</div>
<div id="comment-82764-info" class="comment-info">
<span class="comment-age">(05 Dec '21, 12:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82752" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-82752-form-container" class="comment-form-container">
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

