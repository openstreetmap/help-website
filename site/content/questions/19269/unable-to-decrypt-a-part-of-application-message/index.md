+++
type = "question"
title = "Unable To Decrypt a part of application message."
description = '''Hi All, I am not able to Decrypt some of the avps(in Diameter protocol). My problem is a few avps(diameter protocol)/IE(in 3GPP protocol) of a message is encrypted using AES-CBC Algorithms. Is there any options to decrypt the IEs/AVPs of a 3GPP/Diameter message. Please suggest, how to set the keys a...'''
date = "2013-03-07T03:10:00Z"
lastmod = "2013-04-23T07:31:00Z"
weight = 19269
keywords = [ "mustresa" ]
aliases = [ "/questions/19269" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unable To Decrypt a part of application message.](/questions/19269/unable-to-decrypt-a-part-of-application-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19269-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am not able to Decrypt some of the avps(in Diameter protocol). My problem is a few avps(diameter protocol)/IE(in 3GPP protocol) of a message is encrypted using AES-CBC Algorithms. Is there any options to decrypt the IEs/AVPs of a 3GPP/Diameter message. Please suggest, how to set the keys and all other parameters to decrypt these IEs. If this feature is not supported in Wireshark,then please suggest is there any ways to decrypt these parameters of the message.</p><p>Thanks in advance, Manoj<br />
</p></div><div id="question-tags" class="tags-container tags">mustresa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '13, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/ed7ba9f56100189ae36b7ee613d210f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manoja&#39;s gravatar image" /><p>Manoja<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manoja has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-19269" class="comments-container"></div><div id="comment-tools-19269" class="comment-tools"></div><div class="clear"></div><div id="comment-19269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19273"></span>

<div id="answer-container-19273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19273-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Decryption of Diameter AVP:s is not implemented in Wireshark. I don't know if there is a program that could take the extracted bytes keys etc as input and do decryption.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '13, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-19273" class="comments-container"><span id="19327"></span><div id="comment-19327" class="comment"><div id="post-19327-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Is it posible to decript the value of the Parameter/Avp by writing a Wireshark Diameter dissector?</p></div><div id="comment-19327-info" class="comment-info"><span class="comment-age">(08 Mar '13, 23:14)</span> Manoja</div></div><span id="19328"></span><div id="comment-19328" class="comment"><div id="post-19328-score" class="comment-score"></div><div class="comment-text"><p>Well one should rather expand the Diameter dissector to do decryption. I have no idea how complicated that might be and there is no current plan to implement that. But if you want to give it a go, please do. The ESP and SSL dissectors should be good starting points to look at how to implemnt an UAT to define the keys and how call decryption functions.</p></div><div id="comment-19328-info" class="comment-info"><span class="comment-age">(09 Mar '13, 00:10)</span> Anders ♦</div></div></div><div id="comment-tools-19273" class="comment-tools"></div><div class="clear"></div><div id="comment-19273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20736"></span>

<div id="answer-container-20736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20736-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Manoj<br />
</p><p>Did you try the wireshark menu Analize-&gt; Decode As then in transport select Diameter and ok? for tshark you can try tshark -r InputFile.pcap -d tcp.port==&lt;your port=""&gt;,diameter</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '13, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/ca20bac738bbb8b012045602a77d7115?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fachav2&#39;s gravatar image" /><p>fachav2<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fachav2 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-20736" class="comments-container"></div><div id="comment-tools-20736" class="comment-tools"></div><div class="clear"></div><div id="comment-20736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

