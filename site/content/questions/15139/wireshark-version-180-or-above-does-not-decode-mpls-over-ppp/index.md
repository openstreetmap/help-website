+++
type = "question"
title = "Wireshark version 1.8.0 or above does not decode MPLS over PPP."
description = '''Wireshark version 1.8.0 or above does not decode MPLS over PPP in the Packet Details Pane, however, Wireshark version 1.6.5 works well. the screenshot of version 1.9.0  the screenshot of version 1.6.5 '''
date = "2012-10-21T17:58:00Z"
lastmod = "2014-02-21T16:25:00Z"
weight = 15139
keywords = [ "ppp", "mpls" ]
aliases = [ "/questions/15139" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark version 1.8.0 or above does not decode MPLS over PPP.](/questions/15139/wireshark-version-180-or-above-does-not-decode-mpls-over-ppp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15139-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark version 1.8.0 or above does not decode MPLS over PPP in the Packet Details Pane, however, Wireshark version 1.6.5 works well.</p><p>the screenshot of version 1.9.0 <img src="https://osqa-ask.wireshark.org/upfiles/v190.png" /></p><p>the screenshot of version 1.6.5 <img src="https://osqa-ask.wireshark.org/upfiles/v165.png" /></p></div><div id="question-tags" class="tags-container tags">ppp mpls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '12, 17:58</strong></p><img src="https://secure.gravatar.com/avatar/85b30d9eb7197478a7e0ed4159ea28b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mildblues&#39;s gravatar image" /><p>mildblues<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mildblues has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '12, 18:06</p></div></div><div id="comments-container-15139" class="comments-container"></div><div id="comment-tools-15139" class="comment-tools"></div><div class="clear"></div><div id="comment-15139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30091"></span>

<div id="answer-container-30091" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30091-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9492">bug 9492</a>, which is fixed in the trunk, but was fixed after 1.11.2 was released. I have backported the fix to the 1.8 and 1.10 branches, so it should be fixed in the next 1.8.x and 1.10.x releases.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '14, 16:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '14, 16:33</p></div></div><div id="comments-container-30091" class="comments-container"><span id="31862"></span><div id="comment-31862" class="comment"><div id="post-31862-score" class="comment-score"></div><div class="comment-text"><p>Good job! Thank you.</p></div><div id="comment-31862-info" class="comment-info"><span class="comment-age">(15 Apr '14, 20:43)</span> mildblues</div></div></div><div id="comment-tools-30091" class="comment-tools"></div><div class="clear"></div><div id="comment-30091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15143"></span>

<div id="answer-container-15143" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15143-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the different GUI style, I assume these screenshots were taken from different machines. CAn you check whether all preferences (mainly the PPP and MPLS protocol preferences) are the same on both machines?</p><p>If the problem remains, could you upload the capture file to <a href="http://www.cloudshark.org/">Cloudshark</a> and post the link to it here?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '12, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-15143" class="comments-container"><span id="15144"></span><div id="comment-15144" class="comment"><div id="post-15144-score" class="comment-score"></div><div class="comment-text"><p>Yes, you are very careful.</p><p>Wireshark version 1.9.0 is installed on a Windows XP OS, and 1.6.5 on a Windows 2003 Server OS.</p><p>I have checked the MPLS preferences. I find the two versions have different GUIs.</p><p>And I have also uploaded the capture file to Cloudshark. Its URL is: <a href="https://www.cloudshark.org/captures/3593a49ed149">https://www.cloudshark.org/captures/3593a49ed149</a></p><p>version 1.9.0: <img src="https://osqa-ask.wireshark.org/upfiles/v190-mpls.png" alt="alt text" /></p><p>version 1.6.5 <img src="https://osqa-ask.wireshark.org/upfiles/v165-mpls.png" alt="alt text" /></p></div><div id="comment-15144-info" class="comment-info"><span class="comment-age">(22 Oct '12, 01:40)</span> mildblues</div></div><span id="30076"></span><div id="comment-30076" class="comment"><div id="post-30076-score" class="comment-score"></div><div class="comment-text"><p>The above problem remains unresolved on the latest version 1.11.2.</p></div><div id="comment-30076-info" class="comment-info"><span class="comment-age">(21 Feb '14, 00:54)</span> mildblues</div></div><span id="31864"></span><div id="comment-31864" class="comment"><div id="post-31864-score" class="comment-score"></div><div class="comment-text"><p>Try 1.11.3 - it should have the fix.</p></div><div id="comment-31864-info" class="comment-info"><span class="comment-age">(15 Apr '14, 21:39)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-15143" class="comment-tools"></div><div class="clear"></div><div id="comment-15143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

