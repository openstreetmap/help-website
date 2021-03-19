+++
type = "question"
title = "The tcp sequence number altered?"
description = '''Some thing wrong when I was send a file with FTP . I captured the network card stream ,and found packet was Tagged retransmission by wireshark. client IP:123.160.53.111  sever IP:172.16.8.61was the server SIP and 221.181.100.222 was VIP. I saw that the packet whichTCP sequence number is 70529 retran...'''
date = "2014-02-25T20:53:00Z"
lastmod = "2014-03-13T18:33:00Z"
weight = 30192
keywords = [ "retransmissions", "troubleshooting" ]
aliases = [ "/questions/30192" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [The tcp sequence number altered?](/questions/30192/the-tcp-sequence-number-altered)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30192-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Some thing wrong when I was send a file with FTP . I captured the network card stream ,and found packet was Tagged retransmission by wireshark.</p><p>client IP:123.160.53.111 sever IP:172.16.8.61was the server SIP and 221.181.100.222 was VIP. I saw that the packet whichTCP sequence number is 70529 retransmissed in the ftp client. But in the ftp server,the sequence number was altered,and does not seems a retransmissed packed. I was confused,why ?</p></div><div id="question-tags" class="tags-container tags">retransmissions troubleshooting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '14, 20:53</strong></p><img src="https://secure.gravatar.com/avatar/96dac889270f47c00e9ed9d22615ce2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miaohf&#39;s gravatar image" /><p>miaohf<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miaohf has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Feb '14, 23:35</p></div></div><div id="comments-container-30192" class="comments-container"><span id="30193"></span><div id="comment-30193" class="comment"><div id="post-30193-score" class="comment-score"></div><div class="comment-text"><p>It's too awkful for the captured content showing. I'll put the shotscreen picture like below. <img src="https://osqa-ask.wireshark.org/upfiles/2014-02-26-125321_1440x900_scrot.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/2014-02-26-125303_1440x900_scrot_1.png" alt="alt text" /></p></div><div id="comment-30193-info" class="comment-info"><span class="comment-age">(25 Feb '14, 20:58)</span> miaohf</div></div></div><div id="comment-tools-30192" class="comment-tools"></div><div class="clear"></div><div id="comment-30192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="30194"></span>

<div id="answer-container-30194" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30194-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The client is using TCP segmentation offload. Sequence number 70529 at the sender is part of the large segment starting with 67633. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_038.png" alt="alt text" /> At the server it arrives as the 3rd segment <img src="https://osqa-ask.wireshark.org/upfiles/Selection_039.png" alt="alt text" /> The problem is that these ACKs (73425,76321,79217) never make it back to the client <img src="https://osqa-ask.wireshark.org/upfiles/Selection_040.png" alt="alt text" /> Also the retransmitted seqments 70529 never show up at the server.</p><p>There seems to be a NAT device in the path that might not be handling the high packet rate very well. So I suggest you turn off segmentation offload TSO using ethtool -K as described <a href="http://blog.securityonion.net/2011/10/when-is-full-packet-capture-not-full.html">here</a> and see if this circumvents the problem</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '14, 22:04</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 25 Feb '14, 23:19</p></div></div><div id="comments-container-30194" class="comments-container"><span id="30195"></span><div id="comment-30195" class="comment"><div id="post-30195-score" class="comment-score"></div><div class="comment-text"><p>THANK YOU for your reply, mrEEde. The ACKs (73425,76321,79217) never make it back to the client BECAUSE: the client had never send these packages,maybe the network equipment went wrong,but how it goes ?</p></div><div id="comment-30195-info" class="comment-info"><span class="comment-age">(25 Feb '14, 22:56)</span> miaohf</div></div><span id="30196"></span><div id="comment-30196" class="comment"><div id="post-30196-score" class="comment-score"></div><div class="comment-text"><p>I just updated my answer with a reference to the ethtool -k to turn off segmentation offload</p></div><div id="comment-30196-info" class="comment-info"><span class="comment-age">(25 Feb '14, 23:20)</span> mrEEde</div></div><span id="30203"></span><div id="comment-30203" class="comment"><div id="post-30203-score" class="comment-score"></div><div class="comment-text"><p>[[email protected]_3G_FTP_01 miaohf]# ethtool -K eth2 tso off I turned off the TSO,and the problem appears again. The package captured from client as follow,and I can't get the server's package today.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2014-02-26-175552_1440x900_scrot.png" alt="alt text" /></p></div><div id="comment-30203-info" class="comment-info"><span class="comment-age">(26 Feb '14, 02:02)</span> miaohf</div></div><span id="30302"></span><div id="comment-30302" class="comment"><div id="post-30302-score" class="comment-score"></div><div class="comment-text"><p>When you change the TCP preferences to relative sequence numbers, you can see how many bytes are actually sent befor the session stalls.</p><p>Can you see a pattern in multiple transfers? How many bytes go through before the session stalls?</p></div><div id="comment-30302-info" class="comment-info"><span class="comment-age">(28 Feb '14, 22:47)</span> mrEEde</div></div><span id="30709"></span><div id="comment-30709" class="comment"><div id="post-30709-score" class="comment-score"></div><div class="comment-text"><p>anybody help me ? any advice is expected,thanks. :)</p></div><div id="comment-30709-info" class="comment-info"><span class="comment-age">(12 Mar '14, 01:47)</span> miaohf</div></div><span id="30811"></span><div id="comment-30811" class="comment not_top_scorer"><div id="post-30811-score" class="comment-score"></div><div class="comment-text"><p>"... advice is expected" Diagnosing this with hardcopy pictures of tshark output is not very efficient. For most people here time is a limited resource so could you please post the capture files to <a href="http://cloudshark.org">http://cloudshark.org</a> This way we can use wireshark - this is what this QA site is about ;-) - to speed up understanding what the problem might be. You might want to use editcap -s 64 to strip off the data part of the packets.</p></div><div id="comment-30811-info" class="comment-info"><span class="comment-age">(15 Mar '14, 05:49)</span> mrEEde</div></div></div><div id="comment-tools-30194" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-30194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30749"></span>

<div id="answer-container-30749" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30749-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>sorry, mrEEde my picture is so big ,and I almost not see your reply on 28 Feb. I'll show you the obsolute sequence number below.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '14, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/96dac889270f47c00e9ed9d22615ce2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miaohf&#39;s gravatar image" /><p>miaohf<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miaohf has no accepted answers">0%</span></p></img></div></div><div id="comments-container-30749" class="comments-container"></div><div id="comment-tools-30749" class="comment-tools"></div><div class="clear"></div><div id="comment-30749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30782"></span>

<div id="answer-container-30782" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30782-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/2014-03-14-093339_1425x832_scrot.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/2014-03-14-093442_1404x826_scrot.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '14, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/96dac889270f47c00e9ed9d22615ce2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miaohf&#39;s gravatar image" /><p>miaohf<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miaohf has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '14, 18:36</p></div></div><div id="comments-container-30782" class="comments-container"></div><div id="comment-tools-30782" class="comment-tools"></div><div class="clear"></div><div id="comment-30782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

