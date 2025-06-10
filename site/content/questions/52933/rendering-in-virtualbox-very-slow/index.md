+++
type = "question"
title = "Rendering in VirtualBox very slow"
description = '''Hello, I use ubuntu 16.04. in Virtualbox with Postgresql 9.5, postgis 9.2, mod_tile current git version, 16GiB RAM, 4 CPU, and harddisk non ssd. I use umap as frontend for working with the maps. Should the VirtualBox fast enough? I dont need it superfast like google maps, but still useable. The rend...'''
date = "2016-11-14T14:59:00Z"
lastmod = "2016-11-14T16:52:00Z"
weight = 52933
keywords = [ "renderd", "slow", "mod_tile" ]
aliases = [ "/questions/52933" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering in VirtualBox very slow](/questions/52933/rendering-in-virtualbox-very-slow)

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
<span id="post-52933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52933-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I use ubuntu 16.04. in Virtualbox with Postgresql 9.5, postgis 9.2, mod_tile current git version, 16GiB RAM, 4 CPU, and harddisk non ssd. I use umap as frontend for working with the maps.</p>
<p>Should the VirtualBox fast enough? I dont need it superfast like google maps, but still useable. The rendering is very slow and usable. The Index in the database is created, I checked that. What the problem can be?</p>
<p>Now I try to prerender the whole country...</p>
<pre><code>renderd[14336]: DEBUG: DONE TILE default 7 64-71 40-47 in 829.013 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/7/0/0/0/66/8.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 96-103, new metatile
renderd[14336]: Rendering projected coordinates 8 136 96 -&gt; 1252344.271425|3757032.814275 2504688.542850|5009377.085700 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 96-103 in 1.110 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/134/128.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 104-111, new metatile
renderd[14336]: Rendering projected coordinates 8 136 104 -&gt; 1252344.271425|2504688.542850 2504688.542850|3757032.814275 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 104-111 in 0.280 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/134/136.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 112-119, new metatile
renderd[14336]: Rendering projected coordinates 8 136 112 -&gt; 1252344.271425|1252344.271425 2504688.542850|2504688.542850 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 112-119 in 0.329 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/135/128.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 120-127, new metatile
renderd[14336]: Rendering projected coordinates 8 136 120 -&gt; 1252344.271425|0.000000 2504688.542850|1252344.271425 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 120-127 in 0.247 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/135/136.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 128-135, new metatile
renderd[14336]: Rendering projected coordinates 8 136 128 -&gt; 1252344.271425|-1252344.271425 2504688.542850|0.000000 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 128-135 in 0.304 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/136/128.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 136-143, new metatile
renderd[14336]: Rendering projected coordinates 8 136 136 -&gt; 1252344.271425|-2504688.542850 2504688.542850|-1252344.271425 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 136-143 in 0.291 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/136/136.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 144-151, new metatile
renderd[14336]: Rendering projected coordinates 8 136 144 -&gt; 1252344.271425|-3757032.814275 2504688.542850|-2504688.542850 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 128-135 80-87 in 752.785 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/133/0.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 152-159, new metatile
renderd[14336]: Rendering projected coordinates 8 136 152 -&gt; 1252344.271425|-5009377.085700 2504688.542850|-3757032.814275 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 144-151 in 0.329 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/137/128.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 160-167, new metatile
renderd[14336]: Rendering projected coordinates 8 136 160 -&gt; 1252344.271425|-6261721.357125 2504688.542850|-5009377.085700 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 152-159 in 0.255 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/137/136.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 168-175, new metatile
renderd[14336]: Rendering projected coordinates 8 136 168 -&gt; 1252344.271425|-7514065.628550 2504688.542850|-6261721.357125 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 160-167 in 0.251 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/138/128.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 176-183, new metatile
renderd[14336]: Rendering projected coordinates 8 136 176 -&gt; 1252344.271425|-8766409.899975 2504688.542850|-7514065.628550 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 168-175 in 0.240 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/138/136.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 184-191, new metatile
renderd[14336]: Rendering projected coordinates 8 136 184 -&gt; 1252344.271425|-10018754.171400 2504688.542850|-8766409.899975 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 176-183 in 0.231 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/139/128.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 192-199, new metatile
renderd[14336]: Rendering projected coordinates 8 136 192 -&gt; 1252344.271425|-11271098.442825 2504688.542850|-10018754.171400 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 184-191 in 0.228 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/139/136.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 200-207, new metatile
renderd[14336]: Rendering projected coordinates 8 136 200 -&gt; 1252344.271425|-12523442.714250 2504688.542850|-11271098.442825 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 192-199 in 0.646 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/140/128.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 208-215, new metatile
renderd[14336]: Rendering projected coordinates 8 136 208 -&gt; 1252344.271425|-13775786.985675 2504688.542850|-12523442.714250 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 200-207 in 0.587 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/140/136.meta
&#10;renderd[14336]: DEBUG: START TILE default 8 136-143 216-223, new metatile
renderd[14336]: Rendering projected coordinates 8 136 216 -&gt; 1252344.271425|-15028131.257100 2504688.542850|-13775786.985675 to a 8 x 8 tile
renderd[14336]: DEBUG: DONE TILE default 8 136-143 208-215 in 0.339 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/141/128.meta
&#10;renderd[14336]: DEBUG: DONE TILE default 8 136-143 216-223 in 0.262 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/8/0/0/0/141/136.meta</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '16, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ad332fb85ece95d8d53ae63eea5d534f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hevilp&#39;s gravatar image" />
<p><span>hevilp</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hevilp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52933" class="comments-container">
<span id="52937"></span>
<div id="comment-52937" class="comment">
<div id="post-52937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so, my setup has a normal speed? I dont have a problem to prerender it all, if it working fine...</p>
</div>
<div id="comment-52937-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 15:17)</span> <span class="comment-user userinfo">hevilp</span>
</div>
</div>
<span id="52938"></span>
<div id="comment-52938" class="comment">
<div id="post-52938-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually - looking at the tile numbers above, that's for Antarctica(!) so the "renderd[14336]: DEBUG: DONE TILE default 8 136-143 216-223 in 0.262 seconds" figure isn't very representative. Try dirtying a tile where you have some data...</p>
</div>
<div id="comment-52938-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 15:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52939"></span>
<div id="comment-52939" class="comment">
<div id="post-52939-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And BTW which country are you trying to render (too lazy to check the tiles)?</p>
</div>
<div id="comment-52939-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 16:28)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="52940"></span>
<div id="comment-52940" class="comment">
<div id="post-52940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>whole Germany, it cant be Antartica...</p>
</div>
<div id="comment-52940-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 16:29)</span> <span class="comment-user userinfo">hevilp</span>
</div>
</div>
<span id="52941"></span>
<div id="comment-52941" class="comment">
<div id="post-52941-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How did you set off that render request? Via render_list, perhaps?</p>
</div>
<div id="comment-52941-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 16:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52942"></span>
<div id="comment-52942" class="comment not_top_scorer">
<div id="post-52942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>in normal case, umap sends the renderrequest. that in the example could be from render_list, i dont remember</p>
</div>
<div id="comment-52942-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 16:52)</span> <span class="comment-user userinfo">hevilp</span>
</div>
</div>
</div>
<div id="comment-tools-52933" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-52933-form-container" class="comment-form-container">
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

