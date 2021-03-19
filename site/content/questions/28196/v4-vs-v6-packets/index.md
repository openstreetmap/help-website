+++
type = "question"
title = "v4 vs v6 packets"
description = '''Hi, If I am sending some payload both using v4 and v6 then how it&#x27;ll differ exactly?  I observed the payload difference in both v4 and v6 traffic.  Please clarify on this.'''
date = "2013-12-17T01:23:00Z"
lastmod = "2013-12-17T01:39:00Z"
weight = 28196
keywords = [ "v4v6" ]
aliases = [ "/questions/28196" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [v4 vs v6 packets](/questions/28196/v4-vs-v6-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28196-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, If I am sending some payload both using v4 and v6 then how it'll differ exactly? I observed the payload difference in both v4 and v6 traffic.</p><p>Please clarify on this.</p></div><div id="question-tags" class="tags-container tags">v4v6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '13, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/8764a1fe7fb9ef939125deb02c1d283b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sspallai&#39;s gravatar image" /><p>sspallai<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sspallai has no accepted answers">0%</span></p></div></div><div id="comments-container-28196" class="comments-container"></div><div id="comment-tools-28196" class="comment-tools"></div><div class="clear"></div><div id="comment-28196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28198"></span>

<div id="answer-container-28198" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28198-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <strong>payload</strong> should be identical if you choose a different protocol, <strong>if</strong> the code is really the same. So, what are those differences exactly? Can you post a sample capture somewhere (Google drive, dropbox, clodshark.org or mega.co.nz)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '13, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28198" class="comments-container"><span id="28199"></span><div id="comment-28199" class="comment"><div id="post-28199-score" class="comment-score"></div><div class="comment-text"><p>It might not be identical if the packets are full because the IPv6 header "steals" potentially 20 bytes more from the segment size than the IPv4 header. So you'll see some re-segmentation for IPv6.</p></div><div id="comment-28199-info" class="comment-info"><span class="comment-age">(17 Dec '13, 01:46)</span> Jasper ♦♦</div></div><span id="28200"></span><div id="comment-28200" class="comment"><div id="post-28200-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Please find here the difference. I have used same http traffic. Please check the payload size and all.</p><pre><code>Internet Protocol, Src: 5.0.0.1 (5.0.0.1), Dst: 4.0.0.1 (4.0.0.1)
    Version: 4
    Header length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00)
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..0. = ECN-Capable Transport (ECT): 0
        .... ...0 = ECN-CE: 0
    Total Length: 40
    Identification: 0x0000 (0)
    Flags: 0x04 (Don&#39;t Fragment)
        0... = Reserved bit: Not set
    Total Length: 1140
    Identification: 0x0d05 (3333)
    Flags: 0x00
        0... = Reserved bit: Not set
        .0.. = Don&#39;t fragment: Not set
        ..0. = More fragments: Not set
    Fragment offset: 0
    Time to live: 61
    Protocol: TCP (0x06)
    Header checksum: 0x637e [correct]
        [Good: True]
        [Bad : False]
    Source: 4.0.0.1 (4.0.0.1)
    Destination: 5.0.0.1 (5.0.0.1)

Internet Protocol Version 6
    0110 .... = Version: 6
    .... 0000 0000 .... .... .... .... .... = Traffic class: 0x00000000
    .... .... .... 0000 0000 0000 0000 0000 = Flowlabel: 0x00000000
    Payload length: 1132
    Next header: TCP (0x06)
    Hop limit: 64
    Source: 2001:1000:1111:2222:3333:4444:8005:14d (2001:1000:1111:2222:3333:4444:8005:14d)
    Destination: bfaf:9f71:c8d2:688e:8018:5a0:9002:0 (bfaf:9f71:c8d2:688e:8018:5a0:9002:0)</code></pre><p>Regards, Suchi</p></div><div id="comment-28200-info" class="comment-info"><span class="comment-age">(17 Dec '13, 01:47)</span> sspallai</div></div><span id="28201"></span><div id="comment-28201" class="comment"><div id="post-28201-score" class="comment-score"></div><div class="comment-text"><p>Well, one is IPv4, one is IPv6. It makes not much sense to compare them, unless you want to know which fields the different headers have. For that you could just read the RFCs or any IPv4/IPv6 documentation.</p></div><div id="comment-28201-info" class="comment-info"><span class="comment-age">(17 Dec '13, 01:52)</span> Jasper ♦♦</div></div><span id="28206"></span><div id="comment-28206" class="comment"><div id="post-28206-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, that's only the <strong>headers</strong> (which are obviously different, as it's a different protocol). You said, the <strong>payload</strong> is different (the bytes that your application wants to transmit). I can't check that, as you did not post the <strong>payload</strong> .</p></div><div id="comment-28206-info" class="comment-info"><span class="comment-age">(17 Dec '13, 02:38)</span> Kurt Knochner ♦</div></div><span id="28207"></span><div id="comment-28207" class="comment"><div id="post-28207-score" class="comment-score"></div><div class="comment-text"><p>@Jasper: I believe the OP does not mean the real <strong>payload</strong> although he used that term. I guess he just wonders why IPv4 looks different than IPv6 in Wireshark.</p><p>@sspallai: If that is the case. Don't wonder any longer. It looks different, because some aspects of IPv6 are totally different than in IPv4.</p></div><div id="comment-28207-info" class="comment-info"><span class="comment-age">(17 Dec '13, 02:41)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28198" class="comment-tools"></div><div class="clear"></div><div id="comment-28198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

