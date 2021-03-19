+++
type = "question"
title = "How to export reassembled packets to a .pcapng file?"
description = '''So I wrote a dissector in Lua for a proprietary protocol that is based neither on TCP nor on UDP, it is located on top of the USB layer. In this layer, some of the packets I am dissecting here are fragmented over multiple USB URB frames. I taught my dissector to do the re-assembly itself and display...'''
date = "2017-04-19T05:53:00Z"
lastmod = "2017-04-19T05:53:00Z"
weight = 60889
keywords = [ "lua", "dissector", "tshark", "reassembly" ]
aliases = [ "/questions/60889" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to export reassembled packets to a .pcapng file?](/questions/60889/how-to-export-reassembled-packets-to-a-pcapng-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60889-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I wrote a dissector in Lua for a proprietary protocol that is based neither on TCP nor on UDP, it is located on top of the USB layer. In this layer, some of the packets I am dissecting here are fragmented over multiple USB URB frames. I taught my dissector to do the re-assembly itself and display the re-assembled packet contents with the last frame in the "<a href="https://www.wireshark.org/docs/wsug_html_chunked/ChUsePacketBytesPaneSection.html">Packet Bytes</a>" view.</p><p><strong>Is there an easy way to write those re-assembled buffers to a .pcapng file from my dissector?</strong></p><p>A little more information on my use case: I am using tshark to dissect a given .pcapng file in an automated test scenario - the reassembly is kind of an intermediate step. After this, I would like to be able to open the reassembled (and filtered) packets in the Wireshark GUI.</p><p>Any help is appreciated. Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">lua dissector tshark reassembly</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '17, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/00a96bd28fd02417186122229a517000?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_oppermann&#39;s gravatar image" /><p>patrick_oppe...<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_oppermann has no accepted answers">0%</span></p></div></div><div id="comments-container-60889" class="comments-container"></div><div id="comment-tools-60889" class="comment-tools"></div><div class="clear"></div><div id="comment-60889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

