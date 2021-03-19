+++
type = "question"
title = "Tshark parameter for filtering by given ip and decode it using ssl"
description = '''Which parameters I have to provide to tshark to filter IP packets from a specific IP address (in wireshark I use ip.src == xxx.yyy.zzz.nnn) and which parameters I need to provide to decode these packets using ssl, to do it in wireshark I use the &quot;decode as&quot; and in &quot;Transport tab&quot; I set SSL. The pack...'''
date = "2015-12-31T04:44:00Z"
lastmod = "2016-01-13T06:47:00Z"
weight = 48767
keywords = [ "tshark", "parameters" ]
aliases = [ "/questions/48767" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark parameter for filtering by given ip and decode it using ssl](/questions/48767/tshark-parameter-for-filtering-by-given-ip-and-decode-it-using-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48767-score" class="post-score" title="current number of votes">0</div><span id="post-48767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Which parameters I have to provide to tshark to filter IP packets from a specific IP address (in wireshark I use ip.src == xxx.yyy.zzz.nnn) and which parameters I need to provide to decode these packets using ssl, to do it in wireshark I use the "decode as" and in "Transport tab" I set SSL. The packages, although encoded using ssl, not come from a https connection.</p><p>How can I write the content of all decoded and filtered packets to a file or to stdout ?</p><p>Update: I have tried tshark n -o ssl.keylog_file:/tmp/master.txt -Y ip.src==xxx.yyy.nnn.mmm -d tcp.port==0-999999,ssl I see this Capturing on 'eth0'</p><pre><code>6540 56.156992382 xxx.yyy.nnn.mmm -&gt; 192.168.1.2 TCP 74 7072 → 49188 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1380 WS=256 SACK_PERM=1 TSval=603635523 TSecr=10839353
6546 56.291147285 xxx.yyy.nnn.mmm -&gt; 192.168.1.2 TCP 1434 [TCP segment of a reassembled PDU]
6548 56.293045394 xxx.yyy.nnn.mmm -&gt; 192.168.1.2 TCP 1434 [TCP segment of a reassembled PDU]
6550 56.294313103 xxx.yyy.nnn.mmm -&gt; 192.168.1.2 TLSv1 1300 Server Hello, Certificate, Server Hello Done
6560 56.343469786 xxx.yyy.nnn.mmm -&gt; 192.168.1.2 TLSv1 125 Change Cipher Spec, Encrypted Handshake Message
6575 56.785954188 xxx.yyy.nnn.mmm -&gt; 192.168.1.2 TLSv1 231 Application Data</code></pre><p>How can I dump the packet content as "Follow stream" in wireshark already does ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-parameters" rel="tag" title="see questions tagged &#39;parameters&#39;">parameters</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '15, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/306d7986d36750697c633864525d3775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="famedoro&#39;s gravatar image" /><p><span>famedoro</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="famedoro has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jan '16, 06:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48767" class="comments-container"><span id="49169"></span><div id="comment-49169" class="comment"><div id="post-49169-score" class="comment-score"></div><div class="comment-text"><p>You should really create a different question for your new problem, as other readers now won't be able to follow your original question and my answers to those questions. In addition, if my answer has solved your original issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer.</p><p>This is a Q&amp;A site, not a forum, please see the FAQ for more info.</p></div><div id="comment-49169-info" class="comment-info"><span class="comment-age">(13 Jan '16, 06:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49170"></span><div id="comment-49170" class="comment"><div id="post-49170-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> I'm sorry, I have posted a new question on <a href="https://ask.wireshark.org/questions/49141/how-to-show-ssl-decrypted-packet-content">https://ask.wireshark.org/questions/49141/how-to-show-ssl-decrypted-packet-content</a></p></div><div id="comment-49170-info" class="comment-info"><span class="comment-age">(13 Jan '16, 06:47)</span> <span class="comment-user userinfo">famedoro</span></div></div></div><div id="comment-tools-48767" class="comment-tools"></div><div class="clear"></div><div id="comment-48767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48774"></span>

<div id="answer-container-48774" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48774-score" class="post-score" title="current number of votes">1</div><span id="post-48774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="famedoro has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The answers to your multiple questions are (hopefully) shown below:</p><ol><li>The filter "ip.src == ..." is a display filter, so you should use the <code>-Y</code> display filter option, e.g. <code>-Y ip.src == 1.2.3.4</code></li><li>To set a decode as setting, use the <code>-d</code> option, e.g. <code>-d tcp.port==8888,ssl</code> to decode tcp traffic on port 8888 as ssl.</li><li>To write the output to a file, redirect the output of the command to the required file, e.g. <code>tshark -Y ... -d ... &gt; myfile.txt</code></li></ol><p>You may need to quote some arguments depending on the shell you're using.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '15, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48774" class="comments-container"><span id="48790"></span><div id="comment-48790" class="comment"><div id="post-48790-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response, using -d tcp.port==8888,ssl I decode only traffic on port 8888 as ssl, but I need to decode all the traffic from a specific ip .</p></div><div id="comment-48790-info" class="comment-info"><span class="comment-age">(02 Jan '16, 04:26)</span> <span class="comment-user userinfo">famedoro</span></div></div><span id="48791"></span><div id="comment-48791" class="comment"><div id="post-48791-score" class="comment-score"></div><div class="comment-text"><p>I'm not aware of any method using tshark or Wireshark to decode all traffic from a particular IP as another protocol. You can use a port range in the tcp.port selector, e.g. <code>-d tcp.port==8888:3,ssl</code> to select the 3 ports 8888, 8889, 8890, or <code>-d tcp.port==8888-8890,ssl</code> to specify the extents of the port range.</p><p>You can also list all the selectors available using <code>-d .</code></p></div><div id="comment-48791-info" class="comment-info"><span class="comment-age">(02 Jan '16, 08:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49140"></span><div id="comment-49140" class="comment"><div id="post-49140-score" class="comment-score"></div><div class="comment-text"><p>Possibly that version's too old. I don't have that version to check the possible arguments for you. Check the possible arguments with <code>tshark --help</code></p></div><div id="comment-49140-info" class="comment-info"><span class="comment-age">(12 Jan '16, 11:29)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48774" class="comment-tools"></div><div class="clear"></div><div id="comment-48774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

