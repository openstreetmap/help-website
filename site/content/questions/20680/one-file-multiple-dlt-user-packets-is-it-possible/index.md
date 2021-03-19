+++
type = "question"
title = "One file. Multiple DLT USER packets. Is it possible?"
description = '''Hello everyone, I&#x27;m trying to log RRC messages. There are few RRC protocols: &quot;rrc.ul.ccch&quot; &quot;rrc.dl.ccch&quot; &quot;rrc.ul.dcch&quot; &quot;rrc.dl.dcch&quot; I&#x27;m getting all kind of messages, one after the other, and I want to use wireshark as a log to all the messages that I&#x27;ve captured. Meaning, I want to create one file ...'''
date = "2013-04-21T08:27:00Z"
lastmod = "2013-04-22T07:08:00Z"
weight = 20680
keywords = [ "text2pcap", "mergecap", "dlt_user", "pcapng", "rrc" ]
aliases = [ "/questions/20680" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [One file. Multiple DLT USER packets. Is it possible?](/questions/20680/one-file-multiple-dlt-user-packets-is-it-possible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20680-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, I'm trying to log RRC messages. There are few RRC protocols: "rrc.ul.ccch" "rrc.dl.ccch" "rrc.ul.dcch" "rrc.dl.dcch"</p><p>I'm getting all kind of messages, one after the other, and I want to use wireshark as a log to all the messages that I've captured. Meaning, I want to create one file that will hold all the messages received in the protocols above, in the same order they were received.</p><p>I dont listen on any interface but I have an internal system that gives me the bytes of the messages, and I have a way to tell which message correspond to which protocol.</p><p>I created a DLT_USER for each protocol and I parse the bytes using text2pcap according to the suitable message received. (text2pcap -l DLT_USER textfilewithbytes)</p><p>Now, I want to merge file with 2 (or more) types of protocols to one single file. mergecap won't let me do that. The way I understand it, mergecap doesnt like it when I try to merge different DLT_USER's (which specify different protocols) to one file. What am I missing? Is it possible to have one file with multiple DLT_USER's in it? How can I verify that I'm creating pcapNG and not just regular libpcap?</p><p>Thanks a lot, Dor</p><p>P.S. I have the most updated WireShark installed.<br />
</p></div><div id="question-tags" class="tags-container tags">text2pcap mergecap dlt_user pcapng rrc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '13, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/4f69a72529c7788cca576605b8f29e1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DorZ&#39;s gravatar image" /><p>DorZ<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DorZ has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-20680" class="comments-container"></div><div id="comment-tools-20680" class="comment-tools"></div><div class="clear"></div><div id="comment-20680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20705"></span>

<div id="answer-container-20705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20705-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think there can only be one DLT per interface in PCAP_NG, you could try to crate an IDB per DLT or add some psedo data for your user DLT indicatin the next protocol and write a dissector for the DLT.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '13, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-20705" class="comments-container"><span id="20709"></span><div id="comment-20709" class="comment"><div id="post-20709-score" class="comment-score"></div><div class="comment-text"><p>Hi Andres, Thanks for taking the time to answer. Actually, I AM trying to do just as you said. i.e, creating a new dissector (with LUA) that will dissect the packet according to the packet. But, When Im using DissectorTable.get(..), whatever string I put there I get an error 'no such dissector table' (I tried "ip.proto", "ethertype", "tcp.port", "udp.port". nothing worked).</p><p>Do you have any idea why?</p><p>Thanks, Dor</p></div><div id="comment-20709-info" class="comment-info"><span class="comment-age">(22 Apr '13, 07:20)</span> DorZ</div></div></div><div id="comment-tools-20705" class="comment-tools"></div><div class="clear"></div><div id="comment-20705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

