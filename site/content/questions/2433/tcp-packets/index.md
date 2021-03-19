+++
type = "question"
title = "TCP packets"
description = '''What should I type in filter if I want to see TCP packets and TCP SIN packets that I have sent?'''
date = "2011-02-19T23:39:00Z"
lastmod = "2011-02-20T00:40:00Z"
weight = 2433
keywords = [ "tcppackets" ]
aliases = [ "/questions/2433" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP packets](/questions/2433/tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2433-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What should I type in filter if I want to see TCP packets and TCP SIN packets that I have sent?</p></div><div id="question-tags" class="tags-container tags">tcppackets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '11, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/96e902e433f9ca63286cc774486728f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baran&#39;s gravatar image" /><p>baran<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baran has no accepted answers">0%</span></p></div></div><div id="comments-container-2433" class="comments-container"></div><div id="comment-tools-2433" class="comment-tools"></div><div class="clear"></div><div id="comment-2433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2434"></span>

<div id="answer-container-2434" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2434-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>For seeing only TCP packets, you can use the filter <code>"tcp"</code> which can be used both as a capture filter and as a display filter.</p><p>If you only want to see TCP SYN packets, you can use the display filter <code>"tcp.flags.syn==1"</code> and the capture filter <code>"tcp[13]&amp;2=2"</code>.</p><p>If you want to limit it even further to only the SYN packets that you are sending, you can and an IP filter and get <code>"tcp.flags.syn==1 and ip.src==&lt;YOUR_IP&gt;"</code> (display) and <code>"tcp[13]&amp;2=2 and src host &lt;YOUR_IP&gt;"</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '11, 00:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2434" class="comments-container"><span id="2436"></span><div id="comment-2436" class="comment"><div id="post-2436-score" class="comment-score"></div><div class="comment-text"><p>I do thank U for answering me.</p></div><div id="comment-2436-info" class="comment-info"><span class="comment-age">(20 Feb '11, 00:58)</span> baran</div></div><span id="2486"></span><div id="comment-2486" class="comment"><div id="post-2486-score" class="comment-score"></div><div class="comment-text"><p>How can I see TCP packets that I am sending them?not all TCP packets.</p></div><div id="comment-2486-info" class="comment-info"><span class="comment-age">(22 Feb '11, 09:55)</span> baran</div></div><span id="2488"></span><div id="comment-2488" class="comment"><div id="post-2488-score" class="comment-score"></div><div class="comment-text"><p>See my answer above in which I use a filter to select only packets which have your IP address as the source.</p></div><div id="comment-2488-info" class="comment-info"><span class="comment-age">(22 Feb '11, 10:02)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-2434" class="comment-tools"></div><div class="clear"></div><div id="comment-2434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

