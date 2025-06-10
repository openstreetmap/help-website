+++
type = "question"
title = "Whole world offline map"
description = '''Hello, I would need to get a whole world offline map, ideally from zoom 0 to zoom 12. That map will have to be delivered with my application. I may need to have a specific rendering for this. Basically, I will need country borders, main cities, main roads, topographic lines .. but not much more If p...'''
date = "2020-11-05T10:08:00Z"
lastmod = "2020-11-06T10:10:00Z"
weight = 77406
keywords = [ "world", "offline" ]
aliases = [ "/questions/77406" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Whole world offline map](/questions/77406/whole-world-offline-map)

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
<span id="post-77406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77406-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would need to get a whole world offline map, ideally from zoom 0 to zoom 12. That map will have to be delivered with my application.</p>
<p>I may need to have a specific rendering for this. Basically, I will need country borders, main cities, main roads, topographic lines .. but not much more</p>
<p>If possible, I would prefer to store offline tiles rather than having to maintain my own offline server (delivering an offline server with my application seems too complicate for end user)</p>
<p>What should I do, what is the best for my needs ?</p>
<p>1/ If I understand well, the whole world from zoom 1 to 12 would take 11 193 000 tiles.</p>
<p>With a ratio of 70%sea and 30% land, I would have 7 835 100 sea tiles. With a size of 1kb per sea tile, that would make 7 terra bytes of data, only for seas .... which is totally not efficient to store. Do you agree with my calculation ?</p>
<p>=&gt; If I want to store tiles, I need to reduce my expectations and get only zoom 10 or even better, 9</p>
<p>Then, what would be the best way to get the tiles ?</p>
<p>2/ Build my own tile server using this <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">Switch2Osm tutorial</a> and setup the rendering I need, then download my tiles from it</p>
<p>3/ Do the same but using a docker container as explained also on <a href="https://switch2osm.org/serving-tiles/using-a-docker-container/">SwitchToOsm</a></p>
<p>4/ Render the tiles using tools like <a href="http://maperitive.net/docs/default.html">Maperitive</a></p>
<p>5/ Find a server on the web that has a rendering close to what I need and contact them in order to directly download the tiles from it</p>
<p>6/ Another solution (based on offline tiles or any other easy offline rendering solution that I would not know?)</p>
<p>Thanks a lot in advance for your help,</p>
<p>Have a great day</p>
<p>Antoine</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-world" rel="tag" title="see questions tagged &#39;world&#39;">world</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '20, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/56f209b1de68f4eca634c10a1281ac1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoPich&#39;s gravatar image" />
<p><span>JoPich</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoPich has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77406" class="comments-container">
&#10;</div>
<div id="comment-tools-77406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77406-form-container" class="comment-form-container">
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

<span id="77418"></span>

<div id="answer-container-77418" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77418-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would simply store the tiles (more below) in MBTiles format (which is simply a SQLite database), see <a href="https://github.com/mapbox/mbtiles-spec">https://github.com/mapbox/mbtiles-spec</a> <a href="https://wiki.openstreetmap.org/wiki/MBTiles">https://wiki.openstreetmap.org/wiki/MBTiles</a> there are tons of tools to manipulate them and whatever your application is, it simply needs SQLite support to access the tiles.</p>
<p>As to the tiles themselves, while on the one hand you could go for raster tiles that you've pre-rendered the alternative would be to generate vector tiles and render them with mapbox-gl or similar. The advantage is extra flexibility with styling (as they are rendered on the fly) and further that you don't need the full tile stack. Pre-split/rendered vector tiles can be got for example here: <a href="https://openmaptiles.org/">https://openmaptiles.org/</a></p>
<p>Depending on your target platform, an other alternative could include mapsforge <a href="https://github.com/mapsforge/mapsforge">https://github.com/mapsforge/mapsforge</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '20, 10:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-77418" class="comments-container">
&#10;</div>
<div id="comment-tools-77418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77418-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77408"></span>

<div id="answer-container-77408" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77408-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sea tiles are mostly smaller in size, about 400bytes if you talk about raster tiles.</p>
<p>Even with 1kb per sea tile you miscalculated ~ 8 million sea tiles times 1kb, which would be around 8GB not 8TB.</p>
<p>E.g. I do have produced an offline tile set from zoom 0 to 13 that accounts for about 375 GB in total size at about 100 million tiles.</p>
<p>Depending on your style needs you would have to go with 2) or 5) or 6) (I can't say anything about 4) as I haven't done this yet).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '20, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '20, 11:24</strong> </span></p>
</div>
</div>
<div id="comments-container-77408" class="comments-container">
&#10;</div>
<div id="comment-tools-77408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77408-form-container" class="comment-form-container">
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

