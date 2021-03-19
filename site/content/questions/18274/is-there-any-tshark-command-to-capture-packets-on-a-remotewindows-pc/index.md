+++
type = "question"
title = "Is there any tshark command to capture packets on a remote(windows) PC"
description = '''Hi, i am trying to capture packets on a remote (windows)machine from my linux machine. please suggest me a tshark command to capture packets on a remote windows interface.'''
date = "2013-02-04T01:50:00Z"
lastmod = "2013-02-05T13:43:00Z"
weight = 18274
keywords = [ "tshark" ]
aliases = [ "/questions/18274" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any tshark command to capture packets on a remote(windows) PC](/questions/18274/is-there-any-tshark-command-to-capture-packets-on-a-remotewindows-pc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18274-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i am trying to capture packets on a remote (windows)machine from my linux machine. please suggest me a tshark command to capture packets on a remote windows interface.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '13, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/11d68dee0b0450da0c8ca70eae4566ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anil1982&#39;s gravatar image" /><p>anil1982<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anil1982 has no accepted answers">0%</span></p></div></div><div id="comments-container-18274" class="comments-container"></div><div id="comment-tools-18274" class="comment-tools"></div><div class="clear"></div><div id="comment-18274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18328"></span>

<div id="answer-container-18328" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18328-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please read the <a href="http://wiki.wireshark.org/CaptureSetup/WinPcapRemote">wiki about remote capturing</a>. Quick hint: You need to start rpcapd (WinPcap install directory) on Windows</p><blockquote><p><a href="http://www.winpcap.org/docs/docs_40_2/html/group__remote.html">http://www.winpcap.org/docs/docs_40_2/html/group__remote.html</a></p></blockquote><p>and then add "Remote Interfaces" in Wireshark.</p><blockquote><p><a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCapInterfaceRemoteSection.html">http://www.wireshark.org/docs/wsug_html_chunked/ChCapInterfaceRemoteSection.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '13, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-18328" class="comments-container"></div><div id="comment-tools-18328" class="comment-tools"></div><div class="clear"></div><div id="comment-18328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

