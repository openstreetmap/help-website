+++
type = "question"
title = "large length tcp field during SMB2 copy"
description = '''Hi, I have a trace for SMB2 file copying. When I check this trace, I saw traffic pattern like this during the transfer. (the trace is captured from the server, clients are copying data from the server) ----------  [server -&amp;gt; client, length = 62823bytes] [server -&amp;gt; client, length = 2788bytes] [...'''
date = "2013-12-24T22:09:00Z"
lastmod = "2013-12-25T00:29:00Z"
weight = 28379
keywords = [ "tcp_length_field" ]
aliases = [ "/questions/28379" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [large length tcp field during SMB2 copy](/questions/28379/large-length-tcp-field-during-smb2-copy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28379-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a trace for SMB2 file copying. When I check this trace, I saw traffic pattern like this during the transfer.</p><p>(the trace is captured from the server, clients are copying data from the server)</p><pre><code>----------

[server -&gt; client, length = 62823bytes]
[server -&gt; client, length = 2788bytes]
[client -&gt; server, length = 0, tcp ACK]
[client -&gt; server, length = 0, tcp ACK]
[.....]
[tens of same packets omitted]
[.....]
[client -&gt; server, length = 0, tcp ACK]
[server -&gt; client, length = 32844bytes]
[client -&gt; server, length = 0, tcp ACK]
[.....]
[tens of same packets omitted]
[.....]
[client -&gt; server, length = 0, tcp ACK]
[....]

----------</code></pre><p>I understand that those tens of Acks are for different tcp data transfer segments. But shouldn't I expect to see tens of data transfer tcp segments followed by Acks? Why wireshark only shows one SMB2 packet with a very large, bigger than common 1460 TCP segment, packet followed by all of the Ackes? Like the following:</p><pre><code>----------

[server -&gt; client, length = 1460bytes]
[server -&gt; client, length = 1460bytes]
[server -&gt; client, length = 1460bytes]
[.....]
[server -&gt; client, length = 1460bytes]
[server -&gt; client, length = 1460bytes]
[client -&gt; server, length = 0, Ack1]
[client -&gt; server, length = 0, Ack2]
[......]

----------</code></pre><p>Could anyone let me know the insides?</p><p>thanks a lot!</p></div><div id="question-tags" class="tags-container tags">tcp_length_field</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '13, 22:09</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Dec '13, 01:24</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-28379" class="comments-container"><span id="28380"></span><div id="comment-28380" class="comment"><div id="post-28380-score" class="comment-score"></div><div class="comment-text"><p>I don't know why i cannot row the packets...the format for the example packets are ugly, sorry for that.</p></div><div id="comment-28380-info" class="comment-info"><span class="comment-age">(24 Dec '13, 22:14)</span> SteveZhou</div></div><span id="28381"></span><div id="comment-28381" class="comment"><div id="post-28381-score" class="comment-score"></div><div class="comment-text"><p>I re-formatted each packet with a "[]" for your convenience to separate them.</p></div><div id="comment-28381-info" class="comment-info"><span class="comment-age">(24 Dec '13, 22:18)</span> SteveZhou</div></div></div><div id="comment-tools-28379" class="comment-tools"></div><div class="clear"></div><div id="comment-28379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28383"></span>

<div id="answer-container-28383" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28383-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you can see the frames seen by wireshark are very large. That's due to TCP offloading into the NIC driver. The driver will split those 'large frames' into a lot of smaller frames (according to the MTU). The client then answers to 'some' (or all) of those frames with an ACK.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Dec '13, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Dec '13, 07:43</p></div></div><div id="comments-container-28383" class="comments-container"><span id="28384"></span><div id="comment-28384" class="comment"><div id="post-28384-score" class="comment-score"></div><div class="comment-text"><p>More likely it is answering to each other frame with an ack, at least Windows does. So there should roughly be one ack packet per two packets carrying data segments.</p></div><div id="comment-28384-info" class="comment-info"><span class="comment-age">(25 Dec '13, 02:48)</span> Jasper ♦♦</div></div><span id="28386"></span><div id="comment-28386" class="comment"><div id="post-28386-score" class="comment-score"></div><div class="comment-text"><p>You're of course right. So, my wording (ACK for <strong>each</strong> frame) was not correct ;-) See my correction in the answer.</p></div><div id="comment-28386-info" class="comment-info"><span class="comment-age">(25 Dec '13, 05:12)</span> Kurt Knochner ♦</div></div><span id="28404"></span><div id="comment-28404" class="comment"><div id="post-28404-score" class="comment-score"></div><div class="comment-text"><p>so if disable TCP offloading on the server, should I expect to see patters like below?</p><pre><code>[server -&gt; client, length = 1460bytes]
[server -&gt; client, length = 1460bytes]
[server -&gt; client, length = 1460bytes]
[.....]
[server -&gt; client, length = 1460bytes]
[server -&gt; client, length = 1460bytes]
[client -&gt; server, length = 0, Ack1]
[client -&gt; server, length = 0, Ack2]
[......]</code></pre></div><div id="comment-28404-info" class="comment-info"><span class="comment-age">(26 Dec '13, 06:35)</span> SteveZhou</div></div><span id="28409"></span><div id="comment-28409" class="comment"><div id="post-28409-score" class="comment-score"></div><div class="comment-text"><p>More or less. You will see the same if you capture at the client.</p></div><div id="comment-28409-info" class="comment-info"><span class="comment-age">(26 Dec '13, 07:56)</span> Kurt Knochner ♦</div></div><span id="28415"></span><div id="comment-28415" class="comment"><div id="post-28415-score" class="comment-score"></div><div class="comment-text"><p>I checked the NIC properties on the server, we have Large send offload enabled, is it the TCP offloading you referred to?</p></div><div id="comment-28415-info" class="comment-info"><span class="comment-age">(26 Dec '13, 18:32)</span> SteveZhou</div></div><span id="28418"></span><div id="comment-28418" class="comment not_top_scorer"><div id="post-28418-score" class="comment-score"></div><div class="comment-text"><p>I have confirmed that after disabling LSO, we are now seeing bunch of 1460bytes of TCP segment followed by acks. But the wireshark response became really slow during the capturing. After re-enabling the LSO, no sluggish on the wireshark GUI anymore.</p></div><div id="comment-28418-info" class="comment-info"><span class="comment-age">(26 Dec '13, 22:56)</span> SteveZhou</div></div><span id="28429"></span><div id="comment-28429" class="comment not_top_scorer"><div id="post-28429-score" class="comment-score"></div><div class="comment-text"><p>what do you mean by "wireshark response became really slow during the capturing"? Did the 'reaction time' of the GUI change in any way?</p></div><div id="comment-28429-info" class="comment-info"><span class="comment-age">(27 Dec '13, 03:53)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28383" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-28383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

