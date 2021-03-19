+++
type = "question"
title = "open big .cap file ?"
description = '''Hello. I have a .cap file that is 4Mo leght. When i try to open it with wishark, i have an error that says &quot;pcap: File has 1869904672-byte packet, bigger than maximum of 65535). Someone knows how to open my complete .cap file ? Thank you.'''
date = "2011-05-24T09:59:00Z"
lastmod = "2011-05-24T12:50:00Z"
weight = 4199
keywords = [ "filesize", "error" ]
aliases = [ "/questions/4199" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [open big .cap file ?](/questions/4199/open-big-cap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4199-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>I have a .cap file that is 4Mo leght.</p><p>When i try to open it with wishark, i have an error that says "pcap: File has 1869904672-byte packet, bigger than maximum of 65535).</p><p>Someone knows how to open my complete .cap file ?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">filesize error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '11, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/87d30ec8f180f7a94bd7519f09b56a8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parisien&#39;s gravatar image" /><p>parisien<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parisien has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 25 May '11, 21:47</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4199" class="comments-container"></div><div id="comment-tools-4199" class="comment-tools"></div><div class="clear"></div><div id="comment-4199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4200"></span>

<div id="answer-container-4200" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4200-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's not the file size that's choking Wireshark, it's that a single packet is almost 2 billion bytes in size. Either you guys are running jumbo packets OR there's something wrong with the capture file. Did you capture it with wireshark, or with another tool?</p><p>You can also look into running editcap with the -s parameter and limited the packet lengths to roughly 1500. Of course...this could be a bug with packet reassembly. Which version of WireShark are you using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '11, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-4200" class="comments-container"></div><div id="comment-tools-4200" class="comment-tools"></div><div class="clear"></div><div id="comment-4200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4203"></span>

<div id="answer-container-4203" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4203-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This usually is a result of transferring the file through FTP and not selecting binary mode. This will mess up the CR/LF and/or LF in the file. Did you use FTP to retrieve the file? If so, could you try again, but now with binary mode?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '11, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4203" class="comments-container"></div><div id="comment-tools-4203" class="comment-tools"></div><div class="clear"></div><div id="comment-4203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

