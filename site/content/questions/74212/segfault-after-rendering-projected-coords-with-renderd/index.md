+++
type = "question"
title = "segfault after rendering projected coords with renderd"
description = '''Following the switch2osm guide I&#x27;ve made it to renderd -f -c /usr/local/etc/renderd.conf and navigate to http://localhost/0/0/0.png renderd produces this output:  renderd[17748]: Using web mercator projection settings renderd[17748]: Using web mercator projection settings renderd[17748]: Using web m...'''
date = "2020-04-15T22:59:00Z"
lastmod = "2020-04-27T18:55:00Z"
weight = 74212
keywords = [ "segfault", "renderd", "mapnik" ]
aliases = [ "/questions/74212" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [segfault after rendering projected coords with renderd](/questions/74212/segfault-after-rendering-projected-coords-with-renderd)

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
<span id="post-74212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74212-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Following the switch2osm guide I've made it to <code>renderd -f -c /usr/local/etc/renderd.conf</code> and navigate to <a href="http://localhost/0/0/0.png">http://localhost/0/0/0.png</a> renderd produces this output:</p>
<p><code>renderd[17748]: Using web mercator projection settings renderd[17748]: Using web mercator projection settings renderd[17748]: Using web mercator projection settings renderd[17748]: Using web mercator projection settings renderd[17748]: Using web mercator projection settings renderd[17748]: Using web mercator projection settings renderd[17748]: Using web mercator projection settings renderd[17748]: Using web mercator projection settings renderd[17748]: DEBUG: Got incoming connection, fd 5, number 1 renderd[17748]: DEBUG: Got incoming request with protocol version 2 renderd[17748]: DEBUG: Got command RenderPrio fd(5) xml(ajt), z(0), x(0), y(0), mime(image/png), options() renderd[17748]: DEBUG: START TILE ajt 0 0-0 0-0, new metatile renderd[17748]: Rendering projected coordinates 0 0 0 -&gt; -20037508.342800|-20037508.342800 20037508.342800|20037508.342800 to a 1 x 1 tile Segmentation fault</code></p>
<p>The start of renderd running is:<br />
` renderd[17748]: Rendering daemon started<br />
renderd[17748]: Initiating request_queue<br />
renderd[17748]: Parsing section renderd<br />
renderd[17748]: Parsing render section 0<br />
renderd[17748]: Parsing section mapnik<br />
renderd[17748]: Parsing section ajt<br />
renderd[17748]: config renderd: unix socketname=/var/run/renderd/renderd.sock<br />
renderd[17748]: config renderd: num_threads=8<br />
renderd[17748]: config renderd: num_slaves=0<br />
renderd[17748]: config renderd: tile_dir=/var/lib/mod_tile<br />
renderd[17748]: config renderd: stats_file=/var/run/renderd/renderd.stats<br />
renderd[17748]: config mapnik: plugins_dir=/usr/lib/mapnik/3.0/input<br />
renderd[17748]: config mapnik: font_dir=/usr/share/fonts/opentype/noto<br />
renderd[17748]: config mapnik: font_dir_recurse=1<br />
renderd[17748]: config renderd(0): Active<br />
renderd[17748]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock<br />
renderd[17748]: config renderd(0): num_threads=8<br />
renderd[17748]: config renderd(0): tile_dir=/var/lib/mod_tile<br />
renderd[17748]: config renderd(0): stats_file=/var/run/renderd/renderd.stats<br />
renderd[17748]: config map 0: name(ajt) file(/home/mseagle/anritsu/mapping/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp() host(localhost)<br />
renderd[17748]: Initialising unix server socket on /var/run/renderd/renderd.sock<br />
renderd[17748]: Created server socket 4<br />
renderd[17748]: Renderd is using mapnik version 3.0.23<br />
renderd[17748]: DEBUG: Loading font: /usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc<br />
renderd[17748]: DEBUG: Loading font: /usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc<br />
renderd[17748]: DEBUG: Loading font: /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc<br />
renderd[17748]: DEBUG: Loading font: /usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc<br />
Running in foreground mode...<br />
renderd[17748]: Starting stats thread<br />
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile<br />
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile<br />
renderd[17748]: Loading parameterization function for<br />
renderd[17748]: Loading parameterization function for<br />
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile<br />
renderd[17748]: Loading parameterization function for<br />
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile<br />
renderd[17748]: Loading parameterization function for<br />
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile<br />
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile<br />
renderd[17748]: Loading parameterization function for<br />
renderd[17748]: Loading parameterization function for debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile</p>
<p>renderd[17748]: Loading parameterization function for<br />
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile<br />
renderd[17748]: Loading parameterization function for<br />
Mapnik LOG&gt; 2020-04-15 14:28:16: warning: unable to find face-name 'Noto Sans Regular' in FontSet 'fontset-0'<br />
`</p>
<p>followed by a whole plethora of unable to find font x which can be found in the full output in this pastebin: <a href="https://pastebin.com/PGZvztUu">full output</a></p>
<p>dmesg shows this output:<br />
<code>[ 4140.665927] renderd[17755]: segfault at 0 ip 00007f873cd60084 sp 00007f8722fd1a70 error 4 in libmapnik.so.3.0.23[7f873c816000+949000] [ 4140.665931] Code: 00 00 00 00 00 90 e9 eb 92 ab ff 66 2e 0f 1f 84 00 00 00 00 00 90 53 48 89 fb 48 8b 7e 08 48 8b 35 f9 2c 51 00 48 39 f7 74 0e &lt;80&gt; 3f 2a 74 17 e8 a2 b2 ab ff 85 c0 75 0e 48 8d 43 10 5b c3 0f 1f</code></p>
<p>Any help is appreciated to even point me in the right direction.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-segfault" rel="tag" title="see questions tagged &#39;segfault&#39;">segfault</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '20, 22:59</strong></p>
<img src="https://secure.gravatar.com/avatar/10205e855d83b6ba480cb3023babfbc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mseagull&#39;s gravatar image" />
<p><span>mseagull</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mseagull has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-74212" class="comments-container">
<span id="74380"></span>
<div id="comment-74380" class="comment">
<div id="post-74380-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What OS are you using, how much memory have you got and what data did you load?</p>
<p>Any diversions from the switch2osm guide (perhaps, starting from a slightly differet place in terms of installed components)?</p>
</div>
<div id="comment-74380-info" class="comment-info">
<span class="comment-age">(26 Apr '20, 17:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="74424"></span>
<div id="comment-74424" class="comment">
<div id="post-74424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Debian 10, all the other steps have worked fine. I have 16 Gigs on a 4790K. Rendering the small city of Morgan Hill, CA U.S. I did compile mapnik/mapnik-python manually but it all seems hooked up fine.</p>
<p>As a note, after another day and being unable to figure it out, I switched to my server, a Phenom II X4 BE on 16 gigs running Ubuntu 16 LTS and it works well. Same area, same process as my other system. So possibly just to do with Debian 10?</p>
<p>I'm now looking for information on ways to cross compile the stack.</p>
</div>
<div id="comment-74424-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 18:28)</span> <span class="comment-user userinfo">mseagull</span>
</div>
</div>
<span id="74425"></span>
<div id="comment-74425" class="comment">
<div id="post-74425-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Debian 10</p>
</blockquote>
<p>Ah, OK. I'm not aware of a recent "known working" set of instructions there, apart from using Docker (which you presumably don't want to do). I've certainly had problems of that sort on Debian in the past (and problems reliably building mapnik et al elsewhere). <a href="https://wiki.debian.org/OSM/tileserver/jessie">https://wiki.debian.org/OSM/tileserver/jessie</a> is ancient history now as far as postgres et al is concerned (although still supported for another month!).</p>
<blockquote>
<p>I'm now looking for information on ways to cross compile the stack.</p>
</blockquote>
<p>What problem are you trying to solve by doing here?</p>
</div>
<div id="comment-74425-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 18:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="74426"></span>
<div id="comment-74426" class="comment">
<div id="post-74426-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Having a local mapping server on an arm based embedded device.</p>
<p>Thanks for the response.</p>
</div>
<div id="comment-74426-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 18:50)</span> <span class="comment-user userinfo">mseagull</span>
</div>
</div>
<span id="74427"></span>
<div id="comment-74427" class="comment">
<div id="post-74427-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. If you come up with anything that would be a useful addition to <a href="https://github.com/switch2osm/switch2osm.github.io">https://github.com/switch2osm/switch2osm.github.io</a> please let us know :)</p>
</div>
<div id="comment-74427-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 18:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74212-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

