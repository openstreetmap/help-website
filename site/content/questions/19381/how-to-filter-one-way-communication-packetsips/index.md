+++
type = "question"
title = "How to filter one way communication( packets/IPs)"
description = '''Hello  I have a capture file and in it there are some IP which have only one way traffic means traffic comes to destination but when destination reply back to source that packets are not there in that capture file. So tell me how I can find the missing packets which has no reply (means only one way ...'''
date = "2013-03-12T03:33:00Z"
lastmod = "2013-03-12T03:50:00Z"
weight = 19381
keywords = [ "filter", "communication", "way", "one" ]
aliases = [ "/questions/19381" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter one way communication( packets/IPs)](/questions/19381/how-to-filter-one-way-communication-packetsips)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19381-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><pre><code>  I have a capture file and in it there are some IP which have only one way traffic means traffic comes to destination but when destination reply back to source that packets are not there in that capture file. So tell me how I can find the missing packets which has no reply (means only one way traffic)</code></pre><p>Like I have Client and server<br />
Server = 192.168.1.10 Client1 =192.168.1.21 Client2 =192.168.1.22 Client3 =192.168.1.23 Client4 =192.168.1.24</p><p>In the file I have the packets Client1 to Server and Server to Client1 Client2 to Server and Server to Client2 Client4 to Server and Server to Client4 And only for Client3 I am getting only one way traffic means Traffic is going Client3 to Server but no Traffic is from Server to Client3</p><p>So tell me how I can filter these kind of traffic which have only one way of communication using Wireshark. In real I have a lot of clients so I want to know which client is have only one way traffic.</p><p>Thanks Regards Mudasser</p></div><div id="question-tags" class="tags-container tags">filter communication way one</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/606252e8dfea9cac0294fa56234519a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="togreatmind&#39;s gravatar image" /><p>togreatmind<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="togreatmind has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-19381" class="comments-container"></div><div id="comment-tools-19381" class="comment-tools"></div><div class="clear"></div><div id="comment-19381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19383"></span>

<div id="answer-container-19383" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19383-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Goto menu Statistics|Conversations. Sort the list on 'Packets A-&gt;B', or 'Packets A&lt;-B', and see which has 0 at the one end.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '13, 03:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19383" class="comments-container"><span id="19384"></span><div id="comment-19384" class="comment"><div id="post-19384-score" class="comment-score"></div><div class="comment-text"><p>Thanks alot dear</p></div><div id="comment-19384-info" class="comment-info"><span class="comment-age">(12 Mar '13, 04:45)</span> togreatmind</div></div></div><div id="comment-tools-19383" class="comment-tools"></div><div class="clear"></div><div id="comment-19383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

