+++
type = "question"
title = "Tshark: multiple packets on the same line"
description = '''I noticed that when I filter high speed traffic with tshark from a tcpdump capture file, it will print multiple packets on the same line. For a lot of fields instead of a single value there are multiple values separated by commas.  10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10...'''
date = "2014-12-23T02:36:00Z"
lastmod = "2014-12-23T02:36:00Z"
weight = 38678
keywords = [ "tshark" ]
aliases = [ "/questions/38678" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark: multiple packets on the same line](/questions/38678/tshark-multiple-packets-on-the-same-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38678-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I noticed that when I filter high speed traffic with tshark from a tcpdump capture file, it will print multiple packets on the same line. For a lot of fields instead of a single value there are multiple values separated by commas.</p><pre><code>10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10     10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16,10.0.0.16 101.7.150.218,101.7.150.244,101.7.151.14,101.7.151.40,101.7.151.66,101.7.151.92,101.7.151.118,101.7.151.144,101.7.151.170,101.7.151.196,101.7.151.222,101.7.151.248,101.7.152.18,101.7.152.44,101.7.152.70,101.7.152.96,101.7.152.122,101.7.152.148,101.7.152.174,101.7.152.200,101.7.152.226,101.7.152.252,101.7.153.22,101.7.153.48           192.168.107.10  192.168.107.12  1419291086.335348000</code></pre><p>where every field is separated by one tab.</p><p>This data representation is not a big deal since every field is an array and the information about one specific packet can be found by looking at the same index.</p><p>Please could you explain why does this happen? Does this mean that the computer is not fast enough and the packets are queued in network interface?</p><p>Thank you.</p><p><strong>Edit:</strong></p><p>OS: ubuntu 14.04</p><p>Commnad: <code>sudo tshark -r tmp_capture.pcapng -R "of10.packet_in.type or of10.flow_add.type" -Tfields -e of10.packet_in.type -e of10.flow_add.type -e arp.src.proto_ipv4 -e arp.dst.proto_ipv4 -e of10.match_v1.ipv4_src -e of10.match_v1.ipv4_dst -e ip.src -e ip.dst -e frame.time_epoch</code></p><p>TShark 1.10.6 (v1.10.6 from master-1.10)</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '14, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/1749558d666c39b93beb8b2e3678d64a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skywalker&#39;s gravatar image" /><p>skywalker<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skywalker has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Dec '14, 04:04</p></div></div><div id="comments-container-38678" class="comments-container"><span id="38679"></span><div id="comment-38679" class="comment"><div id="post-38679-score" class="comment-score"></div><div class="comment-text"><p>what is your</p><ul><li>OS and OS version</li><li>tshark version</li><li>tshark commandline</li></ul></div><div id="comment-38679-info" class="comment-info"><span class="comment-age">(23 Dec '14, 03:22)</span> Kurt Knochner ♦</div></div><span id="38683"></span><div id="comment-38683" class="comment"><div id="post-38683-score" class="comment-score"></div><div class="comment-text"><p>I have just updated the question.</p></div><div id="comment-38683-info" class="comment-info"><span class="comment-age">(23 Dec '14, 04:08)</span> skywalker</div></div></div><div id="comment-tools-38678" class="comment-tools"></div><div class="clear"></div><div id="comment-38678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

