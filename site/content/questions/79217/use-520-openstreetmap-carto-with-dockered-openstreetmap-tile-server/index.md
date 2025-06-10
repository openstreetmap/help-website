+++
type = "question"
title = "Use &gt; 5.2.0 openstreetmap-carto with dockered  openstreetmap-tile-server"
description = '''I use OSM tile server deploying with docker from Overv&#x27;s repository and in default configuration it works pretty well. In the dockerfile I tried to manualy upgrade openstreetmap-carto version to the newest version (today 5.3.1) with just: RUN mkdir -p /home/renderer/src &#92;  &amp;amp;&amp;amp; cd /home/render...'''
date = "2021-03-11T16:00:00Z"
lastmod = "2021-03-12T10:19:00Z"
weight = 79217
keywords = [ "openstreetmap-carto", "tiles", "tileserver" ]
aliases = [ "/questions/79217" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Use \> 5.2.0 openstreetmap-carto with dockered openstreetmap-tile-server](/questions/79217/use-520-openstreetmap-carto-with-dockered-openstreetmap-tile-server)

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
<span id="post-79217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79217-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use OSM tile server deploying with docker from <a href="https://github.com/Overv/openstreetmap-tile-server">Overv's repository</a> and in default configuration it works pretty well. In the dockerfile I tried to manualy upgrade <code>openstreetmap-carto</code> version to the newest version (today 5.3.1) with just:</p>
<p><code>RUN mkdir -p /home/renderer/src \ &amp;&amp; cd /home/renderer/src \ &amp;&amp; git clone --single-branch --branch v5.3.0 </code><a href="https://github.com/gravitystorm/openstreetmap-carto.git"><code>https://github.com/gravitystorm/openstreetmap-carto.git</code></a><code> --depth 1 \ &amp;&amp; cd openstreetmap-carto \ &amp;&amp; rm -rf .git \ &amp;&amp; npm install -g carto@0.18.2 \ &amp;&amp; carto project.mml &gt; mapnik.xml \ &amp;&amp; scripts/get-shapefiles.py \ &amp;&amp; rm /home/renderer/src/openstreetmap-carto/data/*.zip</code><br />
but in the newer versions there is no <code>script/get-shapefiles.py</code> file, and building image crashed. I've checked and the highest version of <code>openstreetmap-carto</code> which include that file and builds successfully is <code>5.2.0</code>.<br />
</p>
<p>I have found in <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/v5.2.0/INSTALL.md">INSTALL.md</a> in "Manual download" chapter to download manually <code>*.zip</code> files and put them into <code>path/to/openstreetmap-carto/data</code> folder. But I can see that in deleted <code>get-shapefiles.py</code> script there is much more logic than just downloading files.<br />
Does anyone know if it's good way to use that carto version in OSM Tile server, or maybe there is another way I don't know?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '21, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/735ed8c1abf1a1f7b907b78d9594303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engopy&#39;s gravatar image" />
<p><span>engopy</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engopy has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-79217" class="comments-container">
&#10;</div>
<div id="comment-tools-79217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79217-form-container" class="comment-form-container">
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

<span id="79237"></span>

<div id="answer-container-79237" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79237-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Whenever the method that the "OSM Carto" map style uses for installation changes, sets of instructions for building it also need to change. I regularly update the guides at <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a> when people report that something no longer works.</p>
<p>The dockerfile at <a href="https://github.com/Overv/openstreetmap-tile-server/blob/master/Dockerfile">https://github.com/Overv/openstreetmap-tile-server/blob/master/Dockerfile</a> still has to do the same things, so if something changes between OSM Carto versions that will need updating too. I'd suggesting creating an issue <a href="https://github.com/Overv/openstreetmap-tile-server/issueshttps://github.com/Overv/openstreetmap-tile-server/issues">here</a> to explain the changes that you'd like to see, and (once that's all sorted) an issue <a href="https://github.com/switch2osm/switch2osm.github.io/issues/">here</a> requesting that the <a href="https://switch2osm.org/serving-tiles/using-a-docker-container/">https://switch2osm.org/serving-tiles/using-a-docker-container/</a> page is updated to the new version of the dockerfile. I know you're not using that latter page of course; just asking as a courtesy for everyone who does!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '21, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-79237" class="comments-container">
&#10;</div>
<div id="comment-tools-79237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79237-form-container" class="comment-form-container">
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

