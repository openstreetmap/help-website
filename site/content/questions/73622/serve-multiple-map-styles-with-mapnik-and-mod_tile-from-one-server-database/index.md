+++
type = "question"
title = "Serve multiple map styles with mapnik and mod_tile from one server &amp; database"
description = '''Hi, I struggle to set up two different map styles for the mapnik-osm rendering tool chain. According to some help I already found here and on gis.stackexchange, I have set up the renderd.conf for two map styles. But I can&#x27;t get it to work. When I enter the URL for the second map style (&quot;http://myser...'''
date = "2020-03-19T13:39:00Z"
lastmod = "2020-03-20T16:37:00Z"
weight = 73622
keywords = [ "apache", "style", "mapnik", "mod_tile" ]
aliases = [ "/questions/73622" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Serve multiple map styles with mapnik and mod_tile from one server & database](/questions/73622/serve-multiple-map-styles-with-mapnik-and-mod_tile-from-one-server-database)

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
<span id="post-73622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73622-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I struggle to set up two different map styles for the mapnik-osm rendering tool chain. According to some help I already found here and on gis.stackexchange, I have set up the renderd.conf for two map styles. But I can't get it to work. When I enter the URL for the second map style ("http://myserverurl/print/0/0/0.png") the browser says "The requested URL was not found on this server." With the default map style it is no problem ("http://myserverurl/osm/0/0/0.png").</p>
<p>I coulnd't find any other setting in the mod_tile or renderd config files to enable the "print" map style to work. What did I oversee or is there anything else I need to do? The renderd.conf looks like this:</p>
<hr />
<pre><code>[renderd]
stats_file=/var/run/renderd/renderd.stats
socketname=/var/run/renderd/renderd.sock
num_threads=10
tile_dir=/var/lib/mod_tile
&#10;[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input
font_dir=/usr/share/fonts/truetype/ttf-dejavu
font_dir_recurse=false
&#10;[default]
URI=/osm/
TILEDIR=/var/lib/mod_tile
TILESIZE=256
XML=/home/osm/openstreetmap-carto-4.24.1/style.xml
DESCRIPTION=Default map style
;ATTRIBUTION=&amp;copy;&lt;a href=\&quot;http://www.openstreetmap.org/\&quot;&gt;OpenStreetMap&lt;/a&gt; and &lt;a href=\&quot;http://wiki.openstreetmap.org/w\
iki/Contributors\&quot;&gt;contributors&lt;/a&gt;, &lt;a href=\&quot;http://creativecommons.org/licenses/by-sa/2.0/\&quot;&gt;CC-BY-SA&lt;/a&gt;
;HOST=http://myserverurl
;SERVER_ALIAS=http://a.tile.openstreetmap.org
;SERVER_ALIAS=http://b.tile.openstreetmap.org
;HTCPHOST=proxy.openstreetmap.org
&#10;[print]
URI=/print/
TILEDIR=/var/lib/mod_tile
TILESIZE=512
XML=/home/osm/openstreetmap-carto-4.24.1/print/style.xml
DESCRIPTION=print map style
;ATTRIBUTION=&amp;copy;&lt;a href=\&quot;http://www.openstreetmap.org/\&quot;&gt;OpenStreetMap&lt;/a&gt; and &lt;a href=\&quot;http://wiki.openstreetmap.org/w\
iki/Contributors\&quot;&gt;contributors&lt;/a&gt;, &lt;a href=\&quot;http://creativecommons.org/licenses/by-sa/2.0/\&quot;&gt;CC-BY-SA&lt;/a&gt;
;HOST=http://myserverurl
;SERVER_ALIAS=http://a.tile.openstreetmap.org
;SERVER_ALIAS=http://b.tile.openstreetmap.org
;HTCPHOST=proxy.openstreetmap.org</code></pre>
<hr />
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '20, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/537a2599a1104fc0b9d044b8ee6be379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders2&#39;s gravatar image" />
<p><span>Anders2</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders2 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '20, 13:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-73622" class="comments-container">
&#10;</div>
<div id="comment-tools-73622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73622-form-container" class="comment-form-container">
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

<span id="73623"></span>

<div id="answer-container-73623" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73623-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, make sure to use a different TILEDIR for each style, or else the tiles will overwrite each other. (Typically you would use something like <code>/var/lib/mod_tile/osm</code> and <code>/var/lib/mod_tile/print</code> in your case.) Secondly, assuming you are using the <code>LoadTileConfig</code> directive in your Apache configuration: Have you done a <code>systemctl reload apache2</code> (or <code>apache2ctl restart</code>) after adding your new style?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '20, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73623" class="comments-container">
<span id="73624"></span>
<div id="comment-73624" class="comment">
<div id="post-73624-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, thanks for the quick reply. Yes I restarted both renderd and apache2. I read that depending on the name ("default" and "print") a seperate directory is created automatically. So far I only see the default directory in /var/lib/mod_tile/ I tried it with two different directories now as you recommended, but nothing changed.</p>
</div>
<div id="comment-73624-info" class="comment-info">
<span class="comment-age">(19 Mar '20, 14:12)</span> <span class="comment-user userinfo">Anders2</span>
</div>
</div>
</div>
<div id="comment-tools-73623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73623-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73625"></span>

<div id="answer-container-73625" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73625-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do a</p>
<p><code>sudo -u {yourUserAccountforRenderd} mkdir /var/lib/mod_tile/print</code></p>
<p>and restart renderd and apache2 again.</p>
<p>If that does not help, check the error/info output at <code>/var/log/syslog</code> while restarting renderd.</p>
<p>It smells like a problem with permissions or missing shapefiles (did you load the shapefiles for the print style as well or referenced the osm-carto ones in the project.mml for the print.xml?)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '20, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '20, 14:21</strong> </span></p>
</div>
</div>
<div id="comments-container-73625" class="comments-container">
<span id="73626"></span>
<div id="comment-73626" class="comment">
<div id="post-73626-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that didn't work, but brought me to the solution!</p>
</div>
<div id="comment-73626-info" class="comment-info">
<span class="comment-age">(19 Mar '20, 14:30)</span> <span class="comment-user userinfo">Anders2</span>
</div>
</div>
</div>
<div id="comment-tools-73625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73625-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73649"></span>

<div id="answer-container-73649" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73649-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So the solution was: In the /var/www/ directory was only an "osm" folder (<a href="http://myserverurl/osm/0/0/0.png">http://myserverurl/osm/0/0/0.png</a> worked). I created another directory named like the additional mapstyle ("print"). And gave the permission <code>chmod -R 755 /var/www</code>.</p>
<p>After a restart of Apache it now serves the other map style through <a href="http://myserverurl/print/0/0/0.png.">http://myserverurl/print/0/0/0.png.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '20, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/537a2599a1104fc0b9d044b8ee6be379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders2&#39;s gravatar image" />
<p><span>Anders2</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73649" class="comments-container">
&#10;</div>
<div id="comment-tools-73649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73649-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

