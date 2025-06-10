+++
type = "question"
title = "Prevent mod_tile/renderd from re-rendering cached tile, even if tile is outdated"
description = '''I only have a high-level understanding of how mod_tile and renderd works so bear with me if I make wrong assumptions. On my tile server, I pre-rendered the most important parts of the map. Some parts of the map are not pre-rendered. I want to make it so that mod_tile will never re-render a tile if i...'''
date = "2019-03-28T19:45:00Z"
lastmod = "2019-03-29T08:24:00Z"
weight = 68534
keywords = [ "renderd", "mod_tile", "tileserver" ]
aliases = [ "/questions/68534" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Prevent mod_tile/renderd from re-rendering cached tile, even if tile is outdated](/questions/68534/prevent-mod_tilerenderd-from-re-rendering-cached-tile-even-if-tile-is-outdated)

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
<span id="post-68534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68534-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I only have a high-level understanding of how <code>mod_tile</code> and <code>renderd</code> works so bear with me if I make wrong assumptions.</p>
<p>On my tile server, I pre-rendered the most important parts of the map. Some parts of the map are not pre-rendered.</p>
<p>I want to make it so that <code>mod_tile</code> will never re-render a tile if it is already cached, even if the map has been updated and the tile is outdated. The only exception to this is when I use <code>render_list</code> to perform a pre-rendering - in this case I want <code>mod_tile</code> to check if a tile is outdated and re-render accordingly.</p>
<p>For any map tiles that are not cached, I want <code>mod_tile</code> to work normally and render the tiles.</p>
<p>The reasoning behind this is I'd prefer users to see an outdated tile than to wait 5 seconds to wait for an updated tile to load.</p>
<p>Is there some way I can configure <code>mod_tile</code> to work like this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '19, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/b1e3fbb6f31c5e0144e7b18fcd7d5d33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valachio&#39;s gravatar image" />
<p><span>valachio</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valachio has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '19, 19:56</strong> </span></p>
</div>
</div>
<div id="comments-container-68534" class="comments-container">
&#10;</div>
<div id="comment-tools-68534" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68534-form-container" class="comment-form-container">
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

<span id="68535"></span>

<div id="answer-container-68535" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68535-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="valachio has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, you can achieve your goal by doing something else than you are sketching, namely set <code>ModTileRequestTimeout=0</code> which means "always serve the old tile, but kick off a re-render if the tile you just served was old".</p>
<p>But if you really want to do it as you've described (i.e. serve old tile and <em>not</em> kick off a re-render), then you can disable all re-rendering by adding an empty "planet-import-complete" file to the root of your tile directory having a timestamp that is older than the oldest tile. This will make mod_tile think that all tiles are current.</p>
<p>Your assumption that mod_tile is in any way involved when running render_list is wrong; render_list works without mod_tile. render_list, when run without <code>--force</code>, will also honour the <code>planet-import-complete</code> file and consider all tiles current, and hence not render anything; you will have to remove <code>planet-import-complete</code> or use <code>--force</code>.</p>
<p>Also you might have a mistaken assumption about "checking if a tile is outdated", there's not really any magic that can do this. If you do database reloads in regular intervals then every tile older than the latest import is considered outdated; if you do differential updates then you have to create lists of expired tiles during the import and "touch" meta tiles with an old time stamp OR feed the list of expired tiles to render_list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '19, 22:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68535" class="comments-container">
<span id="68536"></span>
<div id="comment-68536" class="comment">
<div id="post-68536-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I understood your first paragraph correctly - If mod_tile detects an outdated tile upon a request, it will send the outdated tile off to the user first, and then run a re-render in the background.</p>
<p>This means that users will never have to wait for any tiles that are rendered already right? The worse thing that can happen is that they receive an outdated tile. The next user who requests the same tile will get the updated tile (assuming the re-render has been completed).</p>
<p>If that's the case, then my concerns are addressed since <code>ModTileRequestTimeout=0</code> is my current setting.</p>
<p>-</p>
<p>A follow-up question to your last paragraph. I'm assuming when you say "database reloads", you are referring to adding an OSM data file (<code>.osm.pbf</code>) to the database with osm2pgsql.</p>
<p>If I were to re-upload the exact same OSM data file as last time, mod_tile would think that all tiles are outdated, despite the fact that the map data is still the same?</p>
</div>
<div id="comment-68536-info" class="comment-info">
<span class="comment-age">(28 Mar '19, 22:51)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
<span id="68540"></span>
<div id="comment-68540" class="comment">
<div id="post-68540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, with <code>ModTileRequestTimeout=0</code> users will never have to wait for the re-render of and outdated tile and the next user will then get the updated tile. Regarding reloading the data, mod_tile does not magically detect anything about your database. If you do <em>not</em> have a <code>planet-import-complete</code> file and do <em>not</em> somehow fiddle with the file dates of meta tiles, then mod_tile will treat any meta tile older than 3 days as "outdated". If you put a <code>planet-import-complete</code> file then mod_tile will treat every file older than that as outdated. This is totally independent of you having or not having updated the database.</p>
</div>
<div id="comment-68540-info" class="comment-info">
<span class="comment-age">(29 Mar '19, 08:24)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68535-form-container" class="comment-form-container">
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

