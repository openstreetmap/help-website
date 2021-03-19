+++
type = "question"
title = "Microsoft RDP Security Settings"
description = '''I am looking at a packet capture from a Win 7 PC connecting to a Windows 2K8R2 server using RDP. Will the frame details show me the security levels that are negotiated. The host is set to use the High encryption level. Thanks for your help.'''
date = "2014-06-25T12:05:00Z"
lastmod = "2014-06-25T14:13:00Z"
weight = 34186
keywords = [ "security", "rdp" ]
aliases = [ "/questions/34186" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Microsoft RDP Security Settings](/questions/34186/microsoft-rdp-security-settings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34186-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking at a packet capture from a Win 7 PC connecting to a Windows 2K8R2 server using RDP. Will the frame details show me the security levels that are negotiated. The host is set to use the High encryption level. Thanks for your help.</p></div><div id="question-tags" class="tags-container tags">security rdp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '14, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/dd8496c3b0a8c0cb363162326fb6cc0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kevind5&#39;s gravatar image" /><p>kevind5<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kevind5 has no accepted answers">0%</span></p></div></div><div id="comments-container-34186" class="comments-container"></div><div id="comment-tools-34186" class="comment-tools"></div><div class="clear"></div><div id="comment-34186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34190"></span>

<div id="answer-container-34190" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34190-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please apply the following display filter:</p><blockquote><p>rdp.encryptionMethod</p></blockquote><p>Then look at the 'Info' column of the frame. It will show the negotiated encryption method.</p><p>Alternatively, open the RDP protocol in that frame and take a look at the 'serverSecurityData' fields.</p><p>You can try it with the following sample capture file and compare it with your file.</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=RDP-002.pcap.gz">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=RDP-002.pcap.gz</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34190" class="comments-container"><span id="34192"></span><div id="comment-34192" class="comment"><div id="post-34192-score" class="comment-score"></div><div class="comment-text"><p>Thanks much Kurt - if im connecting to a host and my capture doesn't show this frame - what am i missing. the host is configured to use high security settings.</p></div><div id="comment-34192-info" class="comment-info"><span class="comment-age">(25 Jun '14, 14:28)</span> kevind5</div></div><span id="34194"></span><div id="comment-34194" class="comment"><div id="post-34194-score" class="comment-score"></div><div class="comment-text"><blockquote><p>what am i missing.</p></blockquote><p>I don't know. Is it possible to post a sample capture file somewhere (google drive, dropbox, cloudshark.org)?</p></div><div id="comment-34194-info" class="comment-info"><span class="comment-age">(25 Jun '14, 15:17)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34190" class="comment-tools"></div><div class="clear"></div><div id="comment-34190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

