+++
type = "question"
title = "EPLMN issue"
description = '''Can anyone help me out with how to filter EPLMN related data. as we are 3G providers to an operator and he is facing &quot;R&quot; symbol issue while latching onto our network. We have wireshark traces but not able to filter EPLMN related parameters to check if our MSS is sending EPLMN data or not.'''
date = "2015-05-01T02:07:00Z"
lastmod = "2015-05-02T08:59:00Z"
weight = 41998
keywords = [ "eplmn" ]
aliases = [ "/questions/41998" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [EPLMN issue](/questions/41998/eplmn-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41998-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone help me out with how to filter EPLMN related data. as we are 3G providers to an operator and he is facing "R" symbol issue while latching onto our network. We have wireshark traces but not able to filter EPLMN related parameters to check if our MSS is sending EPLMN data or not.</p></div><div id="question-tags" class="tags-container tags">eplmn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '15, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/0bcc91c22d1a15a83aeeb40400aebb40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Surya&#39;s gravatar image" /><p>Surya<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Surya has no accepted answers">0%</span></p></div></div><div id="comments-container-41998" class="comments-container"></div><div id="comment-tools-41998" class="comment-tools"></div><div class="clear"></div><div id="comment-41998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42022"></span>

<div id="answer-container-42022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42022-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If an EPLMN list is being presented, it would be in the NAS messaging in the MSC's acceptance of the CS attach or location area update. What exactly do you have a packet capture of (Iu/A, IuB, Air)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '15, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-42022" class="comments-container"><span id="42050"></span><div id="comment-42050" class="comment"><div id="post-42050-score" class="comment-score"></div><div class="comment-text"><p>I have a normal wireshark trace captured from MSS in which the subscriber was latched.</p></div><div id="comment-42050-info" class="comment-info"><span class="comment-age">(03 May '15, 21:29)</span> Surya</div></div><span id="42070"></span><div id="comment-42070" class="comment"><div id="post-42070-score" class="comment-score"></div><div class="comment-text"><p>So to be clear, you have a RANAP packet capture of Iu control to an RNC, when the subscriber is moving to a roaming network with an active location area update, and you want to confirm where the EPLMN info would be if it was there to be found?</p><p>If not encrypted (as NAS at this level often is), the location update answer from the MSC would have an EPLMN list if one was to be included. Does that answer your question?</p></div><div id="comment-42070-info" class="comment-info"><span class="comment-age">(04 May '15, 17:35)</span> Quadratic</div></div><span id="42226"></span><div id="comment-42226" class="comment"><div id="post-42226-score" class="comment-score"></div><div class="comment-text"><p>no because I myself want to filter it in the traces and want to prove the seeker operator with the help of evidences that the EPLMN parameter are being sent from MSS.</p></div><div id="comment-42226-info" class="comment-info"><span class="comment-age">(08 May '15, 11:26)</span> Surya</div></div><span id="42243"></span><div id="comment-42243" class="comment"><div id="post-42243-score" class="comment-score"></div><div class="comment-text"><p>I'm confused. :)</p><p>You have the trace file, you have the location update accept message, and you want to look at it to see if it contained an EPLMN list. So, what is it that you are unable to do or need assistance with?</p><p>For filtering for the one subscriber, I'd start in Wireshark by going to Edit &gt; Preferences &gt; Protocols &gt; SCCP and making sure "Trace Associations" is checked. After that, search on the subscriber IMSI (assuming it's contained in the trace, eg: in an identification request/response exchange). Then, from that take the SCCP association and search on that for the dialogue of the location update. Finally check the location update accept for an EPLMN list.</p></div><div id="comment-42243-info" class="comment-info"><span class="comment-age">(08 May '15, 18:15)</span> Quadratic</div></div><span id="42246"></span><div id="comment-42246" class="comment"><div id="post-42246-score" class="comment-score"></div><div class="comment-text"><p>Also try filter "gsm_map.ms.eplmn_List". Again you never did confirm what type of trace this was, so depending on what state the message is in in your trace (eg: encrypted) that may or may not display anything.</p></div><div id="comment-42246-info" class="comment-info"><span class="comment-age">(08 May '15, 18:26)</span> Quadratic</div></div></div><div id="comment-tools-42022" class="comment-tools"></div><div class="clear"></div><div id="comment-42022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

