+++
type = "question"
title = "Tirex permissions problem"
description = '''I&#x27;m trying to run an instance of the OpenArdenneMap on my Ubuntu 16.04 server. The tirex systemd units run as user &quot;osm&quot;, which also owns the pgsql database. Nevertheless I&#x27;m getting a permissions error. /var/lib/mod_tile/ard is correctly owned by &quot;osm&quot; (and now even 777): drwxrwxrwx 2 osm osm 4096 ...'''
date = "2018-06-25T00:00:00Z"
lastmod = "2018-06-25T22:27:00Z"
weight = 64350
keywords = [ "tirex", "mapnik" ]
aliases = [ "/questions/64350" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tirex permissions problem](/questions/64350/tirex-permissions-problem)

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
<span id="post-64350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to run an instance of the <a href="https://github.com/nobohan/OpenArdenneMap">OpenArdenneMap</a> on my Ubuntu 16.04 <a href="http://185.219.132.219/ard/0/0/0.png">server</a>. The tirex systemd units run as user "osm", which also owns the pgsql database. Nevertheless I'm getting a permissions error.</p>
<p>/var/lib/mod_tile/ard is correctly owned by "osm" (and now even 777): <code>drwxrwxrwx 2 osm osm 4096 Jun 25 01:22 .</code></p>
<pre><code>Jun 25 01:55:28 host tirex-backend-manager[15979]: tirex-backend-mapnik[17153]: cannot add /etc/tirex/renderer/osm/osm.conf
Jun 25 01:55:28 host tirex-backend-mapnik[17153]: cannot add /etc/tirex/renderer/osm/osm.conf
Jun 25 01:55:28 host tirex-backend-manager[15979]: tirex-backend-mapnik[17153]: Could not create datasource for type: &#39;postgis&#39; (no datasource plugin directories have been successfully registered)  encountered during parsing of layer &#39;landuse&#39; in Layer at line 165 of &#39;/home/osm/OpenArdenneMap/cartoCSS/OpenArdenneMap.xml&#39;
Jun 25 01:55:28 host tirex-backend-mapnik[17153]: Could not create datasource for type: &#39;postgis&#39; (no datasource plugin directories have been successfully registered)  encountered during parsing of layer &#39;landuse&#39; in Layer at line 165 of &#39;/home/osm/OpenArdenneMap/cartoCSS/OpenArdenneMap.xml&#39;
Jun 25 01:55:28 host tirex-backend-manager[15979]: Cannot load any Mapnik styles</code></pre>
<p>These are my tirex config files:</p>
<pre><code>name=osm
tiledir=/var/lib/mod_tile/ard
maxz=18
fontdir=/usr/share/fonts/truetype
font_dir_recurse=1
mapfile=/home/osm/OpenArdenneMap/cartoCSS/OpenArdenneMap.xml
&#10;name=osm
path=/usr/lib/tirex/backends/mapnik
port=9331
procs=5
debug=1
plugindir=/usr/lib/mapnik/3.0/input
fontdir=/usr/share/fonts/truetype
fontdir_recurse=1</code></pre>
<p>What have I overlooked?</p>
<p>----------------------------------- Edit ---</p>
<p>I've now changed the plugindir into plugindir=/usr/lib/mapnik/3.0/input but the error remains.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '18, 00:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ab77a6da4507c0183079f3044856311a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chazanov&#39;s gravatar image" />
<p><span>chazanov</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chazanov has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '18, 09:37</strong> </span></p>
</div>
</div>
<div id="comments-container-64350" class="comments-container">
<span id="64355"></span>
<div id="comment-64355" class="comment">
<div id="post-64355-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Check if the directory you are listing as "plugindir" actually exists, can be accessed by the "tirex" user, and contains a "postgis.input" file that is also readable by tirex. Are you sure that all the required libraries are installed (i.e. did you install with a proper package manager)?</p>
</div>
<div id="comment-64355-info" class="comment-info">
<span class="comment-age">(25 Jun '18, 11:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64364"></span>
<div id="comment-64364" class="comment">
<div id="post-64364-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This error message is something different than the one you reported above. Try <code>chmod 777 /var/run/tirex/master.sock</code> to get rid of the permission issue. Are you running SELinux by any chance?</p>
</div>
<div id="comment-64364-info" class="comment-info">
<span class="comment-age">(25 Jun '18, 16:42)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64350-form-container" class="comment-form-container">
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

<span id="64359"></span>

<div id="answer-container-64359" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64359-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>postgis.input is okay</p>
<pre><code>Cannot open master UNIX domain socket: Permission denied
ls -la /usr/lib/mapnik/3.0/input/postgis.input 
-rwxr-xr-x 1 osm osm 253000 Dec  3  2015 /usr/lib/mapnik/3.0/input/postgis.input</code></pre>
<p>The user is allowed to create the file /var/lib/tirex/modtile.sock</p>
<p>But still I'm getting this when running tirex-master:</p>
<pre><code>Cannot open master UNIX domain socket: Permission denied</code></pre>
<p>My server doesn't contain sensitive data: I would even be ready to give away my login to some expert!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '18, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ab77a6da4507c0183079f3044856311a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chazanov&#39;s gravatar image" />
<p><span>chazanov</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chazanov has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '18, 14:36</strong> </span></p>
</div>
</div>
<div id="comments-container-64359" class="comments-container">
&#10;</div>
<div id="comment-tools-64359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64359-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64365"></span>

<div id="answer-container-64365" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64365-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, this solved my issue.</p>
<p>I've then launched <code>tirex-batch -p 50 map=osm bbox=5.9654,50.3627,9.514,52.5061 z=0,9</code></p>
<p>A few metatiles were generated, but most timed out:</p>
<pre><code>Jun 25 17:52:33 host tirex-master[10737]: Job with id=1529937746_33410336 timed out on rendering list (map=osm z=0 x=0 y=0)
Jun 25 18:02:53 host tirex-master[10737]: Job with id=1529937746_36479432 timed out on rendering list (map=osm z=3 x=0 y=0)
Jun 25 18:02:53 host tirex-master[10737]: Job with id=1529937746_36454544 timed out on rendering list (map=osm z=2 x=0 y=0)</code></pre>
<p>(The map still <a href="http://185.219.132.219/">doesn't load</a> in Leaflet.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '18, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ab77a6da4507c0183079f3044856311a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chazanov&#39;s gravatar image" />
<p><span>chazanov</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chazanov has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '18, 17:24</strong> </span></p>
</div>
</div>
<div id="comments-container-64365" class="comments-container">
<span id="64369"></span>
<div id="comment-64369" class="comment">
<div id="post-64369-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you don't have fast disks you MUST increase the backend_manager_alive_timeout and master_rendering_timeout in tirex.conf (e.g. to 59 and 60 respectively). Also the syntax for zoom levels in tirex-batch is <code>z=0-9</code> not <code>z=0,9</code>.</p>
</div>
<div id="comment-64369-info" class="comment-info">
<span class="comment-age">(25 Jun '18, 22:27)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64365" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64365-form-container" class="comment-form-container">
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

