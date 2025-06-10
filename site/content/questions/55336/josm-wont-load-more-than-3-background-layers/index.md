+++
type = "question"
title = "[closed] JOSM won&#x27;t load more than 3 background layers"
description = '''I am using JOSM on three computers, all roughly equal configured (laptops with Windows 10, Java 1.8.0 and JOSM 11639). On only one machine (the oldest), I am able to load and display more than 3 background layers. On the other two computers, the fourth (and any following) layers will not display in ...'''
date = "2017-03-29T20:40:00Z"
lastmod = "2017-04-04T08:23:00Z"
weight = 55336
keywords = [ "windows", "josm", "bug", "layers" ]
aliases = [ "/questions/55336" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] JOSM won't load more than 3 background layers](/questions/55336/josm-wont-load-more-than-3-background-layers)

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
<span id="post-55336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55336-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using JOSM on three computers, all roughly equal configured (laptops with Windows 10, Java 1.8.0 and JOSM 11639).</p>
<p>On only one machine (the oldest), I am able to load and display more than 3 background layers.</p>
<p>On the other two computers, the fourth (and any following) layers will not display in the map until I delete some of the other layers. When one layer has been deleted, the newest layer immediately starts showing its content.</p>
<p>This is not related to visibility of the layers (even with all 3 layers turned "off", the fourth layer will not display), or the order of the layers (the fourth layer can be the top one or the bottom one, no difference).</p>
<p>Is this a configuration setting (something that I have once set on the oldest machine and forgotten to do for the newer ones), or is it a bug in newer releases of JOSM that only shows up on clean installs, or something else?</p>
<p>I've created a JOSM bug report: <a href="https://josm.openstreetmap.de/ticket/14593">https://josm.openstreetmap.de/ticket/14593</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '17, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2f19e3a960bbc861e85b69c9c13a8e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbb&#39;s gravatar image" />
<p><span>pbb</span><br />
<span class="score" title="621 reputation points">621</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbb has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>04 Apr '17, 08:28</strong> </span></p>
</div>
</div>
<div id="comments-container-55336" class="comments-container">
&#10;</div>
<div id="comment-tools-55336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55336-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by pbb 04 Apr '17, 08:28

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55340"></span>

<div id="answer-container-55340" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55340-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Works for me <em>(update: with data layers)</em> with a fresh config and 11639 with openJDK JRE 1.8.0 on Linux.</p>
<p>Displaying n layers should work with a fresh install.</p>
<p>Please could you open a bug report (use the link in the JOSM help menu) with one of the machines where it does not work? Adding a screenshot of the JOSM window and a detailed list of which layers and how you add them would be good to have.</p>
<p>Afterwards please mention the bug report link here - for reference of others with the same problem. Thank you!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '17, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Mar '17, 19:28</strong> </span></p>
</div>
</div>
<div id="comments-container-55340" class="comments-container">
<span id="55361"></span>
<div id="comment-55361" class="comment">
<div id="post-55361-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks, I've created a <a href="https://josm.openstreetmap.de/ticket/14593">bug report</a>, and also updated my problem description. (It's specifically connected to background layers. I can have as many data layers as I want.)</p>
</div>
<div id="comment-55361-info" class="comment-info">
<span class="comment-age">(30 Mar '17, 09:51)</span> <span class="comment-user userinfo">pbb</span>
</div>
</div>
<span id="55371"></span>
<div id="comment-55371" class="comment">
<div id="post-55371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4016/pbb"></a><a href="https://help.openstreetmap.org/users/4016/pbb">@pbb</a>: ah, okay, I have tested with data layers. Screenshots and a detailed description help! Thanks for the good bug report over there. :-)</p>
</div>
<div id="comment-55371-info" class="comment-info">
<span class="comment-age">(30 Mar '17, 19:28)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="55419"></span>
<div id="comment-55419" class="comment">
<div id="post-55419-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wasn't initially aware than the problem only applied to background layers. But you're right, that would have shown up if I had posted screenshots :)</p>
</div>
<div id="comment-55419-info" class="comment-info">
<span class="comment-age">(01 Apr '17, 18:15)</span> <span class="comment-user userinfo">pbb</span>
</div>
</div>
</div>
<div id="comment-tools-55340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55340-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55467"></span>

<div id="answer-container-55467" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55467-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Apparently the problem was me using the 32-bit version of Java. After installing the 64-bit version, I am able to open many more background layers.</p>
<p>I don't really think this is the whole situation, because my guess is that most people only have 32-bit Java installed (since that is the default that the Java website offers), but it doesn't seem other people have the same problem.</p>
<p>But anyway, if this problem turns up, installing 64-bit Java is an easy work-around.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '17, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2f19e3a960bbc861e85b69c9c13a8e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbb&#39;s gravatar image" />
<p><span>pbb</span><br />
<span class="score" title="621 reputation points">621</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55467" class="comments-container">
&#10;</div>
<div id="comment-tools-55467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55467-form-container" class="comment-form-container">
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

