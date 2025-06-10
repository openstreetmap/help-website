+++
type = "question"
title = "How can I export this single waterway by ID number - Overpass API?"
description = '''If I go to link text I see exactly the data I need:  Way: Forsythe Creek (30257498) name Forsythe Creek waterway river Nodes 324480596 (part of ways Walker Creek (29440670) and Forsythe Creek (29440023)) 324480597 324480598  ...  But if I export that page I also get the Walker Creek (29440670) and F...'''
date = "2018-06-13T01:16:00Z"
lastmod = "2018-06-13T06:02:00Z"
weight = 64188
keywords = [ "node", "query", "api", "export", "way" ]
aliases = [ "/questions/64188" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I export this single waterway by ID number - Overpass API?](/questions/64188/how-can-i-export-this-single-waterway-by-id-number-overpass-api)

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
<span id="post-64188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64188-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I go to <a href="https://www.openstreetmap.org/way/30257498">link text</a> I see exactly the data I need:</p>
<pre><code>Way: Forsythe Creek (30257498)
name    Forsythe Creek
waterway    river
Nodes
324480596 (part of ways Walker Creek (29440670) and Forsythe Creek (29440023))
324480597
324480598 
...</code></pre>
<p>But if I export that page I also get the Walker Creek (29440670) and Forsythe Creek (29440023) waterways, plus a lot of roads. If I cut the map extent down enough I can get just those two "stream" waterways, but somehow that doesn't seem to work for 30257498 (which I believe becomes a "river") - I always get roads along with it.</p>
<p>I tried the Overpass web search, and the QuickOSM plugin in QGIS, and they can't find anything for 30257498. Or for the two upstream numbers. They don't give any errors, they just say "nothing found". I tried various ways to use the &gt;&gt; operator, but it didn't help.</p>
<p>QuickOSM is my easiest route. Is there a way to write an Overpass API query that will return just 30257498?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '18, 01:16</strong></p>
<img src="https://secure.gravatar.com/avatar/8497d1e09444b92e8424122da294aa4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LorenAmelang&#39;s gravatar image" />
<p><span>LorenAmelang</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LorenAmelang has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64188" class="comments-container">
&#10;</div>
<div id="comment-tools-64188" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64188-form-container" class="comment-form-container">
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

<span id="64189"></span>

<div id="answer-container-64189" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64189-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can <a href="http://overpass-turbo.eu/s/zxU">specify objects directly by id</a>:</p>
<pre><code>way(30257498);
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '18, 01:25</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-64189" class="comments-container">
<span id="64191"></span>
<div id="comment-64191" class="comment">
<div id="post-64191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much! That works perfectly at Overpass, and I have the line I need. Can't figure out how to enter it as a QuickOSM query, but I'm much more excited to get on with the next step in the real project.</p>
</div>
<div id="comment-64191-info" class="comment-info">
<span class="comment-age">(13 Jun '18, 06:02)</span> <span class="comment-user userinfo">LorenAmelang</span>
</div>
</div>
</div>
<div id="comment-tools-64189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64189-form-container" class="comment-form-container">
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

