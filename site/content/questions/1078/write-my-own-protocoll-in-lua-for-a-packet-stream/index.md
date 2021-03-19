+++
type = "question"
title = "Write my own protocoll in lua for a packet stream"
description = '''Hi everybody, i wrote my own lua dissector for packets up to the max size of 1440 Bytes. But I would like to capture bigger data packets (e.g. 12k) which a splittet in smaller packets. Is this possible to write a protocoll which capture more than one packet and put these into one &quot;virtuell&quot; big? If ...'''
date = "2010-11-23T06:34:00Z"
lastmod = "2011-01-02T08:22:00Z"
weight = 1078
keywords = [ "lua", "dissector", "protocol" ]
aliases = [ "/questions/1078" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Write my own protocoll in lua for a packet stream](/questions/1078/write-my-own-protocoll-in-lua-for-a-packet-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1078-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody, i wrote my own lua dissector for packets up to the max size of 1440 Bytes. But I would like to capture bigger data packets (e.g. 12k) which a splittet in smaller packets.</p><p>Is this possible to write a protocoll which capture more than one packet and put these into one "virtuell" big? If the answer is yes please give me a hint where I can find it or how I can do that.</p><p>Thanks folks Dennis</p></div><div id="question-tags" class="tags-container tags">lua dissector protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '10, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/1d99f25b0032d5b841c7b5fcc246d7c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="modula&#39;s gravatar image" /><p>modula<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="modula has no accepted answers">0%</span></p></div></div><div id="comments-container-1078" class="comments-container"></div><div id="comment-tools-1078" class="comment-tools"></div><div class="clear"></div><div id="comment-1078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1586"></span>

<div id="answer-container-1586" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1586-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The answer to this may depend on what's splitting the packets. If your protocol is transmitted over TCP, for instance, you can look at <span>http://wiki.wireshark.org/Lua/Dissectors</span> to see how to use the TCP reassembly functions of Wireshark from within a lua dissector.<br />
</p><p>If instead it's over something like UDP, then your protocol handling code will have to do the reassembly. Because your dissector will be called once for each packet, this implies that you'll need to have some persistent storage outside of the dissector routine to "remember" the various packet pieces until you have enough to reassemble.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '11, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p>beroset<br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span> </br></p></div></div><div id="comments-container-1586" class="comments-container"></div><div id="comment-tools-1586" class="comment-tools"></div><div class="clear"></div><div id="comment-1586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

