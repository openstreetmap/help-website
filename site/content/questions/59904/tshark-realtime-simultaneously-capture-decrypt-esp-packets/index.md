+++
type = "question"
title = "tshark - realtime simultaneously capture &amp; decrypt ESP packets"
description = '''Hello there, I&#x27;m creating a C# program in which network traffic from Android device will be forwarded to my PC and be captured using tshark command line. This is how it works In the first CMD window adb shell &quot;tcpdump -i any -n -U -w - not port 1122 | nc -l 1122&quot;  In the second CMD window adb forwar...'''
date = "2017-03-07T19:18:00Z"
lastmod = "2017-03-07T19:18:00Z"
weight = 59904
keywords = [ "decryption", "tshark", "command-line", "real-time" ]
aliases = [ "/questions/59904" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark - realtime simultaneously capture & decrypt ESP packets](/questions/59904/tshark-realtime-simultaneously-capture-decrypt-esp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59904-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there,</p><p>I'm creating a C# program in which network traffic from Android device will be forwarded to my PC and be captured using tshark command line. This is how it works</p><p>In the first CMD window</p><pre><code>adb shell &quot;tcpdump -i any -n -U -w - not port 1122 | nc -l 1122&quot;</code></pre><p>In the second CMD window</p><pre><code>adb forward tcp:1122 tcp:1122 &amp;&amp; nc 127.0.0.1 1122  | tshark -i - -Y &quot;sip||esp&quot; -d tcp.port==&quot;5000-65535&quot;,sip -d udp.port==&quot;5000-65535&quot;,sip -T text -l -O &quot;sip,esp&quot;</code></pre><p>This runs perfectly showing all SIP messages from/to my device in case of no ESP encryption.</p><p>But in case ESP encrypted, I can only see 2 SIP packets with full contents (i.e. REGISTER &amp; 401 Unauthorized) when encryption is not enabled. After that, all packets are ESP encrypted data.</p><p>When IPsec is enabled, I can get Encrypt Key from my device and append to esp_sa file. But tshark seems only read this file at first time running. So, the newly added key is not being used to decode during capturing.</p><p>I would like to ask if anyone knows how to work around in this case.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">decryption tshark command-line real-time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '17, 19:18</strong></p><img src="https://secure.gravatar.com/avatar/a040c26be3c4ca664c92358f3799ae81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viet-Anh%20Dinh&#39;s gravatar image" /><p>Viet-Anh Dinh<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viet-Anh Dinh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Mar '17, 19:22</p></div></div><div id="comments-container-59904" class="comments-container"></div><div id="comment-tools-59904" class="comment-tools"></div><div class="clear"></div><div id="comment-59904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

