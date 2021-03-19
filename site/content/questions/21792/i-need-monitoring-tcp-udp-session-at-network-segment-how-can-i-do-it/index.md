+++
type = "question"
title = "I need monitoring tcp-, udp-session at network segment. How can I do it?"
description = '''Hello, Can i to monitor tcp-, udp-session with wireshark?  session per second. syssion by hour, by day?  Thank&#x27;s'''
date = "2013-06-06T04:02:00Z"
lastmod = "2013-06-10T08:30:00Z"
weight = 21792
keywords = [ "sessions" ]
aliases = [ "/questions/21792" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [I need monitoring tcp-, udp-session at network segment. How can I do it?](/questions/21792/i-need-monitoring-tcp-udp-session-at-network-segment-how-can-i-do-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21792-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Can i to monitor tcp-, udp-session with wireshark?</p><ol><li>session per second.</li><li>syssion by hour, by day?</li></ol><p>Thank's</p></div><div id="question-tags" class="tags-container tags">sessions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '13, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/be22dfa2d0d6b90ca3ed9a17bdebc074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="junglend&#39;s gravatar image" /><p>junglend<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="junglend has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jun '13, 08:25</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-21792" class="comments-container"><span id="21808"></span><div id="comment-21808" class="comment"><div id="post-21808-score" class="comment-score"></div><div class="comment-text"><p>If I understand the question, you want to graph the number of sessions establishes per second? The number of sessions that are being established per second? Could you reword this question?</p></div><div id="comment-21808-info" class="comment-info"><span class="comment-age">(06 Jun '13, 18:11)</span> Quadratic</div></div><span id="21811"></span><div id="comment-21811" class="comment"><div id="post-21811-score" class="comment-score"></div><div class="comment-text"><p>So, it can no graf. I want see tcp-session statistics in any kind, in graf possible too.</p></div><div id="comment-21811-info" class="comment-info"><span class="comment-age">(06 Jun '13, 22:35)</span> junglend</div></div><span id="21816"></span><div id="comment-21816" class="comment"><div id="post-21816-score" class="comment-score"></div><div class="comment-text"><p>But a graph of what specifically? Do you want to see TCP session setup attempts over time? And for UDP, what exactly do you want graphed over time (there's no such thing as a UDP session technically)?</p></div><div id="comment-21816-info" class="comment-info"><span class="comment-age">(07 Jun '13, 06:31)</span> Quadratic</div></div></div><div id="comment-tools-21792" class="comment-tools"></div><div class="clear"></div><div id="comment-21792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21830"></span>

<div id="answer-container-21830" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21830-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not a monitoring tool, it's an analysis tool. It keeps state information to do the best dissection of packets it possibly can. This means its memory use will grow over time and it will run out of memory sooner or later.</p><p>So if you need a long-term monitoring solution, wireshark is not the way forward. Have a look at <a href="http://www.ntop.org/">ntop</a> which might suit you better. Also, check whether your networking devices are capable of exporting NetFlow, sFlow or IPFIX data. If they are, you might want to look into a <a href="http://en.wikipedia.org/wiki/NetFlow">netflow</a> collector to collect the session data and present it to you in graphs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '13, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21830" class="comments-container"><span id="21866"></span><div id="comment-21866" class="comment"><div id="post-21866-score" class="comment-score"></div><div class="comment-text"><p>Thank's. 1.I know that wireshark is a not minitoring tool. But it tool has section "statistics" in menu. And i mean that in this section i can view information about tcp-session. 2. So, i'm have not netflow unfortunately. And i find tool, possible that view session statistics.</p></div><div id="comment-21866-info" class="comment-info"><span class="comment-age">(09 Jun '13, 22:57)</span> junglend</div></div></div><div id="comment-tools-21830" class="comment-tools"></div><div class="clear"></div><div id="comment-21830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21881"></span>

<div id="answer-container-21881" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21881-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could run tshark to generate conversation statistics and then use Excel (or a perl/python/whatever script) to generate the sessions per minute/hour.</p><blockquote><p><code>tshark -nr input.pcap -q -z conv,tcp</code><br />
<code>tshark -nr input.pcap -q -z conv,udp</code><br />
</p></blockquote><p>Sample Output:</p><pre><code>================================================================================
TCP Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |    Relative    |   Duration   |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |
172.16.29.25:32882   &lt;-&gt; 172.16.50.74:3128        314    297506     252     32097     566    329603    33,175361000       313,6527
172.16.29.25:32881   &lt;-&gt; 172.16.50.74:3128        308    279108     228     38839     536    317947    31,675055000       315,1533
172.16.29.25:32883   &lt;-&gt; 172.16.50.74:3128        213    213803     187     19472     400    233275    34,542359000       151,6759
172.16.29.25:32897   &lt;-&gt; 172.16.50.74:3128        198    152229     177     17003     375    169232   185,180690000       161,6476
172.16.29.25:32893   &lt;-&gt; 172.16.50.74:3128        156    120221     111     22966     267    143187    91,233185000       255,5950</code></pre><p>Then load the output of those commands into Excel (or your script) and generate the connections per time interval statistics. Please use the column "Relative Start" for your statistics.</p><p>If you need a solution that does the statistics "on-the-fly" (monitoring the interface and continuously counting the sessions) or for a very long time (days, weeks), Wireshark/tshark is the wrong tool for you.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '13, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-21881" class="comments-container"></div><div id="comment-tools-21881" class="comment-tools"></div><div class="clear"></div><div id="comment-21881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

