+++
type = "question"
title = "How to reduce memory usage in very long-time capture and analyze"
description = '''I modify a version of tshark to analyze real-time packages on Gigabytes port, find out the info I concerned, and write them in files. When facing multi-days capture, the memory grows continuously. I shield the output printing, and write temporary pcapng files in multiple ring buffers to reduce the m...'''
date = "2014-03-03T21:19:00Z"
lastmod = "2014-03-04T04:52:00Z"
weight = 30379
keywords = [ "reduce", "memory" ]
aliases = [ "/questions/30379" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to reduce memory usage in very long-time capture and analyze](/questions/30379/how-to-reduce-memory-usage-in-very-long-time-capture-and-analyze)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30379-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I modify a version of tshark to analyze real-time packages on Gigabytes port, find out the info I concerned, and write them in files. When facing multi-days capture, the memory grows continuously. I shield the output printing, and write temporary pcapng files in multiple ring buffers to reduce the memory cost. However, memory grows at 20 to 30 MB per hour. How to reduce the memory cost further?</p><p>ps: I don't need most of the packets info for summary printing, only request and response pack info are concerned. So I think memory can be kept at a very low level. Any ideas to release the excess memory? Appreciated.</p></div><div id="question-tags" class="tags-container tags">reduce memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '14, 21:19</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p>metamatrix<br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div></div><div id="comments-container-30379" class="comments-container"><span id="30434"></span><div id="comment-30434" class="comment"><div id="post-30434-score" class="comment-score"></div><div class="comment-text"><p>Anyone have idears? @Guy @Kurt</p></div><div id="comment-30434-info" class="comment-info"><span class="comment-age">(05 Mar '14, 00:56)</span> metamatrix</div></div><span id="30444"></span><div id="comment-30444" class="comment"><div id="post-30444-score" class="comment-score"></div><div class="comment-text"><ul><li>what is your protocol?</li><li>how is a 'request' and a 'response' defined?</li><li>Did you use any capture filters? If so: which one?</li><li>what are your modifications to the tshark code so far?</li></ul></div><div id="comment-30444-info" class="comment-info"><span class="comment-age">(05 Mar '14, 10:44)</span> Kurt Knochner ♦</div></div><span id="30446"></span><div id="comment-30446" class="comment"><div id="post-30446-score" class="comment-score">1</div><div class="comment-text"><p>To be honest, if it was easy to do it would have been done long ago. To allow all the fantastic things that Wireshark (and tshark) do, e.g. display filters, reassembly, stats, graphs etc. means maintaining state. If your long term capture requirements don't use all that infrastructure then use dumpcap and you're done. If, however you "need" that infrastructure, then you're stuck.</p></div><div id="comment-30446-info" class="comment-info"><span class="comment-age">(05 Mar '14, 14:14)</span> grahamb ♦</div></div><span id="30462"></span><div id="comment-30462" class="comment"><div id="post-30462-score" class="comment-score"></div><div class="comment-text"><p>My protocol contains 802.11，radius，http(only portal packets are concerned) and bootp(dhcp). 'request' and response packet is mainly for http protocol. I didn't use any capture filter. My modifications are mostly on dissectors, eg. packet-ieee80211.c</p></div><div id="comment-30462-info" class="comment-info"><span class="comment-age">(05 Mar '14, 23:17)</span> metamatrix</div></div><span id="30477"></span><div id="comment-30477" class="comment"><div id="post-30477-score" class="comment-score"></div><div class="comment-text"><p>If you read the stuff in this tread there are some ideas there <a href="https://www.wireshark.org/lists/wireshark-dev/201304/msg00143.html">https://www.wireshark.org/lists/wireshark-dev/201304/msg00143.html</a></p><p>looking into the cashing of IP addresses might yeld something as well. epan/address.[ch]</p><p>If you do something it would be better to do it with the comunity rather than doing private changes.</p></div><div id="comment-30477-info" class="comment-info"><span class="comment-age">(06 Mar '14, 03:52)</span> Anders ♦</div></div></div><div id="comment-tools-30379" class="comment-tools"></div><div class="clear"></div><div id="comment-30379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30392"></span>

<div id="answer-container-30392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30392-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you need "request and response" packet info, by which I think you mean you need the information of which response packet matches which request packet, how would you avoid keeping a list of all previous packets? (that should be what is growing the memory if I recall correctly, by the way)</p><p>I mean as far as tshark knows, packet #100000000 could be a response to packet #3.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '14, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30392" class="comments-container"><span id="30430"></span><div id="comment-30430" class="comment"><div id="post-30430-score" class="comment-score"></div><div class="comment-text"><p>If don't need most packets info(including request and response info), how to free up the memory after dissecting?</p></div><div id="comment-30430-info" class="comment-info"><span class="comment-age">(04 Mar '14, 23:40)</span> metamatrix</div></div><span id="30440"></span><div id="comment-30440" class="comment"><div id="post-30440-score" class="comment-score"></div><div class="comment-text"><p>I think you'd have to download the source and compile it yourself, making the necessary code changes. But if you don't need that kind of info, you may prefer to use a different tool, like dumpcap.</p></div><div id="comment-30440-info" class="comment-info"><span class="comment-age">(05 Mar '14, 03:33)</span> Hadriel</div></div></div><div id="comment-tools-30392" class="comment-tools"></div><div class="clear"></div><div id="comment-30392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

