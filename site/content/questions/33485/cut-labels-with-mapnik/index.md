+++
type = "question"
title = "Cut Labels with Mapnik"
description = '''I&#x27;m getting cut labels on my maps. Same thing is happening on the main map here: https://www.openstreetmap.org/#map=11/52.3303/-1.3774 (look between Coventry and Rugby) Anyone know how to fix them? I made a dynamic tileserver with Mapnik, renderd and Apache mod-tile. Also made a static one with Mapni...'''
date = "2014-05-26T18:12:00Z"
lastmod = "2017-04-12T16:54:00Z"
weight = 33485
keywords = [ "labels", "osm.xml", "cut", "mapnik" ]
aliases = [ "/questions/33485" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Cut Labels with Mapnik](/questions/33485/cut-labels-with-mapnik)

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
<span id="post-33485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33485-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm getting cut labels on my maps. Same thing is happening on the main map here:</p>
<p><a href="https://www.openstreetmap.org/#map=11/52.3303/-1.3774">https://www.openstreetmap.org/#map=11/52.3303/-1.3774</a></p>
<p>(look between Coventry and Rugby)</p>
<p>Anyone know how to fix them?</p>
<p>I made a dynamic tileserver with Mapnik, renderd and Apache mod-tile. Also made a static one with Mapnik and generate_tiles.py to make the tiles. Same thing is happening in both cases.</p>
<p>Did some research and discovered that the problem is caused by not having a buffer around the rendered tiles. So I stated a buffer size in my main xml style file (osm.xml):</p>
<p>&lt;Map background-color="#b5d0d0" buffer-size="128" srs="&amp;srs900913;" minimum-version="2.0.0"&gt;</p>
<p>Did so for the dynamic and the static servers. Made no difference. Tried different sizes for the buffer: 256, 1024, made no difference. I know osm.xml is being loaded because every time I edit it I change the background colour and I can see the new colour in newly rendered tiles.</p>
<p>So Mapnik is reading osm.xml but apparently ignoring the buffer size. Why so?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-osm.xml" rel="tag" title="see questions tagged &#39;osm.xml&#39;">osm.xml</span> <span class="post-tag tag-link-cut" rel="tag" title="see questions tagged &#39;cut&#39;">cut</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '14, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/11e6e819b91b4d177c249c5123d2fa15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Charles%20Sweeney&#39;s gravatar image" />
<p><span>Charles Sweeney</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Charles Sweeney has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33485" class="comments-container">
&#10;</div>
<div id="comment-tools-33485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33485-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="33509"></span>

