+++
type = "question"
title = "How to extract/convert a large .osm into multiple smaller .osm tiles with libosmium C++?"
description = '''Hello, what I&#x27;m trying to achieve is that I&#x27;d like to split a large OSM file into smaller OSM files which are going to be based on web mercator tiles at a particular zoom level, let&#x27;s say 16. I&#x27;m aware of osmium-tool CLI and I know I could use this command:  osmium extract --bbox 28.97369384765625,4...'''
date = "2023-09-02T02:35:00Z"
lastmod = "2023-09-02T13:58:00Z"
weight = 87784
keywords = [ "osmium", "tiles", "osm" ]
aliases = [ "/questions/87784" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract/convert a large .osm into multiple smaller .osm tiles with libosmium C++?](/questions/87784/how-to-extractconvert-a-large-osm-into-multiple-smaller-osm-tiles-with-libosmium-c)

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
<span id="post-87784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87784-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, what I'm trying to achieve is that I'd like to split a large OSM file into smaller OSM files which are going to be based on web mercator tiles at a particular zoom level, let's say 16.</p>
<p>I'm aware of osmium-tool CLI and I know I could use this command:</p>
<blockquote>
<p>osmium extract --bbox 28.97369384765625,41.025499378313754,28.9764404296875,41.027571415339786 --strategy complete_ways -o smaller_tile.osm -f xml large_file.osm.pbf --overwrite</p>
</blockquote>
<p>The issue is that I needed to run a python script that executes the command above with different bbox boundaries (using mercantile package) — and every individual <code>osmium extract ...</code> run is parsing the source <code>large_file.osm.pbf</code> again and again, which makes the whole process rather slow and taking more time than necessary.</p>
<p>So, I'd like to code a C++ tool myself on top of libosmium directly and produce multiple osm files for tiles while handing the source OSM file.</p>
<p>I think I can implement a <code>osmium::handler::Handler</code> and use <code>osmium::apply(reader, handler)</code> API. However, I don't really know how I need to handle node, way and relation entires coming through. Would it be enough to check entry's coordinate against a tile boundary and put it into a map keyed with tile xy and later somehow build and write OSM file while iterating over the main tile-entry map?</p>
<p>A super small and simple example would be really useful for me to understand how I can implement a simpler and less sophisticated version of <code>osmium extract ...</code> by myself.</p>
<p>I'm hoping to find a direction and potentially also shed light on this for other for future reference, thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '23, 02:35</strong></p>
<img src="https://secure.gravatar.com/avatar/88ef3e2d478b563d0b8b6c29e503e641?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfatihmar&#39;s gravatar image" />
<p><span>mfatihmar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfatihmar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87784" class="comments-container">
<span id="87786"></span>
<div id="comment-87786" class="comment">
<div id="post-87786-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why do you want to do this? There may be an existing tool for your end goal.</p>
</div>
<div id="comment-87786-info" class="comment-info">
<span class="comment-age">(02 Sep '23, 10:26)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="87787"></span>
<div id="comment-87787" class="comment">
<div id="post-87787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm trying to break a large OSM file of a city into smaller chunks in web mercator tiles at a particular zoom level, so that I then convert them into 3D OBJ files and stream over the internet (over a real-time network connection). It's a pretty custom workflow and instead of hosting a full-blown tile-server, all I need is static OSM and OBJ files built/baked let's say every month automatically. I have looked at OSM2World, osmosis, osmium etc. and I think I need to write some custom tools on top of lower-level libraries like libosmium. Thank you for asking though :)</p>
</div>
<div id="comment-87787-info" class="comment-info">
<span class="comment-age">(02 Sep '23, 13:37)</span> <span class="comment-user userinfo">mfatihmar</span>
</div>
</div>
</div>
<div id="comment-tools-87784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87784-form-container" class="comment-form-container">
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

<span id="87785"></span>

<div id="answer-container-87785" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87785-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no "super small and simple example" because it is not a super small and simple problem you are trying to solve. You can look at the Osmium source code and find all the details in there.</p>
<p>I suggest a different approach: <code>osmium extract</code> can read a list of extracts to generate from a config file instead of getting the bounding box from the ocmmand line. You can auto-generate that config file. Be aware that there is a limit how many extracts you can generate in one go, though. That's just a question of memory usage. Every extract needs memory, see the man page for details. So for a practical use case you probably want to split the input file into, lets say 100 pieces and then run <code>osmium extract</code> again for each of the pieces to split them further.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '23, 08:05</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-87785" class="comments-container">
<span id="87788"></span>
<div id="comment-87788" class="comment">
<div id="post-87788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had a look at osmium extract and considered --config something.json option but the limits are simply too low for me. On the C++ side, reading and processing a 50-100MB .osm.pbf file is not a big deal but osmium-tool set the memory and file limits simply too low for the pipeline I'm trying to build.</p>
<p>I also had a look at these two places related: - <a href="https://github.com/osmcode/osmium-tool/issues/265">https://github.com/osmcode/osmium-tool/issues/265</a> - <a href="https://github.com/osmcode/osmium-tool/commit/353e9d565342af1ea703c56a15f41dc40732168a">https://github.com/osmcode/osmium-tool/commit/353e9d565342af1ea703c56a15f41dc40732168a</a></p>
<p>Perhaps it's a bit complex than I initially anticipated but at least currently, I'm thinking of processing relations first, ways second and nodes the last to determine dependencies between them and create&amp;use <code>osmium::io::Writer</code>s to write those osmium objects/elements into files. (I hope this would work!)</p>
<p>It is a little bit hard for me to read osmium-tool codebase (command-extract) and follow its logic. I will, however, use <code>osmium extract</code> outputs to compare it against my implementation's output to validate my work.</p>
<p>I wanted to see if there are hints/tips/tricks for this but apparently no, I need to implement a proper tool on top of libosmium.</p>
</div>
<div id="comment-87788-info" class="comment-info">
<span class="comment-age">(02 Sep '23, 13:58)</span> <span class="comment-user userinfo">mfatihmar</span>
</div>
</div>
</div>
<div id="comment-tools-87785" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87785-form-container" class="comment-form-container">
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

