+++
type = "question"
title = "Switch2Osm instructions wrong?"
description = '''I just followed instruction from http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/ on my virtual machine. I tried 3 times, using different countries from http://download.geofabrik.de/openstreetmap/ and couldn&#x27;t get my local tiles generated, browsing to http://localhost/osm/sl...'''
date = "2013-01-11T04:27:00Z"
lastmod = "2013-01-11T10:46:00Z"
weight = 18979
keywords = [ "local-tile-server" ]
aliases = [ "/questions/18979" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Switch2Osm instructions wrong?](/questions/18979/switch2osm-instructions-wrong)

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
<span id="post-18979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18979-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just followed instruction from <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> on my virtual machine. I tried 3 times, using different countries from <a href="http://download.geofabrik.de/openstreetmap/">http://download.geofabrik.de/openstreetmap/</a> and couldn't get my local tiles generated, browsing to <a href="http://localhost/osm/slippymap.html.">http://localhost/osm/slippymap.html.</a></p>
<p>I also tried this instructions: <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04.">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04.</a> However I ended up with the same result.</p>
<p>Are those manuals still viable?</p>
<p>EDIT: I tried on Ubuntu 12.04.1 32-bit</p>
<p>EDIT2: Solved. I will update this post soon after I verify installation/fixing steps again. Seems like libapache2-mod-tile tries to load data from outdated link, getting 404 error and hence making mapnik/renderd unable to render a tile.</p>
<p>EDIT3: OK. So the problem was when I install libapache2-mod-tile, it tries to load <code>ne_10m_populated_places and 110m_admin_0_boundary_lines_land from </code><a href="http://www.naturalearthdata.com"><code>http://www.naturalearthdata.com</code></a><code> and fails to do so:</code></p>
<pre><code>--2013-01-11 15:07:10--  http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/10m-populated-places.zip
Resolving www.naturalearthdata.com (www.naturalearthdata.com)... 66.147.242.194
Connecting to www.naturalearthdata.com (www.naturalearthdata.com)|66.147.242.194|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2013-01-11 15:07:12 ERROR 404: Not Found.
&#10;--2013-01-11 15:07:12--  http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/110m-admin-0-boundary-lines.zip
Resolving www.naturalearthdata.com (www.naturalearthdata.com)... 66.147.242.194
Connecting to www.naturalearthdata.com (www.naturalearthdata.com)|66.147.242.194|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2013-01-11 15:07:13 ERROR 404: Not Found.</code></pre>
<p>So I kept getting this error in /var/log/syslog from renderd:</p>
<pre><code>An error occurred while loading the map layer &#39;default&#39;: Shape Plugin: shapefile &#39;/us
r/share/mapnik-osm-data/world_boundaries/110m_admin_0_boundary_lines_land.shp&#39; does not exist (encountered during parsing of layer &#39;ne
countries&#39; in map &#39;/etc/mapnik-osm-data/osm.xml&#39;)</code></pre>
<p>I am not sure whether it is my own issue since it may get blocked by my company firewall (although error message must be different), so it would've been nice if someone could double check it.</p>
<pre><code>I solved it by manually downloading those archives from links provided by: http://wiki.openstreetmap.org/wiki/Mapnik
(those are: ne_10m_populated_places.zip and ne_110m_admin_0_boundary_lines_land.zip on that wiki page). Then I extracted them and copied .dbf, .prj, .shp, .shx files to /usr/share/mapnik-osm-data/world_boundaries. And I had to rename ne_110m_admin_0_boundary_lines_land to 110m_admin_0_boundary_lines_land, removing ne_ prefix from them.</code></pre>
<p>After that I restarted renderd by:</p>
<pre><code>sudo /etc/init.d/renderd restart</code></pre>
<p>I guess the problem is caused by invalid link during installation of libapache2-mod-tile: <a href="http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural">http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural</a></p>
<p>PS sorry for using "code" tags in inappropriate places. Parser kept "eating" my underscore symbols.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-local-tile-server" rel="tag" title="see questions tagged &#39;local-tile-server&#39;">local-tile-server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '13, 04:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a9ac21e7ac74da624e5b261d159a5847?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashagi&#39;s gravatar image" />
<p><span>ashagi</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashagi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '13, 10:32</strong> </span></p>
</div>
</div>
<div id="comments-container-18979" class="comments-container">
<span id="18981"></span>
<div id="comment-18981" class="comment">
<div id="post-18981-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you complete the installation instructions without encountering any error messages?</p>
</div>
<div id="comment-18981-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 06:56)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="18983"></span>
<div id="comment-18983" class="comment">
<div id="post-18983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, please let us know what the problem was, so that we can get the instructions updated.</p>
</div>
<div id="comment-18983-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 09:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="18984"></span>
<div id="comment-18984" class="comment">
<div id="post-18984-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Looks like someone else had this problem on #osm irc channel on 27th November, and the wiki page was updated since - <a href="http://wiki.openstreetmap.org/wiki/Talk:Mapnik#Download_required_data">http://wiki.openstreetmap.org/wiki/Talk:Mapnik#Download_required_data</a> was added in late December. It looks like the libapache2-mod-tile package may need repackaging.</p>
</div>
<div id="comment-18984-info" class="comment-info">
<span class="comment-age">(11 Jan '13, 10:46)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18979-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

