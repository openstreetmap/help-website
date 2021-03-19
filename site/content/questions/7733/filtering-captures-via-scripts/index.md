+++
type = "question"
title = "Filtering Captures via Scripts"
description = '''I&#x27;d like to write a script (I&#x27;m on Windows) to open a WS capture, apply filters to it and write the output to a file.  I can get the correct information out of Wireshark by applying the filters there. How/what should I write a script in to run the file through WS, apply the filters, and then dump th...'''
date = "2011-12-01T14:16:00Z"
lastmod = "2011-12-06T01:51:00Z"
weight = 7733
keywords = [ "script" ]
aliases = [ "/questions/7733" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering Captures via Scripts](/questions/7733/filtering-captures-via-scripts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7733-score" class="post-score" title="current number of votes">0</div><span id="post-7733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to write a script (I'm on Windows) to open a WS capture, apply filters to it and write the output to a file.</p><p>I can get the correct information out of Wireshark by applying the filters there. How/what should I write a script in to run the file through WS, apply the filters, and then dump the output to a file?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '11, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/586a0ae7ec91cdc42c731a200a57960f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sideslope&#39;s gravatar image" /><p><span>sideslope</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sideslope has no accepted answers">0%</span></p></div></div><div id="comments-container-7733" class="comments-container"></div><div id="comment-tools-7733" class="comment-tools"></div><div class="clear"></div><div id="comment-7733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7734"></span>

<div id="answer-container-7734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7734-score" class="post-score" title="current number of votes">1</div><span id="post-7734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You just call up tshark.exe, which is the command line version of Wireshark, tell it to read the file, filter for whatever display filter you like, and write the file back out again. Here's an example, reading the file "sample.pcap", filter it for ARP packets and write it to "result.pcap":</p><p><strong>tshark -r "sample.pcap" -R "arp" -w "result.pcap"</strong></p><p>tshark.exe can be found in the Wireshark installation directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '11, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7734" class="comments-container"><span id="7778"></span><div id="comment-7778" class="comment"><div id="post-7778-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper! This does what I need. Is there a filter list of paramers somewhere? I need to filter on TCP conversation + Get requests. I see how to do the gets, but I don't see how to filter on conversations too.</p><p>Thanks again!</p></div><div id="comment-7778-info" class="comment-info"><span class="comment-age">(05 Dec '11, 13:43)</span> <span class="comment-user userinfo">sideslope</span></div></div><span id="7793"></span><div id="comment-7793" class="comment"><div id="post-7793-score" class="comment-score"></div><div class="comment-text"><p>If I need to filter a conversation I usually use the popup menu of the packet list and select "Conversation Filter" -&gt; "TCP", which will apply a display filter the sockets of sender and receiver. It can be a bit annoying to filter on conversations by hand, so maybe you can take a look at the tcp stream index and filter on that without having to look for packets of each conversation.</p></div><div id="comment-7793-info" class="comment-info"><span class="comment-age">(06 Dec '11, 01:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-7734" class="comment-tools"></div><div class="clear"></div><div id="comment-7734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7788"></span>

<div id="answer-container-7788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7788-score" class="post-score" title="current number of votes">0</div><span id="post-7788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use TShark to get an overview of the TCP Conversations:</p><pre><code>$ tshark -r Clmt_04.pcap -q -z conv,tcp
===============================================================================
TCP Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                           | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |</code></pre><p>192.168.1.2:1386 &lt;-&gt; 93.184.220.20:80 111 142403 57 3618 168 146021 192.168.1.2:1367 &lt;-&gt; 93.184.220.20:80 54 73813 30 2061 84 75874 192.168.1.2:1344 &lt;-&gt; 204.9.178.11:80 43 57501 29 3622 72 61123</p></pre><p>Some examples:</p><pre><code>tshark -r Clmt_04.pcap -R &quot;(ip.addr==192.168.1.2 &amp;&amp; tcp.port==1386 &amp;&amp; ip.addr==93.184.220.20 &amp;&amp; tcp.port==80) || http.request&quot;
tshark -r Clmt_04.pcap -R &quot;(ip.addr==192.168.1.2 &amp;&amp; tcp.port==1386 &amp;&amp; ip.addr==93.184.220.20 &amp;&amp; tcp.port==80) &amp;&amp; http.request&quot;  -w output1.pcap
tshark -r Clmt_04.pcap -R&quot;(ip.addr==192.168.1.2 &amp;&amp; tcp.port==1367 &amp;&amp; ip.addr==93.184.220.20 &amp;&amp; tcp.port==80) || (ip.addr==192.168.1.2 &amp;&amp; tcp.port==1344 &amp;&amp; ip.addr==204.9.178.11 &amp;&amp; tcp.port==80)&quot;
tshark -r Clmt_04.pcap -R&quot;((ip.addr==192.168.1.2 &amp;&amp; tcp.port==1367 &amp;&amp; ip.addr==93.184.220.20 &amp;&amp; tcp.port==80) || (ip.addr==192.168.1.2 &amp;&amp; tcp.port==1344 &amp;&amp; ip.addr==204.9.178.11 &amp;&amp; tcp.port==80)) &amp;&amp; http.request&quot;  -w output4.pcap</code></pre><p>You can find more information in the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a> man-page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '11, 21:34</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '11, 01:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7788" class="comments-container"></div><div id="comment-tools-7788" class="comment-tools"></div><div class="clear"></div><div id="comment-7788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

