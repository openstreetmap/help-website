+++
type = "question"
title = "How to trigger a repaint for a specific OSM map tile?"
description = '''After a cycling tour through north-western Russia, I&#x27;ve submitted a couple of changesets.  Mapnik map tiles on zoom levels &amp;gt;=12 (here&#x27;s an example) almost instantly reflect the updated data. However, even one or two weeks after the uploads, map tiles on zoom levels &amp;lt; 12 (here&#x27;s an example) are...'''
date = "2010-10-07T11:17:00Z"
lastmod = "2017-01-13T08:46:00Z"
weight = 1049
keywords = [ "tiles", "mapnik" ]
aliases = [ "/questions/1049" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to trigger a repaint for a specific OSM map tile?](/questions/1049/how-to-trigger-a-repaint-for-a-specific-osm-map-tile)

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
<span id="post-1049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1049-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-1049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After a cycling tour through north-western Russia, I've submitted a couple of changesets.</p>
<p>Mapnik map tiles on zoom levels &gt;=12 (here's an <span>example</span>) almost instantly reflect the updated data. However, even one or two weeks after the uploads, map tiles on zoom levels &lt; 12 (here's an <span>example</span>) aren't updated yet.</p>
<p><strong>Questions</strong></p>
<p>How can I explicitly trigger a repaint for a specific mapnik tile?</p>
<p>How can I explicitly trigger a repaint for all tiles on all zoom levels in a specific bounding box?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '10, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c70c3e59f8809e5c2b1140ce4fd9bbfd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guggis&#39;s gravatar image" />
<p><span>guggis</span><br />
<span class="score" title="121 reputation points">121</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guggis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1049" class="comments-container">
&#10;</div>
<div id="comment-tools-1049" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1049-form-container" class="comment-form-container">
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

<span id="1050"></span>

<div id="answer-container-1050" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1050-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-1050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mapnik tryes not to rerender tiles unless needed. If the tiles has not rerendered in 2 weeks the changes is probably not enough to trigger a rerender.</p>
<p>If you want to get more information on a tile you can append <del>/info</del> <code>/status</code> to the end of the url. You might also force a rerender by appending /dirty at the end of the url, but overuse might overload the tile server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '10, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '11, 09:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-1050" class="comments-container">
<span id="4604"></span>
<div id="comment-4604" class="comment">
<div id="post-4604-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a difference between this method and hitting 'r' at z=12 in <a href="http://informationfreeway.org">informationfreeway.org</a>? I use the latter, and it works, but I am worried that it cause more tiles to be rerendered than I absolutely need.</p>
</div>
<div id="comment-4604-info" class="comment-info">
<span class="comment-age">(18 Apr '11, 19:02)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4674"></span>
<div id="comment-4674" class="comment">
<div id="post-4674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hitting 'r' at <a href="http://informationfreeway.org">informationfreeway.org</a> causes Tiles@Home to rerender, not the mapnik map. It's an entirely different map.</p>
</div>
<div id="comment-4674-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 21:37)</span> <span class="comment-user userinfo">Lennard</span>
</div>
</div>
<span id="54015"></span>
<div id="comment-54015" class="comment">
<div id="post-54015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've been reading through this, now old, question as I had the same question. One update for <a href="https://help.openstreetmap.org/users/1224/lennard">@Lennard</a>: informationfreeway.org now seems to use the mapnik map, and not the (now discontinued) Tiles@Home map.</p>
</div>
<div id="comment-54015-info" class="comment-info">
<span class="comment-age">(13 Jan '17, 08:46)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-1050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1050-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3080"></span>

<div id="answer-container-3080" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3080-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-3080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer is <a href="https://wiki.openstreetmap.org/wiki/Slippy_map#Mapnik_tile_rendering">here</a></p>
<blockquote>
<p>If you want to make a tile render before the seven day expiry then you can mark it as dirty by appending /dirty: <a href="http://tile.openstreetmap.org/7/63/42.png/dirty">http://tile.openstreetmap.org/7/63/42.png/dirty</a></p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '11, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-3080" class="comments-container">
&#10;</div>
<div id="comment-tools-3080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3080-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5494"></span>

<div id="answer-container-5494" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5494-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>And for those that are as ignorant as I seem to have been for a few weeks (pondering how to get the URL of a specific tile -- so I can append these /status /dirty additions to them): You can get the URL e.g. directly from your browser (and depending on your browser) with right-clicking a spot on the map and selecting "Open image in new tab" or "Copy image URL".</p>
<p>If you get a c.* in the beginning of the URL that seems to imply to a cached(?) version of the tile and removing that c. from the beginning may show you an already re-rendered tile (my example from few minutes ago: <a href="http://c.tile.openstreetmap.org/17/39201/58652.png">http://c.tile.openstreetmap.org/17/39201/58652.png</a> ). I have no idea if that's browser or server cache -- or something else.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '11, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/280f61ca58a2e8c3d7bc877ed8a3def2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaakkoh&#39;s gravatar image" />
<p><span>jaakkoh</span><br />
<span class="score" title="548 reputation points">548</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaakkoh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5494" class="comments-container">
<span id="25173"></span>
<div id="comment-25173" class="comment">
<div id="post-25173-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi jaakkoh - the "c.tileserver" is not a cached version of the server, but should be an alias that points to the same tile server as plain old "tileserver" would. There are limits on simultaneous connections between a single browser and a single dns address which can limit the throughput of tiles. So... people get around this by setting up multiple dns names for the same server and enable more parallel http connections. I think.</p>
</div>
<div id="comment-25173-info" class="comment-info">
<span class="comment-age">(10 Aug '13, 18:22)</span> <span class="comment-user userinfo">jeffmeyer</span>
</div>
</div>
</div>
<div id="comment-tools-5494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5494-form-container" class="comment-form-container">
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

