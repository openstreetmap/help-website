+++
type = "question"
title = "packet size limited during capture sip truncated"
description = '''Good morning, I see in the following captures message &quot;packet size limited during capture sip truncated&quot; and I do not know why, this did not happen to me with the previous version of WireShark. Please if anyone can tell me some tip about it. Thanks and regards, Camilo. mmxvii'''
date = "2017-06-21T08:30:00Z"
lastmod = "2017-06-21T11:15:00Z"
weight = 62212
keywords = [ "captured" ]
aliases = [ "/questions/62212" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packet size limited during capture sip truncated](/questions/62212/packet-size-limited-during-capture-sip-truncated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62212-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good morning,</p><p>I see in the following captures message "packet size limited during capture sip truncated" and I do not know why, this did not happen to me with the previous version of WireShark. Please if anyone can tell me some tip about it.</p><p>Thanks and regards,</p><p>Camilo.</p><p>mmxvii</p></div><div id="question-tags" class="tags-container tags">captured</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '17, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/fbf9981a3041c74595cc3c193b89b1ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cbarbaste&#39;s gravatar image" /><p>cbarbaste<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cbarbaste has no accepted answers">0%</span></p></div></div><div id="comments-container-62212" class="comments-container"><span id="62214"></span><div id="comment-62214" class="comment"><div id="post-62214-score" class="comment-score"></div><div class="comment-text"><p>Did you capture directly in Wireshark or have you open using Wireshark a capture taken somewhere else?</p><p>If directly using Wireshark, go <code>Capture -&gt; Options</code>, a window with a table of interface parameters will pop up. What values are there in the <code>Snaplen</code> column?</p></div><div id="comment-62214-info" class="comment-info"><span class="comment-age">(21 Jun '17, 09:25)</span> sindy</div></div><span id="62215"></span><div id="comment-62215" class="comment"><div id="post-62215-score" class="comment-score"></div><div class="comment-text"><p>good afternoon Sindy.,</p><p>The capture was external, and the file generated with .cap after open with WireShark.,</p><p>Thanks and regards.,</p><p>Camilo.</p></div><div id="comment-62215-info" class="comment-info"><span class="comment-age">(21 Jun '17, 11:05)</span> cbarbaste</div></div></div><div id="comment-tools-62212" class="comment-tools"></div><div class="clear"></div><div id="comment-62212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62216"></span>

<div id="answer-container-62216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62216-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>While Wireshark by default saves full size of captured frames, other tools (tcpdump at first place) don't - tcpdump saves only first 60 bytes of each frame unless asked to do otherwise. Information about original size of the frame is stored in the pcap or pcapng file. So your issue is most likely not related to Wireshark version but to the absence of <code>-s 0</code> among tcpdump's command line parameters while taking that capture.</p><p>To be 100% sure, you'd have to inspect the pcap file, using e.g. <code>hexdump</code> on linux or some other binary file viewer. Or post the file somewhere and provide a link to it here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '17, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62216" class="comments-container"></div><div id="comment-tools-62216" class="comment-tools"></div><div class="clear"></div><div id="comment-62216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

