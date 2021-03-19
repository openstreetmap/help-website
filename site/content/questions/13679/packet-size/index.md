+++
type = "question"
title = "Packet Size"
description = '''Hi Team I want to Know what is the packet size of the packets captured in the wireshark trace. can you please also confirm is there any way to see the statical way to see how the packets on the Packet size basis. Regards Ankit Jain'''
date = "2012-08-16T04:53:00Z"
lastmod = "2012-08-16T06:43:00Z"
weight = 13679
keywords = [ "ankit" ]
aliases = [ "/questions/13679" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Packet Size](/questions/13679/packet-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13679-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Team</p><p>I want to Know what is the packet size of the packets captured in the wireshark trace. can you please also confirm is there any way to see the statical way to see how the packets on the Packet size basis.</p><p>Regards Ankit Jain</p></div><div id="question-tags" class="tags-container tags">ankit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '12, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/5be87459fcdc28874f21858d797fc326?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ank1t%20Ja1n&#39;s gravatar image" /><p>Ank1t Ja1n<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ank1t Ja1n has no accepted answers">0%</span></p></div></div><div id="comments-container-13679" class="comments-container"></div><div id="comment-tools-13679" class="comment-tools"></div><div class="clear"></div><div id="comment-13679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="13680"></span>

<div id="answer-container-13680" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13680-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, just go to Statistics -&gt; Packet Length for a statistics on packet length in the current trace. You can just leave the filter setting empty if you want the values for the complete file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '12, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13680" class="comments-container"></div><div id="comment-tools-13680" class="comment-tools"></div><div class="clear"></div><div id="comment-13680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13681"></span>

<div id="answer-container-13681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13681-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is also the <a href="http://www.wireshark.org/docs/man-pages/capinfos.html">capinfos</a> tool. That gives average packet size and bit/byte/packet rates among other stats.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '12, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13681" class="comments-container"></div><div id="comment-tools-13681" class="comment-tools"></div><div class="clear"></div><div id="comment-13681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13682"></span>

<div id="answer-container-13682" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13682-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>and finally, there is tshark.</p><blockquote><p><code>tshark -nr input.cap -T fields -E header=y -E separator=; -e frame.time -e frame.time_epoch -e frame.len -e ip.len -e tcp.len &gt; packet_size.csv</code><br />
</p></blockquote><p>You can also use a <a href="http://wiki.wireshark.org/DisplayFilters/">display filter</a> (-R) to narrow down what you need.</p><blockquote><p><code>tshark -nr input.cap -R "tcp.port eq 80" -T fields -E header=y -E separator=; -e frame.time -e frame.time_epoch -e frame.len -e ip.len -e tcp.len &gt; packet_size.csv</code><br />
</p></blockquote><p>Then use MS Excel to create a histogram of the packet sizes (or whatever you need), based on the CSV data.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '12, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Aug '12, 06:47</p></div></div><div id="comments-container-13682" class="comments-container"></div><div id="comment-tools-13682" class="comment-tools"></div><div class="clear"></div><div id="comment-13682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

