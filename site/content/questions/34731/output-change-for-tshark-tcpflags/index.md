+++
type = "question"
title = "Output change for TShark tcp.flags"
description = '''The tshark output of -e tcp.flags has changed from &#x27;0x0018&#x27; to &#x27;18&#x27; at some point in the last few 1.10.x releases. Was this an expected change? Just not something that i would have expected to change outside of a major release. EG  tshark -r &quot;test.pcapng&quot; -R &quot;tcp.port eq 80&quot; -Tfields -E header=y -E ...'''
date = "2014-07-17T11:22:00Z"
lastmod = "2014-07-17T11:22:00Z"
weight = 34731
keywords = [ "tshark" ]
aliases = [ "/questions/34731" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Output change for TShark tcp.flags](/questions/34731/output-change-for-tshark-tcpflags)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34731-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The tshark output of -e tcp.flags has changed from '0x0018' to '18' at some point in the last few 1.10.x releases. Was this an expected change? Just not something that i would have expected to change outside of a major release. EG tshark -r "test.pcapng" -R "tcp.port eq 80" -Tfields -E header=y -E separator=, -e tcp.stream -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e tcp.flags -e tcp.analysis.ack_rtt</p><p>thanks tim</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '14, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/0a68082cb3eb549b4282058b2feb543e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Poth&#39;s gravatar image" /><p>Tim Poth<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Poth has no accepted answers">0%</span></p></div></div><div id="comments-container-34731" class="comments-container"></div><div id="comment-tools-34731" class="comment-tools"></div><div class="clear"></div><div id="comment-34731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

