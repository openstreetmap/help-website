+++
type = "question"
title = "wireshark and server processing time"
description = '''I&#x27;d like to capture the time it takes for the server to process the request. Below is my setup: server &amp;lt;--&amp;gt;switch1&amp;lt;--&amp;gt;WAN&amp;lt;--&amp;gt;switch2&amp;lt;--&amp;gt;client Now the client is accessing the application reside on the server. My plan is to setup Wireshark on switch2 and switch1.  My questions...'''
date = "2013-11-18T19:39:00Z"
lastmod = "2013-11-19T15:46:00Z"
weight = 27081
keywords = [ "wireshark", "network", "slow", "response", "server" ]
aliases = [ "/questions/27081" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark and server processing time](/questions/27081/wireshark-and-server-processing-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27081-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to capture the time it takes for the server to process the request. Below is my setup:</p><p>server &lt;--&gt;switch1&lt;--&gt;WAN&lt;--&gt;switch2&lt;--&gt;client</p><p>Now the client is accessing the application reside on the server. My plan is to setup Wireshark on switch2 and switch1.</p><p>My questions are as follow: - Will the time, that I capture on switch1 when the server sends the response back, be the processing time of the server. - is it possible to merge the two captured file into one?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">wireshark network slow response server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '13, 19:39</strong></p><img src="https://secure.gravatar.com/avatar/4bf9a4681570406f873b404a912f2a7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="character9&#39;s gravatar image" /><p>character9<br />
<span class="score" title="16 reputation points">16</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="character9 has no accepted answers">0%</span></p></div></div><div id="comments-container-27081" class="comments-container"></div><div id="comment-tools-27081" class="comment-tools"></div><div class="clear"></div><div id="comment-27081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27124"></span>

<div id="answer-container-27124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27124-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you need just the 'server processing' time (please define that!), there is no need to capture on switch2 (client side).</p><blockquote><p>Will the time, that I capture on switch1 when the server sends the response back, <strong>be the processing time of the server.</strong></p></blockquote><p>Actually, it will be</p><ol><li>the time needed to transmit the client request from switch1 -&gt; server (if there is another wan or a slow ethernet link this could make up some ms!)</li><li>the time needed to process the client request packet in the TCP/IP stack of the server</li><li>the time needed for the server software to process the request (whatever that means in your context)</li><li>the time needed to process the server response packet in the TCP/IP stack of the server</li><li>the time needed to transmit the server response from server -&gt; switch1</li></ol><p>As you can see, only 3 is the 'server (software) processing' time. But that really depends on the definition of 'server processing' time.</p><p>Furthermore: if you can neglect 1-2 and 4-5, then the time delta between client request and server response at switch1 will the the 'server processing' time.</p><blockquote><p>is it possible to merge the two captured file into one?</p></blockquote><p>Yes, see the tool <a href="http://www.wireshark.org/docs/man-pages/mergecap.html">mergecap</a>. <strong>HOWEVER</strong> as I said, it's not necessary to capture at switch1 and at switch2 in your scenario. You can do it, but if you <strong>then</strong> merge the capture file, you will get duplicate frames, as the frames that appear at switch2 will also be seen at switch1 and vice versa.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '13, 15:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Nov '13, 15:47</p></div></div><div id="comments-container-27124" class="comments-container"><span id="27129"></span><div id="comment-27129" class="comment"><div id="post-27129-score" class="comment-score"></div><div class="comment-text"><p>For the same response packet from the server, would the packet time frame be different between capture on switch1 and switch2 or the client?</p></div><div id="comment-27129-info" class="comment-info"><span class="comment-age">(19 Nov '13, 17:11)</span> SteveZhou</div></div><span id="27161"></span><div id="comment-27161" class="comment"><div id="post-27161-score" class="comment-score">1</div><div class="comment-text"><p>Of course. It will be + t(wan) == time needed to transmit the packet over the wan link.</p></div><div id="comment-27161-info" class="comment-info"><span class="comment-age">(20 Nov '13, 06:57)</span> Kurt Knochner ♦</div></div><span id="27243"></span><div id="comment-27243" class="comment"><div id="post-27243-score" class="comment-score"></div><div class="comment-text"><p>The time Wireshark sees the packet going through from sw1 and from sw2 is different, doesn't it? Let say I capture the packet at sw1 and the time is 1 ms (for example) and that packet can be seen again at sw2 at 2ms. So I know that it takes 1 ms for the packet going from sw1 to sw2. Does it sound right? Now if I merge those two captured files, I will see the same packet with different time. Correct?</p></div><div id="comment-27243-info" class="comment-info"><span class="comment-age">(21 Nov '13, 15:16)</span> character9</div></div><span id="27259"></span><div id="comment-27259" class="comment"><div id="post-27259-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The time Wireshark sees the packet going through from sw1 and from sw2 is different, doesn't it?</p></blockquote><p>sure it's <code>delta t(wan)</code>.</p><blockquote><p>So I know that it takes 1 ms for the packet going from sw1 to sw2. Does it sound right?</p></blockquote><p>yes.</p><blockquote><p>I will see the same packet with different time. Correct?</p></blockquote><p>yes. But I thought you were interested in the 'server processing time' and not the t(wan) !?!</p><p>BTW: If you want to merge capture files of two different capturing devices to do any sort of differential time analysis, the time on the capturing devices must be synchronized to the millisecond, better to the nanosecond, otherwise the delta of the time stamps will be wrong.</p></div><div id="comment-27259-info" class="comment-info"><span class="comment-age">(22 Nov '13, 01:23)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27124" class="comment-tools"></div><div class="clear"></div><div id="comment-27124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

