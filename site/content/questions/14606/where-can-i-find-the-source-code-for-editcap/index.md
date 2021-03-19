+++
type = "question"
title = "where can I find the source code for editcap"
description = '''I would like to know where I can find the source files for editcap. What libpcap API&#x27;s are being called to convert .pcapng to .pcap with the following cmd?  editcap -F libpcap -T ether file.pcapng file.pcap '''
date = "2012-09-28T10:13:00Z"
lastmod = "2012-09-28T10:53:00Z"
weight = 14606
keywords = [ "development", "libpcap" ]
aliases = [ "/questions/14606" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [where can I find the source code for editcap](/questions/14606/where-can-i-find-the-source-code-for-editcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14606-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know where I can find the source files for editcap. What libpcap API's are being called to convert .pcapng to .pcap with the following cmd?</p><blockquote><p>editcap -F libpcap -T ether file.pcapng file.pcap</p></blockquote></div><div id="question-tags" class="tags-container tags">development libpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '12, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/b88b0550acc863f790e891ac21ffb94e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phileo99&#39;s gravatar image" /><p>phileo99<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phileo99 has no accepted answers">0%</span></p></div></div><div id="comments-container-14606" class="comments-container"></div><div id="comment-tools-14606" class="comment-tools"></div><div class="clear"></div><div id="comment-14606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14607"></span>

<div id="answer-container-14607" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14607-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The current stable Wireshark sources, which includes the source code for <code>editcap</code>, can be downloaded from the Wireshark <a href="http://www.wireshark.org/download.html">download</a> page. If you're looking for a specific version, you can find it <a href="http://wiresharkdownloads.riverbed.com/wireshark/src/all-versions/">here</a>. If you want to get the very latest sources, you can visit the Wireshark <a href="http://www.wireshark.org/develop.html">developer</a> web page and follow the instructions provided. You can also view the sources online at <a href="http://anonsvn.wireshark.org/viewvc/">http://anonsvn.wireshark.org/viewvc/</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '12, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-14607" class="comments-container"><span id="14611"></span><div id="comment-14611" class="comment"><div id="post-14611-score" class="comment-score"></div><div class="comment-text"><p>And, <a href="http://www.wireshark.org/lists/wireshark-dev/201209/msg00205.html">as was pointed out in the e-mail thread on the same topic</a>, <em>no</em> libpcap APIs are being called in that case, as, while Wireshark and its tools use libpcap/WinPcap to capture network traffic, they don't use it to read capture files.</p></div><div id="comment-14611-info" class="comment-info"><span class="comment-age">(29 Sep '12, 17:17)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-14607" class="comment-tools"></div><div class="clear"></div><div id="comment-14607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

