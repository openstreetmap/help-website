+++
type = "question"
title = "BPF for protocol exclude list"
description = '''I want to specify filter to exclude list of protocols (arp, tcp) i.e. filter is [not(arp or tcp)].  Packets are mixed from untagged vlan and tagged vlan. How can I specify it since filter:(not arp and not tcp) doesnt work as it works only on untagged vlan packets.  I am using libpcap and I want to f...'''
date = "2015-07-05T23:36:00Z"
lastmod = "2015-07-05T23:36:00Z"
weight = 43879
keywords = [ "filter", "vlan", "protocol", "libpcap", "bpf" ]
aliases = [ "/questions/43879" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [BPF for protocol exclude list](/questions/43879/bpf-for-protocol-exclude-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43879-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to specify filter to exclude list of protocols (arp, tcp) i.e. filter is [not(arp or tcp)].</p><p>Packets are mixed from untagged vlan and tagged vlan. How can I specify it since filter:(not arp and not tcp) doesnt work as it works only on untagged vlan packets.</p><p>I am using libpcap and I want to filter both tagged and untagged packets.</p><p>For example, exp: &lt;filter&gt; or (vlan or &lt;filter&gt;) works for "arp or tcp" But same expression dont work if filter : not(arp or tcp)</p></div><div id="question-tags" class="tags-container tags">filter vlan protocol libpcap bpf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '15, 23:36</strong></p><img src="https://secure.gravatar.com/avatar/b3b6ec2ac3eff45ac2ac23dc6f45737f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tweetstrack&#39;s gravatar image" /><p>tweetstrack<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tweetstrack has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jul '15, 23:37</p></div></div><div id="comments-container-43879" class="comments-container"></div><div id="comment-tools-43879" class="comment-tools"></div><div class="clear"></div><div id="comment-43879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

