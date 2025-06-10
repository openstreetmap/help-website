+++
type = "question"
title = "Switch2osm on Ubuntu 14:04: Map not displayed in the browser and mod_tile folder is empty."
description = '''Hi All, I tried to set MapServer (https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/), for iceland pdf. Every step before worked properly without any error outputs,but once rendered and restarted the apache server...on accessing http://localhost/osm_tiles/0/0/0.png is giving...'''
date = "2015-05-26T11:34:00Z"
lastmod = "2015-07-25T11:38:00Z"
weight = 43219
keywords = [ "rendering", "osm", "tileserver" ]
aliases = [ "/questions/43219" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Switch2osm on Ubuntu 14:04: Map not displayed in the browser and mod_tile folder is empty.](/questions/43219/switch2osm-on-ubuntu-1404-map-not-displayed-in-the-browser-and-mod_tile-folder-is-empty)

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
<span id="post-43219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43219-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I tried to set MapServer (<a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a>), for iceland pdf.</p>
<p>Every step before worked properly without any error outputs,but once rendered and restarted the apache server...on accessing <a href="http://localhost/osm_tiles/0/0/0.png">http://localhost/osm_tiles/0/0/0.png</a> is giving me NOT FOUND ERROR.</p>
<p>When I run "renderd -f -c /usr/local/etc/renderd.conf" I am getting the following console output</p>
<pre><code>$ sudo -u osmtileserver renderd -f -c /usr/local/etc/renderd.conf
renderd[10583]: Rendering daemon started
renderd[10583]: Initiating reqyest_queue
renderd[10583]: Parsing section renderd
renderd[10583]: Parsing render section 0
renderd[10583]: Parsing section mapnik
renderd[10583]: Parsing section default
renderd[10583]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[10583]: config renderd: num_threads=4
renderd[10583]: config renderd: num_slaves=0
renderd[10583]: config renderd: tile_dir=/var/lib/mod_tile
renderd[10583]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[10583]: config mapnik:  plugins_dir=/usr/local/lib/mapnik/input
renderd[10583]: config mapnik:  font_dir=/usr/share/fonts/truetype/ttf-dejavu
renderd[10583]: config mapnik:  font_dir_recurse=1
renderd[10583]: config renderd(0): Active
renderd[10583]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[10583]: config renderd(0): num_threads=4
renderd[10583]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[10583]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[10583]: config map 0:   name(default) file(/usr/local/share/maps/style/OSMBright/OSMBright.xml) uri(/osm_tiles/) htcp() host(localhost)
renderd[10583]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[10583]: Created server socket 4
renderd[10583]: Renderd is using mapnik version 2.2.0
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Bold.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Italic.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-BoldItalic.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-ExtraLight.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Oblique.ttf
renderd[10583]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf
Running in foreground mode...
renderd[10583]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[10583]: Loading parameterization function for 
renderd[10583]: Loading parameterization function for 
renderd[10583]: Loading parameterization function for 
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[10583]: Loading parameterization function for 
renderd[10583]: Using web mercator projection settings
renderd[10583]: Using web mercator projection settings
renderd[10583]: Using web mercator projection settings
renderd[10583]: Using web mercator projection settings</code></pre>
<p>for the command "service apache2 reload" (executed in a second session)</p>
<pre><code>$ 
$ service apache2 reload
 * Reloading web server apache2                                                  * 
$</code></pre>
<p>Searched through the web for a solution, but couldn't find any answers for my case. (all through I found people with similar problems but with different console output, so I didn’t apply to me)</p>
<p>Does anyone have any clue what my problem is?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '15, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/b8ec7bd9fecea0e4f0242f46abec2722?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rocko17&#39;s gravatar image" />
<p><span>rocko17</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rocko17 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jul '15, 11:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-43219" class="comments-container">
<span id="44419"></span>
<div id="comment-44419" class="comment">
<div id="post-44419-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have the same problem :( No solution anywhere! The only thing left is that you re-install everything from scratch. I am doing the same at this moment. Do tell if it works for you!</p>
</div>
<div id="comment-44419-info" class="comment-info">
<span class="comment-age">(25 Jul '15, 08:02)</span> <span class="comment-user userinfo">dmnw15</span>
</div>
</div>
</div>
<div id="comment-tools-43219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43219-form-container" class="comment-form-container">
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

<span id="44425"></span>

<div id="answer-container-44425" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44425-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://help.openstreetmap.org/users/11025/rocko17">@rocko17</a> That console output says that:</p>
<ol>
<li>renderd is running OK and can load the fonts it needs</li>
<li>It's not (at least in the snippet above) getting a request to render a tile</li>
</ol>
<p>The Apache restart says that it doesn't crash at that stage (unlike <a href="https://help.openstreetmap.org/questions/44098/switch2osm-on-ubuntu-1404-no-tiles-generated-suspected-apache-coredump">this</a> problem). There's no indication whether or not mod_tile is set up within Apache (it may be working but just not getting a request).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '15, 11:38</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-44425" class="comments-container">
&#10;</div>
<div id="comment-tools-44425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44425-form-container" class="comment-form-container">
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

