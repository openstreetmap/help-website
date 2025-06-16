+++
type = "question"
title = "Missing tiles at certain zoom level for certain parts on my own tile server"
description = '''Hi all I have setup an osm tile server (following switch2osm) and wrote a simple openlayers script to browse the content. I have seen a problem that is for certain parts on the map when I zoomed into certain levels, the tiles were just missing and the missing areas were simply blank squares. I have ...'''
date = "2015-09-08T10:02:00Z"
lastmod = "2015-09-10T19:01:00Z"
weight = 45114
keywords = [ "tiles", "missing", "tileserver" ]
aliases = [ "/questions/45114" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Missing tiles at certain zoom level for certain parts on my own tile server](/questions/45114/missing-tiles-at-certain-zoom-level-for-certain-parts-on-my-own-tile-server)

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
<span id="post-45114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45114-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I have setup an osm tile server (following switch2osm) and wrote a simple openlayers script to browse the content. I have seen a problem that is for certain parts on the map when I zoomed into certain levels, the tiles were just missing and the missing areas were simply blank squares. I have checked the tiles that are missing are always for the same areas at the same zoom level.</p>
<p>I downloaded the osm data from bbbike.org. Any idea on how this happens and what I should do to fix it? Thanks. I have uploaded a screen-shot as well as a Youtube video that can visually show the problem. Video: <a href="http://youtu.be/vkp3JTbPepo">link text</a></p>
<p><img src="/upfiles/Screenshot_from_2015-09-08_15:49:24.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '15, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0cd6d6bd835d840ee1df1f5a3310d099?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dalishi&#39;s gravatar image" />
<p><span>dalishi</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dalishi has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '15, 10:04</strong> </span></p>
</div>
</div>
<div id="comments-container-45114" class="comments-container">
<span id="45159"></span>
<div id="comment-45159" class="comment">
<div id="post-45159-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Are exactly the same tiles still missing if you try to access them after a few minutes? Try to empty your browser cache before trying to access them again.</p>
</div>
<div id="comment-45159-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 10:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45161"></span>
<div id="comment-45161" class="comment">
<div id="post-45161-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/158/scai">@scai</a> you hit the point. First I deleted all the rendered tiles from /var/lib/mod_tile, observed not exactly the same tiles missing. Some missing tiles come back. Then I tried to clear my browser's cache and problem seems solved. The previous missing tiles appeared. Thanks for your enlightening. But I still want to figure out the reason behind this why it is happening.</p>
</div>
<div id="comment-45161-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 11:18)</span> <span class="comment-user userinfo">dalishi</span>
</div>
</div>
<span id="45163"></span>
<div id="comment-45163" class="comment">
<div id="post-45163-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just a guess but maybe your tile server is just too slow for rendering and/or delivering the tiles within time.</p>
</div>
<div id="comment-45163-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 11:44)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45114" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45114-form-container" class="comment-form-container">
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

<span id="45176"></span>

<div id="answer-container-45176" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45176-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that <a href="https://help.openstreetmap.org/users/158/scai">@scai</a> hit the nail on the head above - the renderer isn't able to render tiles fast enough for them to appear in the browser. When I see this problem I do the following:</p>
<pre><code>sudo tail -f /var/log/syslog | grep &quot;TILE &quot;</code></pre>
<p>(note the space after "TILE")</p>
<p>You should see "START TILE" and "DONE TILE" lines in response for tile requests. If a tile fails to appear, wait for the "DONE TILE" line and then refresh the request for it in the browser and you should see it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '15, 19:01</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-45176" class="comments-container">
&#10;</div>
<div id="comment-tools-45176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45176-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45157"></span>

<div id="answer-container-45157" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45157-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-45157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Dalishi, since you’ve downloaded the OSM data from a third party, there several update changes possible. Tiles are updated at different levels and moments. So ask the operator bbbike.org for their update frequency or even an explanation. Collect them over a certain period and remember that the tiles are updated all the time, just as everything else in OSM. Consider a download directly from the OSM servers as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '15, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-45157" class="comments-container">
<span id="45158"></span>
<div id="comment-45158" class="comment">
<div id="post-45158-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>He is running his own tile server.</p>
</div>
<div id="comment-45158-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 10:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45162"></span>
<div id="comment-45162" class="comment">
<div id="post-45162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/3443/hendrikklaas">@Hendrikklaas</a> thanks for your reply. The problem seems because my browser's cache. I did what <a href="https://help.openstreetmap.org/users/158/scai">@scai</a> suggested and problem solved. Still try to figure out what's going on behind. Thanks.</p>
</div>
<div id="comment-45162-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 11:20)</span> <span class="comment-user userinfo">dalishi</span>
</div>
</div>
</div>
<div id="comment-tools-45157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45157-form-container" class="comment-form-container">
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

