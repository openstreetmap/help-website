+++
type = "question"
title = "Increase / Improve / Speed Up Rendering Performance of my own tileserver"
description = '''Hello Everybody, i try to Create my Own Tileserver. But it is soooo slow. Therefore i use render_list to pre_render Tiles. But why is it so Slow?! And only 740 MB of 5,4 GB are used (13 %) I am running it on a VM. If i only use it for Belgium / one County -&amp;gt; it is fast. But Hole Europe -&amp;gt; Slow...'''
date = "2013-04-27T09:05:00Z"
lastmod = "2017-10-01T13:36:00Z"
weight = 21909
keywords = [ "increase", "performance", "slow", "rendering", "tileserver" ]
aliases = [ "/questions/21909" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Increase / Improve / Speed Up Rendering Performance of my own tileserver](/questions/21909/increase-improve-speed-up-rendering-performance-of-my-own-tileserver)

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
<span id="post-21909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21909-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-21909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Everybody,</p>
<p>i try to Create my Own Tileserver.</p>
<p>But it is soooo slow.</p>
<p>Therefore i use render_list to pre_render Tiles.</p>
<p>But why is it so Slow?! And only 740 MB of 5,4 GB are used (13 %)</p>
<p>I am running it on a VM. If i only use it for Belgium / one County -&gt; it is fast.</p>
<p>But Hole Europe -&gt; Slow</p>
<p>How can i improve the Performance? Please dont tell me use more RAM. You can tell me if there is no more Free RAM left. Ore a better CPU (4 Core, every usage unter 15 %)</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-increase" rel="tag" title="see questions tagged &#39;increase&#39;">increase</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '13, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/8fd83011d6e87db1c8974cae52e89899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asmardemir&#39;s gravatar image" />
<p><span>asmardemir</span><br />
<span class="score" title="76 reputation points">76</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asmardemir has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '13, 18:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-21909" class="comments-container">
&#10;</div>
<div id="comment-tools-21909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21909-form-container" class="comment-form-container">
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

<span id="21930"></span>

<div id="answer-container-21930" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21930-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-21930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The slow part is usually database access. Whereas Belgium is small and therefore fast to access the data, the whole of Europe is already a very substantial amount of data. At low zoom it simply takes a lot of seeks to retrieve the data out of the database.</p>
<p>Actually I will tell you to use more RAM... ;-) Postgresql heavily relies on the operating system disk cache to get acceptable performance, unlike other databases that use their own cache. As such the ram use for the os level disk cache does not get attributed to any application looks free. However, the OS will use all available (usefully) RAM for disk caching. For the whole of Europe, 5.4GB RAM is doable, but you should definitely see some substantial performance increases if you increase it to 16GB or more.</p>
<p>Alternatively switching from conventional harddisks to SSDs helps a lot in rendering performance, as the bottleneck is usually seek performance of the harddisk for database access.</p>
<p>However, it is predominantly the low-zoom tiles that take long to render. Zoom levels 7, 8 and 9 are probably the slowest to render per tile. After about Z12 it gets substantially faster, continously decreasing per tile rendering time until you reach Z18. As there are only very few low zoom tiles, however, it isn't as critical that low zoom tiles are slow.</p>
<p>After a couple of hours of pre-rendering, you should have them (low zoom tiles) all cached and you don't need to render them again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '13, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-21930" class="comments-container">
<span id="21958"></span>
<div id="comment-21958" class="comment">
<div id="post-21958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okey, i will try.</p>
<p>But a little Question:</p>
<p>Is it possible to "split" the Data in different Tables / Different Databases?</p>
</div>
<div id="comment-21958-info" class="comment-info">
<span class="comment-age">(29 Apr '13, 00:13)</span> <span class="comment-user userinfo">asmardemir</span>
</div>
</div>
<span id="21965"></span>
<div id="comment-21965" class="comment">
<div id="post-21965-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not currently. Or at least not with osm2pgsql.</p>
<p>As there are usually only a few long running queries, it is possible to add some additional indexes, specifically designed for those queries which potentially speed up low zoom rendering.</p>
</div>
<div id="comment-21965-info" class="comment-info">
<span class="comment-age">(29 Apr '13, 10:30)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-21930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21930-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59909"></span>

<div id="answer-container-59909" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59909-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>This video may help you in answering your question</p>
<p><a href="https://www.youtube.com/watch?v=Lxloo42gl8A">https://www.youtube.com/watch?v=Lxloo42gl8A</a></p>
<p>[osm2pgsql:mapnik — Optimizing the Rendering Toolchain - Paul Norman]</p>
<p>and this pdf</p>
<p><a href="http://www.geofabrik.de/media/2012-09-08-osm2pgsql-performance.pdf">http://www.geofabrik.de/media/2012-09-08-osm2pgsql-performance.pdf</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '17, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/bf2467b1454ef10dcb8ab27c0588fca4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jason1975&#39;s gravatar image" />
<p><span>jason1975</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jason1975 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Oct '17, 14:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-59909" class="comments-container">
&#10;</div>
<div id="comment-tools-59909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59909-form-container" class="comment-form-container">
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

