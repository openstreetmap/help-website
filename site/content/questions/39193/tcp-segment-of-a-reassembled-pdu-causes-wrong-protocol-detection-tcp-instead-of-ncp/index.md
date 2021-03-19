+++
type = "question"
title = "&quot;TCP segment of a reassembled PDU&quot; causes wrong protocol detection (TCP instead of NCP)"
description = '''Hello, I&#x27;m not sure if this is a bug or a feature, but it is definitely inconvenient: If data is split into several packets, Wireshark does not identify the protocol correctly. Continuation packets are always of the type TCP (or probably UDP where appropriate) instead of the higher protocol this tcp...'''
date = "2015-01-16T00:54:00Z"
lastmod = "2015-01-16T00:54:00Z"
weight = 39193
keywords = [ "ncp", "identification", "protocol" ]
aliases = [ "/questions/39193" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ["TCP segment of a reassembled PDU" causes wrong protocol detection (TCP instead of NCP)](/questions/39193/tcp-segment-of-a-reassembled-pdu-causes-wrong-protocol-detection-tcp-instead-of-ncp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39193-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm not sure if this is a bug or a feature, but it is definitely inconvenient: If data is split into several packets, Wireshark does not identify the protocol correctly. Continuation packets are always of the type TCP (or probably UDP where appropriate) instead of the higher protocol this tcp connection uses (for example HTTP or in our current case NCP). This causes problems with filters and statistics, for example a filter for "http" in the IO Graph of Wireshark will ignore all continuation packets. Thus if even moderately large files are transferred, the statistic is missing packets. The Graph shows a gap between the protocol and all packets and it is not clear which protocol is responsible for those packets. The same happens in the "Conversations" view.</p><p>Maybe I'm just missing the right option: I'm searching for an option to flag the protocol of continuation packets the same as the rest of the conversation. This would allow filters for protocols to work as expected. This of course would require to analyse the whole tcp conversation, not just the packet at hand. I already checked the settings of the relevant protocol, both "Reassemble NCP-over-TCP messages spanning multiple TCP segments" and "Reassemble fragmented NDS messages spanning multiple reply packets" are set to on (the default) as are the similar options for HTTP.</p><p>Is this behaviour intentional? Can it be changed?</p><p>Greetings Markus</p></div><div id="question-tags" class="tags-container tags">ncp identification protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '15, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/b4c929da67f795ae44a32f57db22b371?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Markus68&#39;s gravatar image" /><p>Markus68<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Markus68 has no accepted answers">0%</span></p></div></div><div id="comments-container-39193" class="comments-container"></div><div id="comment-tools-39193" class="comment-tools"></div><div class="clear"></div><div id="comment-39193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

