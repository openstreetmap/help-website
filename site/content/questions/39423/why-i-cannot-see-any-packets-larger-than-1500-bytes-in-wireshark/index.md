+++
type = "question"
title = "Why I cannot see any packets larger than 1500 bytes in wireshark?"
description = '''Hello, I know that max size of IP packet is 65535 bytes. I wanted to see some of these larger packets in wireshark capture and started downloading some files from web, however, every single packet it captured is less than 1500 bytes long. I tried to change views in wireshark and decode everything as...'''
date = "2015-01-27T01:54:00Z"
lastmod = "2015-01-27T01:58:00Z"
weight = 39423
keywords = [ "mtu", "networking", "wireshark" ]
aliases = [ "/questions/39423" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why I cannot see any packets larger than 1500 bytes in wireshark?](/questions/39423/why-i-cannot-see-any-packets-larger-than-1500-bytes-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39423-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I know that max size of IP packet is 65535 bytes.</p><p>I wanted to see some of these larger packets in wireshark capture and started downloading some files from web, however, every single packet it captured is less than 1500 bytes long.</p><p>I tried to change views in wireshark and decode everything as IP packets, but the result was the same. I also tried running torrent download over UDP - still the same.</p><p>Why there are no packets bigger than 1500?</p><p>I am using a laptop over WiFi and capturing packets on WiFi interface.</p></div><div id="question-tags" class="tags-container tags">mtu networking wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '15, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/9b0d51f9eebd1bd5041c75cc76389001?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inzbartosz&#39;s gravatar image" /><p>inzbartosz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inzbartosz has no accepted answers">0%</span></p></div></div><div id="comments-container-39423" class="comments-container"></div><div id="comment-tools-39423" class="comment-tools"></div><div class="clear"></div><div id="comment-39423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39424"></span>

<div id="answer-container-39424" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39424-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's because the MTU (Maximum Transmission Unit) of Ethernet is 1500, which means that no matter how large an IP packet might be is irrelevant. It has to be transported over a layer 2 medium, which in your case is Ethernet. And that limits the size to 1500 (or 9000, if you enable Jumbo Frames, but that's it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '15, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39424" class="comments-container"><span id="39425"></span><div id="comment-39425" class="comment"><div id="post-39425-score" class="comment-score"></div><div class="comment-text"><p>Well, not Ethernet but WiFi, but the MTU is the same ;-)</p></div><div id="comment-39425-info" class="comment-info"><span class="comment-age">(27 Jan '15, 02:02)</span> SYN-bit ♦♦</div></div><span id="39426"></span><div id="comment-39426" class="comment"><div id="post-39426-score" class="comment-score"></div><div class="comment-text"><p>Well, I wanted to see packet size on layer 3 or even segments on L4 which should have larger sizes, but all I see are WiFi frames... How can I change this?</p></div><div id="comment-39426-info" class="comment-info"><span class="comment-age">(27 Jan '15, 02:06)</span> inzbartosz</div></div><span id="39427"></span><div id="comment-39427" class="comment"><div id="post-39427-score" class="comment-score"></div><div class="comment-text"><p>You can't change it. All you can do is force IP fragmentation, e.g. by sending ping packets with large payloads. On windows, the parameter would be "-l size" to do this. But not all pinged nodes do reply to fragmented packets like that.</p></div><div id="comment-39427-info" class="comment-info"><span class="comment-age">(27 Jan '15, 02:09)</span> Jasper ♦♦</div></div><span id="39428"></span><div id="comment-39428" class="comment"><div id="post-39428-score" class="comment-score"></div><div class="comment-text"><p>@SYN-bit: true, of course, but the largest maximum limitation will always be Ethernet those days I guess, WiFi is just the last mile :-)</p></div><div id="comment-39428-info" class="comment-info"><span class="comment-age">(27 Jan '15, 02:10)</span> Jasper ♦♦</div></div><span id="39429"></span><div id="comment-39429" class="comment not_top_scorer"><div id="post-39429-score" class="comment-score"></div><div class="comment-text"><p>@Jasper: Or the first mile for outgoing packets! In which case (for UDP, ICMP, etc) the packets could have been larger if the MTU of the local layer-2 medium was larger ;-)</p></div><div id="comment-39429-info" class="comment-info"><span class="comment-age">(27 Jan '15, 02:16)</span> SYN-bit ♦♦</div></div><span id="39430"></span><div id="comment-39430" class="comment"><div id="post-39430-score" class="comment-score">1</div><div class="comment-text"><p>@SYN-bit yep, but let's not confuse anybody and keep it a secret ;-)</p></div><div id="comment-39430-info" class="comment-info"><span class="comment-age">(27 Jan '15, 02:34)</span> Jasper ♦♦</div></div></div><div id="comment-tools-39424" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-39424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

