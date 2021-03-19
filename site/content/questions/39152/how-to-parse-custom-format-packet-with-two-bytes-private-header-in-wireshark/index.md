+++
type = "question"
title = "How to parse custom format packet with two bytes private header in wireshark?"
description = '''Below is a example dump of the custom format packet, with two bytes of private header &quot;00 01&quot; at the beginning of each packet. So is there a way to ask wireshark to skip the two bytes private header, and treat the remaining content as a normal PDU? Or how to write a custome dissector for this? 0000 ...'''
date = "2015-01-15T03:48:00Z"
lastmod = "2015-01-15T08:29:00Z"
weight = 39152
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/39152" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to parse custom format packet with two bytes private header in wireshark?](/questions/39152/how-to-parse-custom-format-packet-with-two-bytes-private-header-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39152-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Below is a example dump of the custom format packet, with two bytes of private header "00 01" at the beginning of each packet.</p><p>So is there a way to ask wireshark to skip the two bytes private header, and treat the remaining content as a normal PDU? Or how to write a custome dissector for this?</p><pre><code>0000 00 01 ff ff ff ff ff ff f0 1f af 20 18 52 08 00
0010 45 00 01 63 4b cf 00 00 40 11 2d bc 00 00 00 00
0020 ff ff ff ff 00 44 00 43 01 4f 7a 9d 01 01 06 00
0030 09 e9 ac d2 04 00 00 00 00 00 00 00 00 00 00 00
0040 00 00 00 00 00 00 00 00 f0 1f af 20 18 52 00 00
0050 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0060 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0070 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0080 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0090 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00a0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00b0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00c0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00d0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00e0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00f0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0100 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0110 00 00 00 00 00 00 00 00 63 82 53 63 35 01 03 3d
0120 07 01 f0 1f af 20 18 52 32 04 0a 29 04 74 0c 0b
0130 42 4a 4e 47 4c 48 5a 42 41 4f 59 51 1d 00 00 00
0140 42 4a 4e 47 4c 48 5a 42 41 4f 59 2e 61 70 2e 74
0150 68 6d 75 6c 74 69 2e 63 6f 6d 3c 08 4d 53 46 54
0160 20 35 2e 30 37 0c 01 0f 03 06 2c 2e 2f 1f 21 79
0170 f9 2b ff</code></pre></div><div id="question-tags" class="tags-container tags">dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '15, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/f8ff7cac8a632869fec673fd6c9ec22f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HuangY&#39;s gravatar image" /><p>HuangY<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HuangY has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jan '15, 03:49</p></div></div><div id="comments-container-39152" class="comments-container"></div><div id="comment-tools-39152" class="comment-tools"></div><div class="clear"></div><div id="comment-39152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39166"></span>

<div id="answer-container-39166" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39166-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use editcap to remove the two bytes in front of the actual packet (I have seen this on network security monitoring devices, e.g. McAfee IPS sensors), like this:</p><pre><code>editcap -C 2 original.pcapng new.pcapng</code></pre>Make sure you use uppercase "C", because lowercase "c" is something else. Editcap is a command line tool you can find in the Wireshark installation directory.</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '15, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39166" class="comments-container"><span id="39181"></span><div id="comment-39181" class="comment"><div id="post-39181-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, it works!</p><p>And what if I also want to do the same in live capture?</p><p>Could you please tell me is there any good way, or place to change wireshark code to do the job? I have no much idea on that right now.</p></div><div id="comment-39181-info" class="comment-info"><span class="comment-age">(15 Jan '15, 20:29)</span> HuangY</div></div><span id="39183"></span><div id="comment-39183" class="comment"><div id="post-39183-score" class="comment-score"></div><div class="comment-text"><p>From what type of device are you doing the live capture?</p></div><div id="comment-39183-info" class="comment-info"><span class="comment-age">(15 Jan '15, 20:30)</span> Guy Harris ♦♦</div></div><span id="39187"></span><div id="comment-39187" class="comment"><div id="post-39187-score" class="comment-score"></div><div class="comment-text"><p>OK, I am developing some layer 2 device, and the inner communication between different sub-systems will add and remove two bytes of private header. So if I want to analysis the packets between the two, it will be much more convenient that wireshark can ignore these two bytes and parse the remaining content as usual.</p><p>That's it, not for some suspicious intention.</p></div><div id="comment-39187-info" class="comment-info"><span class="comment-age">(15 Jan '15, 23:32)</span> HuangY</div></div><span id="39191"></span><div id="comment-39191" class="comment"><div id="post-39191-score" class="comment-score"></div><div class="comment-text"><p>It's not a question of suspicion, it's a question of either having the <em>capture</em> code path strip the two bytes or of introducing a new link-layer header type for pcap/pcap-ng.</p><p>So on what operating system is this being done, and what software are you using to capture it? Is this Windows, Linux, OS X, {Free,Net,Open,DragonFly}BSD, Solaris, etc.? Are you capturing on a network interface as shown by <code>ifconfig</code>/<code>ipconfig</code> or something else? If you want to do the same in a live capture, we'll have to know into what software to add the code to remove the header, or will need to assign a new link-layer header type so your packets can be processed "natively" by Wireshark.</p></div><div id="comment-39191-info" class="comment-info"><span class="comment-age">(15 Jan '15, 23:49)</span> Guy Harris ♦♦</div></div><span id="39192"></span><div id="comment-39192" class="comment"><div id="post-39192-score" class="comment-score"></div><div class="comment-text"><p>I just capture it using wireshark, on any OS that wireshark can be installed, and on a real network interface, as I can mirror the internal packets out.</p><p>So I think this should not be a common senario, and I don't think it is proper for wireshark to support this as a "native" type. all I want is that if wireshark can have some flexibility to add some mechanism and let user can add such rule, it will be great!</p><p>the rule could be to check first two bytes value, if it is equal to "00 01" or "00 02" or something else, then skip them ...</p></div><div id="comment-39192-info" class="comment-info"><span class="comment-age">(16 Jan '15, 00:34)</span> HuangY</div></div><span id="39195"></span><div id="comment-39195" class="comment not_top_scorer"><div id="post-39195-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I just capture it using wireshark, on any OS that wireshark can be installed</p></blockquote><p>So that means you will see those two extra bytes on Linux, Windows, OS X, and even IRIX? If not, then it won't be "on any OS that wireshark can be installed".</p><blockquote><p>and on a real network interface</p></blockquote><p>Presumably not <em>any</em> network interface, just your layer 2 device, right?</p></div><div id="comment-39195-info" class="comment-info"><span class="comment-age">(16 Jan '15, 01:46)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-39166" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-39166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

