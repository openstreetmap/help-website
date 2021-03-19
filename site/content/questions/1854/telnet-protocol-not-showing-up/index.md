+++
type = "question"
title = "Telnet protocol not showing up"
description = '''I have two servers that act as application servers. When I run wireshark on one of the servers the telnet data packets show up. But when I run wireshark on the other server they don&#x27;t. I can see the TCP handshake but not the data packets. I have uninstalled and reinstalled wireshark several times. I...'''
date = "2011-01-21T12:02:00Z"
lastmod = "2011-01-21T12:18:00Z"
weight = 1854
keywords = [ "protocol", "missing" ]
aliases = [ "/questions/1854" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Telnet protocol not showing up](/questions/1854/telnet-protocol-not-showing-up)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1854-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two servers that act as application servers. When I run wireshark on one of the servers the telnet data packets show up. But when I run wireshark on the other server they don't. I can see the TCP handshake but not the data packets. I have uninstalled and reinstalled wireshark several times. I know the packets are there because a lot of users are using that server and I see the handshakes.</p><p>What should I look at?</p></div><div id="question-tags" class="tags-container tags">protocol missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '11, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/1615a1a2b3014605f2b40304d3615cff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PAML&#39;s gravatar image" /><p>PAML<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PAML has no accepted answers">0%</span></p></div></div><div id="comments-container-1854" class="comments-container"></div><div id="comment-tools-1854" class="comment-tools"></div><div class="clear"></div><div id="comment-1854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1855"></span>

<div id="answer-container-1855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1855-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at the settings of the driver of your network card. It is probably configured to do some offloading. That often makes data packets slip past the capturing code.</p><p>You can find more info on <a href="http://wiki.wireshark.org/CaptureSetup/Offloading">http://wiki.wireshark.org/CaptureSetup/Offloading</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '11, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1855" class="comments-container"><span id="1856"></span><div id="comment-1856" class="comment"><div id="post-1856-score" class="comment-score"></div><div class="comment-text"><p>I looked and that option was not there. Both machines have the network cards configured the same. I dont think that is it, thanks for the answer!</p></div><div id="comment-1856-info" class="comment-info"><span class="comment-age">(21 Jan '11, 12:31)</span> PAML</div></div><span id="1857"></span><div id="comment-1857" class="comment"><div id="post-1857-score" class="comment-score"></div><div class="comment-text"><p>Another thing that could be in the way like this are VPN drivers...</p></div><div id="comment-1857-info" class="comment-info"><span class="comment-age">(21 Jan '11, 12:38)</span> SYN-bit ♦♦</div></div><span id="1858"></span><div id="comment-1858" class="comment"><div id="post-1858-score" class="comment-score"></div><div class="comment-text"><p>These are physical machines not virtual machines, is that what you mean?</p></div><div id="comment-1858-info" class="comment-info"><span class="comment-age">(21 Jan '11, 12:50)</span> PAML</div></div><span id="1860"></span><div id="comment-1860" class="comment"><div id="post-1860-score" class="comment-score"></div><div class="comment-text"><p>:-) No, I meant software that makes a Virtual Private Network connection (VPN). They also nest themselves in the Networking stack which can get in the way of the capturing mechanism.</p></div><div id="comment-1860-info" class="comment-info"><span class="comment-age">(21 Jan '11, 12:58)</span> SYN-bit ♦♦</div></div><span id="1861"></span><div id="comment-1861" class="comment"><div id="post-1861-score" class="comment-score"></div><div class="comment-text"><p>how do I check that. The machines were set up the same, at least that is what the server guys said. LOL</p></div><div id="comment-1861-info" class="comment-info"><span class="comment-age">(21 Jan '11, 13:02)</span> PAML</div></div></div><div id="comment-tools-1855" class="comment-tools"></div><div class="clear"></div><div id="comment-1855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

