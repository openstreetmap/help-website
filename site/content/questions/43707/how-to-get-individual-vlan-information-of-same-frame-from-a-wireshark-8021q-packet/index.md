+++
type = "question"
title = "How to get individual vlan information of same frame from a Wireshark 802.1q packet"
description = '''Hi Team, I have a wireshark packet where two vlan headers are there. I would like to fetch individual vlan information using tshark on Linux environment, but seems not working properly. tshark -Tfields -e vlan.priority frame.number==2 -r ft3088_1_ipv6_static_negative_propagation_port2_1_capture.pcap...'''
date = "2015-06-30T00:20:00Z"
lastmod = "2015-06-30T02:40:00Z"
weight = 43707
keywords = [ "tshark", "linux" ]
aliases = [ "/questions/43707" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to get individual vlan information of same frame from a Wireshark 802.1q packet](/questions/43707/how-to-get-individual-vlan-information-of-same-frame-from-a-wireshark-8021q-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43707-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Team,</p><p>I have a wireshark packet where two vlan headers are there. I would like to fetch individual vlan information using tshark on Linux environment, but seems not working properly.</p><pre><code>tshark -Tfields -e vlan.priority frame.number==2 -r ft3088_1_ipv6_static_negative_propagation_port2_1_capture.pcap</code></pre><p>Could suggest how to do this . Thanks in advance. The pcap file can be downloaded here</p><p><a href="https://drive.google.com/file/d/0BwwI_HENAPomNXFPTW9XakcxT2c/view?usp=sharing">link text</a></p></div><div id="question-tags" class="tags-container tags">tshark linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '15, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/fbfa082235ab499c4eb41ae3d8f6fe36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udaya&#39;s gravatar image" /><p>udaya<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udaya has one accepted answer">100%</span></p></div></div><div id="comments-container-43707" class="comments-container"></div><div id="comment-tools-43707" class="comment-tools"></div><div class="clear"></div><div id="comment-43707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43711"></span>

<div id="answer-container-43711" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43711-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi</p><p>try below syntax</p><p><code>tshark.exe -T fields -e vlan.priority -Y frame.number==2 -r ft3088_1_ipv6_static_negative_propagation_port2_1_capture.pcap</code></p><p>6,0</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/a9b2fb3aab247cf7e64142618d459f73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scheehan&#39;s gravatar image" /><p>scheehan<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scheehan has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jun '15, 02:52</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-43711" class="comments-container"><span id="43726"></span><div id="comment-43726" class="comment"><div id="post-43726-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I tried the same but NOT working. I am with following tshark details. Is it related to version ..</p><pre><code>    tshark: invalid option -- Y
TShark 1.0.8
Dump and analyze network traffic.
See http://www.wireshark.org for more information.</code></pre></div><div id="comment-43726-info" class="comment-info"><span class="comment-age">(30 Jun '15, 04:48)</span> udaya</div></div><span id="43727"></span><div id="comment-43727" class="comment"><div id="post-43727-score" class="comment-score"></div><div class="comment-text"><p>Can you not upgrade your version of tshark, 1.0.8 is pre-historic?</p></div><div id="comment-43727-info" class="comment-info"><span class="comment-age">(30 Jun '15, 04:52)</span> grahamb ♦</div></div><span id="43730"></span><div id="comment-43730" class="comment"><div id="post-43730-score" class="comment-score">1</div><div class="comment-text"><p>Or try substituting <code>-R</code> for <code>-Y</code>.</p></div><div id="comment-43730-info" class="comment-info"><span class="comment-age">(30 Jun '15, 06:46)</span> cmaynard ♦♦</div></div><span id="43764"></span><div id="comment-43764" class="comment"><div id="post-43764-score" class="comment-score"></div><div class="comment-text"><p>Thanks I installed 1.6.7 and tried with -R worked perfect !!!</p><p>:)</p></div><div id="comment-43764-info" class="comment-info"><span class="comment-age">(30 Jun '15, 21:47)</span> udaya</div></div></div><div id="comment-tools-43711" class="comment-tools"></div><div class="clear"></div><div id="comment-43711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

