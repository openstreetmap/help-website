+++
type = "question"
title = "PC AND SSN IN SCCP message decode wrong"
description = '''Hi I am experience a decode issue , When i take a look at the Calling Party Address in SCCP message. It showed ,PC=7420,ssn is unknown ,the code showed 43 fc 1c 73 02, it should decode like 02-73-1c,ssn=252,check the preference of MTP3 already modify to ANSI. Not sure how to fix this issue.'''
date = "2013-05-15T07:48:00Z"
lastmod = "2013-05-16T07:06:00Z"
weight = 21148
keywords = [ "sccp", "decode", "ssn" ]
aliases = [ "/questions/21148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PC AND SSN IN SCCP message decode wrong](/questions/21148/pc-and-ssn-in-sccp-message-decode-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am experience a decode issue , When i take a look at the Calling Party Address in SCCP message. It showed ,PC=7420,ssn is unknown ,the code showed 43 fc 1c 73 02, it should decode like 02-73-1c,ssn=252,check the preference of MTP3 already modify to ANSI.</p><p>Not sure how to fix this issue.</p></div><div id="question-tags" class="tags-container tags">sccp decode ssn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '13, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/f1ab5fbb83d385605eb8ec1504496603?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peter%20c&#39;s gravatar image" /><p>peter c<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peter c has no accepted answers">0%</span></p></div></div><div id="comments-container-21148" class="comments-container"></div><div id="comment-tools-21148" class="comment-tools"></div><div class="clear"></div><div id="comment-21148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21183"></span>

<div id="answer-container-21183" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21183-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hmmm, if it is showing you "PC=7420" then it really looks like the MTP3 dissector thinks it is running ITU.</p><p>Oh, well, the other problem (if this is supposed to be ANSI) is that the high-order ("reserved for national use") bit in the Address Indicator is not set. That means, in ANSI, that the address is coded to international (meaning: not ANSI) standards. If you're using a modern Wireshark there should be an expert info warning about the unusualness of that...</p><p>I suspect that's the problem: either it's not really ANSI or that high-order bit is wrong.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '13, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-21183" class="comments-container"></div><div id="comment-tools-21183" class="comment-tools"></div><div class="clear"></div><div id="comment-21183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

