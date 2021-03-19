+++
type = "question"
title = "Import from.. UDP port"
description = '''I&#x27;m looking for similar feature than what is Wireshark - Import from text file. But instead from text file I would like to send packets to IP/UDP port which wireshark then listens. Then the packet payload contains the information to be decoded by Wireshark.  This looks quite easy to implement functi...'''
date = "2013-03-11T02:46:00Z"
lastmod = "2013-03-11T23:57:00Z"
weight = 19350
keywords = [ "import" ]
aliases = [ "/questions/19350" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Import from.. UDP port](/questions/19350/import-from-udp-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19350-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for similar feature than what is Wireshark - Import from text file.</p><p>But instead from text file I would like to send packets to IP/UDP port which wireshark then listens. Then the packet payload contains the information to be decoded by Wireshark.</p><p>This looks quite easy to implement functionality (for the great masters.., not for me) . Just specify port to listen and Encapsulation type.</p><p>Is this possible to implement example with Lua?</p></div><div id="question-tags" class="tags-container tags">import</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '13, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/26c53c08c255183014ddd777a84f98ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trian%20Geo&#39;s gravatar image" /><p>Trian Geo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trian Geo has no accepted answers">0%</span></p></div></div><div id="comments-container-19350" class="comments-container"></div><div id="comment-tools-19350" class="comment-tools"></div><div class="clear"></div><div id="comment-19350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19373"></span>

<div id="answer-container-19373" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19373-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Such a feature is not implemented and if you like to see it in Wireshark, I suggest to file an enhancement bug at bugs.wireshark.org.</p><p>There are other ways to achieve a similar result.</p><ol><li>use the remote capture feature of Wireshark and WinPcap</li><li>use ssh to forward the captured pcap data stream to Wireshark</li><li>use netcat to forward the captured pcap data stream to Wireshark via UDP</li></ol><blockquote><p>Is this possible to implement example with Lua?</p></blockquote><p>With the embedded Lua in Wireshark: No<br />
With a standalone Lua interpreter: Yes</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '13, 23:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-19373" class="comments-container"></div><div id="comment-tools-19373" class="comment-tools"></div><div class="clear"></div><div id="comment-19373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

