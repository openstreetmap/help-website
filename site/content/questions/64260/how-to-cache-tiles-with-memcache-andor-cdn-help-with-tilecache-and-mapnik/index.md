+++
type = "question"
title = "How to cache Tiles with Memcache and/or CDN? Help with TileCache and Mapnik"
description = '''Hello everyone, So I&#x27;ve used @SomeoneElse&#x27;s guide to creating a tile server. Right now the renderd tiles are being cached/stored in a folder system on the server /var/lib/mod_tile/&amp;lt;map name=&quot;&quot;&amp;gt;. We&#x27;re trying to figure out if there are any ways to cut the costs of requests and cache tiles with ...'''
date = "2018-06-19T19:23:00Z"
lastmod = "2018-06-19T22:47:00Z"
weight = 64260
keywords = [ "tilecache", "cdn", "cache", "proxy", "mapnik" ]
aliases = [ "/questions/64260" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to cache Tiles with Memcache and/or CDN? Help with TileCache and Mapnik](/questions/64260/how-to-cache-tiles-with-memcache-andor-cdn-help-with-tilecache-and-mapnik)

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
<span id="post-64260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64260-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>So I've used <a href="https://wiki.openstreetmap.org/wiki/Use%20…%20erver_load"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>'s guide to creating a tile server</a>. Right now the renderd tiles are being cached/stored in a folder system on the server /var/lib/mod_tile/&lt;map name=""&gt;.</p>
<p>We're trying to figure out if there are any ways to cut the costs of requests and cache tiles with memcache and/or CDN. Our server will be getting about 1k-10k requests per minute. We've already installed the mapnik vector tiles in order to cut costs (<a href="https://github.com/mapbox/mapnik-vector-tile).">https://github.com/mapbox/mapnik-vector-tile).</a> We're trying to figure out how much this will cost and if we could possibly knock those costs down.</p>
<p>I know that there is an option to use <a href="https://wiki.openstreetmap.org/wiki/Tile_Proxy/squid">Squid Cache</a>, so I imagine that someone has done it for memcache and a CDN.</p>
<p>However, I have not found anything online of anyone doing this before.</p>
<p>Has anyone here used memcache and/or a CDN in the past with their tile server, and what steps need to be done for both of these methods?</p>
<hr />
<p>I have been toying around with <a href="https://www.tilecache.org">TileCache</a>, using mod_wsgi, and Mapnik; however, I have run into two problems...</p>
<ol>
<li>I have gotten TileCache to serve tiles. However, these tiles are blank blue ocean tiles. There seems to be a problem with TileCache reading Mapnik's xml file.</li>
<li>I rendered the XML file by using carto of the style's mml file and converting it to the xml. When I use renderd to render these tiles using the xml, it works fine.</li>
<li>TileCache is an old code base. The last time it was updated was 4 years ago and the documentation last updated 8 years ago.</li>
</ol>
<p>So my questions here are:</p>
<p>First, has anyone run into this issue before using TileCache, and if so how did you fix it? Or any ideas on how to fix this issue of the blank tiles.</p>
<p>Second, are there any suitable replacements for TileCache? As I stated above, I am aware of Squid and am also aware of the other <a href="https://wiki.openstreetmap.org/wiki/Tile_proxy">Tile Proxies</a>, but they do not give me the load that these options can handle. If any of these works better or there is a better caching system out there, <strong>PLEASE</strong> let me know.</p>
<p>Thank you all so much,</p>
<p>Will</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilecache" rel="tag" title="see questions tagged &#39;tilecache&#39;">tilecache</span> <span class="post-tag tag-link-cdn" rel="tag" title="see questions tagged &#39;cdn&#39;">cdn</span> <span class="post-tag tag-link-cache" rel="tag" title="see questions tagged &#39;cache&#39;">cache</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '18, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/4a389be371e807913bffdbe1b2a9d671?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="willAirtory&#39;s gravatar image" />
<p><span>willAirtory</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="willAirtory has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '18, 20:39</strong> </span></p>
</div>
</div>
<div id="comments-container-64260" class="comments-container">
<span id="64283"></span>
<div id="comment-64283" class="comment">
<div id="post-64283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seriously... Any help at all would be appreciated immensely. Even pointing me towards a better site to ask this question if nobody here knows.</p>
</div>
<div id="comment-64283-info" class="comment-info">
<span class="comment-age">(19 Jun '18, 22:47)</span> <span class="comment-user userinfo">willAirtory</span>
</div>
</div>
</div>
<div id="comment-tools-64260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64260-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

