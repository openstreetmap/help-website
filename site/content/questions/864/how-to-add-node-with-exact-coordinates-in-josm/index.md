+++
type = "question"
title = "How to add node with exact coordinates in JOSM?"
description = '''Hello, I have a list of points that are written in that format: GG MM.MMM and I want to import it into JOSM. Two things stop me now:  JOSM doesn&#x27;t show coordinates in other format than GG.GGGGGG. How can I change the output format of all coordinates? I can&#x27;t find how to specify the exact coordinates...'''
date = "2010-09-20T12:37:00Z"
lastmod = "2010-09-23T11:05:00Z"
weight = 864
keywords = [ "node", "josm", "coordinates" ]
aliases = [ "/questions/864" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to add node with exact coordinates in JOSM?](/questions/864/how-to-add-node-with-exact-coordinates-in-josm)

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
<span id="post-864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-864-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,<br />
I have a list of points that are written in that format: GG MM.MMM and I want to import it into JOSM. Two things stop me now:</p>
<ul>
<li>JOSM doesn't show coordinates in other format than GG.GGGGGG. How can I change the output format of all coordinates?</li>
<li>I can't find how to specify the exact coordinates of a node. Dragging that node in the editor window and manually <em>fitting</em> it to place while watching the statusbar for the current location is not an useful option.</li>
</ul>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '10, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>21 Sep '10, 19:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-864" class="comments-container">
&#10;</div>
<div id="comment-tools-864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-864-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="868"></span>

<div id="answer-container-868" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-868-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ivanatora has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>On the Settings-&gt;Projection (Globe and grid) -&gt; Map Projection you can set the display coordinate to Degrees Minutes Seconds or Degrees Minutes.</li>
<li>On Tools -&gt; Add Node you can punch in the coordinates of the new node.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '10, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '13, 20:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span></p>
</div>
</div>
<div id="comments-container-868" class="comments-container">
<span id="897"></span>
<div id="comment-897" class="comment">
<div id="post-897-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Tools -&gt; Add Node always accept only the GG.GGGGGG, I think it should accept the currently selected coordinate format?</p>
</div>
<div id="comment-897-info" class="comment-info">
<span class="comment-age">(21 Sep '10, 20:52)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="913"></span>
<div id="comment-913" class="comment">
<div id="post-913-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, I've just added that 5488 request :) Let's see if it is going to be accepted.</p>
</div>
<div id="comment-913-info" class="comment-info">
<span class="comment-age">(23 Sep '10, 11:05)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
</div>
<div id="comment-tools-868" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-868-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="867"></span>

<div id="answer-container-867" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-867-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In JOSM you can create a node at a specific coordinate in GG.GGGGGG notation using <em>shift-D</em>. Note that depending on your locale you might have to use a "<strong>,</strong>" instead of a "<strong>.</strong>" (that is, GG<strong>,</strong>GGGGGG), even though the default entry uses a "<strong>.</strong>" for all locales (see bug <a href="https://josm.openstreetmap.de/ticket/5482">5482</a>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '10, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Sep '10, 21:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-867" class="comments-container">
&#10;</div>
<div id="comment-tools-867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-867-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="866"></span>

<div id="answer-container-866" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-866-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would use my favourite XML generator MS Excel which does two strings operations: convert coordinate format, and put together XML statements, and create .osm file from this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '10, 12:54</strong></p>
<img src="https://secure.gravatar.com/avatar/ff53f6579540c3da3a1ad5180515cc67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JaakL&#39;s gravatar image" />
<p><span>JaakL</span><br />
<span class="score" title="42 reputation points">42</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JaakL has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-866" class="comments-container">
&#10;</div>
<div id="comment-tools-866" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-866-form-container" class="comment-form-container">
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

