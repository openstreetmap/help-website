+++
type = "question"
title = "rtp statistics on a loopback capture"
description = '''Im trying to run TShark with a loopback capture and get a table of RTP statistics using: c:&#92;tshark.exe -q -r &amp;lt;pcap file=&quot;&quot;&amp;gt; -z rtp,streams. for some reason I get an empty table. This is not the case for a non-loopback pcap file. if I open the file with wireshark and decode as RTP I can see the...'''
date = "2013-04-29T04:37:00Z"
lastmod = "2013-05-01T14:05:00Z"
weight = 20837
keywords = [ "rtp_statistics" ]
aliases = [ "/questions/20837" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [rtp statistics on a loopback capture](/questions/20837/rtp-statistics-on-a-loopback-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20837-score" class="post-score" title="current number of votes">0</div><span id="post-20837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im trying to run TShark with a loopback capture and get a table of RTP statistics using: c:\tshark.exe -q -r &lt;pcap file=""&gt; -z rtp,streams.</p><p>for some reason I get an empty table. This is not the case for a non-loopback pcap file.</p><p>if I open the file with wireshark and decode as RTP I can see the RTP streams. Does anyone know why I can't get the statistics for this file??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp_statistics" rel="tag" title="see questions tagged &#39;rtp_statistics&#39;">rtp_statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '13, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/a3b238676c51cb9e45690ad80766ff79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy&#39;s gravatar image" /><p><span>Guy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy has no accepted answers">0%</span></p></div></div><div id="comments-container-20837" class="comments-container"></div><div id="comment-tools-20837" class="comment-tools"></div><div class="clear"></div><div id="comment-20837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20841"></span>

<div id="answer-container-20841" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20841-score" class="post-score" title="current number of votes">0</div><span id="post-20841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>if I open the file with wireshark and decode as RTP</p></blockquote><p>if you have to 'Decode as..' in Wireshark, you'll have to do that in tshark as well, otherwise tshark will not realize that there are any RTP packets.</p><blockquote><p><code>tshark -nr input.pcap -d udp.port==5555,rtp -z rtp,streams</code><br />
</p></blockquote><p>Replace the port 5555 by whatever is used in your environment.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '13, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Apr '13, 08:53</strong> </span></p></div></div><div id="comments-container-20841" class="comments-container"><span id="20860"></span><div id="comment-20860" class="comment"><div id="post-20860-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your reply! the problem is that the udp port is not something I can know in advance. This is why Im using " -o rtp.heuristic_rtp:TRUE" but for some reason it works on all pcap's except for a loopback capture. Do you know if there is a way to use -d udp.port==xxxx for all ports in the pcap file??</p><p>Thanks, Guy</p></div><div id="comment-20860-info" class="comment-info"><span class="comment-age">(01 May '13, 00:24)</span> <span class="comment-user userinfo">Guy</span></div></div><span id="20887"></span><div id="comment-20887" class="comment"><div id="post-20887-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but for some reason it works on all pcap's except for a loopback capture.</p></blockquote><p>can you post a sample capture somewhere?</p><blockquote><p>Do you know if there is a way to use -d udp.port==xxxx for all ports in the pcap file??</p></blockquote><p>well, you could run tshark twice within a script. First, get all ports, then call tshark with multiple -d options for all ports in the capture file.</p></div><div id="comment-20887-info" class="comment-info"><span class="comment-age">(01 May '13, 14:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20841" class="comment-tools"></div><div class="clear"></div><div id="comment-20841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

