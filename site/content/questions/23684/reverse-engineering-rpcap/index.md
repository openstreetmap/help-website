+++
type = "question"
title = "Reverse Engineering RPCAP"
description = '''Hello, I&#x27;ve got an application that requires me to attach a script to an existing RPCAP daemon. So I&#x27;m working on reverse engineering the RPCAP protocol. Wireshark does a fantastic job of decoding the basic authentication, open request, and filter request packets. But I&#x27;m having trouble with the act...'''
date = "2013-08-09T13:46:00Z"
lastmod = "2013-08-09T14:34:00Z"
weight = 23684
keywords = [ "rpcap" ]
aliases = [ "/questions/23684" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse Engineering RPCAP](/questions/23684/reverse-engineering-rpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23684-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I've got an application that requires me to attach a script to an existing RPCAP daemon. So I'm working on reverse engineering the RPCAP protocol. Wireshark does a fantastic job of decoding the basic authentication, open request, and filter request packets. But I'm having trouble with the actual data packets. I can parse the rpcap_header and rpcap_pkthdr. But I'm confused as to what comes next. That is, there is some unstructured (to me, anyway) bytes between the rpcap_pkthdr and the raw payload at the end of the packet.</p><p>Any ideas how to parse this?</p><p>Thanks!</p><p>Norman</p></div><div id="question-tags" class="tags-container tags">rpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '13, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/6ec7697ec27284826a651f7a603d1825?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="normelton&#39;s gravatar image" /><p>normelton<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="normelton has no accepted answers">0%</span></p></div></div><div id="comments-container-23684" class="comments-container"></div><div id="comment-tools-23684" class="comment-tools"></div><div class="clear"></div><div id="comment-23684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23685"></span>

<div id="answer-container-23685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23685-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So I'm working on reverse engineering the RPCAP protocol.</p></blockquote><p>wouldn't it be easier to look at the code of rpcapd (part of WinPcap) instead of reverse engineering the protocol?</p><blockquote><p><a href="http://www.winpcap.org/install/bin/WpcapSrc_4_1_3.zip">http://www.winpcap.org/install/bin/WpcapSrc_4_1_3.zip</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '13, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23685" class="comments-container"></div><div id="comment-tools-23685" class="comment-tools"></div><div class="clear"></div><div id="comment-23685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

