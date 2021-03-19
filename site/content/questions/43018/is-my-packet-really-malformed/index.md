+++
type = "question"
title = "Is my packet really malformed?"
description = '''Hi, Wireshark marked one of my packets as malformed and I am struggling to find the reason. The packet in hex format is: 000000 B4 B5 2F BF BD 5D 00 D0 ........ 000008 95 F8 E8 90 08 00 45 00 ........ 000010 00 29 00 06 00 00 3B 06 ........ 000018 B9 7A 0A 87 19 75 87 FA ........ 000020 1A 59 14 51 ...'''
date = "2015-06-09T11:36:00Z"
lastmod = "2015-06-10T04:06:00Z"
weight = 43018
keywords = [ "decode" ]
aliases = [ "/questions/43018" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is my packet really malformed?](/questions/43018/is-my-packet-really-malformed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43018-score" class="post-score" title="current number of votes">0</div><span id="post-43018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Wireshark marked one of my packets as malformed and I am struggling to find the reason. The packet in hex format is:</p><pre><code>000000 B4 B5 2F BF BD 5D 00 D0 ........
000008 95 F8 E8 90 08 00 45 00 ........
000010 00 29 00 06 00 00 3B 06 ........
000018 B9 7A 0A 87 19 75 87 FA ........
000020 1A 59 14 51 C8 88 00 00 ........
000028 19 72 55 91 72 E4 50 18 ........
000030 5A 3F CE 7B 00 00 02 04 ........
000038 05 AA 41 00             ....</code></pre><p>This is a TCP packet with one byte data. The data byte is the second last byte in the penultimate line ('02').</p><p>The problem is, if I change the data to anything else (say, make the data byte '01'), the Wireshark considers the packet legitimate. I.e, Wireshark considers the following packet good.</p><pre><code>000000 B4 B5 2F BF BD 5D 00 D0 ........
000008 95 F8 E8 90 08 00 45 00 ........
000010 00 29 00 06 00 00 3B 06 ........
000018 B9 7A 0A 87 19 75 87 FA ........
000020 1A 59 14 51 C8 88 00 00 ........
000028 19 72 55 91 72 E4 50 18 ........
000030 5A 3F CE 7B 00 00 01 04 ........
000038 05 AA 41 00             ....</code></pre><p>Will appreciate any help. Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '15, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/d7e5eeb4533805c17908a4109125acbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dineshpandey&#39;s gravatar image" /><p><span>dineshpandey</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dineshpandey has no accepted answers">0%</span></p></div></div><div id="comments-container-43018" class="comments-container"><span id="43019"></span><div id="comment-43019" class="comment"><div id="post-43019-score" class="comment-score"></div><div class="comment-text"><p>Just wanted to add.</p><p>uname -a: Linux venus.localdomain 2.6.32-504.1.3.el6.x86_64 #1 SMP Tue Nov 11 17:57:25 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux</p><p>Wireshark version: 1.8.10</p></div><div id="comment-43019-info" class="comment-info"><span class="comment-age">(09 Jun '15, 11:41)</span> <span class="comment-user userinfo">dineshpandey</span></div></div></div><div id="comment-tools-43018" class="comment-tools"></div><div class="clear"></div><div id="comment-43018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43034"></span>

<div id="answer-container-43034" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43034-score" class="post-score" title="current number of votes">1</div><span id="post-43034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your first frame gets erroneously dissected by the FTMP dissector (Flight Message Transfer Protocol).</p><p><img src="https://osqa-ask.wireshark.org/upfiles/q43018.screenshot_d4KJWf2.png" alt="alt text" /></p><p>If you disable that dissector, the frame is not marked as malformed anymore.</p><blockquote><p>Analyze -&gt; Enabled Protocols -&gt; FMTP (uncheck it).</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '15, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-43034" class="comments-container"></div><div id="comment-tools-43034" class="comment-tools"></div><div class="clear"></div><div id="comment-43034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

