+++
type = "question"
title = "packet content difference in different versions"
description = '''Hi ALL I have captured packets (MPLS) with wire-shark and i am analyzing them. what i really do not understand: I opened the same file with 2 versions of Wireshark: the newest version does not showing me the details of the intern L2 packets (like VLAN/MAC addresses) but only mention &quot;PW control word...'''
date = "2016-08-29T23:31:00Z"
lastmod = "2016-08-30T03:03:00Z"
weight = 55189
keywords = [ "mpls" ]
aliases = [ "/questions/55189" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [packet content difference in different versions](/questions/55189/packet-content-difference-in-different-versions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55189-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ALL</p><p>I have captured packets (MPLS) with wire-shark and i am analyzing them. what i really do not understand: I opened the same file with 2 versions of Wireshark: the newest version does not showing me the details of the intern L2 packets (like VLAN/MAC addresses) but only mention "PW control word"</p><p><img src="https://osqa-ask.wireshark.org/upfiles/same-file-diff-versions.jpg" alt="alt text" /></p><p>the old version (1.0.5) shows me exactly those parameter i miss in the new version (VLAN, PRI,MAC...)</p><p>can someone explains me why there is a different and how can i set the new version to see these parameters ?</p><p>attached here picture of both version opened with the same file/same packet.</p><p>Thanks Eyal</p></div><div id="question-tags" class="tags-container tags">mpls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '16, 23:31</strong></p><img src="https://secure.gravatar.com/avatar/41b6ff54d99111e1b02f77cd7435f0fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eyalp&#39;s gravatar image" /><p>eyalp<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eyalp has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '16, 02:59</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-55189" class="comments-container"></div><div id="comment-tools-55189" class="comment-tools"></div><div class="clear"></div><div id="comment-55189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55194"></span>

<div id="answer-container-55194" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55194-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like the new version is actually telling the truth; when looking at the inner Ethernet MAC addresses they look correct in the new version and bogus in the old one. But lacking the actual capture file makes the determination difficult. If you can share the capture file (through CloudShark for instance) a more detailed analysis can be made.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '16, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55194" class="comments-container"><span id="55197"></span><div id="comment-55197" class="comment"><div id="post-55197-score" class="comment-score"></div><div class="comment-text"><p>HI Thanks for the answer. i assume that the new version supposed to present it more correctly, but still the important details are missing. I am generating these packets by using Ethernet test equipment, and I still do not understand why the new version present the PW control word but not the other L2 parameters (which exists in the packet).</p><p>I also do not understand from where the new version present the SA and the DA ? these are not coming from my systems. How can i attach the original file here ? i can see only posibility for picture. Best Regards Eyal``</p></div><div id="comment-55197-info" class="comment-info"><span class="comment-age">(30 Aug '16, 03:38)</span> eyalp</div></div><span id="55198"></span><div id="comment-55198" class="comment"><div id="post-55198-score" class="comment-score"></div><div class="comment-text"><p>There's no file sharing option here, so you have to use other means. The cloudshark.org site has a cloud based pcap viewer where you can upload your capture file to, for viewing and download. Then further analysis can be made.</p></div><div id="comment-55198-info" class="comment-info"><span class="comment-age">(30 Aug '16, 03:46)</span> Jaap ♦</div></div><span id="55220"></span><div id="comment-55220" class="comment"><div id="post-55220-score" class="comment-score"></div><div class="comment-text"><p>HI Thanks, i added the file to the cloudshark: <a href="https://www.cloudshark.org/captures/4d160d42aab0">https://www.cloudshark.org/captures/4d160d42aab0</a> the strange thing is, that if i look at the file i shared on the cloudshark (on-line view), i can see it perfect as it should be. There is the PW control word, but also the L2 parameters... real strange!</p><p>Thanks</p></div><div id="comment-55220-info" class="comment-info"><span class="comment-age">(30 Aug '16, 21:53)</span> eyalp</div></div><span id="55222"></span><div id="comment-55222" class="comment"><div id="post-55222-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid it is the "PW with or without CW, or no PW at all" heuristic which fails in the new version, possibly on your home-brewed MAC addresses with so many leading <code>00</code> bytes. To let your frames be dissected properly, you have to use <code>Decode as...</code> and say that MPLS label 4099 indicates that the MPLS payload contains just an Ethernet frame without any PW. The version running at Cloudshark does show a PW line in the dissection but no data matching to it in the packet bytes pane.</p></div><div id="comment-55222-info" class="comment-info"><span class="comment-age">(31 Aug '16, 01:06)</span> sindy</div></div></div><div id="comment-tools-55194" class="comment-tools"></div><div class="clear"></div><div id="comment-55194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

