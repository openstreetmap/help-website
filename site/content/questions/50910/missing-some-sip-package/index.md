+++
type = "question"
title = "Missing some SIP package."
description = '''I capture the network log file as *.pkt and analyze it with wireshark. I filter with SIP and just show one &quot;REGISTER&quot; and one &quot;401 Unauthorized&quot; on my NB. ON another NB, it shows more of SIP package like INVITE...etc in the same captured file. Is there any possible wrong settings in wireshark on my ...'''
date = "2016-03-15T01:04:00Z"
lastmod = "2016-03-15T01:04:00Z"
weight = 50910
keywords = [ "sip" ]
aliases = [ "/questions/50910" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing some SIP package.](/questions/50910/missing-some-sip-package)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50910-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I capture the network log file as *.pkt and analyze it with wireshark. I filter with SIP and just show one "REGISTER" and one "401 Unauthorized" on my NB. ON another NB, it shows more of SIP package like INVITE...etc in the same captured file. Is there any possible wrong settings in wireshark on my NB?</p><p>Version 2.0.2 (v2.0.2-0-ga16e22e from master-2.0)</p></div><div id="question-tags" class="tags-container tags">sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '16, 01:04</strong></p><img src="https://secure.gravatar.com/avatar/b7255922ef1e35f5de3495a9bdb93bf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="godyayaya&#39;s gravatar image" /><p>godyayaya<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="godyayaya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '16, 01:09</p></div></div><div id="comments-container-50910" class="comments-container"><span id="50927"></span><div id="comment-50927" class="comment"><div id="post-50927-score" class="comment-score"></div><div class="comment-text"><p>Are you using AKAv1 authentication with IPSec? If yes, you will need to configure IPSec keys so as to decrypt the packets and see SIP messages after the 401 Unauthorized.</p></div><div id="comment-50927-info" class="comment-info"><span class="comment-age">(15 Mar '16, 07:22)</span> Pascal Quantin</div></div></div><div id="comment-tools-50910" class="comment-tools"></div><div class="clear"></div><div id="comment-50910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

