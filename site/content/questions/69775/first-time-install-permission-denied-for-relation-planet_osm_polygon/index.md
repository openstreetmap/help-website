+++
type = "question"
title = "First Time Install - permission denied for relation planet_osm_polygon"
description = '''First time install and I&#x27;m getting the error below when I try to run rendered as render account.  My test box is smaller so I imported each US state one by one. Not sure if this has an effect or not.  Mapnik LOG&amp;gt; 2019-06-27 16:21:41: warning: unable to find face-name &#x27;unifont Medium&#x27; in FontSet &#x27;...'''
date = "2019-06-27T17:39:00Z"
lastmod = "2019-06-29T18:06:00Z"
weight = 69775
keywords = [ "installation", "renderd", "newbie" ]
aliases = [ "/questions/69775" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [First Time Install - permission denied for relation planet_osm_polygon](/questions/69775/first-time-install-permission-denied-for-relation-planet_osm_polygon)

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
<span id="post-69775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69775-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>First time install and I'm getting the error below when I try to run rendered as render account.</p>
<p>My test box is smaller so I imported each US state one by one. Not sure if this has an effect or not.</p>
<pre><code>Mapnik LOG&gt; 2019-06-27 16:21:41: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[22208]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  permission denied for relation planet_osm_polygon
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM planet_osm_polygon WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 755 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;
renderd[22208]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  permission denied for relation planet_osm_polygon
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM planet_osm_polygon WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 755 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '19, 17:39</strong></p>
<img src="https://secure.gravatar.com/avatar/2f2802a91a7b23b9a654d5d1f3e4b917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chavenor1&#39;s gravatar image" />
<p><span>chavenor1</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chavenor1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69775" class="comments-container">
<span id="69776"></span>
<div id="comment-69776" class="comment">
<div id="post-69776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"permission denied for relation planet_osm_polygon" implies that the accounts used for part of the installation didn't match the account used for another part. I'm guessing that you're following <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> , perhaps recheck what accoun you used for each part of that? Maybe you did some things as root and therefore can't access them as a non-root user?</p>
</div>
<div id="comment-69776-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 20:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69777"></span>
<div id="comment-69777" class="comment">
<div id="post-69777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What account should be used through that guide? Not sure it's clear if I should be root or renderaccount. Should I delete and re-install? Is rendered run by root or render account?</p>
</div>
<div id="comment-69777-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 20:36)</span> <span class="comment-user userinfo">chavenor1</span>
</div>
</div>
<span id="69778"></span>
<div id="comment-69778" class="comment">
<div id="post-69778-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>From memory, everything to be done as root has a "sudo" at the front, such as "sudo apt-get install ...". If you type in the commands as written, everything will work.</p>
<p>As written, the guide uses a Linux user account called "renderaccount" to run things like renderd from. The postgres side of things is handled at "ALTER TABLE geometry_columns OWNER TO renderaccount;" and the Linux system side at "sudo useradd -m renderaccount".</p>
</div>
<div id="comment-69778-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 21:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69779"></span>
<div id="comment-69779" class="comment">
<div id="post-69779-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm usually logged in as root is that a problem? Or should I make renderaccount part of the sudo group? What account root or renderaccount or Postgres should this command be run at?</p>
<p>osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 1000 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/delaware-latest.osm.pbf</p>
</div>
<div id="comment-69779-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 21:09)</span> <span class="comment-user userinfo">chavenor1</span>
</div>
</div>
<span id="69782"></span>
<div id="comment-69782" class="comment">
<div id="post-69782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You have a Postgres user issue, not a Linux user one: they are separate things. Running 'psql -l' will tell us who owns your gis database.</p>
</div>
<div id="comment-69782-info" class="comment-info">
<span class="comment-age">(29 Jun '19, 06:21)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
</div>
<div id="comment-tools-69775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69775-form-container" class="comment-form-container">
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

<span id="69790"></span>

<div id="answer-container-69790" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69790-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Re-loading the .osm.pbf files into the PostGIS DB while using the renderaccount fixed the issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '19, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/2f2802a91a7b23b9a654d5d1f3e4b917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chavenor1&#39;s gravatar image" />
<p><span>chavenor1</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chavenor1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69790" class="comments-container">
&#10;</div>
<div id="comment-tools-69790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69790-form-container" class="comment-form-container">
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

