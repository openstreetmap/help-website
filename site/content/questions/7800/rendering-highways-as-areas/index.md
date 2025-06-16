+++
type = "question"
title = "rendering highways as areas"
description = '''I was recently coding highways as areas, here the rose revolution square in tbilisi, which consists of open spaces of various kinds of roads: https://www.openstreetmap.org/?lat=41.7037&amp;amp;lon=44.792045&amp;amp;zoom=18&amp;amp;layers=M Question: The pedestrian area and the residential-highway-area render ok,...'''
date = "2011-09-12T15:58:00Z"
lastmod = "2011-09-13T14:47:00Z"
weight = 7800
keywords = [ "renderer", "highway", "area" ]
aliases = [ "/questions/7800" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [rendering highways as areas](/questions/7800/rendering-highways-as-areas)

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
<span id="post-7800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7800-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was recently coding highways as areas, here the rose revolution square in tbilisi, which consists of open spaces of various kinds of roads: <a href="https://www.openstreetmap.org/?lat=41.7037&amp;lon=44.792045&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=41.7037&amp;lon=44.792045&amp;zoom=18&amp;layers=M</a></p>
<p>Question: The pedestrian area and the residential-highway-area render ok, but the part with the secondary highway only renders the outlines. But I added "area=yes". Did I make a mistake or is it only the renderer's problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '11, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-7800" class="comments-container">
&#10;</div>
<div id="comment-tools-7800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7800-form-container" class="comment-form-container">
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

<span id="7807"></span>

<div id="answer-container-7807" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7807-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="moszkva ter has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a rendering issue. The combination "highway=secondary" and "<a href="https://wiki.openstreetmap.org/wiki/Key:area">area=yes</a>" is not supported currently in Mapnik but we could discuss the opportunity of having a plazza or a square with a seconday highway importance since there is no given direction. Such areas are usually better controlled in roundabouts (to avoid collisions ;-).</p>
<p>If the square or plazza is crossed with a given direction (e.g. with street lines within it), you might consider the proposed tag "<a href="https://wiki.openstreetmap.org/wiki/Proposed_features/area:highway">area:highway</a>".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '11, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-7807" class="comments-container">
<span id="7837"></span>
<div id="comment-7837" class="comment">
<div id="post-7837-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I now changed it back to linear highways and added the area:highway tag for an area around. This represents the situation of such intersections like here much better: <a href="http://img.fisgonia.com/image?webcam=tbilisi">http://img.fisgonia.com/image?webcam=tbilisi</a></p>
<p>Thanks for the advice!</p>
</div>
<div id="comment-7837-info" class="comment-info">
<span class="comment-age">(13 Sep '11, 14:47)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-7807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7807-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7801"></span>

<div id="answer-container-7801" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7801-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looking at the <a href="https://www.openstreetmap.org/browse/way/129497616">details</a> of the way reveals that the start node is not the same as the end node. There is <a href="https://www.openstreetmap.org/browse/node/1428668235">one node</a> connected at the start of the way. You curently have a way looking like A-&gt;B-&gt;...-&gt;Z-&gt;B, but an area are on the form A-&gt;B-&gt;...-&gt;Z-&gt;A.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '11, 16:14</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Sep '11, 16:14</strong> </span></p>
</div>
</div>
<div id="comments-container-7801" class="comments-container">
<span id="7804"></span>
<div id="comment-7804" class="comment">
<div id="post-7804-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks! I will check it and repair.</p>
</div>
<div id="comment-7804-info" class="comment-info">
<span class="comment-age">(12 Sep '11, 16:40)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="7808"></span>
<div id="comment-7808" class="comment">
<div id="post-7808-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>looks even worse now... the secondary highway is now not rendering at all :(</p>
</div>
<div id="comment-7808-info" class="comment-info">
<span class="comment-age">(12 Sep '11, 16:56)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-7801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7801-form-container" class="comment-form-container">
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

