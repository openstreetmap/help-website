+++
type = "question"
title = "SSH Capture question"
description = '''I am currently reviewing some SSH captures for a client. We are trying to validate the SSH version that is in use Cisco&#x27;s SSH v 1.99 (OpenSSH). I am trying to create a case that outlines if certain features are in place then it must be SSH v1.99 (e.g. DH Key exchange, DSA auth method, etc).  One que...'''
date = "2013-04-23T12:16:00Z"
lastmod = "2013-04-24T15:38:00Z"
weight = 20741
keywords = [ "ssh" ]
aliases = [ "/questions/20741" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSH Capture question](/questions/20741/ssh-capture-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20741-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am currently reviewing some SSH captures for a client. We are trying to validate the SSH version that is in use Cisco's SSH v 1.99 (OpenSSH). I am trying to create a case that outlines if certain features are in place then it must be SSH v1.99 (e.g. DH Key exchange, DSA auth method, etc).<br />
</p><p>One question I do have is within the capture I am noticing under the SSH protocol section there is an indicator or a "Message Code: Public Key (2)". What does that mean?</p><p>Any help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">ssh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '13, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/ddd54bba47ddfcc6d807a8266e2d9833?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="netwerk&#39;s gravatar image" /><p>netwerk<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="netwerk has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-20741" class="comments-container"></div><div id="comment-tools-20741" class="comment-tools"></div><div class="clear"></div><div id="comment-20741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20787"></span>

<div id="answer-container-20787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20787-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>then it must be SSH v1.99</p></blockquote><p>version 1.99 is defined in <a href="http://tools.ietf.org/html/rfc4253">RFC 4253</a>. It's a 'flag' that signals compatibility with old ssh protocol versions, meaning that server is able to speak the ssh-1 and ssh-2 protocol. So, I don't think that version is directly related to DH Key exchange and DSA auth method.</p><blockquote><p>"Message Code: Public Key (2)". What does that mean?</p></blockquote><p>That's defined in the ssh-1 protocol.</p><blockquote><p><code>http://www.snailbook.com/docs/protocol-1.5.txt</code><br />
</p></blockquote><p>Search for this string: 2 SSH_SMSG_PUBLIC_KEY</p><p>It's a packet that contains information about the public key of the server.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '13, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20787" class="comments-container"></div><div id="comment-tools-20787" class="comment-tools"></div><div class="clear"></div><div id="comment-20787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

