+++
type = "question"
title = "Tshark Command Line"
description = '''Hello, Can anyone can help me with a command line in Tshark that will provide me the same information as if I go to Wireshark &amp;gt; Statistics &amp;gt; Conversations &amp;gt; TCP Tab with NO Name Resolution? I need to write lots of appcapture files in text with this specific format. I&#x27;m trying to write a BAT...'''
date = "2011-08-26T10:51:00Z"
lastmod = "2011-08-26T13:15:00Z"
weight = 5889
keywords = [ "tshark" ]
aliases = [ "/questions/5889" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark Command Line](/questions/5889/tshark-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5889-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Can anyone can help me with a command line in Tshark that will provide me the same information as if I go to <strong>Wireshark &gt; Statistics &gt; Conversations &gt; TCP</strong> Tab with NO Name Resolution?</p><p>I need to write lots of appcapture files in text with this specific format. I'm trying to write a BAT file that will convert hundreds of files at once.</p><p>This is what I have so far:</p><pre><code>tshark -nn -r INPUT_FILE.appcapture -T fields -E separator=; -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport &gt;OUTPUT_FILE.txt</code></pre><p>Thanks in advance,</p><p>Andre B. Bueno.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '11, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/2a0f2ff9cb09225c5e4db93e3e112207?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AndreBueno&#39;s gravatar image" /><p>AndreBueno<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AndreBueno has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Aug '11, 13:59</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5889" class="comments-container"></div><div id="comment-tools-5889" class="comment-tools"></div><div class="clear"></div><div id="comment-5889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5891"></span>

<div id="answer-container-5891" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5891-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>How about: <code>tshark -r INPUT_FILE -z conv,tcp -q -n</code></p><p>That returns output like this:</p><pre><code>================================================================================
TCP Conversations
Filter:&lt;No Filter&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |
192.168.69.217:57900 &lt;-&gt; 192.168.69.240:9220       10       673       7       441      17      1114
192.168.69.217:57899 &lt;-&gt; 192.168.69.240:9220       10       673       7       441      17      1114
192.168.69.217:57898 &lt;-&gt; 192.168.69.240:9220       10       673       7       441      17      1114
192.168.69.217:57901 &lt;-&gt; 209.85.227.147:80          2       126       3      1556       5      1682
192.168.69.217:57854 &lt;-&gt; 209.85.227.147:80          1        60       2       108       3       168
================================================================================</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '11, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5891" class="comments-container"><span id="5894"></span><div id="comment-5894" class="comment"><div id="post-5894-score" class="comment-score"></div><div class="comment-text"><p>Hi Thanks for the answer...I need to get only TCP conversations but I need also this specific format:</p><p>Address A,Port A,Address B,Port B,Packets,Bytes,Packets A-&gt;B,Bytes A-&gt;B,Packets A&lt;-B,Bytes A&lt;-B,Rel Start,Duration,bps A-&gt;B,bps A&lt;-B.</p><p>any thoughts?</p></div><div id="comment-5894-info" class="comment-info"><span class="comment-age">(26 Aug '11, 15:31)</span> AndreBueno</div></div></div><div id="comment-tools-5891" class="comment-tools"></div><div class="clear"></div><div id="comment-5891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

