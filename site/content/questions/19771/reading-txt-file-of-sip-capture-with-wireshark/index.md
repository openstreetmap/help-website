+++
type = "question"
title = "Reading TXT file of SIP capture  with Wireshark"
description = '''I have an Allworx VoIP PBX in the PBX there is a tool section that allows me to capture SIP Messages and save it as a TXT file. I can view the TXT file with notepad. Is there a way with wireshark to just filter this so I see only the one call I would like to look at so its not so confusing on trying...'''
date = "2013-03-23T08:56:00Z"
lastmod = "2013-03-23T09:30:00Z"
weight = 19771
keywords = [ "txt" ]
aliases = [ "/questions/19771" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reading TXT file of SIP capture with Wireshark](/questions/19771/reading-txt-file-of-sip-capture-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19771-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an Allworx VoIP PBX in the PBX there is a tool section that allows me to capture SIP Messages and save it as a TXT file. I can view the TXT file with notepad. Is there a way with wireshark to just filter this so I see only the one call I would like to look at so its not so confusing on trying to follow the call mainly I am looking to see if its my PBX or provider sending the BYE msg.</p></div><div id="question-tags" class="tags-container tags">txt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '13, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/5bdd5034dc86ae3d92be607db3e97262?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ATItelcom&#39;s gravatar image" /><p>ATItelcom<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ATItelcom has no accepted answers">0%</span></p></div></div><div id="comments-container-19771" class="comments-container"></div><div id="comment-tools-19771" class="comment-tools"></div><div class="clear"></div><div id="comment-19771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19773"></span>

<div id="answer-container-19773" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19773-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, No wireshark can't read a pure text file. But in your text file search for the number/sip-uri you need, find the call-id of the INVITE then find the packets based on that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '13, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-19773" class="comments-container"></div><div id="comment-tools-19773" class="comment-tools"></div><div class="clear"></div><div id="comment-19773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

