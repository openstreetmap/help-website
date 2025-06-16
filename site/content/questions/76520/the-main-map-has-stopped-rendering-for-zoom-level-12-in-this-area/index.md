+++
type = "question"
title = "The main map has stopped rendering for zoom level &lt;= 12 in this area"
description = '''There are many edits in this area such as this one (more than one week old) that have not been rendered at zoom level &amp;lt;= 12. Is this an issue/bug? If yes, is this the right place to report such issues?  I have already read discussions like this one talking about tens of minutes wait time to rende...'''
date = "2020-09-09T06:18:00Z"
lastmod = "2020-09-09T15:03:00Z"
weight = 76520
keywords = [ "rendering", "mapnik" ]
aliases = [ "/questions/76520" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [The main map has stopped rendering for zoom level \<= 12 in this area](/questions/76520/the-main-map-has-stopped-rendering-for-zoom-level-12-in-this-area)

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
<span id="post-76520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76520-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are many edits in this area such as <a href="https://www.openstreetmap.org/changeset/90207780#map=12/26.6846/62.0872">this one</a> (more than one week old) that have not been rendered at zoom level &lt;= 12. Is this an issue/bug? If yes, is this the right place to report such issues?</p>
<p>I have already read discussions like <a href="/questions/178/how-often-does-the-main-mapnik-map-get-updated">this one</a> talking about tens of minutes wait time to render a tile. Is there any other more recent (or live!) performance number/graph that can be used to get a more accurate estimation of the rendering time? e.g. any of <a href="https://munin.openstreetmap.org/renderd-day.html">the munin graphs</a> ?</p>
<p><strong>Update:</strong> Changes in that area are now visible at all zoom levels after almost 4 weeks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '20, 06:18</strong></p>
<img src="https://secure.gravatar.com/avatar/88ff25eff27e96e4540119269236c692?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Althemapper&#39;s gravatar image" />
<p><span>Althemapper</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Althemapper has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Sep '20, 17:54</strong> </span></p>
</div>
</div>
<div id="comments-container-76520" class="comments-container">
&#10;</div>
<div id="comment-tools-76520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76520-form-container" class="comment-form-container">
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

<span id="76523"></span>

<div id="answer-container-76523" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76523-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-76523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Althemapper has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tiles with zoom level &lt;= 12 are not rendered on demand, instead they are regularly created by a batch process every now and then. The reason for this is that the tiles at lower zoom levels normally contain too much data to render reasonably fast on demand (the area in question is an exception to the rule).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '20, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-76523" class="comments-container">
<span id="76526"></span>
<div id="comment-76526" class="comment">
<div id="post-76526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>. Thank you for clarifying rendering of different zoom levels. Based on that, there is an issue in the area I reported, right?</p>
</div>
<div id="comment-76526-info" class="comment-info">
<span class="comment-age">(09 Sep '20, 13:46)</span> <span class="comment-user userinfo">Althemapper</span>
</div>
</div>
<span id="76527"></span>
<div id="comment-76527" class="comment">
<div id="post-76527-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>No, nothing to be reported as the batch process to rerender those tiles &lt;= 12 don't even run weekly, afaik. Better wait for up to a month.</p>
</div>
<div id="comment-76527-info" class="comment-info">
<span class="comment-age">(09 Sep '20, 13:55)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="76529"></span>
<div id="comment-76529" class="comment">
<div id="post-76529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/17439/spiekerooger">@Spiekerooger</a>. Very good to know that the rendering frequency of tiles of zoom level&lt;=12 is so low! Do you know if there is any statistic/graph related to those available?</p>
</div>
<div id="comment-76529-info" class="comment-info">
<span class="comment-age">(09 Sep '20, 15:03)</span> <span class="comment-user userinfo">Althemapper</span>
</div>
</div>
</div>
<div id="comment-tools-76523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76523-form-container" class="comment-form-container">
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

