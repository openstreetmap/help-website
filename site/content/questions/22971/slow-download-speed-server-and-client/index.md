+++
type = "question"
title = "Slow download speed server and client."
description = '''we are getting very slow spped download from server 192.168.1.1 . Rest all download speed is good only speed with this server server is slow over port 80 763 0.000096000 0.000096000 10.10.10.1 192.168.1.1 TCP 54 51816 &amp;gt; http [ACK] Seq=1 Ack=1 Win=66048 Len=0 0.000096000 258 762  762 0.117565000 0...'''
date = "2013-07-15T03:41:00Z"
lastmod = "2013-07-15T03:59:00Z"
weight = 22971
keywords = [ "wireshark" ]
aliases = [ "/questions/22971" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow download speed server and client.](/questions/22971/slow-download-speed-server-and-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22971-score" class="post-score" title="current number of votes">-1</div><span id="post-22971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>we are getting very slow spped download from server 192.168.1.1 .</p><p>Rest all download speed is good only speed with this server server is slow over port 80</p><pre><code>763 0.000096000 0.000096000 10.10.10.1  192.168.1.1 TCP 54  51816 &gt; http [ACK] Seq=1 Ack=1 Win=66048 Len=0  0.000096000 258 762

762 0.117565000 0.319337000 192.168.1.1 10.10.10.1  TCP 66  http &gt; 51816 [SYN, ACK] Seq=0 Ack=1 Win=64240 Len=0 MSS=1380 WS=1 SACK_PERM=1   0.319337000 64240   747

763 0.000096000 0.000096000 10.10.10.1  192.168.1.1 TCP 54  51816 &gt; http [ACK] Seq=1 Ack=1 Win=66048 Len=0  0.000096000 258 762

764 0.000100000 0.000100000 10.10.10.1  192.168.1.1 HTTP    240 GET /offshorelibs/SACS/?cmd=capabilities HTTP/1.1   0.000100000 258

766 0.275298000 0.321532000 192.168.1.1 10.10.10.1  TCP 1434    [TCP segment of a reassembled PDU]  0.321532000 64054   764

767 0.000186000 0.000186000 192.168.1.1 10.10.10.1  HTTP    546 HTTP/1.1 401 Unauthorized  (text/html)  0.000186000 64054

768 0.000027000 0.000027000 10.10.10.1  192.168.1.1 TCP 54  51816 &gt; http [ACK] Seq=187 Ack=1873 Win=66048 Len=0 0.000027000 258 767

769 0.051942000 0.051942000 10.10.10.1  192.168.1.1 HTTP    274 GET /offshorelibs/SACS/?cmd=capabilities HTTP/1.1 , NTLMSSP_NEGOTIATE   0.051942000 258

770 0.065125000 0.065125000 192.168.1.1 10.10.10.1  TCP 60  [TCP Dup ACK 767#1] http &gt; 51816 [ACK] Seq=1873 Ack=187 Win=64054 Len=0 0.065125000 64054

777 0.187790000 0.252737000 192.168.1.1 10.10.10.1  TCP 1434    [TCP segment of a reassembled PDU]  0.252737000 63834   769

778 0.000424000 0.000424000 192.168.1.1 10.10.10.1  HTTP    689 HTTP/1.1 401 Unauthorized , NTLMSSP_CHALLENGE (text/html)   0.000424000 63834

779 0.000023000 0.000023000 10.10.10.1  192.168.1.1 TCP 54  51816 &gt; http [ACK] Seq=407 Ack=3888 Win=66048 Len=0 0.000023000 258 778

780 0.000630000 0.000630000 10.10.10.1  192.168.1.1 HTTP    818 GET /offshorelibs/SACS/?cmd=capabilities HTTP/1.1 , NTLMSSP_AUTH, User: BENTLEY\formsys-service 0.000630000 258</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '13, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/6615a61d69b703d89076bb0f18342bbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m_1607&#39;s gravatar image" /><p><span>m_1607</span><br />
<span class="score" title="35 reputation points">35</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m_1607 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '13, 03:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-22971" class="comments-container"><span id="22973"></span><div id="comment-22973" class="comment"><div id="post-22973-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@m_1607</span>, the purpose of this site is to get answers to questions you have about wireshark and how to use it. We do take the occasional detour of answering questions related to a specific networking issue, but that is not standard and we need a certain amount of information to be able to help out.</p><p>This site is <strong>not</strong> about asking questions about your network issues every time one comes up. We tried to help you as best as we can in your last questions. But I would advice you to look for a consultancy firm that does network analysis to help you out with your issues as you are not able to share the information needed to help you and your issues don't seem to be isolated.</p></div><div id="comment-22973-info" class="comment-info"><span class="comment-age">(15 Jul '13, 03:59)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-22971" class="comment-tools"></div><div class="clear"></div><div id="comment-22971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22972"></span>

<div id="answer-container-22972" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22972-score" class="post-score" title="current number of votes">0</div><span id="post-22972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry but I'm not going to repeat myself - like in your other 4+ questions where everybody was trying to help you out, same answers apply here</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '13, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-22972" class="comments-container"></div><div id="comment-tools-22972" class="comment-tools"></div><div class="clear"></div><div id="comment-22972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

