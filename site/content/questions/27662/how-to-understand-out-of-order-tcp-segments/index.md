+++
type = "question"
title = "how to understand out-of-order TCP segments?"
description = '''Hi, I would like to know the meaning of out-of-order TCP segments in wireshark with the following question  What would make wireshark mark a segment as out-of-order?  IP layer should re-order IP packets correctly and then give them to TCP, why could out-of-order occur? Does out-of-order always mean ...'''
date = "2013-12-02T07:29:00Z"
lastmod = "2014-06-05T15:27:00Z"
weight = 27662
keywords = [ "out-of-order" ]
aliases = [ "/questions/27662" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to understand out-of-order TCP segments?](/questions/27662/how-to-understand-out-of-order-tcp-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27662-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I would like to know the meaning of out-of-order TCP segments in wireshark with the following question</p><ol><li>What would make wireshark mark a segment as out-of-order?</li><li>IP layer should re-order IP packets correctly and then give them to TCP, why could out-of-order occur?</li><li>Does out-of-order always mean bad things?</li><li>What should we do when we see out-of-order TCP segments, especially when there are lots of them.</li></ol><p>thank you!</p></div><div id="question-tags" class="tags-container tags">out-of-order</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '13, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-27662" class="comments-container"></div><div id="comment-tools-27662" class="comment-tools"></div><div class="clear"></div><div id="comment-27662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27664"></span>

<div id="answer-container-27664" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27664-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>The SEQ number is not what Wireshark would have expected as next SEQ number (see below)</li><li>Different devices on the way my handle IP packets differently, and thus forwarding one frame earlier/later than another. Or different IP frames take different routes (rather seldom).</li><li>No, if it's not too many of them</li><li>Figure out what causes them. Capture at the sender <strong>and</strong> the receiver side and compare the capture files. If that does not help, move along the path and take captures at different places (if possible - obviously a problem if the data path 'crosses' the internet). Make sure, the 'out-of-order' frames aren't just duplicated frames, by checking the IP ID (try to find duplicate IP IDs).</li></ol><p>From packet-tcp.c:</p><pre><code>       
       /* If the segment came &lt;3ms since the segment with the highest
         * seen sequence number and it doesn&#39;t look like a retransmission
         * then it is an OUT-OF-ORDER segment.
         *   (3ms is an arbitrary number)
         */
    
        t=(pinfo-&gt;fd-&gt;abs_ts.secs-tcpd-&gt;fwd-&gt;nextseqtime.secs)*1000000000;
        t=t+(pinfo-&gt;fd-&gt;abs_ts.nsecs)-tcpd-&gt;fwd-&gt;nextseqtime.nsecs;
        if( t&lt;3000000
        &amp;&amp; tcpd-&gt;fwd-&gt;nextseq != seq + seglen ) {
            if(!tcpd-&gt;ta) {
                tcp_analyze_get_acked_struct(pinfo-&gt;fd-&gt;num, seq, ack, TRUE, tcpd);
            }
            tcpd-&gt;ta-&gt;flags|=TCP_A_OUT_OF_ORDER;
            goto finished_checking_retransmission_type;
        }</code></pre><p>BTW: See also other questions with the tag: out-of-order</p><blockquote><p><a href="http://ask.wireshark.org/tags/out-of-order/">http://ask.wireshark.org/tags/out-of-order/</a></p></blockquote><p>Basically the same explanation as I gave above, just different (real world) examples ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '13, 08:20</p></div></div><div id="comments-container-27664" class="comments-container"><span id="27767"></span><div id="comment-27767" class="comment"><div id="post-27767-score" class="comment-score"></div><div class="comment-text"><p>So IP doesn't have the responsibility to put the packets in a right order, does it? It is TCP's job, what if the application layer protocol doesn't use TCP? Who will put the packets in a right order? Application layer protocol?</p></div><div id="comment-27767-info" class="comment-info"><span class="comment-age">(04 Dec '13, 07:20)</span> SteveZhou</div></div><span id="27768"></span><div id="comment-27768" class="comment"><div id="post-27768-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>So IP doesn't have the responsibility to put the packets in a right order</p></blockquote><p>No. The job of IP is just to route/transport the frames to the destination, regardless of packet order or the way/path it chooses.</p><blockquote><p>It is TCP's job,</p></blockquote><p>For TCP: Yes, it's TCP that will deliver data in the right order to the application, which will/can cause delays if you have a lot of out-of-order packets, as TCP must wait until all required segments have arrived.</p><blockquote><p>Who will put the packets in a right order? Application layer protocol?</p></blockquote><p>the application itself or the 'application protocol', if that is implemented 'outside' of the application - for whatever reason.</p></div><div id="comment-27768-info" class="comment-info"><span class="comment-age">(04 Dec '13, 07:23)</span> Kurt Knochner ♦</div></div><span id="27892"></span><div id="comment-27892" class="comment"><div id="post-27892-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot!</p></div><div id="comment-27892-info" class="comment-info"><span class="comment-age">(07 Dec '13, 08:20)</span> SteveZhou</div></div><span id="27893"></span><div id="comment-27893" class="comment"><div id="post-27893-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-27893-info" class="comment-info"><span class="comment-age">(07 Dec '13, 08:29)</span> grahamb ♦</div></div></div><div id="comment-tools-27664" class="comment-tools"></div><div class="clear"></div><div id="comment-27664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33481"></span>

<div id="answer-container-33481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33481-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A common reason why Wireshark marks certain segments "Out-of-order" is because of a known bug in Wireshark:</p><p>In a sequence like the following:</p><p>1) A ------SYN-----&gt; B</p><p>2) A &lt;-----SYN------ B</p><p>3) A ----SYN/ACK---&gt; B</p><p>, Wireshark will mark segment 3) "Out-of-order".</p><p>This is of course a mistake. This sequence is a normal TCP sequence, often called "TCP simultaneous connect". Since P2P applications use TCP simultaneous connect a lot to perform TCP NAT punching, you might see such sequences and false positives often.</p><p>Someone at Wireshark should fix it imho, it looks bad when a network analyzer doesn't understand the basic TCP state diagram.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '14, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/4e9f89b1e3c59a814cc87248e7532113?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abdul&#39;s gravatar image" /><p>abdul<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abdul has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jun '14, 15:29</p></div></div><div id="comments-container-33481" class="comments-container"><span id="33871"></span><div id="comment-33871" class="comment"><div id="post-33871-score" class="comment-score"></div><div class="comment-text"><p>Hi Abdul, do you have a bug ID for this known issue? I'm really curious about it. I'm seeing TCP out-of-order packets and I'm wondering if it could be related.</p></div><div id="comment-33871-info" class="comment-info"><span class="comment-age">(16 Jun '14, 13:11)</span> calpolygrad</div></div><span id="33901"></span><div id="comment-33901" class="comment"><div id="post-33901-score" class="comment-score"></div><div class="comment-text"><blockquote><p>A common reason why Wireshark marks certain segments "Out-of-order" is because of a known bug in Wireshark:</p></blockquote><p>@abdul: can you post a sample capture file (google drive, dropbox, cloudshark.org) that shows the mentioned behavior?</p></div><div id="comment-33901-info" class="comment-info"><span class="comment-age">(17 Jun '14, 11:51)</span> Kurt Knochner ♦</div></div><span id="35165"></span><div id="comment-35165" class="comment"><div id="post-35165-score" class="comment-score"></div><div class="comment-text"><p>I have a capture example of what Abdul is talking about:</p><pre><code>67  11:11:17.7  74.118.32.157   209.112.4.11    TCP 66  https &gt; 50486 [SYN, ACK] Seq=0 Ack=1 Win=4140 Len=0 MSS=1460 WS=1 SACK&lt;em&gt;PERM=1

68  11:11:17.7  74.118.32.157   209.112.4.11    TCP 66  [TCP Out-Of-Order] https &gt; 50486 [SYN, ACK] Seq=0 Ack=1 Win=4140 Len=0 MSS=1460 WS=1 SACK&lt;/em&gt;PERM=1</code></pre></div><div id="comment-35165-info" class="comment-info"><span class="comment-age">(04 Aug '14, 11:53)</span> Frank Murray</div></div><span id="35166"></span><div id="comment-35166" class="comment"><div id="post-35166-score" class="comment-score"></div><div class="comment-text"><p>Can you post the capture somewhere? what were the circumstances of the capture?</p></div><div id="comment-35166-info" class="comment-info"><span class="comment-age">(04 Aug '14, 12:03)</span> grahamb ♦</div></div><span id="41256"></span><div id="comment-41256" class="comment"><div id="post-41256-score" class="comment-score"></div><div class="comment-text"><p>@frank murray did you see grahamb's comment?</p></div><div id="comment-41256-info" class="comment-info"><span class="comment-age">(07 Apr '15, 10:08)</span> barlop</div></div></div><div id="comment-tools-33481" class="comment-tools"></div><div class="clear"></div><div id="comment-33481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

