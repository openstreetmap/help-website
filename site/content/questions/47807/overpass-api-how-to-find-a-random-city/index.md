+++
type = "question"
title = "[Overpass-api] How to find a random city?"
description = '''I&#x27;m in a process of making a game based on OSM data. I will have the player starting in a random city.  I have something that is kinda working. It is not producing a result every time, it is slow, and possibly stressful for the server: node[&quot;place&quot;~&quot;village|town|city&quot;]  (around: 100000, -32.950,23.3...'''
date = "2016-02-02T07:30:00Z"
lastmod = "2016-02-03T08:14:00Z"
weight = 47807
keywords = [ "overpass", "game", "random" ]
aliases = [ "/questions/47807" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[Overpass-api\] How to find a random city?](/questions/47807/overpass-api-how-to-find-a-random-city)

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
<span id="post-47807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47807-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm in a process of making a game based on OSM data. I will have the player starting in a random city.</p>
<p>I have something that is kinda working. It is not producing a result every time, it is slow, and possibly stressful for the server:</p>
<p><code>node["place"~"village|town|city"] (around: 100000, -32.950,23.325); out 1;</code></p>
<p>I am generating a random coordinates and search for any node with <code>place=village|town|city</code> tag within 100 km. The problem is that some of the random coordinates appear in the ocean or in deserts where there are no cities in that radius. I tried increasing it, but the query is getting even slower (expected) and I'm not sure if it is not bad for the Overpass server.</p>
<p>Can you see any way to improve this query? Can you suggest entirely different method of finding a random city?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-game" rel="tag" title="see questions tagged &#39;game&#39;">game</span> <span class="post-tag tag-link-random" rel="tag" title="see questions tagged &#39;random&#39;">random</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '16, 07:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Feb '16, 07:50</strong> </span></p>
</div>
</div>
<div id="comments-container-47807" class="comments-container">
&#10;</div>
<div id="comment-tools-47807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47807-form-container" class="comment-form-container">
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

<span id="47847"></span>

<div id="answer-container-47847" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47847-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ivanatora has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How about retrieving <em>all</em> cities of the world once, storing them in a list and choosing a random list element every time you need it? This seems to be a better approach since there isn't a new city appearing every 5 minutes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '16, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47847" class="comments-container">
<span id="47809"></span>
<div id="comment-47809" class="comment">
<div id="post-47809-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This might be getting me to some place. I managed to filter world cities based on population between 100000 - 399999 and it seems there are only 800 cities matching this criteria. I did not mean to use the pop filter in the game, but it is okay way to reduce the size of the list that will be kept locally. <a href="http://overpass-turbo.eu/s/e8c">http://overpass-turbo.eu/s/e8c</a></p>
</div>
<div id="comment-47809-info" class="comment-info">
<span class="comment-age">(02 Feb '16, 08:32)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
</div>
<div id="comment-tools-47847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47847-form-container" class="comment-form-container">
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

