+++
type = "question"
title = "FCS incorrect"
description = '''Hi, We are facing an issue in our network. To debug this issue when we decided to do a capture using wireshark, the capture shows some frames with &quot;Frame check sequence: 0xa78b22ce [incorrect, should be 0x56e60339]&quot;. The wireshark version that this is seen on was 1.0.4. Then I upgraded to the latest...'''
date = "2011-07-18T02:10:00Z"
lastmod = "2011-07-18T02:23:00Z"
weight = 5092
keywords = [ "fcs", "error" ]
aliases = [ "/questions/5092" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [FCS incorrect](/questions/5092/fcs-incorrect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5092-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are facing an issue in our network. To debug this issue when we decided to do a capture using wireshark, the capture shows some frames with "Frame check sequence: 0xa78b22ce [incorrect, should be 0x56e60339]". The wireshark version that this is seen on was 1.0.4. Then I upgraded to the latest version of wireshark, i.e. 1.6.0. And this same trace does not show this FCS incorrect anymore. It only says "Trailer: a78b22ce". So now I am confused if the previous wireshark was actually showing us an FCS error or not? Which wireshark is showing the right information?</p></div><div id="question-tags" class="tags-container tags">fcs error</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '11, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/cbb4a16d75609625cddf7ac54ec28b5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws_user&#39;s gravatar image" /><p>ws_user<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws_user has no accepted answers">0%</span></p></div></div><div id="comments-container-5092" class="comments-container"></div><div id="comment-tools-5092" class="comment-tools"></div><div class="clear"></div><div id="comment-5092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5095"></span>

<div id="answer-container-5095" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5095-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might need to enable "Assume frames have FCS" in the Ethernet protocol preferences.</p><p>BTW (as a personal interest) what NIC / Capture hardware have you used that passes the FCS to Wireshark?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '11, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5095" class="comments-container"><span id="5098"></span><div id="comment-5098" class="comment"><div id="post-5098-score" class="comment-score"></div><div class="comment-text"><p>I have tried with both "Assume frames have FCS" enabled as well as disabled on the newer version (1.6.0) in both cases I get the same result i.e. frame only shows "Trailer: a78b22ce". On new version it never says as FCS incorrect or anything. The old version does not have that option under preferences / protocol / ethernet! I was using Dell laptop E6400 with Broadcom netextreme gige NIC, the setup was a port mirrored cisco router and laptop connected to mirrored port. Not every frame shows to be carrying FCS / trailer only some frames have it out of which in problem situation older version is showing 90% having this FCS incorrect thing. The cisco'c CRC counter is always 0!!</p></div><div id="comment-5098-info" class="comment-info"><span class="comment-age">(18 Jul '11, 03:45)</span> ws_user</div></div><span id="5100"></span><div id="comment-5100" class="comment"><div id="post-5100-score" class="comment-score"></div><div class="comment-text"><p>FYI, I converted your answer to a comment to keep the Q&amp;A nature of this forum.</p><p>Can you tell if the FCS maybe only exists for outgoing frames?</p></div><div id="comment-5100-info" class="comment-info"><span class="comment-age">(18 Jul '11, 05:33)</span> Jasper ♦♦</div></div><span id="5113"></span><div id="comment-5113" class="comment"><div id="post-5113-score" class="comment-score"></div><div class="comment-text"><p>Hi, FCS incorrect is seen on both inbound and outbound frames for the routers! What confuses me is that the FCS actually does not change for inbound and outbound frame. Which I think it should. Also if the router encountered an CRC error it will drop the frame and update the counter, which it is not doing. So my doubt regarding what WS is showing</p></div><div id="comment-5113-info" class="comment-info"><span class="comment-age">(19 Jul '11, 00:28)</span> ws_user</div></div><span id="6332"></span><div id="comment-6332" class="comment"><div id="post-6332-score" class="comment-score"></div><div class="comment-text"><p>The handling of the FCS in Ethernet frames was broken when the Ethernet dissector was changed to process VLAN tags itself. I've checked a fix into the trunk, and will schedule it to be included in 1.6.3.</p></div><div id="comment-6332-info" class="comment-info"><span class="comment-age">(13 Sep '11, 14:20)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5095" class="comment-tools"></div><div class="clear"></div><div id="comment-5095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