<div id="answer-container-33509" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33509-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Fixed it myself. Not sure if it's the "correct" solution but it works very well for me and gets rid of all the cut labels.</p>
<p>Used "avoid-edges" in the xml.</p>
<p>On the dynamic server (Mapnik, renderd, mod_tile):</p>
<p>Edited the main xml file /etc/mapnik-osm-data/osm.xml</p>
<p>Added the "avoid-edges" parameter with a value of "true" to every instance of the &lt;ShieldSymbolizer&gt; tag (13 of them). So for example, this line:</p>
<p>&lt;ShieldSymbolizer size="10" fill="#fff" placement="line" file="&amp;symbols;/mot_shield[length].png" spacing="750" minimum-distance="30" fontset-name="bold-fonts"&gt;[ref]&lt;/ShieldSymbolizer&gt;</p>
<p>...became:</p>
<p>&lt;ShieldSymbolizer size="10" fill="#fff" avoid-edges="true" placement="line" file="&amp;symbols;/mot_shield[length].png" spacing="750" minimum-distance="30" fontset-name="bold-fonts"&gt;[ref]&lt;/ShieldSymbolizer&gt;</p>
<p>After editing, stop and start renderd:</p>
<p>/etc/init.d/renderd stop</p>
<p>/etc/init.d/renderd start</p>
<p>You can go to a new area of the map to see newly generated tiles to see the effect of the changes. In my case on a test server I deleted ALL existing tiles, then went onto the map again, getting every tile fresh.</p>
<p>The tiles are here (on my setup):</p>
<p>/var/lib/mod_tile/default</p>
<p>To delete all the tiles, delete the "default" directory:</p>
<p>cd /var/lib/mod_tile/</p>
<p>rm -fr default</p>
<p>The "default" directory is automatically created again the next time a tile is rendered.</p>
<p>I was delighted with the result. My worry was that there would be more labels and pairs of labels where there was previously cut labels, but to my pleasant surprise there was the same number of labels as before but those that were previously cut had been moved slightly (within the edge of the tile) and displayed perfectly!</p>
<p>Still had buffer-size="128" in the &lt;Map&gt; attribute, though not sure if that is necessary as it didn't appear to make any difference there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '14, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/11e6e819b91b4d177c249c5123d2fa15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Charles%20Sweeney&#39;s gravatar image" />
<p><span>Charles Sweeney</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Charles Sweeney has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33509" class="comments-container">
<span id="33510"></span>
<div id="comment-33510" class="comment">
<div id="post-33510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>similar solutions for the label cutting problem are discussed in this video <a href="http://stateofthemap.us/session/advanced-cartocss-tricks/,">http://stateofthemap.us/session/advanced-cartocss-tricks/,</a> but for CartoCss</p>
</div>
<div id="comment-33510-info" class="comment-info">
<span class="comment-age">(27 May '14, 17:17)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-33509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33509-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55502"></span>

<div id="answer-container-55502" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55502-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi. I applied the solution above, but I am still having road labels being a little cut off. Why is this and can I fix it ?</p>
<p><img src="/upfiles/s3.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '17, 23:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f98ed179efe75af596090a497cefeb90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koles500&#39;s gravatar image" />
<p><span>Koles500</span><br />
<span class="score" title="68 reputation points">68</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koles500 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-55502" class="comments-container">
<span id="55504"></span>
<div id="comment-55504" class="comment">
<div id="post-55504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The answer at <a href="/questions/54196/how-to-make-symbols-visible-on-a-lesser-zoom-level/54202">https://help.openstreetmap.org/questions/54196/how-to-make-symbols-visible-on-a-lesser-zoom-level/54202</a> suggests that you might have been using the old pre-carto style. If you are, then there are two things that you're doing differently to "most people" (the other is running this on Windows). My guess is that your problem here is related to something that you're doing differently - perhaps try a more recent map style, or the same style on differently-built version of Mapnik (for example <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> just fetches from a repository so there's less to go wrong).</p>
</div>
<div id="comment-55504-info" class="comment-info">
<span class="comment-age">(07 Apr '17, 00:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="55522"></span>
<div id="comment-55522" class="comment">
<div id="post-55522-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We have newest mapnik tools that I downloaded from SVN repository. I can try different style. Which one exactly do you suggest? Maybe this one : ? <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a></p>
</div>
<div id="comment-55522-info" class="comment-info">
<span class="comment-age">(07 Apr '17, 14:04)</span> <span class="comment-user userinfo">Koles500</span>
</div>
</div>
<span id="55584"></span>
<div id="comment-55584" class="comment">
<div id="post-55584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded style from <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> and compared it with my usual default.style file and they are exactly the same. I re-imported data and re-rendered tiles and the problem is still the same as shown above. Any ideas ?</p>
</div>
<div id="comment-55584-info" class="comment-info">
<span class="comment-age">(12 Apr '17, 15:53)</span> <span class="comment-user userinfo">Koles500</span>
</div>
</div>
<span id="55585"></span>
<div id="comment-55585" class="comment">
<div id="post-55585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As mentioned elsewhere, the "default.style" file just determines what columns are imported, not what map style you get. That file is usually called "mapnik.xml". To take one example of how that is created see <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> up to where it says "carto project.mml &gt; mapnik.xml". In that example the "source" for the style is in the files referred to by "project.mml" and "carto" converts that into "mapnik.xml" which is something that Mapnik can understand (but most humans can't).</p>
<p>To compare non-carto map styles you'd need to compare the mapnik.xml files, but that will be difficult because the file format is very difficult to understand.</p>
</div>
<div id="comment-55585-info" class="comment-info">
<span class="comment-age">(12 Apr '17, 16:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55502-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55586"></span>

<div id="answer-container-55586" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55586-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Finally, I fixed it! &lt;Map buffer-size="512" AND &lt;ShieldSymbolizer clip="false" instead of &lt;ShieldSymbolizer avoid-edges="true" (all occurences) in osm.xml worked.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '17, 16:54</strong></p>
<img src="https://secure.gravatar.com/avatar/f98ed179efe75af596090a497cefeb90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koles500&#39;s gravatar image" />
<p><span>Koles500</span><br />
<span class="score" title="68 reputation points">68</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koles500 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '17, 16:55</strong> </span></p>
</div>
</div>
<div id="comments-container-55586" class="comments-container">
&#10;</div>
<div id="comment-tools-55586" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55586-form-container" class="comment-form-container">
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

