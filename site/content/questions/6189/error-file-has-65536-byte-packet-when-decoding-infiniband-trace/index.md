+++
type = "question"
title = "Error File has 65536-byte packet when decoding Infiniband trace"
description = '''Hello all, With Wireshark Version 1.6.1 (SVN Rev 38096 from /trunk-1.6), I get the error &quot;File has 65536-bye packet, bigger than maximum of of 65535&quot;. mtu size is 65520 which is correct accoding to the Mellanox User Guide. DEVICE=ib0 HWADDR= IPADDR=10.3.1.1 NETMASK=255.255.0.0 BOOTPROTO=static ONBOO...'''
date = "2011-09-07T08:30:00Z"
lastmod = "2011-09-07T08:30:00Z"
weight = 6189
keywords = [ "infiniband" ]
aliases = [ "/questions/6189" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error File has 65536-byte packet when decoding Infiniband trace](/questions/6189/error-file-has-65536-byte-packet-when-decoding-infiniband-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6189-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all, With Wireshark Version 1.6.1 (SVN Rev 38096 from /trunk-1.6), I get the error "File has 65536-bye packet, bigger than maximum of of 65535".</p><p>mtu size is 65520 which is correct accoding to the Mellanox User Guide. DEVICE=ib0 HWADDR= IPADDR=10.3.1.1 NETMASK=255.255.0.0 BOOTPROTO=static ONBOOT=yes MTU=65520</p><p>Would someone know why the error is occuring and if there is any solution in Wireshark to overcome this problem.</p><p>Thanks, Paul Savoie</p></div><div id="question-tags" class="tags-container tags">infiniband</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '11, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/e09afe6c2b07de6793d0a3d30660b6ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pauljsavoie&#39;s gravatar image" /><p>pauljsavoie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pauljsavoie has no accepted answers">0%</span></p></div></div><div id="comments-container-6189" class="comments-container"><span id="6190"></span><div id="comment-6190" class="comment"><div id="post-6190-score" class="comment-score"></div><div class="comment-text"><p>An often occurring reason for this error is that the capture file somehow is corrupted.</p><p>So: (just to start at the beginning and to get this out of the way): Was the capture file copied/transferred before being read by Wireshark ? (Also: how was the capture file created ?)</p></div><div id="comment-6190-info" class="comment-info"><span class="comment-age">(07 Sep '11, 09:10)</span> Bill Meier ♦♦</div></div><span id="6213"></span><div id="comment-6213" class="comment"><div id="post-6213-score" class="comment-score">1</div><div class="comment-text"><p>The MTU size isn't the raw link-layer packet size; with an MTU of 65520, if the link-layer header length is 16 bytes or more, that means that the packet length will really <em>be</em> 65536, in which case Wireshark should increase its maximum packet size (and libpcap needs to increase <em>its</em> maximum packet size, and tcpdump needs to increase its default snapshot length).</p><p>Wireshark <em>does</em> have to check for a too-large packet, as does libpcap, in order to avoid some denial-of-service attacks with bad capture files, but the limit may need to be increased.</p></div><div id="comment-6213-info" class="comment-info"><span class="comment-age">(08 Sep '11, 10:00)</span> Guy Harris ♦♦</div></div><span id="6239"></span><div id="comment-6239" class="comment"><div id="post-6239-score" class="comment-score"></div><div class="comment-text"><p>Hello Bill, We captured a new trace and took care to transfer the data as you suggested but the problem persisted.</p><p>Hello Guy, If your analysis is correct, are there config settings I can modify or Wireshark will needs to be modified?</p><p>I will check this site for the procedure to submit ane enhancemen request.</p><p>Thanks to you both for replying.</p><p>Cheers, Paul</p></div><div id="comment-6239-info" class="comment-info"><span class="comment-age">(09 Sep '11, 18:56)</span> pauljsavoie</div></div><span id="6240"></span><div id="comment-6240" class="comment"><div id="post-6240-score" class="comment-score"></div><div class="comment-text"><p>If, with Infiniband, you can get 65536-byte packets, then Wireshark (and libpcap and tcpdump) need to be modified. Submit the enhancement request (with one of the Infiniband capture files, if possible) as a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div id="comment-6240-info" class="comment-info"><span class="comment-age">(09 Sep '11, 22:55)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-6189" class="comment-tools"></div><div class="clear"></div><div id="comment-6189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

