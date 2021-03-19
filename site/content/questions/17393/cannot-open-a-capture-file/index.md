+++
type = "question"
title = "Cannot open a capture file"
description = '''When trying to open a capture file I get an error: &quot;This application has requested the Runitime to terminate it in an unusual way. Please contact the application&#x27;s support team for more information.&quot;'''
date = "2013-01-02T12:01:00Z"
lastmod = "2013-01-02T13:29:00Z"
weight = 17393
keywords = [ "failure", "open", "file" ]
aliases = [ "/questions/17393" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot open a capture file](/questions/17393/cannot-open-a-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17393-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When trying to open a capture file I get an error: "This application has requested the Runitime to terminate it in an unusual way. Please contact the application's support team for more information."</p></div><div id="question-tags" class="tags-container tags">failure open file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '13, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/471df17e8b4b85de7a6848f8a9b3b85b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MMArtinezNCH&#39;s gravatar image" /><p>MMArtinezNCH<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MMArtinezNCH has no accepted answers">0%</span></p></div></div><div id="comments-container-17393" class="comments-container"></div><div id="comment-tools-17393" class="comment-tools"></div><div class="clear"></div><div id="comment-17393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17397"></span>

<div id="answer-container-17397" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17397-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like either a bug or <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">OutOfMemory</a>, how big is the pcap file that you are opening?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '13, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17397" class="comments-container"></div><div id="comment-tools-17397" class="comment-tools"></div><div class="clear"></div><div id="comment-17397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17394"></span>

<div id="answer-container-17394" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17394-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like there is something wrong with the capture file. Did you transfer it via FTP to your PC? If so, please do again and use <strong>binary</strong> mode. If no: can you post the capture file somewhere?</p><p>BTW: What is your Wireshark version?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '13, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-17394" class="comments-container"></div><div id="comment-tools-17394" class="comment-tools"></div><div class="clear"></div><div id="comment-17394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

