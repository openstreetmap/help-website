+++
type = "question"
title = "PCAP file is compressed file format?"
description = '''HI All, I am very new to world of wireshark and pcap. I just like to understand that after capturing packets by tshark, it got stored in PCAP file. This PCAP file is compressed file? e.g Suppose the data transferred on wire is 1 MB so after capturing this data the PCAP file created by tshark will be...'''
date = "2015-04-21T23:49:00Z"
lastmod = "2015-04-22T02:04:00Z"
weight = 41656
keywords = [ "pcap", "compressed" ]
aliases = [ "/questions/41656" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PCAP file is compressed file format?](/questions/41656/pcap-file-is-compressed-file-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41656-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI All,</p><p>I am very new to world of wireshark and pcap. I just like to understand that after capturing packets by tshark, it got stored in PCAP file. This PCAP file is compressed file? e.g Suppose the data transferred on wire is 1 MB so after capturing this data the PCAP file created by tshark will be 1MB or less than that?<br />
</p></div><div id="question-tags" class="tags-container tags">pcap compressed</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 23:49</strong></p><img src="https://secure.gravatar.com/avatar/904e19785874be39705426e578c4c029?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aditi&#39;s gravatar image" /><p>Aditi<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aditi has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-41656" class="comments-container"></div><div id="comment-tools-41656" class="comment-tools"></div><div class="clear"></div><div id="comment-41656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41663"></span>

<div id="answer-container-41663" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41663-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It will be more than that, unless you decide to capture only parts of each frame. The data on the wire is divided into multiple frames, with each frame carrying a couple of protocol headers (which adds to the PCAP file size compared to the raw data). Plus each frame has a frame header in the PCAP file, and the PCAP file again has a file header. So no, the file size is greater than 1MB under normal circumstances, and PCAP does not compress.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41663" class="comments-container"></div><div id="comment-tools-41663" class="comment-tools"></div><div class="clear"></div><div id="comment-41663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

