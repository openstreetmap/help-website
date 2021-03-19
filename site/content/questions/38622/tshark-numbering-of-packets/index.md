+++
type = "question"
title = "Tshark -numbering of packets"
description = '''When I run tshark in this way in Ubuntu then I do not get the packet numbers: tshark -Nt -f &quot;host abc.com&quot;   tshark: Lua: Error during loading: [string &quot;/usr/share/wireshark/init.lua&quot;]:45: dofile has been disabled Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous. Capturing on eth0  0...'''
date = "2014-12-18T06:35:00Z"
lastmod = "2014-12-18T06:35:00Z"
weight = 38622
keywords = [ "tshark" ]
aliases = [ "/questions/38622" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark -numbering of packets](/questions/38622/tshark-numbering-of-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38622-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I run tshark in this way in Ubuntu then I do not get the packet numbers:</p><pre><code>tshark -Nt -f &quot;host abc.com&quot;</code></pre><blockquote></blockquote><pre><code>tshark: Lua: Error during loading:
[string &quot;/usr/share/wireshark/init.lua&quot;]:45: dofile has been disabled
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Capturing on eth0

0.000000    10.0.2.15 -&gt; 92.223.112.104 TCP 74 49224 &gt; https [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=463966 TSecr=0 WS=128
0.019933 92.223.112.104 -&gt; 10.0.2.15    TCP 60 https &gt; 49224 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460
0.020102    10.0.2.15 -&gt; 92.223.112.104 TCP 54 49224 &gt; https [ACK] Seq=1 Ack=1 Win=14600 Len=0</code></pre><p>but in Windows I would get</p><pre><code>1 0.000000    10.0.2.15 -&gt; 92.223.112.104 TCP 74 49224 &gt; https [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=463966 TSecr=0 WS=128
2 0.019933 92.223.112.104 -&gt; 10.0.2.15    TCP 60 https &gt; 49224 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460
3 0.020102    10.0.2.15 -&gt; 92.223.112.104 TCP 54 49224 &gt; https [ACK] Seq=1 Ack=1 Win=14600 Len=0</code></pre><p>how can I make the numbering of packet in Ubuntu?</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '14, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/356961d480eb308238931511a398a65f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="regexmix&#39;s gravatar image" /><p>regexmix<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="regexmix has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Dec '14, 06:40</p></div></div><div id="comments-container-38622" class="comments-container"><span id="38624"></span><div id="comment-38624" class="comment"><div id="post-38624-score" class="comment-score"></div><div class="comment-text"><p>I would gess that the version of Wireshark on Ubuntu is older and don't have the feature. What versions do you have?</p></div><div id="comment-38624-info" class="comment-info"><span class="comment-age">(18 Dec '14, 07:45)</span> Anders ♦</div></div><span id="38627"></span><div id="comment-38627" class="comment"><div id="post-38627-score" class="comment-score"></div><div class="comment-text"><p>TShark 1.6.7</p><p>wireshark 1.6.7</p><p>Ubuntu 12.04.5 LTS</p></div><div id="comment-38627-info" class="comment-info"><span class="comment-age">(18 Dec '14, 07:57)</span> regexmix</div></div></div><div id="comment-tools-38622" class="comment-tools"></div><div class="clear"></div><div id="comment-38622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

