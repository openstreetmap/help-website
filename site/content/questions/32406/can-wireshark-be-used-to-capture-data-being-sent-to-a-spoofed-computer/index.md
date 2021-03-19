+++
type = "question"
title = "Can wireshark be used to capture data being sent to a spoofed computer?"
description = '''I have to think about cause and consequence so defense is really the best offense. I am wondering... (theoretically) by spoofing computer x and by capturing its packets and data being sent (in and out to computer x)... can i (for example) capture a word document (.doc)... that computer Y has sent to...'''
date = "2014-05-02T07:19:00Z"
lastmod = "2014-05-02T07:21:00Z"
weight = 32406
keywords = [ "wireshark", "spoof", "computer", "mac", "address" ]
aliases = [ "/questions/32406" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can wireshark be used to capture data being sent to a spoofed computer?](/questions/32406/can-wireshark-be-used-to-capture-data-being-sent-to-a-spoofed-computer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32406-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to think about cause and consequence so defense is really the best offense.</p><p>I am wondering... (theoretically) by spoofing computer x and by capturing its packets and data being sent (in and out to computer x)... can i (for example) capture a word document (.doc)... that computer Y has sent to the computer x?</p><p>Best regards.</p></div><div id="question-tags" class="tags-container tags">wireshark spoof computer mac address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '14, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/2ac6e5d91e7ef47a57c9a614b14b68f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philosopher&#39;s gravatar image" /><p>philosopher<br />
<span class="score" title="10 reputation points">10</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philosopher has no accepted answers">0%</span></p></div></div><div id="comments-container-32406" class="comments-container"></div><div id="comment-tools-32406" class="comment-tools"></div><div class="clear"></div><div id="comment-32406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32408"></span>

<div id="answer-container-32408" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32408-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to be able to capture the packets in the first place, so your point of capture needs to be somewhere where the packets pass by. If you can achieve that, and the documents are not transferred over an encrypted link, then you can extract them from the capture.</p><p>Problem with spoofing is that usually the answer packets do not make it back to you but get sent to the real computer instead, so it won't help you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '14, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32408" class="comments-container"><span id="32409"></span><div id="comment-32409" class="comment"><div id="post-32409-score" class="comment-score"></div><div class="comment-text"><p>(in theory)</p><p>What if i use a vmware (computer Z) connected to the network.</p><p>computer y send a .pdf document... and i want to intercept this document</p><p>i spoof (change its mac address to the same as computer x) use vmware (windows xp os, 'computer z') to spoof this address and i use wireshark to receive the packets (and the document)?</p></div><div id="comment-32409-info" class="comment-info"><span class="comment-age">(02 May '14, 07:28)</span> philosopher</div></div><span id="32410"></span><div id="comment-32410" class="comment"><div id="post-32410-score" class="comment-score">1</div><div class="comment-text"><p>Well, in a local segment using ARP spoofing you can MITM the transfer and capture the documents, but that doesn't work anymore as soon as you try to do it outside your own layer 2 segment.</p></div><div id="comment-32410-info" class="comment-info"><span class="comment-age">(02 May '14, 07:30)</span> Jasper ♦♦</div></div><span id="32413"></span><div id="comment-32413" class="comment"><div id="post-32413-score" class="comment-score"></div><div class="comment-text"><p>(theoretically) I was thinking in something like "Cain and Abel"... or some similiar software.</p><p>i assign a very close ip and then using these softwares (arp poisen a mac address) i start the poisoning...</p><p>computer x ip: 192.168.80.1 - "victim" (the one getting intercepted)</p><p>computer y ip: 192.168.80.2 - "sender" (the one who sends the document without any clue</p><p>computer z ip: 192.168.80.3 - vmware (the attacker)</p></div><div id="comment-32413-info" class="comment-info"><span class="comment-age">(02 May '14, 07:39)</span> philosopher</div></div><span id="32414"></span><div id="comment-32414" class="comment"><div id="post-32414-score" class="comment-score">1</div><div class="comment-text"><p>Please stop answering, instead use comments - I converted your last two answers for you ;-)</p><p>Sure, C&amp;A can do this, as long as all nodes are in the same ethernet segment, as I already said.</p></div><div id="comment-32414-info" class="comment-info"><span class="comment-age">(02 May '14, 07:49)</span> Jasper ♦♦</div></div><span id="32415"></span><div id="comment-32415" class="comment"><div id="post-32415-score" class="comment-score"></div><div class="comment-text"><p>I didn't notice your answer :)</p><p>Thank you very much for your help :D</p><p>If you ever need anything.. feel free to message me ;)</p></div><div id="comment-32415-info" class="comment-info"><span class="comment-age">(02 May '14, 07:57)</span> philosopher</div></div><span id="32417"></span><div id="comment-32417" class="comment not_top_scorer"><div id="post-32417-score" class="comment-score"></div><div class="comment-text"><p>If you're happy with the answers you get here, you should accept them as answered (checkmark button on the left next to an answer) ;-)</p></div><div id="comment-32417-info" class="comment-info"><span class="comment-age">(02 May '14, 07:59)</span> Jasper ♦♦</div></div></div><div id="comment-tools-32408" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-32408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

