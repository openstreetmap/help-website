+++
type = "question"
title = "Getting capture stats manually"
description = '''Hello to all, I am curious how can i get the stats from a packet capture manually ( instead of going to statistics-&amp;gt;summary menu), such as packet count, total bytes, and avg MBit/sec. It&#x27;s just an educational question, i don&#x27;t want to use it in real life. Thanks!!!'''
date = "2012-12-22T03:26:00Z"
lastmod = "2012-12-22T03:52:00Z"
weight = 17159
keywords = [ "bytes", "statistics", "manually", "packet", "wireshark" ]
aliases = [ "/questions/17159" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting capture stats manually](/questions/17159/getting-capture-stats-manually)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17159-score" class="post-score" title="current number of votes">0</div><span id="post-17159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello to all, I am curious how can i get the stats from a packet capture manually ( instead of going to statistics-&gt;summary menu), such as packet count, total bytes, and avg MBit/sec.</p><p>It's just an educational question, i don't want to use it in real life.</p><p>Thanks!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bytes" rel="tag" title="see questions tagged &#39;bytes&#39;">bytes</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-manually" rel="tag" title="see questions tagged &#39;manually&#39;">manually</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '12, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/07b3ae5bcfad5fe365c384d9e64023cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EvilDude&#39;s gravatar image" /><p><span>EvilDude</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EvilDude has no accepted answers">0%</span></p></div></div><div id="comments-container-17159" class="comments-container"></div><div id="comment-tools-17159" class="comment-tools"></div><div class="clear"></div><div id="comment-17159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17160"></span>

<div id="answer-container-17160" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17160-score" class="post-score" title="current number of votes">0</div><span id="post-17160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Isn't going to statistics-&gt;summary the manual way to get the statistics? You can get to the stats from the CLI with capinfos:</p><pre><code>[email protected]:~$ capinfos http.cap 
File name:           http.cap
File type:           Wireshark - pcapng
File encapsulation:  Ethernet
Packet size limit:   file hdr: (not set)
Number of packets:   186
File size:           109184 bytes
Data size:           102706 bytes
Capture duration:    26 seconds
Start time:          Tue Jul 26 10:51:38 2011
End time:            Tue Jul 26 10:52:03 2011
Data byte rate:      3996.21 bytes/sec
Data bit rate:       31969.72 bits/sec
Average packet size: 552.18 bytes
Average packet rate: 7.24 packets/sec
SHA1:                b17a997e66f0b3acd41d6a6f8359d756a1b206fb
RIPEMD160:           eedf16dd6f4d25e0dba9d1b9b94cdbd1548dbf04
MD5:                 150ffdaaafab74613510e33ca2d39bd4
Strict time order:   True
[email protected]:~$</code></pre><p>But maybe you mean how you can calculate the individual values themselves? Well, that would require libpcap programming to read the files and keep count of all the necessary data and then output the results. So basically you would want to write your own capinfos tool :-)</p><p>(have a look at the <a href="http://anonsvn.wireshark.org/viewvc/trunk/capinfos.c?revision=45015&amp;view=markup">capinfos source code</a> for more details)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '12, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17160" class="comments-container"></div><div id="comment-tools-17160" class="comment-tools"></div><div class="clear"></div><div id="comment-17160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

