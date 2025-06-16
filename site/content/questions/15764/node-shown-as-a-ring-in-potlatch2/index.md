+++
type = "question"
title = "Node shown as a ring in Potlatch2"
description = '''Prompted by the OSM Inspector, I tried to correct a fault shown as &#x27;single node in way&#x27;. One of the building corner nodes at the centre of this view (https://www.openstreetmap.org/?lat=50.904897&amp;amp;lon=-1.335221&amp;amp;zoom=18&amp;amp;layers=M) was shown as an intersection, so I split it, dragged one of th...'''
date = "2012-09-03T19:10:00Z"
lastmod = "2012-09-04T07:25:00Z"
weight = 15764
keywords = [ "node", "potlatch2", "ring" ]
aliases = [ "/questions/15764" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Node shown as a ring in Potlatch2](/questions/15764/node-shown-as-a-ring-in-potlatch2)

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
<span id="post-15764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15764-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Prompted by the OSM Inspector, I tried to correct a fault shown as 'single node in way'. One of the building corner nodes at the centre of this view (<a href="https://www.openstreetmap.org/?lat=50.904897&amp;lon=-1.335221&amp;zoom=18&amp;layers=M)">https://www.openstreetmap.org/?lat=50.904897&amp;lon=-1.335221&amp;zoom=18&amp;layers=M)</a> was shown as an intersection, so I split it, dragged one of the nodes away, and deleted it. The remaining node is still where it should be at the corner of the building, but Potlatch2 shows it as a red ring rather than as a filled circle. The node is now node 1895396700, and Potlatch considers that I created it. What have I done, and how do I put it right? I suppose that the obvious answer is to delete the node and create another one in the same place, but I would like to know what Potlatch is really trying to tell me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-ring" rel="tag" title="see questions tagged &#39;ring&#39;">ring</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '12, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15764" class="comments-container">
&#10;</div>
<div id="comment-tools-15764" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15764-form-container" class="comment-form-container">
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

<span id="15765"></span>

<div id="answer-container-15765" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15765-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Madryn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a "dupe node" (duplicate) - two nodes in exactly the same location. One of them, I'm guessing, is the single-node way.</p>
<p>P2 doesn't show single-node ways so there's no easy way to delete it. However, you can do it this way:</p>
<ol>
<li>Control-drag (or command-drag on a Mac) to select the area including the two ways.</li>
<li>Control-click the house to remove it from the selection</li>
<li>Click the 'delete' icon in the toolbox</li>
</ol>
<p>That should do the trick.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '12, 19:52</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-15765" class="comments-container">
<span id="15769"></span>
<div id="comment-15769" class="comment">
<div id="post-15769-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that worked. I found that the same effect could be achieved by selecting the duplicate node and pressing J to join the two nodes. However, it was necessary to press J twice. I have a slight suspicion that there may have been three nodes at that location.</p>
</div>
<div id="comment-15769-info" class="comment-info">
<span class="comment-age">(03 Sep '12, 21:43)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="15779"></span>
<div id="comment-15779" class="comment">
<div id="post-15779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if you unjoin (press J) a crossing, all ways get unjoined from each other. After moving/deleting the one node, the others must be rejoined again.</p>
<p>In the case you describe, the more easy way is to select a way, from there select the node in question (the intersection) and press minus (-). Then the node gets deleted <em>only from the selected way</em>, the rest stays intact.</p>
</div>
<div id="comment-15779-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 07:25)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-15765" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15765-form-container" class="comment-form-container">
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

