+++
type = "question"
title = "Would like to extract all the waterways in Europe"
description = '''Hello, I would like to extract all the waterways in a large extent including Europe using Openstreetmap API capabilities. Eventually I would like to include this in a python script. However running it directly through overpass API or one of the openstreetmap-provided mirrors would be the first step ...'''
date = "2018-10-25T13:14:00Z"
lastmod = "2018-11-06T21:56:00Z"
weight = 66460
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/66460" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Would like to extract all the waterways in Europe](/questions/66460/would-like-to-extract-all-the-waterways-in-europe)

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
<span id="post-66460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66460-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I would like to extract all the waterways in a large extent including Europe using Openstreetmap API capabilities. Eventually I would like to include this in a python script. However running it directly through overpass API or one of the openstreetmap-provided mirrors would be the first step in this process.</p>
<p>I tried running the following through Overpass</p>
<pre><code>way(35.359872101102724, -29.628211426818392, 70.90180289857001, 47.014599265244506)[&quot;waterway&quot; = &quot;river&quot;];
out;</code></pre>
<p>But got an error:</p>
<pre><code>runtime error: Query ran out of memory in &quot;query&quot; at line 1. It would need at least 531 MB of RAM to continue.</code></pre>
<p>I then tried prepending the above with <code>[maxsize:1073741824];</code> and then running, but I still got the same memory error.</p>
<p>How can I extract this data and avoid the memory errors? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '18, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/23d42f5f532e8b985b9f0815c7897079?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awa5114&#39;s gravatar image" />
<p><span>awa5114</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awa5114 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66460" class="comments-container">
&#10;</div>
<div id="comment-tools-66460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66460-form-container" class="comment-form-container">
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

<span id="66469"></span>

<div id="answer-container-66469" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66469-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This clearly outside of the scope of any of the public Overpass API servers. You should simply download an OSM data extract for Europe and extract whatever you want from that, for example with osmfilter <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a> or one of the other tools available.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '18, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-66469" class="comments-container">
<span id="66482"></span>
<div id="comment-66482" class="comment">
<div id="post-66482-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed that is what I have tried to do. I currently have downloaded several files from the GeoFabrik website: euriope-latest.osm, europe-latest.osm.pbf and albania-latest.osm. I also have all the command line tools osmconvert, osmfilter and osmosis. I have tried various queries on all of them but it takes a very long time, and there is no way of judging how long it will take. Do these query tools provide any possibilities in terms of extracting large datasets aside from just getting it all at once?</p>
</div>
<div id="comment-66482-info" class="comment-info">
<span class="comment-age">(26 Oct '18, 10:19)</span> <span class="comment-user userinfo">awa5114</span>
</div>
</div>
</div>
<div id="comment-tools-66469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66469-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66709"></span>

<div id="answer-container-66709" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66709-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might also need to include more tag options. I found that to get all the navigable waterways in the UK, I also needed</p>
<ul>
<li>water=river with boat=yes</li>
<li>waterway=canal with boat=yes</li>
<li>waterway=river with boat=yes</li>
</ul>
<p>I did it with overpass, in about 8 manual slices- probably not an option for all of Europe.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '18, 21:56</strong></p>
<img src="https://secure.gravatar.com/avatar/b5c5070032df7883181003f187eacae0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spiregrain&#39;s gravatar image" />
<p><span>spiregrain</span><br />
<span class="score" title="183 reputation points">183</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spiregrain has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66709" class="comments-container">
&#10;</div>
<div id="comment-tools-66709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66709-form-container" class="comment-form-container">
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

