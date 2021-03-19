+++
type = "question"
title = "Lua wireshark dissector registered to multiple ports"
description = '''Hi, I&#x27;m working lua based custom dissector in wireshark which runs over tcp. The port numbers through which the devices send request and response keeps changing everytime. I need a way to register the new port found everytime. I figured out a way to get the src or dst port numbers from pinfo by usin...'''
date = "2014-05-27T22:40:00Z"
lastmod = "2014-05-27T22:40:00Z"
weight = 33126
keywords = [ "dissectortable", "lua", "dissector", "dynamic", "port" ]
aliases = [ "/questions/33126" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua wireshark dissector registered to multiple ports](/questions/33126/lua-wireshark-dissector-registered-to-multiple-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33126-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm working lua based custom dissector in wireshark which runs over tcp. The port numbers through which the devices send request and response keeps changing everytime. I need a way to register the new port found everytime. I figured out a way to get the src or dst port numbers from pinfo by using pinfo.src_port or pinfo.dst_port. But I need to way to register the new found port number in the DissectorTable. Please help me out here.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">dissectortable lua dissector dynamic port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '14, 22:40</strong></p><img src="https://secure.gravatar.com/avatar/dd75facc5cb1c5c7eb78ba3c7b28ff85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PradeepKR&#39;s gravatar image" /><p>PradeepKR<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PradeepKR has no accepted answers">0%</span></p></div></div><div id="comments-container-33126" class="comments-container"><span id="34040"></span><div id="comment-34040" class="comment"><div id="post-34040-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I understand the problem you're having. Nothing prevents you adding to a <code>DissectorTable</code> while you're dissecting a packet. You would add it the same way you add it outside of that function.</p><p>Having said that... you said you're getting the port number from <code>pinfo.src_port</code> or <code>pinfo.dst_port</code>, but those are the port numbers of the packet you're dissecting... so if you're already dissecting it, why do you need to add your <code>Proto</code> to the <code>DissectorTable</code>? Or do you need to add a different <code>Proto</code> to the <code>DissectorTable</code>?</p></div><div id="comment-34040-info" class="comment-info"><span class="comment-age">(22 Jun '14, 10:35)</span> Hadriel</div></div></div><div id="comment-tools-33126" class="comment-tools"></div><div class="clear"></div><div id="comment-33126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

