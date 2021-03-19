+++
type = "question"
title = "Startup Traffic"
description = '''I have detected an inusual network traffic in PC&#x27;s startup. With a wireshark capture you see after the user introduces his password, the Windows XP Client connecting to remote registry of the domain controller (W2000 cluster) and trying to set or query some registry keys related to terminal services...'''
date = "2014-09-20T06:30:00Z"
lastmod = "2014-09-20T06:30:00Z"
weight = 36479
keywords = [ "terminal", "traffic", "startup", "server" ]
aliases = [ "/questions/36479" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Startup Traffic](/questions/36479/startup-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36479-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have detected an inusual network traffic in PC's startup. With a wireshark capture you see after the user introduces his password, the Windows XP Client connecting to remote registry of the domain controller (W2000 cluster) and trying to set or query some registry keys related to terminal services. In brief,</p><p>Client-&gt;Domain Controler: Open Query HKLM \SYSTEM \CurrentControlSet \Control \Terminal Server\DeafultConfiguration</p><p>and followed by the secuence:</p><p>Client-&gt;Domain Controller: QueryValue request fInheritAutologon Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritResetBroken Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritReconnectSame Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritInitialProgram Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritCallBack Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritCallBackNumber Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritShadow Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritMaxSessionTime Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritMaxDesconectionTime Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritMaxIdleTime Domain controller-Client: QueryValue response</p><p>Client-&gt;Domain Controller: QueryValue request fInheritAutoclient Domain controller-Client: QueryValue response Error: WERR_BADFILE</p><p>Client-&gt;Domain Controller: QueryValue request fInheritSecurity Domain controller-Client: QueryValue response Error: WERR_BADFILE</p><p>Client-&gt;Domain Controller: QueryValue request fInheritColorDepth Domain controller-Client: QueryValue response Error: WERR_BADFILE</p><p>Client-&gt;Domain Controller: QueryValue request fpromptforpassword Domain controller-Client: QueryValue response</p><p>and there are more keys being consulted. Another hive that is consulted in the same trace is useroverride\Control Panel\Desktop with other keys. This traffic is produced after the default domain policy is applied but we don´t have any configuration for terminal server in this policy. Until I know this is not normal because PC clients in a domain don´t try to configure the terminal service. We only have the execution of a script in netlogon folder to map three server folder and certain policies that after are applied. I have seen this traffic in certain PCs but in others are different. What can produce this situation (malware, kernel driver, installed service, etc..? Can somenone help me to find the cause?</p><p>Best Regards and thanks in advance.</p></div><div id="question-tags" class="tags-container tags">terminal traffic startup server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '14, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/d483adfbcf277a7694953592d06c68b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pim&#39;s gravatar image" /><p>Pim<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pim has no accepted answers">0%</span></p></div></div><div id="comments-container-36479" class="comments-container"></div><div id="comment-tools-36479" class="comment-tools"></div><div class="clear"></div><div id="comment-36479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

