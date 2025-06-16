+++
type = "question"
title = "Tile Server ubuntu 14 not working"
description = '''Hi, I am a Linux newbie, and want to create a tile server on my Ubuntu computer for the application Xastir to grab maps (for ham radio APRS use). I am trying to test it out, but I am just getting pink tiles when I visit http://localhost/osm/slippymap.html and select &quot;local tiles&quot; The Command I ran w...'''
date = "2015-11-17T15:33:00Z"
lastmod = "2015-11-20T01:29:00Z"
weight = 46661
keywords = [ "tileserver" ]
aliases = [ "/questions/46661" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile Server ubuntu 14 not working](/questions/46661/tile-server-ubuntu-14-not-working)

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
<span id="post-46661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46661-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am a Linux newbie, and want to create a tile server on my Ubuntu computer for the application Xastir to grab maps (for ham radio APRS use).</p>
<p>I am trying to test it out, but I am just getting pink tiles when I visit <a href="http://localhost/osm/slippymap.html">http://localhost/osm/slippymap.html</a> and select "local tiles"</p>
<p>The Command I ran was</p>
<p>osm2pgsql --slim -C 1500 --number-processes 4 ireland-and-northern-ireland-latest.osm.pbf (I used the Ireland maps for testing, and I ran this command on the home directory, and the same directory as the html page.)</p>
<p>Here is how the above code finished executing:</p>
<pre><code>All indexes on  planet_osm_line created  in 730s
Completed planet_osm_line
Stopped table: planet_osm_ways in 1310s
Osm2pgsql took 3916s overall</code></pre>
<p>According to the <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">website</a></p>
<p>"If you are not opening slippymap.html on localhost and you are seeing only pink tiles, you will need to edit the html page and replace localhost with the correct server name in ‘new OpenLayers.Layer.OSM(“Local Tiles”…’ or change it to a relative URL."</p>
<p>Well, I am using localhost, and I don't know how to find the correct server name, nor what the relative URL means.</p>
<p>Could someone point me in the right direction?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Nov '15, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/b5d7e5fcef098b8ba280914b5ea846de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skyler&#39;s gravatar image" />
<p><span>Skyler</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skyler has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '15, 17:26</strong> </span></p>
</div>
</div>
<div id="comments-container-46661" class="comments-container">
<span id="46682"></span>
<div id="comment-46682" class="comment">
<div id="post-46682-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not sure about any solution, but maybe you kan do a search on this FAQ site for "localhost" ...</p>
</div>
<div id="comment-46682-info" class="comment-info">
<span class="comment-age">(18 Nov '15, 17:03)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-46661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46661-form-container" class="comment-form-container">
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

<span id="46683"></span>

<div id="answer-container-46683" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46683-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Taking a bit of a step back, it's worth checking that tiles are being generated. Here's a location in Ireland (using osm.org to display it):</p>
<p><a href="https://www.openstreetmap.org/#map=18/54.50222/-8.18998">https://www.openstreetmap.org/#map=18/54.50222/-8.18998</a></p>
<p>and if I right-click in the browser and "View image" the browser URL changes to:</p>
<p><a href="http://b.tile.openstreetmap.org/18/125108/83543.png">http://b.tile.openstreetmap.org/18/125108/83543.png</a></p>
<p>The first part of this - "b.tile.openstreetmap.org" describes the server that's serving the tiles out. The second part "/18/125108/83543.png" is the path to one particular tile.</p>
<p>It's a while since I've been through a "from packages", but from memory the URL for an individual tile is likely to be something like:</p>
<p><a href="http://localhost/osm/18/125108/83543.png">http://localhost/osm/18/125108/83543.png</a></p>
<p>When you go to this URL on a web browser on the same machine that you have gone through the "switch2osm" instructions on, you should see (after a short delay) is a map tile with an "Abrakebabra" on it, similar to what you get from "openstreetmap.org". If that doesn't work try just:</p>
<p><a href="http://localhost/">http://localhost/</a></p>
<p>and see what happens. "localhost" is just a name used to refer to the IPv4 address of the local machine - "127.0.0.1". If you know an actual IP address of the machine you've installed on you can replace "localhost" with that. Supposing I know that I'd installed on a machine with IP address "192.168.101.41" I could browse to:</p>
<p><a href="http://192.168.101.41/osm/18/125108/83543.png">http://192.168.101.41/osm/18/125108/83543.png</a></p>
<p>to see the same tile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '15, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-46683" class="comments-container">
<span id="46694"></span>
<div id="comment-46694" class="comment">
<div id="post-46694-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are no tiles. I can't find any PNG files on my system that were generated. When I right click on the image it says "not found" weather I view from localhost or the local IP.</p>
</div>
<div id="comment-46694-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 02:08)</span> <span class="comment-user userinfo">Skyler</span>
</div>
</div>
<span id="46707"></span>
<div id="comment-46707" class="comment">
<div id="post-46707-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I wouldn't expect to see .png files on disk - I'd expect to see ".meta" files (each one combining several .pngs) in directories below e.g. /var/lib/mod_tile/default/ (though "default" might be different for you).</p>
<p>When "it says not found", what was the full URL of the thing that it said was not found?</p>
</div>
<div id="comment-46707-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 09:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46731"></span>
<div id="comment-46731" class="comment">
<div id="post-46731-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The requested URL /osm/18/125108/83543.png was not found on this server.</p>
</div>
<div id="comment-46731-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 01:18)</span> <span class="comment-user userinfo">Skyler</span>
</div>
</div>
<span id="46732"></span>
<div id="comment-46732" class="comment">
<div id="post-46732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is definitely something wrong with my tile server. In /var/lib/mod_tile, there is only a file by the name of planet_import_complete.</p>
<p>When I looked at this file with nano, it was blank.</p>
</div>
<div id="comment-46732-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 01:29)</span> <span class="comment-user userinfo">Skyler</span>
</div>
</div>
</div>
<div id="comment-tools-46683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46683-form-container" class="comment-form-container">
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

