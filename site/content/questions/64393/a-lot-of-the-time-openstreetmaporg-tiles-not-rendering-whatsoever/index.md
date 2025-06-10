+++
type = "question"
title = "A lot of the time, openstreetmap.org tiles not rendering whatsoever"
description = '''&amp;gt; tile.openstreetmap.org debug Server Stats  Cache Server: saphira.openstreetmap.org  Render Server: orm.openstreetmap.org Load Average: 23.25 File Status  world_boundaries-spherical.tgz last modified: Tue Jun 4 11:59:57 2013 simplified-land-polygons-complete-3857.zip last modified: Sun Jun 10 08...'''
date = "2018-06-26T17:54:00Z"
lastmod = "2018-06-27T18:58:00Z"
weight = 64393
keywords = [ "website", "rendering", "openstreetmap-carto" ]
aliases = [ "/questions/64393" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [A lot of the time, openstreetmap.org tiles not rendering whatsoever](/questions/64393/a-lot-of-the-time-openstreetmaporg-tiles-not-rendering-whatsoever)

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
<span id="post-64393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64393-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code>&gt; tile.openstreetmap.org debug
Server Stats
&#10;Cache Server: saphira.openstreetmap.org
&#10;Render Server: orm.openstreetmap.org
Load Average: 23.25
File Status
&#10;world_boundaries-spherical.tgz last modified: Tue Jun 4 11:59:57 2013
simplified-land-polygons-complete-3857.zip last modified: Sun Jun 10 08:04:39 2018
ne_110m_admin_0_boundary_lines_land.zip last modified: Tue Jun 4 12:00:51 2013
land-polygons-split-3857.zip last modified: Sun Jun 10 08:05:13 2018
antarctica-icesheet-polygons-3857.zip last modified: Sun Jun 24 07:04:16 2018
antarctica-icesheet-outlines-3857.zip last modified: Sun Jun 24 07:04:30 2018
Browser Request Headers
&#10;CONTEXT_DOCUMENT_ROOT: /srv/tile.openstreetmap.org/cgi-bin/
SERVER_SOFTWARE: Apache/2.4.18 (Ubuntu)
CONTEXT_PREFIX: /cgi-bin/
SERVER_SIGNATURE:
Apache/2.4.18 (Ubuntu) Server at tile.openstreetmap.org Port 443
&#10;REQUEST_METHOD: GET
SERVER_PROTOCOL: HTTP/1.0
QUERY_STRING:
PATH: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HTTP_USER_AGENT: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
HTTP_CONNECTION: keep-alive
SERVER_NAME: tile.openstreetmap.org
REMOTE_ADDR: 185.73.44.30
HTTP_VIA: 1.1 saphira.openstreetmap.org:3128 (squid/2.7.STABLE9)
SERVER_PORT: 443
SERVER_ADDR: 193.63.75.98
DOCUMENT_ROOT: /srv/tile.openstreetmap.org/html
SCRIPT_FILENAME: /srv/tile.openstreetmap.org/cgi-bin/debug
SERVER_ADMIN: webmaster@openstreetmap.org
SCRIPT_URI: https://tile.openstreetmap.org/cgi-bin/debug
HTTP_DNT: 1
HTTP_HOST: tile.openstreetmap.org
SCRIPT_URL: /cgi-bin/debug
HTTPS: on
HTTP_UPGRADE_INSECURE_REQUESTS: 1
HTTP_CACHE_CONTROL: max-age=518400
REQUEST_URI: /cgi-bin/debug
HTTP_ACCEPT: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8
GATEWAY_INTERFACE: CGI/1.1
HTTP_X_FORWARDED_FOR: 80.189.200.188, 127.0.0.1
SCRIPT_NAME: /cgi-bin/debug
REMOTE_PORT: 48352
HTTP_ACCEPT_LANGUAGE: en-US,en;q=0.5
REQUEST_SCHEME: https</code></pre>
<p>This is the tile debug when it happened.</p>
<p>The error still occurs - but the tile server for me has now changed:</p>
<pre><code>&gt; 
tile.openstreetmap.org debug
Server Stats
&#10;Cache Server: katie.openstreetmap.org
&#10;Render Server: yevaud.openstreetmap.org
Load Average: 36.21
File Status
&#10;world_boundaries-spherical.tgz last modified: Wed Apr 29 09:30:45 2015
simplified-land-polygons-complete-3857.zip last modified: Sun Jun 10 07:49:56 2018
ne_110m_admin_0_boundary_lines_land.zip last modified: Wed Apr 29 09:31:00 2015
land-polygons-split-3857.zip last modified: Sun Jun 10 07:50:20 2018
antarctica-icesheet-polygons-3857.zip last modified: Tue Jun 26 06:53:32 2018
antarctica-icesheet-outlines-3857.zip last modified: Tue Jun 26 06:53:45 2018
Browser Request Headers
&#10;CONTEXT_DOCUMENT_ROOT: /srv/tile.openstreetmap.org/cgi-bin/
SERVER_SOFTWARE: Apache/2.4.18 (Ubuntu)
CONTEXT_PREFIX: /cgi-bin/
SERVER_SIGNATURE:
Apache/2.4.18 (Ubuntu) Server at tile.openstreetmap.org Port 443
&#10;REQUEST_METHOD: GET
SERVER_PROTOCOL: HTTP/1.0
QUERY_STRING:
PATH: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HTTP_USER_AGENT: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
HTTP_CONNECTION: keep-alive
SERVER_NAME: tile.openstreetmap.org
REMOTE_ADDR: 144.76.70.77
HTTP_VIA: 1.1 katie.openstreetmap.org:3128 (squid/2.7.STABLE9)
SERVER_PORT: 443
SERVER_ADDR: 193.60.236.22
DOCUMENT_ROOT: /srv/tile.openstreetmap.org/html
SCRIPT_FILENAME: /srv/tile.openstreetmap.org/cgi-bin/debug
SERVER_ADMIN: webmaster@openstreetmap.org
SCRIPT_URI: https://tile.openstreetmap.org/cgi-bin/debug
HTTP_DNT: 1
HTTP_HOST: tile.openstreetmap.org
SCRIPT_URL: /cgi-bin/debug
HTTPS: on
HTTP_UPGRADE_INSECURE_REQUESTS: 1
HTTP_CACHE_CONTROL: max-age=518400
REQUEST_URI: /cgi-bin/debug
HTTP_ACCEPT: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
GATEWAY_INTERFACE: CGI/1.1
HTTP_X_FORWARDED_FOR: 51.9.73.35, 127.0.0.1
SCRIPT_NAME: /cgi-bin/debug
REMOTE_PORT: 39604
HTTP_ACCEPT_LANGUAGE: en-US,en;q=0.5
REQUEST_SCHEME: https</code></pre>
<p>Here is a example with the new cache server: <img src="https://help.openstreetmap.org/upfiles/another_bad_layer.png" alt="another example bad" /></p>
<p><img src="https://help.openstreetmap.org/upfiles/another_good_layer.png" alt="another example good" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '18, 17:54</strong></p>
<img src="https://secure.gravatar.com/avatar/99c118410f297395eacc2f8b11510ebd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CuriousPerson1234&#39;s gravatar image" />
<p><span>CuriousPerso...</span><br />
<span class="score" title="34 reputation points">34</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CuriousPerson1234 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '18, 08:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</img>
</div>
</div>
<div id="comments-container-64393" class="comments-container">
<span id="64396"></span>
<div id="comment-64396" class="comment">
<div id="post-64396-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Btw this is happening everywhere and anywhere I try to zoom into. I can't even see house numbers because cyclemap/ travel map don't show them and in standard / humanitarian the tiles stop loading before it reaches a zoom where house numbers are shown.</p>
</div>
<div id="comment-64396-info" class="comment-info">
<span class="comment-age">(26 Jun '18, 21:41)</span> <span class="comment-user userinfo">CuriousPerso...</span>
</div>
</div>
<span id="64397"></span>
<div id="comment-64397" class="comment">
<div id="post-64397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>not sure if it may be useful, but... what is the HTTP status code of the tile requests in your browser (in Firefox hit ctrl+shift+E and then pan the map or reload the page)? Do you get something back from the server or is the request waiting?</p>
</div>
<div id="comment-64397-info" class="comment-info">
<span class="comment-age">(26 Jun '18, 22:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="64415"></span>
<div id="comment-64415" class="comment">
<div id="post-64415-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>when all the map tiles load, I get something back, but when some of the tiles don't load, the pie chart thing is stuck on "Loading..." forever.</p>
</div>
<div id="comment-64415-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 18:58)</span> <span class="comment-user userinfo">CuriousPerso...</span>
</div>
</div>
</div>
<div id="comment-tools-64393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64393-form-container" class="comment-form-container">
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

<span id="64402"></span>

<div id="answer-container-64402" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64402-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Some of the tile caches have been experiencing issues for a couple of days, if this is the reason for your issues is best determined on the #osm-dev IRC channel. Run <a href="https://tile.openstreetmap.org/cgi-bin/debug">https://tile.openstreetmap.org/cgi-bin/debug</a> first to determine which tile cache your are using.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '18, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-64402" class="comments-container">
<span id="64414"></span>
<div id="comment-64414" class="comment">
<div id="post-64414-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have the output of <a href="https://tile.openstreetmap.org/cgi-bin/debug">https://tile.openstreetmap.org/cgi-bin/debug</a> in the question</p>
</div>
<div id="comment-64414-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 18:52)</span> <span class="comment-user userinfo">CuriousPerso...</span>
</div>
</div>
</div>
<div id="comment-tools-64402" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64402-form-container" class="comment-form-container">
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

