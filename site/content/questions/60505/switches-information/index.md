+++
type = "question"
title = "Switches information"
description = '''How will i get information about switches in a topology using wireshark so i able to find out which switch used by most??'''
date = "2017-04-01T06:42:00Z"
lastmod = "2017-04-06T12:08:00Z"
weight = 60505
keywords = [ "switches" ]
aliases = [ "/questions/60505" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Switches information](/questions/60505/switches-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60505-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How will i get information about switches in a topology using wireshark so i able to find out which switch used by most??</p></div><div id="question-tags" class="tags-container tags">switches</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '17, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/44748226de71145e36fde26bfdd367b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rainy&#39;s gravatar image" /><p>Rainy<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rainy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Apr '17, 06:47</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-60505" class="comments-container"></div><div id="comment-tools-60505" class="comment-tools"></div><div class="clear"></div><div id="comment-60505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60506"></span>

<div id="answer-container-60506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60506-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may be able to find out about the switches in your environment if they are manageable and have features like CDP or LLDP active. But to be able to capture the packets you need to connect to each switch since they won't be forwarded across switches - you can only see them on a link from each switch. So connecting Wireshark anywhere to the network and hoping to get all information in one spot is not possible.</p><p>If the switches are non-managed, you won't be able to find anything about them at all.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '17, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60506" class="comments-container"><span id="60508"></span><div id="comment-60508" class="comment"><div id="post-60508-score" class="comment-score"></div><div class="comment-text"><p>i want to find out heavy loaded switches in a topology using wireshark and mininet</p></div><div id="comment-60508-info" class="comment-info"><span class="comment-age">(01 Apr '17, 07:15)</span> Rainy</div></div><span id="60509"></span><div id="comment-60509" class="comment"><div id="post-60509-score" class="comment-score"></div><div class="comment-text"><p>For that you should log into the switches and check their stats, it's much more useful than doing it with captures.</p></div><div id="comment-60509-info" class="comment-info"><span class="comment-age">(01 Apr '17, 07:49)</span> Jasper ♦♦</div></div></div><div id="comment-tools-60506" class="comment-tools"></div><div class="clear"></div><div id="comment-60506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60624"></span>

<div id="answer-container-60624" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60624-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Even if you're connected to a switch, you won't see most traffic through other ports, unless it's a managed switch with port mirroring available. I bought a cheap 5 port gigabit managed switch that I configured for port mirroring. That way I can connect it into a network and see traffic passing through that port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '17, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/ba86f283d614d2cd9b6116140eaddded?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesK&#39;s gravatar image" /><p>JamesK<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesK has no accepted answers">0%</span></p></div></div><div id="comments-container-60624" class="comments-container"><span id="60625"></span><div id="comment-60625" class="comment"><div id="post-60625-score" class="comment-score"></div><div class="comment-text"><p>This is mininet we're talking about, so all virtual hosts with open vSwitch.</p></div><div id="comment-60625-info" class="comment-info"><span class="comment-age">(06 Apr '17, 12:53)</span> Jaap ♦</div></div></div><div id="comment-tools-60624" class="comment-tools"></div><div class="clear"></div><div id="comment-60624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

