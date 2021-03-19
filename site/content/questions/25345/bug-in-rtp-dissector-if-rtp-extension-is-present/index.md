+++
type = "question"
title = "Bug in RTP dissector if RTP extension is present"
description = '''It&#x27;s been a while this bug is present and it&#x27;s annoying as hell to explain everyone that it&#x27;s not our code produces malformed packets but whireshark has this bug. Basically, when RTP extension is present wireshark shows this: 43 17:14:58.142025 10.0.105.172 64.254.226.140 RTP PT=H264, SSRC=0xEDE1806...'''
date = "2013-09-29T17:38:00Z"
lastmod = "2013-09-29T23:15:00Z"
weight = 25345
keywords = [ "rtp" ]
aliases = [ "/questions/25345" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bug in RTP dissector if RTP extension is present](/questions/25345/bug-in-rtp-dissector-if-rtp-extension-is-present)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25345-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It's been a while this bug is present and it's annoying as hell to explain everyone that it's not our code produces malformed packets but whireshark has this bug.</p><p>Basically, when <a href="http://tools.ietf.org/html/rfc3550#section-5.3.1">RTP extension</a> is present wireshark shows this:</p><pre><code>43  17:14:58.142025 10.0.105.172    64.254.226.140  RTP PT=H264, SSRC=0xEDE18064, Seq=5, Time=0, Mark[Malformed Packet]</code></pre><p><a href="https://docs.google.com/file/d/0B5G49ZxwEWB6TThwUktxbHQ2Mk0/edit?usp=sharing">Here's sample pcap file with malformed RTP packet (#8)</a></p><p>Wireshark version: Version 1.10.2 (SVN Rev 51934 from /trunk-1.10) on Win2008</p><p>I suspect that it starts to parse RTP payload without advancing properly for extension header size, and, perhaps, it may have similar bug for CSRC fields (that's usually 0 in p2p calls)</p></div><div id="question-tags" class="tags-container tags">rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '13, 17:38</strong></p><img src="https://secure.gravatar.com/avatar/85a49cd89084e6512dee0f140e86d5b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="psp80&#39;s gravatar image" /><p>psp80<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="psp80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Sep '13, 21:11</p></div></div><div id="comments-container-25345" class="comments-container"><span id="25346"></span><div id="comment-25346" class="comment"><div id="post-25346-score" class="comment-score"></div><div class="comment-text"><p>can you please post a sample capture file (google docs, dropbox, cloudshark)?</p><p>And what is your OS and Wireshark version?</p></div><div id="comment-25346-info" class="comment-info"><span class="comment-age">(29 Sep '13, 17:42)</span> Kurt Knochner ♦</div></div><span id="25348"></span><div id="comment-25348" class="comment"><div id="post-25348-score" class="comment-score"></div><div class="comment-text"><p>sample pcap and wireshark version info added.</p></div><div id="comment-25348-info" class="comment-info"><span class="comment-age">(29 Sep '13, 17:59)</span> psp80</div></div><span id="25351"></span><div id="comment-25351" class="comment"><div id="post-25351-score" class="comment-score"></div><div class="comment-text"><p>O.K. looks 'kind of odd'. Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> (please attach the sample capture file).</p></div><div id="comment-25351-info" class="comment-info"><span class="comment-age">(29 Sep '13, 19:02)</span> Kurt Knochner ♦</div></div><span id="25355"></span><div id="comment-25355" class="comment"><div id="post-25355-score" class="comment-score"></div><div class="comment-text"><p>Added bug report: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9204">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9204</a></p></div><div id="comment-25355-info" class="comment-info"><span class="comment-age">(29 Sep '13, 21:29)</span> psp80</div></div></div><div id="comment-tools-25345" class="comment-tools"></div><div class="clear"></div><div id="comment-25345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25356"></span>

<div id="answer-container-25356" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25356-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here's the bug fix: <a href="http://pastie.org/8366148">http://pastie.org/8366148</a></p><p>I attached this bugfix to the bug report. By the way, if you check the pcap file, it uses our extension (it's standard now):</p><pre><code>a=extmap:1 urn:3gpp:video-orientation</code></pre><p>How do I teach wireshark to understand that one-byte RFC 5285 header with id#1 is 3gpp:video-orientation (as specified in sdp) and properly interpret the data of that header according to 3gpp:video-orientation?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '13, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/85a49cd89084e6512dee0f140e86d5b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="psp80&#39;s gravatar image" /><p>psp80<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="psp80 has no accepted answers">0%</span></p></div></div><div id="comments-container-25356" class="comments-container"></div><div id="comment-tools-25356" class="comment-tools"></div><div class="clear"></div><div id="comment-25356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

