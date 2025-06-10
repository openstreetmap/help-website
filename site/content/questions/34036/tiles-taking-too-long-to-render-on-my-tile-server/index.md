+++
type = "question"
title = "Tiles taking too long to render on my tile server"
description = '''Hello, I&#x27;ve followed the tutorial available here. The installation worked alright, but opening the tile in a browser leads to a 404 error. The only error from the server is &quot;Failed to read cmd on fd 10&quot;. After a long while, the tile is rendered (here, 1600 seconds): renderd[18586]: DEBUG: DONE TILE ...'''
date = "2014-06-17T16:32:00Z"
lastmod = "2016-08-28T01:21:00Z"
weight = 34036
keywords = [ "mod_tile", "mapnik", "tileserver" ]
aliases = [ "/questions/34036" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tiles taking too long to render on my tile server](/questions/34036/tiles-taking-too-long-to-render-on-my-tile-server)

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
<span id="post-34036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34036-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I've followed the tutorial available <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/" title="Manually building a tile server">here</a>. The installation worked alright, but opening the tile in a browser leads to a 404 error. The only error from the server is "Failed to read cmd on fd 10".</p>
<p>After a long while, the tile is rendered (here, 1600 seconds):</p>
<p>renderd[18586]: DEBUG: DONE TILE default 13 4264-4271 2984-2991 in 1594.968 seconds debug: Creating and writing a metatile to /var/lib/mod_tile/default/13/0/16/11/170/136.meta</p>
<p>How can I solve this problem?</p>
<p>Thank you for your help. Regards, Alex.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '14, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f36ee4312cb91587eed59341e9761d18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ale42&#39;s gravatar image" />
<p><span>ale42</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ale42 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jun '14, 22:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-34036" class="comments-container">
&#10;</div>
<div id="comment-tools-34036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34036-form-container" class="comment-form-container">
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

<span id="34037"></span>

<div id="answer-container-34037" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34037-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-34037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can increase the timeout in your mod_tile configuration, in your case a</p>
<p>ModTileMissingRequestTimeout 1800</p>
<p>would have made the browser wait for up to 1800 seconds instead of returning a 404 after a couple of seconds.</p>
<p>To achieve faster rendering, try one or a combination of the following:</p>
<ul>
<li>have your whole OSM database in RAM or on an SSD disk, or at least on a RAID-10 volume of spinning disks;</li>
<li>tune your database (depends on machine, memory, and PostGIS version - often toying with PostGIS memory settings can help);</li>
<li>create more indexes (temporarily activate PostGIS logging to find out which queries take most of the time, then create specific index for those);</li>
<li>modify your map style to make less expensive queries;</li>
<li>pre-render the tiles that you expect are likely to be viewed.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '14, 16:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-34037" class="comments-container">
<span id="34138"></span>
<div id="comment-34138" class="comment">
<div id="post-34138-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer Fred.</p>
<p>I will try to put the whole OSM database in RAM.</p>
<p>About the error (Failed to read cmd on fd 10),have you any idea if it can influence the very long time to render tile? How can this be fix?</p>
<p>Tks, Alex.</p>
</div>
<div id="comment-34138-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 12:50)</span> <span class="comment-user userinfo">ale42</span>
</div>
</div>
<span id="34139"></span>
<div id="comment-34139" class="comment">
<div id="post-34139-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For info I mentioned the "failed to read cmd" issue here:</p>
<p><a href="https://github.com/openstreetmap/mod_tile/issues/77">https://github.com/openstreetmap/mod_tile/issues/77</a></p>
<p>In my case it didn't have any adverse impact on serving tiles.</p>
</div>
<div id="comment-34139-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 13:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34140"></span>
<div id="comment-34140" class="comment">
<div id="post-34140-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok thanks for your answer.</p>
<p>I really don't understand why it's taking this long time to render these tiles.</p>
<p>I try to set up the same configuration on a virtual machine and it takes less than 5 seconds to render one tile. Here, I try this in a OVH server which is more powerfull. I really don't understand.</p>
</div>
<div id="comment-34140-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 13:50)</span> <span class="comment-user userinfo">ale42</span>
</div>
</div>
<span id="34143"></span>
<div id="comment-34143" class="comment">
<div id="post-34143-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In that case I would start by comparing things like CPU usage, memory (including swap!) usage and I/O load (via <code>iotop</code>) as well as I/O wait ("wa" in <code>top</code>) between those two systems.</p>
</div>
<div id="comment-34143-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 14:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="34171"></span>
<div id="comment-34171" class="comment">
<div id="post-34171-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My configuration for the server is like this : - RAM : 64 Go DDR ECC 1600 Mhz - CPU : Intel Xeon E5-1620v2 - No SSD - 2 disks x 2 To SATA3HGST Ent. 7K4000</p>
<p>So I don't think my configuration is a problem, isn't it?</p>
<p>I check PostgreSQL queries and these queries don't take more than 1 or 2 ms. So, put the whole database will not be usefull, isn't it?</p>
</div>
<div id="comment-34171-info" class="comment-info">
<span class="comment-age">(20 Jun '14, 09:31)</span> <span class="comment-user userinfo">ale42</span>
</div>
</div>
<span id="42390"></span>
<div id="comment-42390" class="comment not_top_scorer">
<div id="post-42390-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9046/ale42">@ale42</a> did you resolve this? I have an <em>incredibly</em> slow tile server.</p>
</div>
<div id="comment-42390-info" class="comment-info">
<span class="comment-age">(16 Apr '15, 15:35)</span> <span class="comment-user userinfo">haroldship</span>
</div>
</div>
</div>
<div id="comment-tools-34037" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-34037-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34141"></span>

<div id="answer-container-34141" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34141-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another possibility that could drastically slow down database access would be if for some reason the index creation process failed at import time?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '14, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-34141" class="comments-container">
<span id="34142"></span>
<div id="comment-34142" class="comment">
<div id="post-34142-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>How can I check that? Or rebuild it?</p>
</div>
<div id="comment-34142-info" class="comment-info">
<span class="comment-age">(19 Jun '14, 13:57)</span> <span class="comment-user userinfo">ale42</span>
</div>
</div>
<span id="51759"></span>
<div id="comment-51759" class="comment">
<div id="post-51759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To answer the first bit, when osm2pgsql completes it'll say something like "Osm2pgsql took 238s overall" (or much longer). It it doesn't say that, it hasn't finished, and indexes probably aren't created.</p>
</div>
<div id="comment-51759-info" class="comment-info">
<span class="comment-age">(28 Aug '16, 01:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-34141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34141-form-container" class="comment-form-container">
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

