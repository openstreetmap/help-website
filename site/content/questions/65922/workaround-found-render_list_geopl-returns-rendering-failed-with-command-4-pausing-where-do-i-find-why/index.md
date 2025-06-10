+++
type = "question"
title = "(Workaround found) render_list_geo.pl returns &quot;rendering failed with command 4, pausing&quot;, where do I find why?"
description = '''Have installed openstreetmap-carto on Ubuntu 18.04.  Have also imported whole planet into postgresql.  Using generate_tiles.py on a part of denmark, generate tiles pretty fast for zoom level 1-13 (about 6 minutes). When I try to generate for most of the world, first 4 tiles (zoom 1) took about 45 mi...'''
date = "2018-09-16T18:51:00Z"
lastmod = "2018-09-20T16:54:00Z"
weight = 65922
keywords = [ "rendering" ]
aliases = [ "/questions/65922" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [(Workaround found) render_list_geo.pl returns "rendering failed with command 4, pausing", where do I find why?](/questions/65922/workaround-found-render_list_geopl-returns-rendering-failed-with-command-4-pausing-where-do-i-find-why)

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
<span id="post-65922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65922-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Have installed openstreetmap-carto on Ubuntu 18.04. Have also imported whole planet into postgresql. Using generate_tiles.py on a part of denmark, generate tiles pretty fast for zoom level 1-13 (about 6 minutes).</p>
<p>When I try to generate for most of the world, first 4 tiles (zoom 1) took about 45 minutes. (When I opened another terminal window and run top (while the generate_tiles.py was running), then I can see that there are many postgresql processes, but most of them are marked with D in the S column, and sometimes R. I do not understand why they are not running most of the time)</p>
<p><strong>UPDATE START</strong> I added some indexes to the database, and now the generate_tiles.py is flying, and generating tiles superfast. As much as I would like to get renderd to work, it is not so important anymore since what I need is to pre-render the tiles. Since this now works so fast, I can skip fiddling with renderd and the perl script I mentioned below (for now). <strong>UPDATE END</strong></p>
<p>So I just closed the terminal window and installed the script render_list_geo.pl, to see if there was any improvement. This is what I get in the terminal window when I run the script for a part of denmark:</p>
<pre><code>    ./render_list_geo.pl -n 4 -m default -z 7 -Z 7 -x 7.9 -X 10.97 -y 55.39 -Y 57.06
&#10;Rendering started at: sø. 16. sep. 19:31:50 +0200 2018
&#10;render_list -a -z 7 -Z 7 -x 66 -X 71 -y 39 -Y 47 -n 4 -m default
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
Rendering client
Starting 4 rendering threads
Rendering all tiles from zoom 7 to zoom 7
Rendering all tiles for zoom 7 from (66, 39) to (71, 47)
Waiting for rendering threads to finish
rendering failed with command 4, pausing.
rendering failed with command 4, pausing.
&#10;*****************************************************
*****************************************************
Total for all tiles rendered
Meta tiles rendered: Rendered 2 tiles in 10.00 seconds (0.20 tiles/s)
Total tiles rendered: Rendered 128 tiles in 10.00 seconds (12.80 tiles/s)
Total tiles handled: Rendered 2 tiles in 10.00 seconds (0.20 tiles/s)
*****************************************************
*****************************************************
*****************************************************
&#10;Zoom factor: 7 finished at
sø. 16. sep. 19:32:00 +0200 2018
&#10;Rendering finished at: sø. 16. sep. 19:32:00 +0200 2018
&#10;
&#10;**Which file or files do I have to inspect to find out what cause this:
&quot;rendering failed with command 4, pausing.&quot;**
&#10;When I look in the directory: /var/lib/mod_tile
then there is no tiles from the script (render_list_geo.pl).
&#10;When I look in the /var/log/syslog I see this, but did not understand much:
&#10;    Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Got incoming connection, fd 15, number 1
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Got incoming connection, fd 16, number 2
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Got incoming connection, fd 17, number 3
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Got incoming connection, fd 18, number 4
Sep 16 20:08:40 Mapnik render_list: DEBUG: Sending render cmd(6 default 7/66/39) with protocol version 2 to fd 3
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Failed to read cmd on fd 16
Sep 16 20:08:40 Mapnik render_list: DEBUG: Sending render cmd(6 default 7/66/47) with protocol version 2 to fd 6
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Connection 1, fd 16 closed, now 3 left
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Got incoming request with protocol version 2
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Got command RenderBulk fd(15) xml(default), z(7), x(66), y(39), mime(image/png), options()
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Failed to read cmd on fd 17
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Connection 1, fd 17 closed, now 2 left
Sep 16 20:08:40 Mapnik renderd[1438]: Received request for map layer &#39;default&#39; which failed to load
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Got incoming request with protocol version 2
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Sending render cmd(4 default 7/66/39) with protocol version 2 to fd 15
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Got command RenderBulk fd(18) xml(default), z(7), x(66), y(47), mime(image/png), options()
Sep 16 20:08:40 Mapnik render_list: DEBUG: Got incoming request with protocol version 2
Sep 16 20:08:40 Mapnik renderd[1438]: Received request for map layer &#39;default&#39; which failed to load
Sep 16 20:08:40 Mapnik renderd[1438]: DEBUG: Sending render cmd(4 default 7/66/47) with protocol version 2 to fd 18
Sep 16 20:08:40 Mapnik render_list: DEBUG: Got incoming request with protocol version 2
Sep 16 20:08:50 Mapnik renderd[1438]: DEBUG: Failed to read cmd on fd 15
Sep 16 20:08:50 Mapnik renderd[1438]: DEBUG: Connection 0, fd 15 closed, now 1 left
Sep 16 20:08:50 Mapnik renderd[1438]: DEBUG: Failed to read cmd on fd 18
Sep 16 20:08:50 Mapnik renderd[1438]: DEBUG: Connection 0, fd 18 closed, now 0 left
Sep 16 20:08:55 Mapnik org.gnome.Shell.desktop[1631]: Window manager warning: Buggy client sent a _NET_ACTIVE_WINDOW message with a timestamp of 0 for 0x3400081 (*syslog (/)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '18, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0da1f043b943c87172fb4dc60f017440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MapViking&#39;s gravatar image" />
<p><span>MapViking</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MapViking has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '18, 13:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-65922" class="comments-container">
<span id="65989"></span>
<div id="comment-65989" class="comment">
<div id="post-65989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a question here any more? Clearly something went wrong with the initial import if zoom 1 tiles took 45 minutes each, but it sounds like you have fixed that?</p>
</div>
<div id="comment-65989-info" class="comment-info">
<span class="comment-age">(20 Sep '18, 13:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="65993"></span>
<div id="comment-65993" class="comment">
<div id="post-65993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"Is there a question here any more?"</p>
<p>No, not after I found a workaround. If you want me to delete the whole thread, please let me know.</p>
</div>
<div id="comment-65993-info" class="comment-info">
<span class="comment-age">(20 Sep '18, 16:54)</span> <span class="comment-user userinfo">MapViking</span>
</div>
</div>
</div>
<div id="comment-tools-65922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65922-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

