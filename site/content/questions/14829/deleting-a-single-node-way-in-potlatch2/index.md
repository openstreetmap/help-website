+++
type = "question"
title = "Deleting a single-node way in Potlatch2"
description = '''I recently discovered the OSM Inspector, and it pointed out a way containing just a single node here http://tools.geofabrik.de/osmi/debug.html?view=geometry&amp;amp;lon=-1.16749&amp;amp;lat=50.78635&amp;amp;zoom=18. It&#x27;s an area that I know quite well, so I thought I might be able to fix it. The node in questio...'''
date = "2012-08-04T13:46:00Z"
lastmod = "2012-08-17T10:22:00Z"
weight = 14829
keywords = [ "potlatch2", "way", "delete" ]
aliases = [ "/questions/14829" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Deleting a single-node way in Potlatch2](/questions/14829/deleting-a-single-node-way-in-potlatch2)

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
<span id="post-14829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14829-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently discovered the OSM Inspector, and it pointed out a way containing just a single node here <a href="http://tools.geofabrik.de/osmi/debug.html?view=geometry&amp;lon=-1.16749&amp;lat=50.78635&amp;zoom=18.">http://tools.geofabrik.de/osmi/debug.html?view=geometry&amp;lon=-1.16749&amp;lat=50.78635&amp;zoom=18.</a> It's an area that I know quite well, so I thought I might be able to fix it. The node in question marks a bend in Stokes Bay Promenade, and Potlatch2 shows the node as a red dot with a black outer circle, which I believe means that it either has tags (this node doesn't) or is part of anther way. My question is how best to delete the errant way. Because it has no length, I cannot highlight it in Potlatch. I could delete the node and then create a new node in exactly the same place, but that seems inelegant when what I really want to do is to delete a way. Is there a better method?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Aug '12, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '12, 08:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-14829" class="comments-container">
&#10;</div>
<div id="comment-tools-14829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14829-form-container" class="comment-form-container">
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

<span id="14830"></span>

<div id="answer-container-14830" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14830-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Madryn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can select overlapping ways or nodes in Potlatch 2 by pressing the '/' key, see:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Potlatch_2/Shortcuts">http://wiki.openstreetmap.org/wiki/Potlatch_2/Shortcuts</a></p>
<p>Thus you can select the single node, press / to get the isolated node and then delete it as that node adds no value.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '12, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/074785ea4eae108f0e4e89456bf74737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robbieonsea&#39;s gravatar image" />
<p><span>robbieonsea</span><br />
<span class="score" title="904 reputation points">904</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robbieonsea has 4 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-14830" class="comments-container">
<span id="14843"></span>
<div id="comment-14843" class="comment">
<div id="post-14843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that worked.</p>
</div>
<div id="comment-14843-info" class="comment-info">
<span class="comment-age">(05 Aug '12, 12:12)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="15185"></span>
<div id="comment-15185" class="comment">
<div id="post-15185-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Further note the latest Potlatch 2 deployed on main OSM site now lists <em>ALL</em> the shortcut keys available by clicking on the Help button -&gt; Shortcuts tab</p>
<p>Fixed by yours truly ;)</p>
</div>
<div id="comment-15185-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 00:17)</span> <span class="comment-user userinfo">robbieonsea</span>
</div>
</div>
<span id="15188"></span>
<div id="comment-15188" class="comment">
<div id="post-15188-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is that key dependent on the keyboard layout? Nothing happens when I press the "/" key on my Norwegian MacBook keyboard...</p>
</div>
<div id="comment-15188-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 07:35)</span> <span class="comment-user userinfo">pbb</span>
</div>
</div>
<span id="15194"></span>
<div id="comment-15194" class="comment">
<div id="post-15194-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes - see <a href="http://wiki.openstreetmap.org/wiki/Potlatch_2/Shortcuts">http://wiki.openstreetmap.org/wiki/Potlatch_2/Shortcuts</a></p>
<p>"*" for you allegedly.</p>
</div>
<div id="comment-15194-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 08:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15205"></span>
<div id="comment-15205" class="comment">
<div id="post-15205-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SomeoneElse</span>: Thanks!!!!</p>
</div>
<div id="comment-15205-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 10:22)</span> <span class="comment-user userinfo">pbb</span>
</div>
</div>
</div>
<div id="comment-tools-14830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14830-form-container" class="comment-form-container">
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

