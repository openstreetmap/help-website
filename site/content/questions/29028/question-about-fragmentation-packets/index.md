+++
type = "question"
title = "Question about fragmentation packets"
description = '''Hi all,  I&#x27;m posting to know a header structure of fragmented packets.  and don&#x27;t know how can i upload image and wireshark files  so link my question as the below.  (it&#x27;s my blog and image, wireshark includes) http://blog.daum.net/bungbung77/16781142  1~2 : fragmented packets 3~4 : fragmented packe...'''
date = "2014-01-20T07:25:00Z"
lastmod = "2014-01-20T08:48:00Z"
weight = 29028
keywords = [ "fragmentation" ]
aliases = [ "/questions/29028" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Question about fragmentation packets](/questions/29028/question-about-fragmentation-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29028-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm posting to know a header structure of fragmented packets.</p><p>and don't know how can i upload image and wireshark files so link my question as the below. (it's my blog and image, wireshark includes) <a href="http://blog.daum.net/bungbung77/16781142">http://blog.daum.net/bungbung77/16781142</a></p><p><img src="https://osqa-ask.wireshark.org/upfiles/1.jpg" alt="alt text" /> 1~2 : fragmented packets</p><p>3~4 : fragmented packets</p><p>Header structure</p><p>1: IP/UDP/SIP (1500bytes = ip header 20bytes + payload 1480bytes)</p><p>2: IP/Data</p><p>3: IP/Data (1444bytes = ip header 20bytes + payload 1424bytes)</p><p>4:IP/UDP/SIP</p><p>in my guess, 1's structure is same with 3 (and 2 is same with 4)</p><p>but 1's header structure isn't same with 3 (and 2 didn't with 4)</p><p>why wireshark shows like the above?</p></div><div id="question-tags" class="tags-container tags">fragmentation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '14, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/40370b1bbff86a18085b9fa17feb01f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ray_Han007&#39;s gravatar image" /><p>Ray_Han007<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ray_Han007 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jan '14, 07:28</p></div></div><div id="comments-container-29028" class="comments-container"><span id="29041"></span><div id="comment-29041" class="comment"><div id="post-29041-score" class="comment-score"></div><div class="comment-text"><p>Just to answer that side question on how to upload a packet capture, one easy way to do that is cloudshark: <a href="http://cloudshark.org/">http://cloudshark.org/</a></p></div><div id="comment-29041-info" class="comment-info"><span class="comment-age">(20 Jan '14, 18:24)</span> Quadratic</div></div></div><div id="comment-tools-29028" class="comment-tools"></div><div class="clear"></div><div id="comment-29028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29030"></span>

<div id="answer-container-29030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29030-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That happens because your Wireshark is doing IPv4 datagram reassembly, which means that it gathers all datagrams and displays them in a reassembled order.</p><p>To see the "real" packets you can turn that feature off. Go to Edit -&gt; Preferences -&gt; Protocols -&gt; IPv4 and deselect "Reassemble fragmented IPv4 datagrams" (or something similar; these captions change sometimes depending on your version of Wireshark).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '14, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '14, 01:35</p></div></div><div id="comments-container-29030" class="comments-container"><span id="29038"></span><div id="comment-29038" class="comment"><div id="post-29038-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper thanks for your comments it's a great help to understand my question. and hope to have a good day!! Thanks</p></div><div id="comment-29038-info" class="comment-info"><span class="comment-age">(20 Jan '14, 18:21)</span> Ray_Han007</div></div></div><div id="comment-tools-29030" class="comment-tools"></div><div class="clear"></div><div id="comment-29030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

