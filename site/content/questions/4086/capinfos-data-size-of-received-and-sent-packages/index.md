+++
type = "question"
title = "capinfos:  data size of received and sent packages"
description = '''Hi, I&#x27;m using dumpcap and capinfos to get the total size of traffic data. But I want to split these in total SENT traffic, and total RECEIVED traffic. capinfos -D &amp;lt;file&amp;gt; (this command just give me the total) Is it possible to do something like this: capinfos -D &amp;lt;file&amp;gt; -SENT (just the tot...'''
date = "2011-05-14T05:18:00Z"
lastmod = "2011-09-27T21:43:00Z"
weight = 4086
keywords = [ "received", "tshark", "sent", "capinfos" ]
aliases = [ "/questions/4086" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [capinfos: data size of received and sent packages](/questions/4086/capinfos-data-size-of-received-and-sent-packages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4086-score" class="post-score" title="current number of votes">0</div><span id="post-4086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using dumpcap and capinfos to get the total size of traffic data. But I want to split these in total SENT traffic, and total RECEIVED traffic.</p><p>capinfos -D &lt;file&gt; (this command just give me the total)</p><p>Is it possible to do something like this:</p><p>capinfos -D &lt;file&gt; -SENT (just the total sent) capinfos -D &lt;file&gt; -RECEIVED (just the total received)</p><p>I know that tshark have a lot of features for especial scenarios like this, but I'm not too familiar with the syntax. From what I read in the docs, I can specify fields to retrieve and even do the SUM expression.</p><p>Any help?</p><p>Thanks in advance,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-received" rel="tag" title="see questions tagged &#39;received&#39;">received</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-sent" rel="tag" title="see questions tagged &#39;sent&#39;">sent</span> <span class="post-tag tag-link-capinfos" rel="tag" title="see questions tagged &#39;capinfos&#39;">capinfos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '11, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/689335f2a74e2def3648f713b254e379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Israel%20Fonseca&#39;s gravatar image" /><p><span>Israel Fonseca</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Israel Fonseca has no accepted answers">0%</span></p></div></div><div id="comments-container-4086" class="comments-container"></div><div id="comment-tools-4086" class="comment-tools"></div><div class="clear"></div><div id="comment-4086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4087"></span>

<div id="answer-container-4087" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4087-score" class="post-score" title="current number of votes">3</div><span id="post-4087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> can do the trick:<br />
Here are some examples:<br />
</p><pre><code>$ tshark -r http.pcap -q -z conv,eth -z conv,ip -z conv,tcp
TCP Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |
192.168.108.128:1047 &lt;-&gt; 64.186.152.93:80           9      7834       7      1358      16      9192
192.168.108.128:1048 &lt;-&gt; 64.186.152.93:80           4      1868       4       623       8      2491
================================================================================
================================================================================
IPv4 Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |
192.168.108.128      &lt;-&gt; 64.186.152.93             13      9702      11      1981      24     11683
192.168.108.128      &lt;-&gt; 192.168.108.2              1       202       1        73       2       275
================================================================================
================================================================================
Ethernet Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |
00:0c:29:61:82:89    &lt;-&gt; 00:50:56:ee:98:59         14      9904      13      2096      27     12000
00:50:56:ee:98:59    &lt;-&gt; ff:ff:ff:ff:ff:ff          0         0       1        60       1        60
================================================================================
================================================================================
$ tshark -r http.pcap -q -z conv,eth,eth.addr==00:0c:29:61:82:89 -z conv,ip,ip.addr==192.168.108.2 -z conv,tcp,ip.addr==64.186.152.93
================================================================================
TCP Conversations
Filter:ip.addr==64.186.152.93
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |
192.168.108.128:1047 &lt;-&gt; 64.186.152.93:80           9      7834       7      1358      16      9192
192.168.108.128:1048 &lt;-&gt; 64.186.152.93:80           4      1868       4       623       8      2491
================================================================================
================================================================================
IPv4 Conversations
Filter:ip.addr==192.168.108.2
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |
192.168.108.128      &lt;-&gt; 192.168.108.2              1       202       1        73       2       275
================================================================================
================================================================================
Ethernet Conversations
Filter:eth.addr==00:0c:29:61:82:89
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |
00:0c:29:61:82:89    &lt;-&gt; 00:50:56:ee:98:59         14      9904      13      2096      27     12000
================================================================================
$ tshark -r update.pcap -qz io,stat,60,&quot;COUNT(frame.cap_len)frame.cap_len&quot;,&quot;MIN(frame.cap_len)frame.cap_len&quot;,&quot;MAX(frame.cap_len)frame.cap_len&quot;,&quot;AVG(frame.cap_len)frame.cap_len&quot;
===================================================================
IO Statistics
Interval: 60.000 secs
Column #0: COUNT(frame.cap_len)frame.cap_len
Column #1: MIN(frame.cap_len)frame.cap_len
Column #2: MAX(frame.cap_len)frame.cap_len
Column #3: AVG(frame.cap_len)frame.cap_len
                |   Column #0    |   Column #1    |   Column #2    |   Column #3
Time            |          COUNT |            MIN |            MAX |            AVG
000.000-060.000               547               42             1514              829
060.000-120.000             32857               42             1514              998
120.000-180.000             39550               42             1514              997
180.000-240.000                30               42              403              211
240.000-300.000                17               60              403              312
300.000-360.000                22               60              403              265
360.000-420.000                41               46              403              263
===================================================================</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '11, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 May '11, 06:47</strong> </span></p></div></div><div id="comments-container-4087" class="comments-container"></div><div id="comment-tools-4087" class="comment-tools"></div><div class="clear"></div><div id="comment-4087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6602"></span>

<div id="answer-container-6602" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6602-score" class="post-score" title="current number of votes">0</div><span id="post-6602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi there,</p><p>I'm using the -z conv,ip option and I have a doubt. Tshark show as columns "frames" and "bytes" for each endpoint in the conversation, the question is:</p><p>when tshark says "bytes", are RX o TX ? It's looks like Tshark show us the RX byte. Is there any switch to choose TX field specifically?</p><p>Thanks!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '11, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/f5a60c14bfbe79406dc402d1cd539469?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Julian%20Diaz&#39;s gravatar image" /><p><span>Julian Diaz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Julian Diaz has no accepted answers">0%</span></p></div></div><div id="comments-container-6602" class="comments-container"></div><div id="comment-tools-6602" class="comment-tools"></div><div class="clear"></div><div id="comment-6602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6605"></span>

<div id="answer-container-6605" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6605-score" class="post-score" title="current number of votes">0</div><span id="post-6605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark man-page</a>:<br />
"The table is presented with one line for each conversation and displays the number of packets/bytes in each direction as well as the total number of packets/bytes. The table is sorted according to the total number of bytes."<br />
</p><pre><code>$ tshark -r test.pcap -qz conv,ip

IPv4 Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                             |       &lt;-      | |       -&gt;      | |     Total     |
                             | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '11, 21:43</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-6605" class="comments-container"></div><div id="comment-tools-6605" class="comment-tools"></div><div class="clear"></div><div id="comment-6605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

