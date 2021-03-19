+++
type = "question"
title = "Identify sequence number errors in UDP captures"
description = '''I have a 10 minute period of captures, during which we have seen out of sequence packets being delivered over a UDP channel in a log file. This is on a custom trading platform that does not subscribe to the exchanges retransmission service, so our retail platforms are fine but the custom one is bein...'''
date = "2013-08-22T02:30:00Z"
lastmod = "2013-08-26T10:39:00Z"
weight = 23945
keywords = [ "udp", "you", "thank", "help", "sequence" ]
aliases = [ "/questions/23945" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Identify sequence number errors in UDP captures](/questions/23945/identify-sequence-number-errors-in-udp-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23945-score" class="post-score" title="current number of votes">0</div><span id="post-23945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a 10 minute period of captures, during which we have seen out of sequence packets being delivered over a UDP channel in a log file. This is on a custom trading platform that does not subscribe to the exchanges retransmission service, so our retail platforms are fine but the custom one is being spanked 2-3 times per hour.</p><p><strong>Is there a way I can quickly view where a sequence is broken or packets are missing?</strong></p><p>I can see it increment but there are far too many captures to go through 1 by 1 every time there is an issue.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-you" rel="tag" title="see questions tagged &#39;you&#39;">you</span> <span class="post-tag tag-link-thank" rel="tag" title="see questions tagged &#39;thank&#39;">thank</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '13, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/5d71feabdbcdb779bb775fcfcf4fae1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SJennings&#39;s gravatar image" /><p><span>SJennings</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SJennings has no accepted answers">0%</span></p></div></div><div id="comments-container-23945" class="comments-container"><span id="23959"></span><div id="comment-23959" class="comment"><div id="post-23959-score" class="comment-score"></div><div class="comment-text"><p>There are people much smarter than me who will weigh in here...but using the terms "sequence" and "UDP" together seems contradictory. By definition, UDP is connectionless. So in the context of your description, I fail to understand how one UDP packet can be seen as being related any other. Perhaps the application sees them as being related, but Wireshark doesn't know anything about your application - it only knows the UDP protocol as defined by the RFC, which is connectionless. I wouldn't expect Wireshark to be able to find any "sequence" of UDP packets.</p></div><div id="comment-23959-info" class="comment-info"><span class="comment-age">(22 Aug '13, 06:31)</span> <span class="comment-user userinfo">smp</span></div></div><span id="23961"></span><div id="comment-23961" class="comment"><div id="post-23961-score" class="comment-score"></div><div class="comment-text"><p>If the ip identifier for that stream goes up by one each time, then you could use that to detect sequence problems. It may be possible to add support for this to the ip or udp dissector..</p></div><div id="comment-23961-info" class="comment-info"><span class="comment-age">(22 Aug '13, 07:06)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="23962"></span><div id="comment-23962" class="comment"><div id="post-23962-score" class="comment-score"></div><div class="comment-text"><p>: If the ip identifier for that stream goes up by one each time</p><p>Perhaps the OP is talking about IP sequence, and I misinterpreted as UDP sequence. See, that's what I meant by "smarter people"...</p></div><div id="comment-23962-info" class="comment-info"><span class="comment-age">(22 Aug '13, 07:17)</span> <span class="comment-user userinfo">smp</span></div></div><span id="23967"></span><div id="comment-23967" class="comment"><div id="post-23967-score" class="comment-score"></div><div class="comment-text"><p>More likely, it's an upper-layer protocol sequence number that is being referred to here. What protocol atop UDP is this?</p><p>And maybe OP could be a little more clear as to what, "<em>the custom one is being spanked 2-3 times per hour.</em>" means?</p></div><div id="comment-23967-info" class="comment-info"><span class="comment-age">(22 Aug '13, 10:22)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-23945" class="comment-tools"></div><div class="clear"></div><div id="comment-23945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23970"></span>

<div id="answer-container-23970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23970-score" class="post-score" title="current number of votes">0</div><span id="post-23970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have a 10 minute period of captures, during which we have seen out of sequence packets being delivered over a UDP channel in a log file.</p></blockquote><p>As Chris Maynard and smp both noted, there is no such thing as a sequence number error in an arbitrary UDP channel (or even such a thing as a UDP channel!). There might be sequence errors in, for example, an RTP channel running <em>over</em> UDP, but, to recognize that, you need to dissect RTP.</p><p>The sequence errors are in whatever protocol you're running over UDP, so you'd need a dissector for whatever protocol that is.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '13, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23970" class="comments-container"></div><div id="comment-tools-23970" class="comment-tools"></div><div class="clear"></div><div id="comment-23970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24062"></span>

<div id="answer-container-24062" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24062-score" class="post-score" title="current number of votes">0</div><span id="post-24062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>during which we have seen out of sequence packets being delivered over a UDP channel in a log file. <strong>This is on a custom trading platform</strong></p></blockquote><p>O.K. so, you have a trading system that sends <strong>transactions</strong> via UDP and obviously depends on the order of the transactions.</p><p>UDP gives <strong>no guarantee at all</strong> about the receive order of the packets, unless you enabled additional 'measures' on the whole network to prevent packet reordering, however you would do that with your network equipment.</p><blockquote><p>Is there a way I can quickly view where a sequence is broken</p></blockquote><p>Well, as there is no sequence number in UDP and you did not mention the application protocol used, the short answer is: NO, as UDP itself cannot tell you anything about packet re-odering in the network.</p><p><strong>HOWEVER</strong>: As you only need to know if the packets arrived in the same order they were sent, you can use the IP ID of the packets as an indicator for packet reordering. If the IP ID within a conversation (client IP, source port --&gt; server IP, destination port) constantly increases (only positive deltas), there is no packet reordering (please think about the wrap around of the IP ID at 65535!). If there are negative deltas, there is packet reordering.</p><p>Example #1: no reordering</p><pre><code>IP ID: 10478
IP ID: 10552   Delta: 74
IP ID: 10564   Detla: 12
IP ID: 10587   Delta: 23</code></pre><p>Example #2: reordering took place (somewhere in the network)</p><pre><code>IP ID: 10478
IP ID: 10552   Delta: 74
IP ID: 10587   Delta: 35
IP ID: 10564   Detla: -23  !!!</code></pre><p>So, you need the sequence of IP IDs for all UDP conversations and you can do this with tshark and some scripting.</p><p>The following command will return all UDP conversations</p><blockquote><p>tshark -nr input.pcap -q -z conv,udp</p></blockquote><p>Take that output and extract the IP addresses and the ports for each conversation. Then, loop over all conversations (through a script) and run this command</p><blockquote><p>tshark -nr input.pcap -R "ip.addr eq x.x.x.x and ip.addr eq y.y.y.y and udp.port eq aaaa and udp.port eq bbbb" -T fields -e frame.number -e IP.ID</p></blockquote><p>Take that output and generate the delta of the IP IDs as shown above. As soon as you get a negative delta, you found packet reordering. Think about the IP ID wrap around at 65535!! as you will then get a negative delta, although there is no packet reordering?</p><blockquote><p>or packets are missing?</p></blockquote><p>With only one capture point and <strong>no</strong> sequence number whatsoever in the application protocol, there is no way to know if a UDP packet got lost or not! The IP ID does not help you, unless you know for sure, that the packets were sent with a constantly increasing IP ID (+1, +2, +4, etc.), which is very rarely the case!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '13, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24062" class="comments-container"><span id="24069"></span><div id="comment-24069" class="comment"><div id="post-24069-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If the IP ID within a conversation (client IP, source port --&gt; server IP, destination port) constantly increases (only positive deltas)</p></blockquote><p>...<em>AND</em> if the operating system sending the packets assigns sequential numbers as IP IDs...</p><blockquote><p>there is no packet reordering</p></blockquote></div><div id="comment-24069-info" class="comment-info"><span class="comment-age">(26 Aug '13, 10:39)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-24062" class="comment-tools"></div><div class="clear"></div><div id="comment-24062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

