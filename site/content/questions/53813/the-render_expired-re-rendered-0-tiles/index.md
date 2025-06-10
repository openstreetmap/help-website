+++
type = "question"
title = "The render_expired re-rendered 0 tiles."
description = '''My expire.list file has only one line &quot;15/26973/12408&quot;, when i use &quot;cat /data/mod_map/expire.list | /root/src/mod_tile/render_expired -t /var/lib/mod_tile/osmcarto/ -z 10 -Z 18 -T=10&quot; command to rederd the changed tiles, it shows no tile has been renderd. And the map did not shows the changes that i...'''
date = "2017-01-03T09:01:00Z"
lastmod = "2017-01-04T02:14:00Z"
weight = 53813
keywords = [ "renderd", "mod_tile" ]
aliases = [ "/questions/53813" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The render_expired re-rendered 0 tiles.](/questions/53813/the-render_expired-re-rendered-0-tiles)

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
<span id="post-53813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53813-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My expire.list file has only one line "15/26973/12408", when i use "<strong>cat /data/mod_map/expire.list | /root/src/mod_tile/render_expired -t /var/lib/mod_tile/osmcarto/ -z 10 -Z 18 -T=10</strong>" command to rederd the changed tiles, it shows no tile has been renderd. And the map did not shows the changes that i edited before. What should i do?</p>
<p>cat /data/mod_map/expire.list | /root/src/mod_tile/render_expired -t /var/lib/mod_tile/osmcarto/ -z 10 -Z 18 -T=10 Rendering client</p>
<p>debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile/osmcarto/</p>
<p>Total for all tiles rendered</p>
<p>Meta tiles rendered: Rendered 0 tiles in 0.00 seconds (0.00 tiles/s)</p>
<p>Total tiles rendered: Rendered 0 tiles in 0.00 seconds (0.00 tiles/s)</p>
<p>Total tiles in input: 1</p>
<p>Total tiles expanded from input: 9</p>
<p>Total meta tiles deleted: 0</p>
<p>Total meta tiles touched: 0</p>
<p>Total tiles ignored (not on disk): 9</p>
<p>I think the tile has been renderd before, because i have viewed it on the map. I wonder if the tile_dir parameter -t is right, as it has set five stylesheet and has five different directories to cache different stylesheet tiles. I have tried "<strong>-t /var/lib/mod_tile/osmcarto/</strong>" and "<strong>-t /var/lib/mod_tile</strong>" to run the command, but the result is same.</p>
<p>However, i made a test on another host which only set one stylesheet and only has a default directory under /var/lib/mod_tile directory, when i run the render_expired command with "<strong>-t /var/lib/mod_tile/default</strong>", the result is same, then i changed the render_expired command with "<strong>-t /var/lib/mod_tile</strong>", and it shows the different result as below.</p>
<p>cat expire.list | render_expired -t /var/lib/mod_tile -z 10 -Z 18 -d=10</p>
<p>Rendering client</p>
<p>debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile</p>
<p>debug: Deleting metatile from /var/lib/mod_tile/default/18/49/72/163/236/128.meta</p>
<p>debug: Deleting metatile from /var/lib/mod_tile/default/17/16/172/81/126/0.meta</p>
<p>debug: Deleting metatile from /var/lib/mod_tile/default/16/0/214/32/191/128.meta</p>
<p>debug: Deleting metatile from /var/lib/mod_tile/default/15/0/99/144/87/136.meta</p>
<p>Total for all tiles rendered</p>
<p>Meta tiles rendered: Rendered 0 tiles in 0.01 seconds (0.00 tiles/s)</p>
<p>Total tiles rendered: Rendered 0 tiles in 0.01 seconds (0.00 tiles/s)</p>
<p>Total tiles in input: 1</p>
<p>Total tiles expanded from input: 9</p>
<p>Total meta tiles deleted: 4</p>
<p>Total meta tiles touched: 0</p>
<p>Total tiles ignored (not on disk): 5</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '17, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '17, 14:06</strong> </span></p>
</div>
</div>
<div id="comments-container-53813" class="comments-container">
<span id="53828"></span>
<div id="comment-53828" class="comment">
<div id="post-53828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Was that tile rendered before? My recollection is that "render_expired" won't re-rerender tiles that have never been rendered - that's what "Total tiles ignored (not on disk)" means. You could of course change it to "render tiles that don't exist", but that would need a code change; I don't believe that there is a parameter that you can use to tell it to do that.</p>
</div>
<div id="comment-53828-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 13:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53831"></span>
<div id="comment-53831" class="comment">
<div id="post-53831-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think the tile has been renderd before, because i have viewed it on the map.</p>
</div>
<div id="comment-53831-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 13:40)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
<span id="53832"></span>
<div id="comment-53832" class="comment">
<div id="post-53832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The tile in question is <a href="http://tile.openstreetmap.org/15/26973/12408.png">http://tile.openstreetmap.org/15/26973/12408.png</a> - if you replace tile.openstreetmap.org with your server name do you get a tile? If you do, then it <em>is</em> on disk and you'll need to investigate why render_expired thinks it isn't. Perhaps you're using a different map style?</p>
</div>
<div id="comment-53832-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 14:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53833"></span>
<div id="comment-53833" class="comment">
<div id="post-53833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, i can get a tile when i replace tile.openstreetmap.org with my server.</p>
</div>
<div id="comment-53833-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 14:25)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-53813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53813-form-container" class="comment-form-container">
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

<span id="53851"></span>

<div id="answer-container-53851" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53851-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is my fault, i lost the -m parameter in the comand, when i run "<strong><em>cat /data/mod_map/expire.list | /root/src/mod_tile/render_expired -m osmcarto -z 10 -Z 18 -T=10</em></strong>", it works well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '17, 02:14</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-53851" class="comments-container">
&#10;</div>
<div id="comment-tools-53851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53851-form-container" class="comment-form-container">
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

