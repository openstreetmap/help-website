+++
type = "question"
title = "Question about the least packet size of Ethernet?"
description = '''Hi all,  I&#x27;m posting to get help about the least packet size of Ethernet.  as i know, the least packet size of ehternet is 64bytes  when i capure my laptop computer during access some web-server(www.daum.net)  i found some strange about packet(or frame) size of it.  A size of some packet of them is ...'''
date = "2014-04-08T22:16:00Z"
lastmod = "2014-04-09T01:08:00Z"
weight = 31658
keywords = [ "mtu" ]
aliases = [ "/questions/31658" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Question about the least packet size of Ethernet?](/questions/31658/question-about-the-least-packet-size-of-ethernet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31658-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm posting to get help about the least packet size of Ethernet. as i know, the least packet size of ehternet is 64bytes when i capure my laptop computer during access some web-server(www.daum.net) i found some strange about packet(or frame) size of it.</p><p>A size of some packet of them is less than 64bytes. for all that, everything was good exept very small some packets tcp ack packet size was just 54bytes(includes L2 header)</p><p>I wonder why the packet was so small(it less than 64bytes)? and why it was considered as a good packet?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ScreenHunter_05_Apr._09_14.12.jpg" alt="alt text" /></p><p>detail information of frame#15 <img src="https://osqa-ask.wireshark.org/upfiles/ScreenHunter_06_Apr._09_14.15.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '14, 22:16</strong></p><img src="https://secure.gravatar.com/avatar/27e4d1e97303115b07caf9ba39267f2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ray_Han&#39;s gravatar image" /><p>Ray_Han<br />
<span class="score" title="56 reputation points">56</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ray_Han has no accepted answers">0%</span></p></img></div></div><div id="comments-container-31658" class="comments-container"></div><div id="comment-tools-31658" class="comment-tools"></div><div class="clear"></div><div id="comment-31658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31663"></span>

<div id="answer-container-31663" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31663-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's because your capture setup is flawed. You captured <strong>on</strong> the PC sending and receiving packets, and that gives you wrong results.</p><p>What happens here is that your PC is running with a modern network card that takes over certain tasks from the main CPU, like calculating the checksums, large payload segmentation, and padding. This means that your PC is sending incomplete packets to the network card which then does all the work, but by then, Wireshark has already captured the packet before it was finalized. That way the padding to the full minimum size of 64 bytes wasn't complete and you end up with apparently short packets.</p><p>To verify this capture with a 3rd PC on a SPAN port and you'll see that your packets are fine. You can also verify this by capturing on the other system (that your PC is talking to) and you'll see perfect frames coming in.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '14, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-31663" class="comments-container"><span id="31664"></span><div id="comment-31664" class="comment"><div id="post-31664-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper Thanks for your explanation. it's good help to understand my capture. thanks again and have a nice day!</p></div><div id="comment-31664-info" class="comment-info"><span class="comment-age">(09 Apr '14, 02:01)</span> Ray_Han</div></div><span id="31665"></span><div id="comment-31665" class="comment"><div id="post-31665-score" class="comment-score"></div><div class="comment-text"><p>@Ray_Han If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-31665-info" class="comment-info"><span class="comment-age">(09 Apr '14, 02:34)</span> grahamb ♦</div></div><span id="31723"></span><div id="comment-31723" class="comment"><div id="post-31723-score" class="comment-score"></div><div class="comment-text"><p>(Actually, even ancient Ethernet adapters calculate the <em>Ethernet</em> CRC and pad the packets out to the minimum size; it's TCP and IP checksum offloading, and TCP large payload segmentation, that are relatively new features for network adapters.</p><p>So, no matter what Ethernet adapter you have, packets sent from the machine running Wireshark will not, when captured, be padded out to the minimum length.)</p></div><div id="comment-31723-info" class="comment-info"><span class="comment-age">(10 Apr '14, 10:45)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-31663" class="comment-tools"></div><div class="clear"></div><div id="comment-31663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

