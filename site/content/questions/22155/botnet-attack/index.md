+++
type = "question"
title = "botnet attack"
description = '''Hi all,today in our symmantec siem product we observed botnet log showing destination port as 7000 but strange thing is,it is showing protocol as icmp.as par my knowledge icmp has nothing do with tcp ports?symantec siem products gets this logs from our firewall and in firewall we have only allow icm...'''
date = "2013-06-19T06:22:00Z"
lastmod = "2013-06-19T08:54:00Z"
weight = 22155
keywords = [ "icmp" ]
aliases = [ "/questions/22155" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [botnet attack](/questions/22155/botnet-attack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22155-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,today in our symmantec siem product we observed botnet log showing destination port as 7000 but strange thing is,it is showing protocol as icmp.as par my knowledge icmp has nothing do with tcp ports?symantec siem products gets this logs from our firewall and in firewall we have only allow icmp eco request and reply service.i am sure it is icmp traffic only but why port is showing,source of traffic is linux machine.</p></div><div id="question-tags" class="tags-container tags">icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '13, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-22155" class="comments-container"></div><div id="comment-tools-22155" class="comment-tools"></div><div class="clear"></div><div id="comment-22155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22156"></span>

<div id="answer-container-22156" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22156-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i am sure it is icmp traffic only but why port is showing</p></blockquote><p>some possibilities:</p><ul><li>a bug in your SIEM product</li><li>your interpretation of the "port" statement in the SIEM logs is wrong</li><li>there is really a TCP/UDP port involved (IP tunnel via ICMP) and the firewall detected that (rather unlikely)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '13, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jun '13, 02:31</p></div></div><div id="comments-container-22156" class="comments-container"></div><div id="comment-tools-22156" class="comment-tools"></div><div class="clear"></div><div id="comment-22156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22175"></span>

<div id="answer-container-22175" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22175-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe it was an ICMP Destination Unreachable packet and the port number was taken from the original IP packet, which is returned inside the ICMP Destination Unreachable packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '13, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-22175" class="comments-container"></div><div id="comment-tools-22175" class="comment-tools"></div><div class="clear"></div><div id="comment-22175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

