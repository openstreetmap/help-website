+++
type = "question"
title = "Convert osm.pbf to pbf tree to use on apache"
description = '''I have the file spain.osm.pbf (~800MB). I can&#x27;t find any form to convert into tiles tre 0/0/0.pbf... 10/497/400.pbf files (~kb)...  Some clue?'''
date = "2020-01-30T16:04:00Z"
lastmod = "2020-02-03T10:04:00Z"
weight = 72780
keywords = [ "osmconvert" ]
aliases = [ "/questions/72780" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Convert osm.pbf to pbf tree to use on apache](/questions/72780/convert-osmpbf-to-pbf-tree-to-use-on-apache)

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
<span id="post-72780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72780-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the file spain.osm.pbf (~800MB). I can't find any form to convert into tiles tre 0/0/0.pbf... 10/497/400.pbf files (~kb)...</p>
<p>Some clue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '20, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/eaf944bd8cb136d291c0141e5f6a8c2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="11sma&#39;s gravatar image" />
<p><span>11sma</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="11sma has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '20, 16:21</strong> </span></p>
</div>
</div>
<div id="comments-container-72780" class="comments-container">
&#10;</div>
<div id="comment-tools-72780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72780-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="72782"></span>

<div id="answer-container-72782" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72782-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you are asking for is "rendering the OSM data into tiles" - this is much more than a simple "conversion". In addition, producing all tiles (the "tree" you speak of) for all of Spain on zoom levels 0-18 will take many days and you'll end up with 100 million files using over 300 GB altogether!</p>
<p>Most people, instead of computing all the tiles, set up a tile server (see switch2osm.org) which can then produce these tiles on demand, instead of creating them all upfront. If you want to create tiles for a smaller area upfront, you can do this with the "Maperitive" GUI software, but doing it for all of Spain will likely require the tile server setup.</p>
<p>One of the inputs for the rendering process is the "map style", i.e. the rules that govern how something is drawn on the map - this information is not contained in the .pbf file you have. The .pbf only has information on where and what something <em>is</em>, not how it appears on the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '20, 16:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-72782" class="comments-container">
&#10;</div>
<div id="comment-tools-72782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72782-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72827"></span>

<div id="answer-container-72827" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72827-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hei Frederik! First at all thousands of thanks for your answer and your amazing speed.</p>
<p>I'm going a little deeper even if I'm maybe creating "another post"... but you'll be able to find the "why" of my question.</p>
<p>The initial process that I used was to get osm.pbf and use the <a href="https://github.com/openmaptiles/openmaptiles">https://github.com/openmaptiles/openmaptiles</a> project to generate the file tiles.mbtiles. The process of generate mbtiles took me about 30 minutes (0-14 zoom). Then with these file generate an tileserver with (in this case docker klokantech/tileserver-gl).</p>
<p>I can show these maps in a webbrowser (and in App) with mapbox js with additional one layer... but sometimes with a random tiles (at map or layer) I get blanks in some zooms. I'm going to explain better... - If I do zoom in some place, from for example, 12 to 14, in 13.2 I have blank, even having a status 200 of that tile and having the correct content, but if i go to 13.6 the there is no blank and the content is shown perfectly. - Same if I do vertical or horizontal movement. With the same tile the content are appearing or not, seems random... - If I do F5, with the same 200 status in all tiles magicly appears or magicly not...</p>
<p>I don't know if blame the generation of mbtiles, but seems to be here the problem. If i use some free tiler provider, the map works perfect for all zooms and all moves. But the generation of tiles is a process large proved (openmaptiles software at github) and the original data comes from (test 1: catalonia.osm.pbf (a region)) from geofabrik and (test 2: spain-latest.osm.pbf) from direct ./quickstart spain that download (I guess) official data...</p>
<p>By other way... in a powerful mobile or a light map prototype, works better than the app or webapp (more heavy)... Then the problem is the component? I guess not too... with the free maptiler works fine...</p>
<p>Sorry for the extension and praying for some light in that weird issue.... Lots of thanks anticipated for the help and read, could you give an answer or not.</p>
<p>P.S.: The reason to create pbf tiles was to test another way to serve the pbf files instead using tilserver with the mbtiles file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '20, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/eaf944bd8cb136d291c0141e5f6a8c2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="11sma&#39;s gravatar image" />
<p><span>11sma</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="11sma has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Feb '20, 10:28</strong> </span></p>
</div>
</div>
<div id="comments-container-72827" class="comments-container">
&#10;</div>
<div id="comment-tools-72827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72827-form-container" class="comment-form-container">
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

