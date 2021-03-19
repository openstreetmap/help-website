+++
type = "question"
title = "Between CAT and PLC"
description = '''Can I use Wireshark to capture data over Ethernet between a CAT engine and an Allen-Bradley PLC?'''
date = "2011-10-13T12:34:00Z"
lastmod = "2011-10-14T10:42:00Z"
weight = 6878
keywords = [ "ethernet", "plc", "allen-bradley", "cat" ]
aliases = [ "/questions/6878" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Between CAT and PLC](/questions/6878/between-cat-and-plc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6878-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I use Wireshark to capture data over Ethernet between a CAT engine and an Allen-Bradley PLC?</p></div><div id="question-tags" class="tags-container tags">ethernet plc allen-bradley cat</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '11, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/445d053df2ec8a1c3d700c45b1f9838b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mgriffin2&#39;s gravatar image" /><p>mgriffin2<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mgriffin2 has no accepted answers">0%</span></p></div></div><div id="comments-container-6878" class="comments-container"></div><div id="comment-tools-6878" class="comment-tools"></div><div class="clear"></div><div id="comment-6878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6886"></span>

<div id="answer-container-6886" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6886-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've no idea what you mean by a 'CAT engine', but there's two forms of 'communication' with a PLC.</p><p>On the data acquisition side where the PLC acquires the data from the I/O sensors Wireshark won't help as these are usually analog signals, and even where they are digital they are usually some form of serial protocol.</p><p>On the data reporting side, the PLC can communicate with other equipment, such as an HMI or SCADA system, and where this communication takes place over a medium that Wireshark can capture on, such as Ethernet, then this communication can be captured. You will somehow need to allow the Wireshark capturing device access to the Ethernet link.</p><p>Whether Wireshark can then dissect the communication depends on the protocol in use by the PLC and the other equipment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '11, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-6886" class="comments-container"><span id="6889"></span><div id="comment-6889" class="comment"><div id="post-6889-score" class="comment-score"></div><div class="comment-text"><p>Ok, thank you so much! A CAT engine is a Caterpillar engine. I'm trying to avoid using expensive equipment to read my data over ehternet between the Caterpillar and PLC.</p></div><div id="comment-6889-info" class="comment-info"><span class="comment-age">(14 Oct '11, 06:19)</span> mgriffin2</div></div><span id="6891"></span><div id="comment-6891" class="comment"><div id="post-6891-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure if you'll be able to see anything useful over that link, as that's likely to be the data acquisition side, i.e. the PLC is for some form of engine management.</p></div><div id="comment-6891-info" class="comment-info"><span class="comment-age">(14 Oct '11, 07:07)</span> grahamb ♦</div></div></div><div id="comment-tools-6886" class="comment-tools"></div><div class="clear"></div><div id="comment-6886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6893"></span>

<div id="answer-container-6893" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6893-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you post the information on the device that's sending the data to the PLC we might be able to tell you which protocol it would use. Best bet would to just download and try it, though. OPC would be a likely protocol, not sure if Wireshark can decode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '11, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/821d4bd4c56175f8f58198d7772d169b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="San%20Juan%20Vet&#39;s gravatar image" /><p>San Juan Vet<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="San Juan Vet has no accepted answers">0%</span></p></div></div><div id="comments-container-6893" class="comments-container"><span id="6896"></span><div id="comment-6896" class="comment"><div id="post-6896-score" class="comment-score"></div><div class="comment-text"><p>The CAT will use a M5X protocol. I think WireShark is probably fitted for different issues, but I just wantd to check out all of my options.</p></div><div id="comment-6896-info" class="comment-info"><span class="comment-age">(14 Oct '11, 12:08)</span> mgriffin2</div></div></div><div id="comment-tools-6893" class="comment-tools"></div><div class="clear"></div><div id="comment-6893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

