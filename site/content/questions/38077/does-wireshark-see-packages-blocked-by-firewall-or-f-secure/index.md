+++
type = "question"
title = "Does Wireshark see packages blocked by Firewall or F-Secure?"
description = '''Hi I&#x27;m an occasional user of Wireshark to trouble shoot networking problems in private environments. Due to a current problem, I&#x27;m wondering what packets Wireshark can see when capturing traffic which might get blocked by either a local firewall (Windows 7) or some internet security software such as...'''
date = "2014-11-23T03:20:00Z"
lastmod = "2014-11-24T04:09:00Z"
weight = 38077
keywords = [ "firewall", "intenert-security", "blocking", "capturing" ]
aliases = [ "/questions/38077" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark see packages blocked by Firewall or F-Secure?](/questions/38077/does-wireshark-see-packages-blocked-by-firewall-or-f-secure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38077-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm an occasional user of Wireshark to trouble shoot networking problems in private environments.</p><p>Due to a current problem, I'm wondering what packets Wireshark can see when capturing traffic which might get blocked by either a local firewall (Windows 7) or some internet security software such as F-Secure Internet Security with its Broser Protection.</p><p>I understand the latter is very specific to the security product, but maybe some has some knowledge on this part, too.</p><p>Suppose there is a software (not a browser) running on my PC that is retrieving data from a server using HTTP protocol.</p><p>a) Would Wireshark be able to capture packets sent out if the Windows Firewall would block this outgoing traffic?</p><p>b) Would Wireshark be able to capture packets received from the server if the Windows Firewall would block this incomming traffic?</p><p>c) Would Wireshark be able to capture packets received from the server if the Windows Firewall would let them through, but "Browser Protection" decides to block that traffic.</p><p>Any insight is appreciated. Thanks Peter</p></div><div id="question-tags" class="tags-container tags">firewall intenert-security blocking capturing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '14, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/669b7fab6a5859dcc122a654d440d7fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phunsoft&#39;s gravatar image" /><p>phunsoft<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phunsoft has no accepted answers">0%</span></p></div></div><div id="comments-container-38077" class="comments-container"></div><div id="comment-tools-38077" class="comment-tools"></div><div class="clear"></div><div id="comment-38077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38095"></span>

<div id="answer-container-38095" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38095-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In a win7 environment it is winpcap that is actually capturing traffic not wireshark itself. On the inbound path that packets are captured before any local FW / Security Software sees them. On the outbound path it is after the FW/Security. So if the FW blocks outbound traffic you won't see it.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '14, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-38095" class="comments-container"><span id="38096"></span><div id="comment-38096" class="comment"><div id="post-38096-score" class="comment-score"></div><div class="comment-text"><p>Hi Matthias, Just the answer I've been looking for! Thanks a lot.</p><p>Regards Peter</p></div><div id="comment-38096-info" class="comment-info"><span class="comment-age">(24 Nov '14, 04:22)</span> phunsoft</div></div></div><div id="comment-tools-38095" class="comment-tools"></div><div class="clear"></div><div id="comment-38095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

