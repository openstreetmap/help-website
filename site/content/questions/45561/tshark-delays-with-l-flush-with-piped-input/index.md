+++
type = "question"
title = "tshark delays with -l flush with piped input"
description = '''Hi, I&#x27;m using tshark with a &quot;special feeding application&quot; as described on https://wiki.wireshark.org/CaptureSetup/Pipes I am seeing significant delays in packets being displayed from tshark. I can reproduce this using a pipe to stdin from tcpdump: sudo tcpdump -i en0 -w - -U icmp | tshark -r - -l  w...'''
date = "2015-09-01T04:02:00Z"
lastmod = "2015-09-01T04:02:00Z"
weight = 45561
keywords = [ "buffer", "tshark", "stdout" ]
aliases = [ "/questions/45561" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark delays with -l flush with piped input](/questions/45561/tshark-delays-with-l-flush-with-piped-input)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45561-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using tshark with a "special feeding application" as described on <a href="https://wiki.wireshark.org/CaptureSetup/Pipes">https://wiki.wireshark.org/CaptureSetup/Pipes</a> I am seeing significant delays in packets being displayed from tshark.</p><p>I can reproduce this using a pipe to stdin from tcpdump:</p><pre><code>sudo tcpdump -i en0 -w - -U icmp | tshark -r - -l</code></pre><p>where my pings are not displayed packet-by-packet, but instead in batches, as can be seen in the following gist <a href="https://gist.github.com/sk2/b0df982766eec12c40d2">https://gist.github.com/sk2/b0df982766eec12c40d2</a></p><pre><code>Sep 01 20:08:03   1 10:37:47.179530 192.168.178.20 -&gt; 192.168.178.1 ICMP 70 Destination unreachable (Port unreachable)
Sep 01 20:08:03   2 10:37:47.530679 192.168.178.20 -&gt; 150.101.140.197 ICMP 98 Echo (ping) request
Sep 01 20:08:03   3 10:37:47.576863 150.101.140.197 -&gt; 192.168.178.20 ICMP 98 Echo (ping) reply    
Sep 01 20:08:03   4 10:37:48.531085 192.168.178.20 -&gt; 150.101.140.197 ICMP 98 Echo (ping) request
Sep 01 20:08:03   5 10:37:48.561909 150.101.140.197 -&gt; 192.168.178.20 ICMP 98 Echo (ping) reply    
Sep 01 20:08:03   6 10:37:49.535383 192.168.178.20 -&gt; 150.101.140.197 ICMP 98 Echo (ping) request
Sep 01 20:08:03   7 10:37:49.571962 150.101.140.197 -&gt; 192.168.178.20 ICMP 98 Echo (ping) reply    
Sep 01 20:08:03   8 10:37:50.540535 192.168.178.20 -&gt; 150.101.140.197 ICMP 98 Echo (ping) request</code></pre><p>if I change from tshark to Wireshark, then the packets display as they are received from tcpdump</p><pre><code>sudo tcpdump -i en0 -w - -U icmp | wireshark -k -i -</code></pre><p>Do I need any additional options to the <code>-l</code> flag to flush the output from tshark? I am using <code>TShark 1.12.6 (v1.12.6-0-gee1fce6 from master-1.12)</code> on OS X Yosemite.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">buffer tshark stdout</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '15, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/cd77b2ab2e12ba051d78fddd7e2e3e52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eskaytwo&#39;s gravatar image" /><p>eskaytwo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eskaytwo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Sep '15, 17:12</p></div></div><div id="comments-container-45561" class="comments-container"></div><div id="comment-tools-45561" class="comment-tools"></div><div class="clear"></div><div id="comment-45561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

