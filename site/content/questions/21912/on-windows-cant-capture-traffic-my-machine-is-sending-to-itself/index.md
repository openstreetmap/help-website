+++
type = "question"
title = "On Windows, can&#x27;t capture traffic my machine is sending to itself"
description = '''Hi, I couldn&#x27;t capture SNTP packets using wireshark v1.10.0 running system (same system is using tool running as both server and client)can anyone help me out of this problem? thanks in advance, monisha'''
date = "2013-06-11T03:17:00Z"
lastmod = "2013-06-11T05:05:00Z"
weight = 21912
keywords = [ "windows", "loopback" ]
aliases = [ "/questions/21912" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [On Windows, can't capture traffic my machine is sending to itself](/questions/21912/on-windows-cant-capture-traffic-my-machine-is-sending-to-itself)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21912-score" class="post-score" title="current number of votes">0</div><span id="post-21912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I couldn't capture SNTP packets using wireshark v1.10.0 running system (same system is using tool running as both server and client)can anyone help me out of this problem? thanks in advance, monisha</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-loopback" rel="tag" title="see questions tagged &#39;loopback&#39;">loopback</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '13, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/cc0f627200f978a2b79eac84ddbfca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monisha&#39;s gravatar image" /><p><span>monisha</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monisha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jun '13, 16:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-21912" class="comments-container"><span id="21915"></span><div id="comment-21915" class="comment"><div id="post-21915-score" class="comment-score"></div><div class="comment-text"><p>did you use any capture filter? If so, please tell us which one. What is the SNTP tool used and what is the OS used?</p></div><div id="comment-21915-info" class="comment-info"><span class="comment-age">(11 Jun '13, 03:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="21918"></span><div id="comment-21918" class="comment"><div id="post-21918-score" class="comment-score"></div><div class="comment-text"><p>I'm using ntp server and client tool for time synchronisation(same as server and client)i need to capture the data what client is receiving.</p><p>I'm not using any filters. can I know what filters I can make use of</p></div><div id="comment-21918-info" class="comment-info"><span class="comment-age">(11 Jun '13, 03:41)</span> <span class="comment-user userinfo">monisha</span></div></div></div><div id="comment-tools-21912" class="comment-tools"></div><div class="clear"></div><div id="comment-21912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21916"></span>

<div id="answer-container-21916" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21916-score" class="post-score" title="current number of votes">1</div><span id="post-21916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're running on Windows, then capturing traffic between a client and server on the same machine is difficult if not impossible for the current WinPCap implementation.</p><p>Running on another OS such as Linux or OSX this should be possible.</p><p>See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">loopback capturing</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-21916" class="comments-container"><span id="21919"></span><div id="comment-21919" class="comment"><div id="post-21919-score" class="comment-score"></div><div class="comment-text"><p>yes I'm using windows 8. using single tool as both client and server. I need to capture the data of what the client receives. can i use wireshark in other windows and capture the data?</p></div><div id="comment-21919-info" class="comment-info"><span class="comment-age">(11 Jun '13, 03:47)</span> <span class="comment-user userinfo">monisha</span></div></div><span id="21924"></span><div id="comment-21924" class="comment"><div id="post-21924-score" class="comment-score"></div><div class="comment-text"><p>The easiest way is to run the client and server applications on different machines, then capture on either machine.</p></div><div id="comment-21924-info" class="comment-info"><span class="comment-age">(11 Jun '13, 05:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-21916" class="comment-tools"></div><div class="clear"></div><div id="comment-21916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

