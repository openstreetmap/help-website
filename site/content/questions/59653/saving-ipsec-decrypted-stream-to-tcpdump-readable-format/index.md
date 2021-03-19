+++
type = "question"
title = "Saving IPSec decrypted stream to tcpdump-readable format"
description = '''Hi, I have IPSec encrypted pcap file. My goal is to decrypt it using Wireshark and then export/save the resulting decrypted stream so that it can be read from/analyzed with tcpdump. [Aside: Actually the decrypted stream will be read with a tool that builds on top of tcpdump -- hence it NEEDS to be r...'''
date = "2017-02-23T23:43:00Z"
lastmod = "2017-02-24T01:55:00Z"
weight = 59653
keywords = [ "ipsec" ]
aliases = [ "/questions/59653" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Saving IPSec decrypted stream to tcpdump-readable format](/questions/59653/saving-ipsec-decrypted-stream-to-tcpdump-readable-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59653-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have IPSec encrypted pcap file. My goal is to decrypt it using Wireshark and then export/save the resulting decrypted stream so that it can be read from/analyzed with tcpdump. [Aside: Actually the decrypted stream will be read with a tool that builds on top of tcpdump -- hence it NEEDS to be readable by tcpdump; wireshark won't do]</p><p>I used wireshark 2.2.3 on MacBook to decrypt ESP (IPSec) packets just fine. I could "Export to PDUs" and then select "OSI Layer(3)" to get a resulting pcap file. I tried saving that as WireShark pcap, Redhat 6.1 pcap and in both cases when I try to read the file via tcpdump, I get the following error:</p><p><strong>$ tcpdump -r temp2.pcap reading from file temp2.pcap, link-type 252 tcpdump: packet printing is not supported for link type 252: use -w</strong></p><p>Perhaps I am missing something obvious/basic. Would really appreciate any tip/help to get past this.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">ipsec</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '17, 23:43</strong></p><img src="https://secure.gravatar.com/avatar/bac88a0eb09740c46700839972c297b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joeshmoe&#39;s gravatar image" /><p>joeshmoe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joeshmoe has no accepted answers">0%</span></p></div></div><div id="comments-container-59653" class="comments-container"></div><div id="comment-tools-59653" class="comment-tools"></div><div class="clear"></div><div id="comment-59653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59654"></span>

<div id="answer-container-59654" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59654-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think it is like the printout says tcpdump can't handle exported_pdu linktype packets. I think your options are: extend tcpdump to handle the linktype. Change your program to use tshark. Use text2pcap to add (back) a fake transport layer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '17, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-59654" class="comments-container"></div><div id="comment-tools-59654" class="comment-tools"></div><div class="clear"></div><div id="comment-59654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

