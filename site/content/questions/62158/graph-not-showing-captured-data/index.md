+++
type = "question"
title = "Graph not showing captured data?"
description = '''Hi, I&#x27;m new to wireshark and have to use it to capture a ddos attack for an assignment.  I have the captured traffic, but every time I try to open the graph it shows no data. I&#x27;m not sure what filters to use; I&#x27;ve tried all the ones I can think of, and I&#x27;m and still getting nothing coming up.  All o...'''
date = "2017-06-20T01:39:00Z"
lastmod = "2017-06-20T01:39:00Z"
weight = 62158
keywords = [ "filter", "graph", "tcp" ]
aliases = [ "/questions/62158" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Graph not showing captured data?](/questions/62158/graph-not-showing-captured-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62158-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm new to wireshark and have to use it to capture a ddos attack for an assignment.</p><p>I have the captured traffic, but every time I try to open the graph it shows no data. I'm not sure what filters to use; I've tried all the ones I can think of, and I'm and still getting nothing coming up.</p><p>All of the traffic captured is TCP protocol, hitting port 80. I have a TCP traffic filter, IP address (127.0.0.1), an all packets filter and a tcp.port == 80 || udp.port == 80.</p><p>Pleeease help me if possible, I am about to put my fist through the laptop.</p><p>Cheers</p></div><div id="question-tags" class="tags-container tags">filter graph tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '17, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/ba7e11362370df03395f0e47bef76854?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C19&#39;s gravatar image" /><p>C19<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C19 has no accepted answers">0%</span></p></div></div><div id="comments-container-62158" class="comments-container"><span id="62171"></span><div id="comment-62171" class="comment"><div id="post-62171-score" class="comment-score"></div><div class="comment-text"><p>Which Wireshark version do you use? In 2.2.x (in my case, 2.2.7) you go <code>Statistics -&gt; I/O graph</code>, and if you haven't used the graph before, you should have there two active traces - one named "All packets" with no display filter, and another one named TCP Errors with display filter <code>tcp.analysis.flags</code>. If you have something else there, click one of the lines and press the [-] button until the list is empty, then close the graph and open it again. You should see at least the "all packets" line.</p><p>Then, you can fill in the "display filter" field, press enter when the filter meets your needs, and then tick the checkbox next to the name as it unchecks after you change the filter.</p><p>Which of these steps does not work for you?</p></div><div id="comment-62171-info" class="comment-info"><span class="comment-age">(20 Jun '17, 07:30)</span> sindy</div></div></div><div id="comment-tools-62158" class="comment-tools"></div><div class="clear"></div><div id="comment-62158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

