+++
type = "question"
title = "Penetration Testing"
description = '''Can Wireshark be used for internal penetration testing? I am new to penetration testing but I need to learn quickly and start performing internal scans and tests.'''
date = "2015-03-24T08:02:00Z"
lastmod = "2015-03-25T17:50:00Z"
weight = 40802
keywords = [ "test", "penetration" ]
aliases = [ "/questions/40802" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Penetration Testing](/questions/40802/penetration-testing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40802-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can Wireshark be used for internal penetration testing? I am new to penetration testing but I need to learn quickly and start performing internal scans and tests.</p></div><div id="question-tags" class="tags-container tags">test penetration</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '15, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/721100b04a60608df24ae128a72f27bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="japonzio&#39;s gravatar image" /><p>japonzio<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="japonzio has no accepted answers">0%</span></p></div></div><div id="comments-container-40802" class="comments-container"></div><div id="comment-tools-40802" class="comment-tools"></div><div class="clear"></div><div id="comment-40802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40809"></span>

<div id="answer-container-40809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40809-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes and no. Wireshark is a recording/analyzing tool, it does not scan or otherwise create packets. Still, Wireshark is helpful in recording your scans (e.g. performed by using <a href="http://nmap.org/">nmap</a>) to be able to see/prove afterwards what the scan really did.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40809" class="comments-container"><span id="40838"></span><div id="comment-40838" class="comment"><div id="post-40838-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the feedback. I will have to get familiar with Wireshark and learn how to use it. I am not sure if I need to keep looking for a good pen test program or just use Wireshark.</p></div><div id="comment-40838-info" class="comment-info"><span class="comment-age">(25 Mar '15, 07:35)</span> japonzio</div></div></div><div id="comment-tools-40809" class="comment-tools"></div><div class="clear"></div><div id="comment-40809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40867"></span>

<div id="answer-container-40867" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40867-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am not sure if I need to <strong>keep looking for a good pen test program</strong> or just use Wireshark.</p></blockquote><p>The most important thing for pentesting is not a single tool/program, it's good old Know-how. Knowing protocols, network architectures, web architectures, typical security problems/bugs, cryptography know how, and many more things.</p><p>Having said that, there is not one single best pentest tool. There a lot of "supporting" tools you can use during the pentest process. One good collection of such tools is Kali Linux, which also includes Wireshark.</p><blockquote><p><a href="http://www.kali.org">http://www.kali.org</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '15, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Mar '15, 17:50</p></div></div><div id="comments-container-40867" class="comments-container"></div><div id="comment-tools-40867" class="comment-tools"></div><div class="clear"></div><div id="comment-40867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

