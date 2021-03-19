+++
type = "question"
title = "Search data spanned over multiple TCP packets"
description = '''This pcap has a TCP session of slowloris attack. When I tried to search for the string &quot;www.t.co&quot;, it failed to find the packets that contain it. This string actually span two TCP data packets. Wonder if Wireshark supports searching across packets. Thanks. My wireshark version is 1.10.6.'''
date = "2015-09-07T12:38:00Z"
lastmod = "2015-09-07T21:41:00Z"
weight = 45673
keywords = [ "wireshark" ]
aliases = [ "/questions/45673" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Search data spanned over multiple TCP packets](/questions/45673/search-data-spanned-over-multiple-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45673-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This <a href="https://www.cloudshark.org/captures/4a0c06802d74">pcap</a> has a TCP session of slowloris attack. When I tried to search for the string "www.t.co", it failed to find the packets that contain it. This string actually span two TCP data packets. Wonder if Wireshark supports searching across packets. Thanks.</p><p>My wireshark version is 1.10.6.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '15, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-45673" class="comments-container"></div><div id="comment-tools-45673" class="comment-tools"></div><div class="clear"></div><div id="comment-45673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45676"></span>

<div id="answer-container-45676" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45676-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Wonder if Wireshark supports searching across packets.</p></blockquote><p>No, it doesn't.</p><p>However, you can follow a TCP stream and then search within the text of the pop-up window.</p><blockquote><p>right click any frame -&gt; Follow TCP Stream</p></blockquote><p>Then use Find function.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45676" class="comments-container"><span id="45701"></span><div id="comment-45701" class="comment"><div id="post-45701-score" class="comment-score"></div><div class="comment-text"><p>The issue is we don't know which session in a pcap contains that string (that may span over multiple data packet). I was afraid it's outside the scope of Wireshark. Thanks for confirming it.</p></div><div id="comment-45701-info" class="comment-info"><span class="comment-age">(08 Sep '15, 07:24)</span> pktUser1001</div></div></div><div id="comment-tools-45676" class="comment-tools"></div><div class="clear"></div><div id="comment-45676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45686"></span>

<div id="answer-container-45686" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45686-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well in this case Wireshark can do it.<br />
</p><p>At the packet detail pane right click the TCP layer and activate</p><pre><code> Protcol Preferences -&gt; Allow subdissectors to reassemble TCP Streams</code></pre><p>Then at the packet detail pane right click the HTTP layer and activate</p><pre><code>Protcol Preferences -&gt; Reassemble HTTP headers spanning multiple segments</code></pre><p>And then you can see the host and the url <code>www.t.co</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 21:41</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Sep '15, 14:43</p></div></div><div id="comments-container-45686" class="comments-container"><span id="45702"></span><div id="comment-45702" class="comment"><div id="post-45702-score" class="comment-score"></div><div class="comment-text"><p>Thanks @Christian_R for the answer. It helps in the case of searching for HTTP host header. In the general case of search for a string in TCP stream, it can't be done as Kurt confirmed.</p></div><div id="comment-45702-info" class="comment-info"><span class="comment-age">(08 Sep '15, 07:26)</span> pktUser1001</div></div><span id="45704"></span><div id="comment-45704" class="comment"><div id="post-45704-score" class="comment-score"></div><div class="comment-text"><p>You also can reassemble the http bodies .</p></div><div id="comment-45704-info" class="comment-info"><span class="comment-age">(08 Sep '15, 07:43)</span> Christian_R</div></div></div><div id="comment-tools-45686" class="comment-tools"></div><div class="clear"></div><div id="comment-45686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

