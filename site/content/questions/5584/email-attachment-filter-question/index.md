+++
type = "question"
title = "Email attachment filter question?"
description = '''I have used Wireshark in University a little bit when I was studying Computer security and forensics. But now that I am employed as a IT security officer my company is looking at implementing a email monitoring solution on our network.  Does anyone know if it&#x27;s possible for Wireshark to perform the ...'''
date = "2011-08-09T06:18:00Z"
lastmod = "2016-09-27T06:37:00Z"
weight = 5584
keywords = [ "encryption", "email" ]
aliases = [ "/questions/5584" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Email attachment filter question?](/questions/5584/email-attachment-filter-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5584-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have used Wireshark in University a little bit when I was studying Computer security and forensics. But now that I am employed as a IT security officer my company is looking at implementing a email monitoring solution on our network.</p><p>Does anyone know if it's possible for Wireshark to perform the following task?</p><p>Filter all SMTP traffic within a set IP range and show the destination address and attachment format. But exclude the internal email address domain from the results.</p><p>Basically the purpose of this is because we have a policy in place that all emails containing attachments that are sent outside of the company must be encrypted using 7zip. Therefore we are keen to enforce this to prevent any leakage of sensitive information.</p></div><div id="question-tags" class="tags-container tags">encryption email</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '11, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/671171f0afed7e964e3d089d7155e7b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RogueViper&#39;s gravatar image" /><p>RogueViper<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RogueViper has no accepted answers">0%</span></p></div></div><div id="comments-container-5584" class="comments-container"></div><div id="comment-tools-5584" class="comment-tools"></div><div class="clear"></div><div id="comment-5584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5585"></span>

<div id="answer-container-5585" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5585-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wouldn't this be better handled by your email server, presuming you have an internal one that all users send their email to?</p><p>If you allow all users to directly transmit emails to some outside server then life will be more difficult.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '11, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5585" class="comments-container"><span id="5590"></span><div id="comment-5590" class="comment"><div id="post-5590-score" class="comment-score"></div><div class="comment-text"><p>Ok thanks. This is my first job in IT since graduating so I am on a massive learning curve. This is something my boss asked me to investigate. Thanks for the suggestion.</p></div><div id="comment-5590-info" class="comment-info"><span class="comment-age">(09 Aug '11, 10:47)</span> RogueViper</div></div></div><div id="comment-tools-5585" class="comment-tools"></div><div class="clear"></div><div id="comment-5585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55902"></span>

<div id="answer-container-55902" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55902-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @grahamb pointed out, it's better processed by email server with a plugin. In case you really need to process it at packet level, you may want to learn something basic on packet programming. More specifically</p><ul><li>read packets using libpcap (or other equivalent)</li><li>Classify each (tcp) packets into the right TCP sessions.</li><li>Assemble the data for SMTP sessions and check MIME headers and perform your logic there.</li></ul><p>You may find you really learned a lot about networking and you feel like a network expert :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '16, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/0228802baecfa9b8d8764a043fea883b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharkfun&#39;s gravatar image" /><p>sharkfun<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharkfun has no accepted answers">0%</span></p></div></div><div id="comments-container-55902" class="comments-container"></div><div id="comment-tools-55902" class="comment-tools"></div><div class="clear"></div><div id="comment-55902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

