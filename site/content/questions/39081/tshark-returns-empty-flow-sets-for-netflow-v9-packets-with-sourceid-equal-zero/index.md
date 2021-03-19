+++
type = "question"
title = "Tshark returns empty flow sets for NetFlow v9 packets with SourceId equal zero"
description = '''I am using Tshark to gather information on Flow Sets and found that if the field cflow.source_id == 0 then Tshark returns an empty field for all the fields selected. I would like to know the reason for this and if there is any workaround or fix available. I was running a command like this: tshark -r...'''
date = "2015-01-12T07:52:00Z"
lastmod = "2015-01-13T04:19:00Z"
weight = 39081
keywords = [ "sourceid", "netflow", "tshark" ]
aliases = [ "/questions/39081" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark returns empty flow sets for NetFlow v9 packets with SourceId equal zero](/questions/39081/tshark-returns-empty-flow-sets-for-netflow-v9-packets-with-sourceid-equal-zero)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39081-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Tshark to gather information on Flow Sets and found that if the field cflow.source_id == 0 then Tshark returns an empty field for all the fields selected.</p><p>I would like to know the reason for this and if there is any workaround or fix available.</p><p>I was running a command like this:</p><pre><code>tshark -r TWR.pcap -T fields -e frame.number -e cflow.octets -e cflow.packets -e cflow.inputint -e cflow.outputint -e cflow.srcaddr -e cflow.dstaddr -e cflow.protocol -e cflow.tos -e cflow.srcport -e cflow.dstport -e cflow.sampler_id -e cflow.flow_class -e cflow.nexthop -e cflow.dstmask -e cflow.srcmask -e cflow.tcpflags -e cflow.direction -E header=y -E separator=, -E quote=d -E occurrence=a -E aggregator=/s &gt; TWRWFrameNo.txt</code></pre><p>A sample of the output file is below.</p><pre><code>&quot;8284&quot;,,,,,,,,,,,,,,,,,
&quot;8285&quot;,,,,,,,,,,,,,,,,,
&quot;8286&quot;,,,,,,,,,,,,,,,,,
&quot;8287&quot;,&quot;1775 2582 168 522 3122 29575 724 500 475 1504 1250 136 73 276 136 319 276 276 276 52 336 56320 276 276 504 358 6350 276 52 276&quot;,&quot;12 4 2 5 19 211 4 5 2 6 9 2 1 3 2 2 3 3 3 1 2 704 3 3 4 4 44 3 1 3&quot;,&quot;9 5 3 8 9 2 3 5 8 8 8 8 5 3 8 5 3 3 3 8 8 3 3 3 3 3 8 3 3 3&quot;,&quot;2 8 8 3 2 8 8 8 5 3 5 5 9 9 3 8 8 9 8 2 3 8 8 8 9 9 2 8 9 8&quot;,&quot;10.166.4.105 10.5.34.50 10.5.32.103 10.167.0.16 10.166.4.105 10.0.29.30 10.2.133.90 10.0.29.253 10.164.117.204 10.174.22.120 10.172.5.170 10.164.132.126 10.5.32.101 10.2.133.90 10.164.132.125 10.4.18.198 10.2.133.90 10.2.133.90 10.2.133.90 10.152.85.7 10.192.136.1 10.3.100.254 10.2.133.90 10.2.133.90 10.2.133.90 10.2.130.6 10.166.17.62 10.2.133.90 10.2.133.81 10.2.133.90&quot;,&quot;172.16.2.221 10.172.29.99 10.173.208.60 10.0.29.253 172.16.2.221 10.168.19.12 10.172.29.155 10.167.0.16 10.5.34.50 10.20.3.11 10.2.133.90 10.1.164.100 10.164.116.112 10.142.68.161 10.2.133.82 10.164.64.7 10.171.206.103 10.174.4.112 10.139.17.141 10.0.29.251 10.4.18.198 10.188.5.37 10.171.4.87 10.134.12.152 10.160.25.111 10.160.20.101 10.2.133.90 10.168.26.82 10.164.116.54 10.138.4.172&quot;,&quot;6 6 17 6 6 17 6 6 6 6 6 6 17 6 6 17 6 6 6 6 17 17 6 6 6 6 6 6 6 6&quot;,&quot;0x00 0x00 0x00 0x68 0x00 0x00 0x00 0x60 0x28 0x68 0x28 0x28 0x00 0x00 0x28 0x00 0x00 0x00 0x00 0x28 0x28 0x00 0x00 0x00 0x00 0x00 0x28 0x00 0x00 0x00&quot;,&quot;61589 5061 137 24787 61592 1713 22295 1720 60840 65381 59631 57293 53 45252 49536 42211 45252 45252 45252 50233 161 22186 45252 45252 45252 45349 52168 45252 55950 45252&quot;,&quot;8080 50529 137 1720 8080 161 53344 24787 5061 22 45252 445 53422 54055 47771 161 56820 57234 50037 2000 34902 32534 53443 60375 65054 57614 29489 60956 52834 49401&quot;,&quot;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&quot;,&quot;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&quot;,&quot;10.20.1.30 10.4.248.130 10.4.248.130 10.20.1.2 10.20.1.30 10.4.248.130 10.4.248.130 10.4.248.130 10.20.1.54 10.20.1.2 10.20.1.54 10.20.1.54 10.4.248.138 10.4.248.138 10.20.1.2 10.4.248.130 10.4.248.130 10.4.248.138 10.4.248.130 10.20.1.30 10.20.1.2 10.4.248.130 10.4.248.130 10.4.248.130 10.4.248.138 10.4.248.138 10.20.1.30 10.4.248.130 10.4.248.138 10.4.248.130&quot;,&quot;24 24 24 24 24 24 24 32 24 28 24 24 24 24 24 32 24 24 24 24 24 24 24 24 24 24 24 24 24 24&quot;,&quot;24 24 24 32 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 32 16 24 24 24 24 24 24 24 24&quot;,&quot;0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00&quot;,&quot;0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&quot;</code></pre><p>--</p></div><div id="question-tags" class="tags-container tags">sourceid netflow tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '15, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/b0839e4d51be08759ab9a1087360714c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IanRees&#39;s gravatar image" /><p>IanRees<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IanRees has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jan '15, 08:06</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39081" class="comments-container"><span id="39082"></span><div id="comment-39082" class="comment"><div id="post-39082-score" class="comment-score"></div><div class="comment-text"><p>Ian, would it be possible to make available a capture showing this?</p></div><div id="comment-39082-info" class="comment-info"><span class="comment-age">(12 Jan '15, 08:13)</span> MartinM</div></div></div><div id="comment-tools-39081" class="comment-tools"></div><div class="clear"></div><div id="comment-39081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39088"></span>

<div id="answer-container-39088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39088-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If wireshark is showing the data, but tshark is not, you would need to use two-pass processing in tshark (option "-2"), as flow template record might come after the packet with the flow data, so tshark does not know yet how to interpret the flow data for the specific source ID.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '15, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '15, 04:21</p></div></div><div id="comments-container-39088" class="comments-container"></div><div id="comment-tools-39088" class="comment-tools"></div><div class="clear"></div><div id="comment-39088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