<span id="52935"></span>

<div id="answer-container-52935" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52935-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Low zoom tiles <strong>are</strong> slow to render even in a more performant setup, that is the main reason you typically pre-render them.</p>
<p>Having the rendering database on SSD would however likely help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '16, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-52935" class="comments-container">
&#10;</div>
<div id="comment-tools-52935" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52935-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52936"></span>

<div id="answer-container-52936" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52936-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>VirtualBox per se shouldn't be the problem (though do check that you've allocated all the CPUs and memory that you think you have). "Time to render" times don't look too slow at z8. For comparison here (cheap "desktop" spec CPU, Virtualbox, SSD, 1 cpu and 5Gb memory allocated):</p>
<pre><code>Nov 14 15:06:46 ubuntu renderd[1417]: DEBUG: START TILE ajt 8 136-143 80-87, age 20.99 days
Nov 14 15:06:52 ubuntu renderd[1417]: DEBUG: DONE TILE ajt 8 136-143 80-87 in 6.525 seconds</code></pre>
<p>That's for a 2 tiles in parallel in a detailed area of the UK, which is fairly well mapped. You don't say what style you're using or where, which will also have an effect.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '16, 15:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-52936" class="comments-container">
&#10;</div>
<div id="comment-tools-52936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52936-form-container" class="comment-form-container">
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

