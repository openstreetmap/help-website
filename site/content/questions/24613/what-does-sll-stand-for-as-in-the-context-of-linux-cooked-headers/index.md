+++
type = "question"
title = "What does SLL stand for (as in the context of Linux &quot;cooked&quot; headers)?"
description = '''What does SLL stand for? On the Wireshark SLL wiki page, it states that,  For those who are curious, &quot;SLL&quot; stands for &quot;sockaddr_ll&quot;&quot;, but then goes on to say: This means that information such as the link-layer protocol&#x27;s packet type field, if any, isn&#x27;t available, so libpcap constructs a synthetic l...'''
date = "2013-09-12T12:47:00Z"
lastmod = "2013-09-12T13:52:00Z"
weight = 24613
keywords = [ "sll", "cooked", "linux" ]
aliases = [ "/questions/24613" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What does SLL stand for (as in the context of Linux "cooked" headers)?](/questions/24613/what-does-sll-stand-for-as-in-the-context-of-linux-cooked-headers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24613-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What does SLL stand for? On the Wireshark <a href="http://wiki.wireshark.org/SLL">SLL</a> wiki page, it states that,</p><p><em>For those who are curious, "SLL" stands for "sockaddr_ll"</em>", but then goes on to say:</p><p><em>This means that information such as the link-layer protocol's packet type field, if any, isn't available, so libpcap constructs a <strong>synthetic link-layer [emphasis added]</strong> header from the address supplied when it does a recvfrom() on the socket.</em></p><p>In any case, if it does stand for "sockaddr_ll", is there an actual reference somewhere to corroborate that? And here, the "ll" presumably stands for "Link Layer", would that be correct?</p><p>I was thinking that "Synthetic Link-Layer", "Synthesized Link-Layer", or possibly even "Substitue[d] Link-Layer" might be more likely, but I can't find any real definition anywhere. Even in the Linux "sll.h" header file, it doesn't specifically mention it, only that it, <em>"... is derived from the Stanford/CMU enet packet filter, (net/enet.c) distributed as part of 4.3BSD, ..."</em></p><p>I am interested in order to possibly update some Wireshark documentation.</p></div><div id="question-tags" class="tags-container tags">sll cooked linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '13, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24613" class="comments-container"><span id="24664"></span><div id="comment-24664" class="comment"><div id="post-24664-score" class="comment-score"></div><div class="comment-text"><blockquote><p>is derived from the Stanford/CMU enet packet filter, (net/enet.c) distributed as part of 4.3BSD, ..."</p></blockquote><p>That was me, copying and pasting the standard copyright notice from bpf.h; that particular part really didn't belong in sll.h (or ipnet.h).</p></div><div id="comment-24664-info" class="comment-info"><span class="comment-age">(13 Sep '13, 17:58)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-24613" class="comment-tools"></div><div class="clear"></div><div id="comment-24613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24616"></span>

<div id="answer-container-24616" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24616-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>"SLL" stands for "sockaddr_ll""<br />
In any case, if it does stand for "sockaddr_ll", is there an actual reference somewhere to corroborate that?</p></blockquote><p>I guess that's because of the definition of <strong>s</strong>ockaddr_<strong>ll</strong> in the Linux kernel.</p><blockquote><p><a href="http://kerneldox.com/kdox-linux/d8/d92/if__packet_8h_source.html">http://kerneldox.com/kdox-linux/d8/d92/if__packet_8h_source.html</a></p></blockquote><pre><code>struct sockaddr_ll {
         unsigned short  sll_family;
         __be16          sll_protocol;
         int             sll_ifindex;
         unsigned short  sll_hatype;
         unsigned char   sll_pkttype;
         unsigned char   sll_halen;
         unsigned char   sll_addr[8];
};</code></pre><blockquote><p>And here, the "ll" presumably stands for "Link Layer", would that be correct?</p></blockquote><p>I would say yes, although there is no clear reference in the kernel code from 'll' to "Link Layer". But in the context where is defined, it makes sense.</p><p>However: In the man page of packet(7), it is referenced as "Link Level".</p><blockquote><p><a href="http://linux.die.net/man/7/packet">http://linux.die.net/man/7/packet</a></p></blockquote><pre><code>The link level header information is available in a common format in a sockaddr_ll. protocol is the</code></pre><p>Link <strong>Layer</strong> or Link <strong>Level</strong>? I would vote for <strong>Link Layer</strong>, as that's a pretty common term.</p><p>Let's wait what the libpcap hackers have to say ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '13, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Sep '13, 14:07</p></div></div><div id="comments-container-24616" class="comments-container"><span id="24653"></span><div id="comment-24653" class="comment"><div id="post-24653-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply, Kurt. I guess I'll just leave it as "SLL" without any further elaboration.</p></div><div id="comment-24653-info" class="comment-info"><span class="comment-age">(13 Sep '13, 08:33)</span> cmaynard ♦♦</div></div><span id="24673"></span><div id="comment-24673" class="comment"><div id="post-24673-score" class="comment-score"></div><div class="comment-text"><p>I guess, for the 'regular' user it is not that important to know where the SLL acronym originated from.</p><p>The explanation in the Wiki is good enough, to understand what cooked mode is and why/where it is needed.</p></div><div id="comment-24673-info" class="comment-info"><span class="comment-age">(14 Sep '13, 04:29)</span> Kurt Knochner ♦</div></div><span id="24696"></span><div id="comment-24696" class="comment"><div id="post-24696-score" class="comment-score"></div><div class="comment-text"><p>Well, I was thinking that it might be nice to document it in the Wireshark packet details pane and status line so it would be more obvious to users who, for example, might want to apply an "sll*" filter. In that way, they would have a better idea as to why it's "sll" instead of something like, "lcc" for "Linux cooked capture".</p></div><div id="comment-24696-info" class="comment-info"><span class="comment-age">(14 Sep '13, 16:07)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-24616" class="comment-tools"></div><div class="clear"></div><div id="comment-24616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

