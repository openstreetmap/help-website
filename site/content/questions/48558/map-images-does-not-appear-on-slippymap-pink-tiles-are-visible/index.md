+++
type = "question"
title = "map images does not appear on slippymap, pink tiles are visible"
description = '''this is what can be seen while rendering sudo -u tharakk renderd -f -c /usr/local/etc/renderd.conf renderd[31905]: Rendering daemon started renderd[31905]: Initiating reqyest_queue renderd[31905]: Parsing section renderd renderd[31905]: Parsing render section 0 renderd[31905]: Parsing section mapnik...'''
date = "2016-03-08T07:53:00Z"
lastmod = "2016-03-14T05:05:00Z"
weight = 48558
keywords = [ "map", "renderd", "localhost", "slippymap", "mod_tile" ]
aliases = [ "/questions/48558" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [map images does not appear on slippymap, pink tiles are visible](/questions/48558/map-images-does-not-appear-on-slippymap-pink-tiles-are-visible)

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
<span id="post-48558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48558-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>this is what can be seen while rendering <strong>sudo -u tharakk renderd -f -c /usr/local/etc/renderd.conf</strong></p>
<pre><code>renderd[31905]: Rendering daemon started
renderd[31905]: Initiating reqyest_queue
renderd[31905]: Parsing section renderd
renderd[31905]: Parsing render section 0
renderd[31905]: Parsing section mapnik
renderd[31905]: Parsing section default
renderd[31905]: Parsing section style2
renderd[31905]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[31905]: config renderd: num_threads=4
renderd[31905]: config renderd: num_slaves=0
renderd[31905]: config renderd: tile_dir=/var/lib/mod_tile
renderd[31905]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[31905]: config mapnik:  plugins_dir=/usr/local/lib/mapnik/input
renderd[31905]: config mapnik:  font_dir=/usr/share/fonts/truetype/ttf-dejavu
renderd[31905]: config mapnik:  font_dir_recurse=1
renderd[31905]: config renderd(0): Active
renderd[31905]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[31905]: config renderd(0): num_threads=4
renderd[31905]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[31905]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[31905]: config map 0:   name(default) file(/usr/local/share/maps/style/OSMBright/OSMBright.xml) uri(/osm/) htcp() host(localhost)
renderd[31905]: config map 1:   name(style2) file() uri() htcp() host()
renderd[31905]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[31905]: Created server socket 4
renderd[31905]: Renderd is using mapnik version 2.2.0
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Italic.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Bold.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Oblique.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-BoldItalic.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-ExtraLight.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf
renderd[31905]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf
Running in foreground mode...
renderd[31905]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[31905]: Loading parameterization function for 
renderd[31905]: Loading parameterization function for 
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[31905]: Loading parameterization function for 
renderd[31905]: Loading parameterization function for 
renderd[31905]: Using web mercator projection settings
renderd[31905]: Using web mercator projection settings
renderd[31905]: Using web mercator projection settings
renderd[31905]: Using web mercator projection settings</code></pre>
<p>this is what happens when i restart apache</p>
<pre><code>* Restarting web server apache2                                                                                                                                        [Tue Mar 08 12:59:41.710074 2016] [tile:notice] [pid 31978] Loading tile config default at /osm/ for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png
&#10;[Tue Mar 08 12:59:41.710146 2016] [tile:notice] [pid 31978] Loading tile config style2 at  for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png
    AH00558: apache2: Could not reliably determine the server&#39;s fully qualified domain name, using 127.0.1.1. Set the &#39;ServerName&#39; directive globally to suppress this message</code></pre>
<p>but it will give me pink maps when i try <strong><a href="http://localhost:8080/osm/slippymap.html">http://localhost:8080/osm/slippymap.html</a></strong> or <strong><a href="http://localhost/osm/0/0/0.png">http://localhost/osm/0/0/0.png</a></strong> giving me the error on the browser</p>
<pre><code>`failed to load resource: net::ERR_CONNECTION_REFUSED`</code></pre>
<p>I found the same problem and tried to change localhost path in slippymap.html but no luck This is my osm layer in slippymap</p>
<pre><code>var layer = new OpenLayers.Layer.OSM(&#39;My Layer&#39;, &#39;${z}/${x}/${y}.png&#39;, {
            format: &#39;image/png&#39;,
            layers: &#39;my:layer&#39;
        }, {
            ttileOptions: {crossOriginKeyword: &#39;anonymous&#39;},
            transitionEffect: null
        });
        map.addLayer(layer);</code></pre>
<p>i am using linux mint platform and no Virtual machines involved. I carefully followed the instructions from <strong><a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></strong>. I am using apache to load tiles and apache is on port 8080. my /var/lib/mod_tiles look like this after rendering,</p>
<pre><code>tharakk@nimbusthree-G500 /var/lib/mod_tile $ ls -la
total 12
drwxrwxrwx  3 tharakk root    4096 මාර්  11 15:38 .
drwxr-xr-x 79 root    root    4096 මාර්  11 11:42 ..
drwxr-xr-x 13 tharakk tharakk 4096 මාර්  11 16:03 default</code></pre>
<p><a href="http://localhost:8080/mod_tile">http://localhost:8080/mod_tile</a> will return this on browser</p>
<pre><code>NoResp200: 0
NoResp304: 0
NoResp404: 0
NoResp503: 0
NoResp5XX: 0
NoRespOther: 0
NoFreshCache: 0
NoOldCache: 0
NoVeryOldCache: 0
NoFreshRender: 0
NoOldRender: 0
NoVeryOldRender: 0
NoRespZoom00: 0
NoRespZoom01: 0
NoRespZoom02: 0
NoRespZoom03: 0
NoRespZoom04: 0
NoRespZoom05: 0
NoRespZoom06: 0
NoRespZoom07: 0
NoRespZoom08: 0
NoRespZoom09: 0
NoRespZoom10: 0
NoRespZoom11: 0
NoRespZoom12: 0
NoRespZoom13: 0
NoRespZoom14: 0
NoRespZoom15: 0
NoRespZoom16: 0
NoRespZoom17: 0
NoRespZoom18: 0
NoRespZoom19: 0
NoRespZoom20: 0
NoTileBufferReads: 0
DurationTileBufferReads: 0
NoTileBufferReadZoom00: 0
DurationTileBufferReadZoom00: 0
NoTileBufferReadZoom01: 0
DurationTileBufferReadZoom01: 0
NoTileBufferReadZoom02: 0
DurationTileBufferReadZoom02: 0
NoTileBufferReadZoom03: 0
DurationTileBufferReadZoom03: 0
NoTileBufferReadZoom04: 0
DurationTileBufferReadZoom04: 0
NoTileBufferReadZoom05: 0
DurationTileBufferReadZoom05: 0
NoTileBufferReadZoom06: 0
DurationTileBufferReadZoom06: 0
NoTileBufferReadZoom07: 0
DurationTileBufferReadZoom07: 0
NoTileBufferReadZoom08: 0
DurationTileBufferReadZoom08: 0
NoTileBufferReadZoom09: 0
DurationTileBufferReadZoom09: 0
NoTileBufferReadZoom10: 0
DurationTileBufferReadZoom10: 0
NoTileBufferReadZoom11: 0
DurationTileBufferReadZoom11: 0
NoTileBufferReadZoom12: 0
DurationTileBufferReadZoom12: 0
NoTileBufferReadZoom13: 0
DurationTileBufferReadZoom13: 0
NoTileBufferReadZoom14: 0
DurationTileBufferReadZoom14: 0
NoTileBufferReadZoom15: 0
DurationTileBufferReadZoom15: 0
NoTileBufferReadZoom16: 0
DurationTileBufferReadZoom16: 0
NoTileBufferReadZoom17: 0
DurationTileBufferReadZoom17: 0
NoTileBufferReadZoom18: 0
DurationTileBufferReadZoom18: 0
NoTileBufferReadZoom19: 0
DurationTileBufferReadZoom19: 0
NoTileBufferReadZoom20: 0
DurationTileBufferReadZoom20: 0</code></pre>
<p>but when i prerender using it renders like this and metatiles are created in <strong>/var/lib/mod_tile</strong> folder</p>
<pre><code>cd ~/src/mod_tile
time ./render_list -m default -a -z 0 -Z 10
&#10;DEBUG: DONE TILE default 10 264-271 416-423 in 0.523 seconds
renderd[8432]: DEBUG: Sending render cmd(3 default 10/264/416) with protocol version 2 to fd 8
renderd[8432]: DEBUG: Got incoming request with protocol version 2
renderd[8432]: DEBUG: Got command RenderBulk fd(8) xml(default), z(10), x(264), y(424), mime(image/png), options()
renderd[8432]: DEBUG: START TILE default 10 264-271 424-431, new metatile
renderd[8432]: Rendering projected coordinates 10 264 424 -&gt; -9705668.103544|3130860.678562 -9392582.035687|3443946.746419 to a 8 x 8 tile</code></pre>
<p>all looks good but what did i do wrong here? Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-localhost" rel="tag" title="see questions tagged &#39;localhost&#39;">localhost</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '16, 07:53</strong></p>
<img src="https://secure.gravatar.com/avatar/226294f6552d8c74ee10799c893da4e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tharaka%20Rajith&#39;s gravatar image" />
<p><span>Tharaka Rajith</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tharaka Rajith has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '16, 11:00</strong> </span></p>
</div>
</div>
<div id="comments-container-48558" class="comments-container">
<span id="48570"></span>
<div id="comment-48570" class="comment">
<div id="post-48570-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Low zoom tiles will typically take substantially longer to render than the browser/whatever timeout. Have you checked that they are not eventually getting created?</p>
<p>I would further suggest checking if there is actually a webserver running on localhost ports 80 and 8080.</p>
</div>
<div id="comment-48570-info" class="comment-info">
<span class="comment-age">(08 Mar '16, 13:39)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="48586"></span>
<div id="comment-48586" class="comment">
<div id="post-48586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank You SimonPoole. yes my apache is on port 8080, mod tiles are created in /var/lib/mod_tiles after rendering &amp; also apache is not giving errors when restarting after rendering.i have updated the above path directory.</p>
</div>
<div id="comment-48586-info" class="comment-info">
<span class="comment-age">(09 Mar '16, 04:13)</span> <span class="comment-user userinfo">Tharaka Rajith</span>
</div>
</div>
<span id="48632"></span>
<div id="comment-48632" class="comment">
<div id="post-48632-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I somehow suspect that mod_tile is not finding your tiles/that there is a config error or difference between renderd.conf and the mod_tile configuration (alternatively your layer config on the test web page might be wrong).</p>
</div>
<div id="comment-48632-info" class="comment-info">
<span class="comment-age">(11 Mar '16, 14:56)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="48647"></span>
<div id="comment-48647" class="comment">
<div id="post-48647-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank You SimonPoole. Yes my layer config in slippymap.html should be wrong.But I can't think of why <a href="http://localhost:8080/mod_tile">http://localhost:8080/mod_tile</a> will give the above result and http:localhost/osm_tiles/0/0/0.png &amp; <a href="http://localhost:8080/osm_tiles/0/0/0.png">http://localhost:8080/osm_tiles/0/0/0.png</a> will gice 404 error since i followed Configure renderd, Configure mod_tile only according to <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></p>
</div>
<div id="comment-48647-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 05:05)</span> <span class="comment-user userinfo">Tharaka Rajith</span>
</div>
</div>
</div>
<div id="comment-tools-48558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48558-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

