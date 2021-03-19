+++
type = "question"
title = "How to decode mpeg ts payload?"
description = '''Hello, I need to decode mpeg ts payload in a .pcap file (UDPs with mpegts). Especially I need PAT/PMT information data. The PAT (Program Association Table) stores the PIDs of all PMTs. I need the PIDs of these PMTs. What I done is to decode the UDP packets as mp2t. So far so good, but I get only the...'''
date = "2013-05-21T03:32:00Z"
lastmod = "2013-05-21T03:32:00Z"
weight = 21344
keywords = [ "pmt", "pid", "pat", "mpegts" ]
aliases = [ "/questions/21344" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode mpeg ts payload?](/questions/21344/how-to-decode-mpeg-ts-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21344-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I need to decode mpeg ts payload in a .pcap file (UDPs with mpegts).</p><p>Especially I need PAT/PMT information data. The PAT (Program Association Table) stores the PIDs of all PMTs. I need the PIDs of these PMTs.</p><p>What I done is to decode the UDP packets as mp2t. So far so good, but I get only the headers of ISO/IEC 13818-1 like "Sync Byte", "Transport Layer Indicator", "Payload Unit Start Indicator", ..., and finally "Continuity Counter".</p><p>What I need is the Information stored in PAT (PIDs of all PMTs) and the information stored in these PMTs (PIDs of all streams).</p><p>How I can to that? Thanks Guys!</p><p>Regards Robert</p></div><div id="question-tags" class="tags-container tags">pmt pid pat mpegts</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '13, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/d341850a5fd2d1e4ea160e6d71d30c1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hampek&#39;s gravatar image" /><p>Hampek<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hampek has no accepted answers">0%</span></p></div></div><div id="comments-container-21344" class="comments-container"></div><div id="comment-tools-21344" class="comment-tools"></div><div class="clear"></div><div id="comment-21344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

