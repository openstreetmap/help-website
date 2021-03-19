+++
type = "question"
title = "tcp source port starting byte in gre tunnel"
description = '''hi, for a traffic shaping experiment i would like to mark packets with iptables or tc on the ppp0 interface. the packet itself goes over a gre tunnel and ive been looking into finding out the exact location of the destination port within such a packet. capturing with tcpdump like this: tcpdump -i pp...'''
date = "2017-03-16T09:51:00Z"
lastmod = "2017-03-16T14:30:00Z"
weight = 60114
keywords = [ "iptables" ]
aliases = [ "/questions/60114" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcp source port starting byte in gre tunnel](/questions/60114/tcp-source-port-starting-byte-in-gre-tunnel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60114-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>for a traffic shaping experiment i would like to mark packets with iptables or tc on the ppp0 interface. the packet itself goes over a gre tunnel and ive been looking into finding out the exact location of the destination port within such a packet.</p><p>capturing with tcpdump like this: tcpdump -i ppp0 -nnXSs 0 -c 2 -w /tmp/gre-test.pcap proto gre</p><p>is shown in wireshark with these layers: frame -&gt; linux cooked capture -&gt; ipv4 -&gt; gre -&gt; ipv4 -&gt; tcp</p><p>it looks like the "linux cooked capture" header is 32 bits long - now when writing tc rules, should i include these 8 bytes into my calculation or not?</p><p>theres a explanation what "linux cooked capture" is here: <a href="https://wiki.wireshark.org/SLL">https://wiki.wireshark.org/SLL</a> but im not sure which of the cases it could be.</p><p>assuming that the ipv4 headers come without options and therefore are 20bytes long i would calculate like this:<br />
(assuming that pppoe is added by ppp, the ppp0 interface comes up with the mtu 1492.<br />
ipv4 (20) -&gt; gre (4) -&gt; ipv4 (20) -&gt; tcp = 44bytes</p><p>so starting at position 46 should begin the tcp destination port of the innermost packet.</p><p>but since my calculation does assume ipv4 as the first level and not linux cooked capture im not really sure which number it will be. my first test:<br />
iptables -I POSTROUTING -t mangle -m u32 --u32 "46&amp;0xFFFF=0x1194" -j LOG<br />
</p><p>for udp destination port (0x1194 = 4500, starting at position 46)<br />
</p><p>was not successfully.<br />
i used nc, the receiving side was run with: nc -l -p 4500 -s 10.0.5.1 showed the text output but did not increate the iptables counter</p></div><div id="question-tags" class="tags-container tags">iptables</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '17, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/b30cb1095b17ef123aedc0a68e09d69e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steven_2&#39;s gravatar image" /><p>Steven_2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steven_2 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Mar '17, 14:07</p></div></div><div id="comments-container-60114" class="comments-container"></div><div id="comment-tools-60114" class="comment-tools"></div><div class="clear"></div><div id="comment-60114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60128"></span>

<div id="answer-container-60128" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60128-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>it looks like the "linux cooked capture" header is 32 bits long - now when writing tc rules, should i include these 16bytes into my calculation or not?</em></p><p>To be clear, the Linux cooked capture header length is 16 bytes, not 32 bits.</p><p>I think you will need to change the offset to 44, e.g.:</p><p><code>     iptables -I POSTROUTING -t mangle -m u32 --u32 "44&amp;0xFFFF=0x1194" -j LOG</code></p><p>u32 grabs 4 bytes, not 2 bytes, so you should grab the 4 bytes starting with the source port and then apply the mask to the upper 2 bytes to isolate the lower 2 bytes, which are the 2 bytes that comprise the destination port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '17, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-60128" class="comments-container"><span id="60129"></span><div id="comment-60129" class="comment"><div id="post-60129-score" class="comment-score"></div><div class="comment-text"><p>thank you for the answer, seems that its working...but i need some sleep.</p><p>do you meant that 8 bytes and not 16 bytes like i wrote? in wireshark in the detail view it uses one line and goes from left to right up to the end.</p></div><div id="comment-60129-info" class="comment-info"><span class="comment-age">(16 Mar '17, 15:21)</span> Steven_2</div></div><span id="60130"></span><div id="comment-60130" class="comment"><div id="post-60130-score" class="comment-score"></div><div class="comment-text"><p>You first wrote, <em>"it looks like the "linux cooked capture" header is 32 bits long ..."</em>, but that's wrong. 32-bits is 4 bytes, not 16 bytes. You must have realized the header was actually 16 bytes though because you then continued with, <em>"should i include these 16bytes into my calculation or not?"</em>. So, I merely thought that I'd clarify the length for the benefit of anyone else who might be reading and might otherwise be confused by these conflicting length values.</p></div><div id="comment-60130-info" class="comment-info"><span class="comment-age">(16 Mar '17, 15:48)</span> cmaynard ♦♦</div></div><span id="60131"></span><div id="comment-60131" class="comment"><div id="post-60131-score" class="comment-score"></div><div class="comment-text"><p>yes you are right, my mistake</p></div><div id="comment-60131-info" class="comment-info"><span class="comment-age">(16 Mar '17, 16:05)</span> Steven_2</div></div></div><div id="comment-tools-60128" class="comment-tools"></div><div class="clear"></div><div id="comment-60128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

