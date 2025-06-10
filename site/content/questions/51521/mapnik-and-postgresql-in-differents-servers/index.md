+++
type = "question"
title = "mapnik and postgresql in differents servers"
description = '''I have installed: on a server: mapnik, openstreetmap-carto and mod_tile in apache2 in another: postgresql, postgis where I have to put the connection parameters to the database: user, password, host, port, ... I tried:  set | grep MAPNIK MAPNIK_DBHOST=192.168.1.1 MAPNIK_DBNAME=gis MAPNIK_DBPASS=xxxx...'''
date = "2016-08-18T16:08:00Z"
lastmod = "2016-08-19T10:10:00Z"
weight = 51521
keywords = [ "postgis", "mapnik", "mod_tile" ]
aliases = [ "/questions/51521" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mapnik and postgresql in differents servers](/questions/51521/mapnik-and-postgresql-in-differents-servers)

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
<span id="post-51521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51521-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed:</p>
<p>on a server: mapnik, openstreetmap-carto and mod_tile in apache2</p>
<p>in another: postgresql, postgis</p>
<p>where I have to put the connection parameters to the database: user, password, host, port, ...</p>
<p>I tried:</p>
<pre><code> set | grep MAPNIK
MAPNIK_DBHOST=192.168.1.1
MAPNIK_DBNAME=gis
MAPNIK_DBPASS=xxxxxxxx
MAPNIK_DBPORT=5432
MAPNIK_DBUSER=userdb</code></pre>
<p>with the same result</p>
<p><strong>Do I have to install Mapnik-style (default) Or there somewhere to register values?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '16, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/304bf9b97689c5eb6191600403aaf65b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arcadio%20ortega&#39;s gravatar image" />
<p><span>arcadio ortega</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arcadio ortega has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '16, 16:52</strong> </span></p>
</div>
</div>
<div id="comments-container-51521" class="comments-container">
&#10;</div>
<div id="comment-tools-51521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51521-form-container" class="comment-form-container">
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

<span id="51527"></span>

<div id="answer-container-51527" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51527-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've never run Postgres on a different server, but I think you'd have to change the <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/ef48cd7448ff3b139e717f161bccddd164c47665/project.yaml#L31-L36">osm2pgsql connection settings</a> inside the openstreetmap-carto project.</p>
<p>Add a <code>host</code>/<code>user</code>/etc value to this part:</p>
<pre><code>  osm2pgsql: &amp;osm2pgsql
    type: &quot;postgis&quot;
    dbname: &quot;gis&quot;
    key_field: &quot;&quot;
    geometry_field: &quot;way&quot;
    extent: &quot;-20037508,-20037508,20037508,20037508&quot;</code></pre>
<p>See also: <a href="https://github.com/mapnik/mapnik/wiki/PostGIS">Mapnik's PostgreSQL settings</a>.</p>
<p>The openstreetmap-carto style makes use of some shapefiles, you will need to have them locally on the mapnik server, not the postgresql server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '16, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-51527" class="comments-container">
<span id="51529"></span>
<div id="comment-51529" class="comment">
<div id="post-51529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I execute "carto project.mml &gt; osm.xml" if I change something in project.yaml then nothing changes in osm.xml and everything stays the same.</p>
</div>
<div id="comment-51529-info" class="comment-info">
<span class="comment-age">(19 Aug '16, 08:12)</span> <span class="comment-user userinfo">arcadio ortega</span>
</div>
</div>
<span id="51538"></span>
<div id="comment-51538" class="comment">
<div id="post-51538-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where I add this: <a href="https://github.com/mapnik/mapnik/wiki/PostGIS#user-content-usage-from-c">PostGIS_user-content-usage-from-c</a> it can be the solution</p>
</div>
<div id="comment-51538-info" class="comment-info">
<span class="comment-age">(19 Aug '16, 10:10)</span> <span class="comment-user userinfo">arcadio ortega</span>
</div>
</div>
</div>
<div id="comment-tools-51527" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51527-form-container" class="comment-form-container">
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

