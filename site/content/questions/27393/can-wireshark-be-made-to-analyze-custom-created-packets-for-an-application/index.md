+++
type = "question"
title = "Can Wireshark be made to analyze custom-created packets for an application?"
description = '''I have created custom IP packets using Java jpcap library. The packet header and data are assigned 20 and 26 respectively. As data I am sending &quot;ABCDEFGHIJKLMNOPQRSTUVWXYZ&quot;. But when I analyze the packets using wireshark, it reads the 1st byte of the data, and treats it as a part of some upper layer...'''
date = "2013-11-26T02:42:00Z"
lastmod = "2013-11-26T02:50:00Z"
weight = 27393
keywords = [ "ip", "jpcap", "packet", "wireshark" ]
aliases = [ "/questions/27393" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can Wireshark be made to analyze custom-created packets for an application?](/questions/27393/can-wireshark-be-made-to-analyze-custom-created-packets-for-an-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27393-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have created custom IP packets using Java jpcap library. The packet header and data are assigned 20 and 26 respectively. As data I am sending "ABCDEFGHIJKLMNOPQRSTUVWXYZ". But when I analyze the packets using wireshark, it reads the 1st byte of the data, and treats it as a part of some upper layer header (say TCP!). Say the 1st IP data byte is 0x41 , i.e. 'A' so it reads 4 and treats it as start of another IPv4 header. I think I may have to change some settings! If I change the 1st data byte to some other value say 0x65, it now assumes a 'TCP' header follows.</p><p>This can happen, as wireshark reads the IP header length and data length from IP header, but it does not know when does the IP data start. It may also follow a TCP header. Is there a way I can get around this problem??</p></div><div id="question-tags" class="tags-container tags">ip jpcap packet wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/24af0b45730f0aeb823e25cd0c541bc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mohit93&#39;s gravatar image" /><p>mohit93<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mohit93 has no accepted answers">0%</span></p></div></div><div id="comments-container-27393" class="comments-container"></div><div id="comment-tools-27393" class="comment-tools"></div><div class="clear"></div><div id="comment-27393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27395"></span>

<div id="answer-container-27395" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27395-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're creating packets you need to follow protocol specifications. Most likely you set a protocol type of 6 in your IP header, which means that the next protocol layer is TCP. And of course Wireshark will then try to decode the next bytes after the IP header as TCP - it's not Wireshark's fault that you put something else entirely in those bytes.</p><p>So if you're making stuff up try to keep it valid, so no, you do not need to change "some settings". You need to make sure your packet generator does things the right way ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-27395" class="comments-container"><span id="27400"></span><div id="comment-27400" class="comment"><div id="post-27400-score" class="comment-score"></div><div class="comment-text"><p>The IP header has protocol specification as 4, and it reads IP header fine. How do I make sure that Wireshark knows -- What follows this IP header is IP data, and not the start of some other protocol header?</p><p>The first character of my IP data is 'A' or 0x41, so it reads 4 and thinks it is the start of another IP header!</p><p>I am generating my packets using jpcap and the following code:</p><p><code>IPPacket p=new IPPacket(); //specify IPv4 header parameters p.setIPv4Parameter(0,false,false,false,0,false,false,false,0,65,128, IPPacket.IPPROTO_IP,InetAddress.getByName("10.109.22.96"),InetAddress.getByName("10.109.22.17")); p.data=("ABCDEFGHIJKLMNOPQRSTUVWXYZ").getBytes(); EthernetPacket ether=new EthernetPacket(); ether.frametype=EthernetPacket.ETHERTYPE_IP; //set source and destination MAC addresses String strdst = new String("54:42:49:73:99:18"); ether.dst_mac = strdst.getBytes(); String strsrc = new String("70:5a:b6:8a:3b:e9"); ether.src_mac = strsrc.getBytes(); //set the datalink frame of the packet p as ether p.datalink=ether;</code></p></div><div id="comment-27400-info" class="comment-info"><span class="comment-age">(26 Nov '13, 03:31)</span> mohit93</div></div><span id="27401"></span><div id="comment-27401" class="comment"><div id="post-27401-score" class="comment-score"></div><div class="comment-text"><p>What is the protocol type you use? You might want to take a look at this list to select a protocol type that works for you:</p><p><a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml</a></p></div><div id="comment-27401-info" class="comment-info"><span class="comment-age">(26 Nov '13, 03:32)</span> Jasper ♦♦</div></div><span id="27404"></span><div id="comment-27404" class="comment"><div id="post-27404-score" class="comment-score"></div><div class="comment-text"><p>I think you're creating an IPv4 header with a protocol type of IPv4, which means that the first IP layer marks the bytes following itself as another IPv4 header. I have no documentation about the "setIPv4Parameter" function (and I don't want to waste time on googling it), but I guess the "IPPacket.IPPROTO_IP" parameter is what is causing this.</p></div><div id="comment-27404-info" class="comment-info"><span class="comment-age">(26 Nov '13, 03:45)</span> Jasper ♦♦</div></div><span id="27405"></span><div id="comment-27405" class="comment"><div id="post-27405-score" class="comment-score"></div><div class="comment-text"><p>@mohit93: see my answer to your other question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/27372/two-ip-headers-before-data-using-jpcap">http://ask.wireshark.org/questions/27372/two-ip-headers-before-data-using-jpcap</a></p></blockquote><p>I think you might (probably) misunderstand the IPv4 header structure.</p></div><div id="comment-27405-info" class="comment-info"><span class="comment-age">(26 Nov '13, 03:46)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27395" class="comment-tools"></div><div class="clear"></div><div id="comment-27395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

