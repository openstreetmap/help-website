+++
type = "question"
title = "IO graph throughput calculation"
description = '''Hello, I’ve some ftp-data frames which I am plotting in IO graph under statistics. The bytes/sec in Wireshark is considering the header of Ethernet + IP + TCP as well but I want only TCP payload (not the entire frame) to be taken to calculate the throughput, is there any way to do this?'''
date = "2014-10-21T23:32:00Z"
lastmod = "2014-10-28T02:40:00Z"
weight = 37261
keywords = [ "ftp", "iograph" ]
aliases = [ "/questions/37261" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IO graph throughput calculation](/questions/37261/io-graph-throughput-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37261-score" class="post-score" title="current number of votes">1</div><span id="post-37261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I’ve some ftp-data frames which I am plotting in IO graph under statistics. The bytes/sec in Wireshark is considering the header of Ethernet + IP + TCP as well but I want only TCP payload (not the entire frame) to be taken to calculate the throughput, is there any way to do this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-iograph" rel="tag" title="see questions tagged &#39;iograph&#39;">iograph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/00a8c62ea3ab8725821654856d0d19ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vish777&#39;s gravatar image" /><p><span>Vish777</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vish777 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '14, 02:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-37261" class="comments-container"></div><div id="comment-tools-37261" class="comment-tools"></div><div class="clear"></div><div id="comment-37261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37275"></span>

<div id="answer-container-37275" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37275-score" class="post-score" title="current number of votes">2</div><span id="post-37275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use the Advanced graph within the IO graphs.</p><p>"regular" Bytes/sec graph:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/IO_graph_bytes_per_second.png" alt="&quot;regular&quot; Bytes/sec graph" /></p><p>Advanced graph for tcp.len, showing bytes/sec for the TCP payload only:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/IO_graph_tcp.len.png" alt="alt text" /></p><p>As you can see, the shape of the graph is the same. However the values for the second graph are lower, as it shows only the TCP payload.</p><p>And no, you cannot show it in bit/s, only in byte/s. At least I don't know a way to do that.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '14, 05:21</strong> </span></p></div></div><div id="comments-container-37275" class="comments-container"><span id="37367"></span><div id="comment-37367" class="comment"><div id="post-37367-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. I think it is working fine now (showing only the TCP payload). By the way what is tcp.len actually? Does it mean the payload of TCP for every case?</p></div><div id="comment-37367-info" class="comment-info"><span class="comment-age">(26 Oct '14, 23:33)</span> <span class="comment-user userinfo">Vish777</span></div></div><span id="37386"></span><div id="comment-37386" class="comment"><div id="post-37386-score" class="comment-score"></div><div class="comment-text"><p>tcp.len is the length of the TCP segment (amount of data that was sent).</p></div><div id="comment-37386-info" class="comment-info"><span class="comment-age">(28 Oct '14, 02:10)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="37387"></span><div id="comment-37387" class="comment"><div id="post-37387-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much Kurt.</p></div><div id="comment-37387-info" class="comment-info"><span class="comment-age">(28 Oct '14, 02:27)</span> <span class="comment-user userinfo">Vish777</span></div></div><span id="37389"></span><div id="comment-37389" class="comment"><div id="post-37389-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p></div><div id="comment-37389-info" class="comment-info"><span class="comment-age">(28 Oct '14, 02:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-37275" class="comment-tools"></div><div class="clear"></div><div id="comment-37275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

