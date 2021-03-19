+++
type = "question"
title = "how to display the packet&#x27;s CRC in the GUI and how to edit CRC with bad value"
description = '''I want to generate a cap file with bad CRC packets using wireshark. I recorded the traffic I want but: 1. I don&#x27;t see the CRC in the wireshark GUI and couldn&#x27;t find where to enable this view  2. I cant find a way to &quot;corrupt&quot; the CRC of all packets in the cap file thank you in advance!'''
date = "2013-05-01T00:50:00Z"
lastmod = "2013-05-01T01:49:00Z"
weight = 20862
keywords = [ "crc32", "crc" ]
aliases = [ "/questions/20862" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to display the packet's CRC in the GUI and how to edit CRC with bad value](/questions/20862/how-to-display-the-packets-crc-in-the-gui-and-how-to-edit-crc-with-bad-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20862-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to generate a cap file with bad CRC packets using wireshark. I recorded the traffic I want but: 1. I don't see the CRC in the wireshark GUI and couldn't find where to enable this view 2. I cant find a way to "corrupt" the CRC of all packets in the cap file</p><p>thank you in advance!</p></div><div id="question-tags" class="tags-container tags">crc32 crc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '13, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/7ee67ba3b6a071cfebc04dfdc07624d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ihovav&#39;s gravatar image" /><p>ihovav<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ihovav has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 May '13, 00:51</p></div></div><div id="comments-container-20862" class="comments-container"><span id="20863"></span><div id="comment-20863" class="comment"><div id="post-20863-score" class="comment-score"></div><div class="comment-text"><p>In which protocol is the bad CRC? Wireshark can't (currently) edit packets, you'll need to use another tool to do that, see the <a href="http://wiki.wireshark.org/Tools">tools</a> page on the wiki.</p></div><div id="comment-20863-info" class="comment-info"><span class="comment-age">(01 May '13, 01:35)</span> grahamb ♦</div></div></div><div id="comment-tools-20862" class="comment-tools"></div><div class="clear"></div><div id="comment-20862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20865"></span>

<div id="answer-container-20865" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20865-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you mean the CRC of the ethernet frame, then you're out of luck with a normal NIC. Most NIC (drivers) strip it before passing the packet to the system. That means wireshark (actually libpcap/WinPcap which does the capturing for wireshark) does not get to see the CRC.</p><p>There are capture cards that do not strip the CRC, but I have not used them myself so I can't advice you on that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '13, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20865" class="comments-container"><span id="20866"></span><div id="comment-20866" class="comment"><div id="post-20866-score" class="comment-score"></div><div class="comment-text"><p>thank you very much!</p></div><div id="comment-20866-info" class="comment-info"><span class="comment-age">(01 May '13, 01:51)</span> ihovav</div></div><span id="20877"></span><div id="comment-20877" class="comment"><div id="post-20877-score" class="comment-score"></div><div class="comment-text"><p>Network General S6040 devices do capture the FCS. I have tons of traces like that, some of which I took in a lab setup so I could offer to put excerpts of them up at Cloudshark. I haven't checked if any of them has a bad CRC, but I doubt it - it's not even the capture device that is the problem, but the switch will not forward it to the device if the checksum isn't correct (unless it's in cut through mode, which the switches in the lab weren't).</p></div><div id="comment-20877-info" class="comment-info"><span class="comment-age">(01 May '13, 09:04)</span> Jasper ♦♦</div></div></div><div id="comment-tools-20865" class="comment-tools"></div><div class="clear"></div><div id="comment-20865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

