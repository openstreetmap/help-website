+++
type = "question"
title = "JOSM: Support of Unicode"
description = '''When entering Unicode Characters (Ethiopic / Amharic in our case) in tags, such as &quot;name:am&quot;, only boxes are being displayed. Is this an JOSM bug or just a wrong system setting? We are using Ubuntu/GNOME and in other parts of the system, it is just displayed fine.'''
date = "2012-12-05T18:36:00Z"
lastmod = "2019-07-19T16:40:00Z"
weight = 18218
keywords = [ "josm", "java", "unicode" ]
aliases = [ "/questions/18218" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM: Support of Unicode](/questions/18218/josm-support-of-unicode)

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
<span id="post-18218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18218-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When entering Unicode Characters (Ethiopic / Amharic in our case) in tags, such as "name:am", only boxes are being displayed.</p>
<p>Is this an JOSM bug or just a wrong system setting?</p>
<p>We are using Ubuntu/GNOME and in other parts of the system, it is just displayed fine.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-unicode" rel="tag" title="see questions tagged &#39;unicode&#39;">unicode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '12, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '12, 23:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-18218" class="comments-container">
<span id="18220"></span>
<div id="comment-18220" class="comment">
<div id="post-18220-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I can confirm this here. It might be a font problem because other unicode characters work fine, but even with the packages <code>fonts-senamirmir-washra fonts-sil-abyssinica</code> installed I just get boxes in JOSM whereas other programs (like firefox) display the same characters without problems. I suggest creating a <a href="http://josm.openstreetmap.de/newticket">bug report</a>.</p>
</div>
<div id="comment-18220-info" class="comment-info">
<span class="comment-age">(06 Dec '12, 07:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18218-form-container" class="comment-form-container">
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

<span id="18256"></span>

<div id="answer-container-18256" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18256-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is actually working in Ubuntu 12.04 and Java 7. But I made a ticket for Input Method support: <a href="http://josm.openstreetmap.de/ticket/8259">http://josm.openstreetmap.de/ticket/8259</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '12, 17:35</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18256" class="comments-container">
&#10;</div>
<div id="comment-tools-18256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18256-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70136"></span>

<div id="answer-container-70136" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70136-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It was not working any longer in Java 8 ... but i figured out it is working for openjdk-11</p>
<p>On Ubuntu 18.04:</p>
<ol>
<li><code>apt install m17n openjdk-11-jre</code></li>
<li>Language Settings -&gt; IBus as input method</li>
<li>IBUS Settings &gt; add amharic, use Super+Space for switching</li>
<li>Start JOSM with the openjdk, for example <code>/usr/lib/jvm/java-11-openjdk-amd64/bin/java -jar josm-tested.jar</code> or by using <code>sudo update-alternatives --config</code> and choose the openjdk (in case you had oracle Java installed as well)</li>
<li>Now press Windows-Space to switch</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '19, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '19, 16:41</strong> </span></p>
</div>
</div>
<div id="comments-container-70136" class="comments-container">
&#10;</div>
<div id="comment-tools-70136" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70136-form-container" class="comment-form-container">
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

