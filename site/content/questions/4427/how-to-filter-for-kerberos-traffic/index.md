+++
type = "question"
title = "how to filter for Kerberos traffic"
description = '''During Security Log review on a Windows 2003 server I came across a repeated Event ID 531.  Event gets logged 11 times every hour and does not have much details other than it’s a network log on/off (Ex. 11 times @ 5:11:15AM, 11 times @ 6:11:15AM, 11 times @ 7:11:15AM) Logon Failure: Reason: Account ...'''
date = "2011-06-07T06:43:00Z"
lastmod = "2011-06-07T07:25:00Z"
weight = 4427
keywords = [ "filter", "kerberos", "531" ]
aliases = [ "/questions/4427" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to filter for Kerberos traffic](/questions/4427/how-to-filter-for-kerberos-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4427-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>During Security Log review on a Windows 2003 server I came across a repeated Event ID 531. Event gets logged 11 times every hour and does not have much details other than it’s a network log on/off (Ex. 11 times @ 5:11:15AM, 11 times @ 6:11:15AM, 11 times @ 7:11:15AM)</p><p>Logon Failure:</p><pre><code>Reason:     Account currently disabled
User Name:  
Domain:     
Logon Type: 3
Logon Process:  Authz   
Authentication Package: Kerberos
Workstation Name:   MAILSRV1
Caller User Name:   MAILSRV1$
Caller Domain:  CORP
Caller Logon ID:    (0x0,0x3E7)
Caller Process ID:  7152
Transited Services: -
Source Network Address: -
Source Port:    -</code></pre><p>For more information, see Help and Support Center at http://go.microsoft.com/fwlink/events.asp.</p><p>Is there a way to create a filter in wireshark what would help identify the computer initiating the logon attempt?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">filter kerberos 531</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '11, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jun '11, 06:51</p></div></div><div id="comments-container-4427" class="comments-container"><span id="4428"></span><div id="comment-4428" class="comment"><div id="post-4428-score" class="comment-score"></div><div class="comment-text"><p>Process ID: 7152 is w3wp.exe</p></div><div id="comment-4428-info" class="comment-info"><span class="comment-age">(07 Jun '11, 06:47)</span> net_tech</div></div><span id="4433"></span><div id="comment-4433" class="comment"><div id="post-4433-score" class="comment-score"></div><div class="comment-text"><p>should my filter look like "tcp.port == 88 or udp.port == 88" ?</p></div><div id="comment-4433-info" class="comment-info"><span class="comment-age">(07 Jun '11, 07:02)</span> net_tech</div></div></div><div id="comment-tools-4427" class="comment-tools"></div><div class="clear"></div><div id="comment-4427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4434"></span>

<div id="answer-container-4434" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4434-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Figured it out and found the name of the Disabled Account in AD</p><p>(tcp.port == 88 or udp.port == 88) and (kerberos.msg.type == 30)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-4434" class="comments-container"></div><div id="comment-tools-4434" class="comment-tools"></div><div class="clear"></div><div id="comment-4434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

