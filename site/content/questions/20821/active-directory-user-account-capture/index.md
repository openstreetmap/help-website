+++
type = "question"
title = "Active Directory User Account Capture"
description = '''I am novice user of Wireshark and I am trying to track down a PC where an unauthorized user is trying to logon to our network. I have searched numerous capture files and have not found any Active Directory user accounts. Is this information not contained in a packet? If it, how do I extract the info...'''
date = "2013-04-27T07:23:00Z"
lastmod = "2013-04-28T03:46:00Z"
weight = 20821
keywords = [ "active", "directory", "account", "user" ]
aliases = [ "/questions/20821" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Active Directory User Account Capture](/questions/20821/active-directory-user-account-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20821-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am novice user of Wireshark and I am trying to track down a PC where an unauthorized user is trying to logon to our network. I have searched numerous capture files and have not found any Active Directory user accounts. Is this information not contained in a packet? If it, how do I extract the information.</p></div><div id="question-tags" class="tags-container tags">active directory account user</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '13, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/1a72d77d32801c281977b6759ff08491?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThomasJoeP&#39;s gravatar image" /><p>ThomasJoeP<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThomasJoeP has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Apr '13, 07:28</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-20821" class="comments-container"></div><div id="comment-tools-20821" class="comment-tools"></div><div class="clear"></div><div id="comment-20821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20822"></span>

<div id="answer-container-20822" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20822-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You won't find any. Active Directory uses encryption and hashing to prevent anyone from capturing readable account information - for obvious security reasons.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '13, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20822" class="comments-container"></div><div id="comment-tools-20822" class="comment-tools"></div><div class="clear"></div><div id="comment-20822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20831"></span>

<div id="answer-container-20831" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20831-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am trying to track down a PC where an unauthorized user is trying to logon to our network.</p></blockquote><p>The security log of Windows is a far better tool to find such an event.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '13, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20831" class="comments-container"></div><div id="comment-tools-20831" class="comment-tools"></div><div class="clear"></div><div id="comment-20831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

