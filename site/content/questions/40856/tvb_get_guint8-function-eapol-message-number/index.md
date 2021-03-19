+++
type = "question"
title = "tvb_get_guint8( ) function / EAPOL message number"
description = '''Where can I find more information about the tvb_get_guint8( ) function?'''
date = "2015-03-25T13:45:00Z"
lastmod = "2015-04-02T10:28:00Z"
weight = 40856
keywords = [ "function", "eapol" ]
aliases = [ "/questions/40856" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tvb\_get\_guint8( ) function / EAPOL message number](/questions/40856/tvb_get_guint8-function-eapol-message-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40856-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Where can I find more information about the tvb_get_guint8( ) function?</p></div><div id="question-tags" class="tags-container tags">function eapol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '15, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Mar '15, 13:18</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-40856" class="comments-container"><span id="40858"></span><div id="comment-40858" class="comment"><div id="post-40858-score" class="comment-score"></div><div class="comment-text"><p>Tvbuff.h but as the function name implies it fetches a byte from the tvb at offset. What more information are you want?</p></div><div id="comment-40858-info" class="comment-info"><span class="comment-age">(25 Mar '15, 13:52)</span> Anders ♦</div></div><span id="40902"></span><div id="comment-40902" class="comment"><div id="post-40902-score" class="comment-score"></div><div class="comment-text"><p>I was able to determine that the tvb_get(tvb,offset) function tells Wireshark the length of the data to highlight in the hex display window with tvb starting at the beginning of the data passed to the dissector and the offset parameter is the location in bytes within the dissector. However, I was unable to answer my original question.<br />
I believe that Wireshark is not labeling the EAPOL key messages correctly when WPA Key descriptors are used. Please see capture at: <a href="https://drive.google.com/file/d/0B9Lstpa35JuGVzRibmYyazhFeUE/view?usp=sharing">https://drive.google.com/file/d/0B9Lstpa35JuGVzRibmYyazhFeUE/view?usp=sharing</a></p><p>Please refer to packets #9 and #11. They are both labelled as Message 4 of 4. However, packet #9 should be Message 2 of 4. I tried to determine what was causing the error. I found the dissectors-packet-ieee80211.c file and investigated lines 18327 through 18345. The dissector is using the following to distinguish between Message 2 and Message 4: counter = tvb_get_guint8(tvb, offset+11) So why does the capture show both packet #9 and packet#11 as Message 4? Message 2 should not have counter set - refer to line 18336 in the dissector file.</p></div><div id="comment-40902-info" class="comment-info"><span class="comment-age">(26 Mar '15, 08:26)</span> Amato_C</div></div><span id="40907"></span><div id="comment-40907" class="comment"><div id="post-40907-score" class="comment-score"></div><div class="comment-text"><p>It looks to me to be a dissector bug in that it simplistically expects the first byte of the 8 byte replay counter to be 0 for message 2 and non-zero for message 4. IIUC the spec says simply that the replay counter should be incremented by the Authenticator, i.e. message 4 should have a replay counter that is 1 more that that in message 2.</p></div><div id="comment-40907-info" class="comment-info"><span class="comment-age">(26 Mar '15, 09:52)</span> grahamb ♦</div></div><span id="40908"></span><div id="comment-40908" class="comment"><div id="post-40908-score" class="comment-score"></div><div class="comment-text"><p>Should I create a Wireshark bug for this issue?</p></div><div id="comment-40908-info" class="comment-info"><span class="comment-age">(26 Mar '15, 10:25)</span> Amato_C</div></div><span id="40910"></span><div id="comment-40910" class="comment"><div id="post-40910-score" class="comment-score"></div><div class="comment-text"><p>Yes, although I'm uncertain if the replay counter should always be set to 0 for the first message, but I think that's unlikely as it then doesn't have much point in being there.</p></div><div id="comment-40910-info" class="comment-info"><span class="comment-age">(26 Mar '15, 10:32)</span> grahamb ♦</div></div><span id="40911"></span><div id="comment-40911" class="comment not_top_scorer"><div id="post-40911-score" class="comment-score"></div><div class="comment-text"><p>I agree about the counter being 0. However, the logic should determine the counter values in Message 2 and Message 4. Then determine the message type where counter for Message 2 &lt; counter for Message 4.</p></div><div id="comment-40911-info" class="comment-info"><span class="comment-age">(26 Mar '15, 10:43)</span> Amato_C</div></div><span id="40912"></span><div id="comment-40912" class="comment not_top_scorer"><div id="post-40912-score" class="comment-score"></div><div class="comment-text"><p>This error has already reported. Please refer to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10557">bug #10557</a>. It was originally reported in October 2014 as a possible driver issue. However, it appears to be a dissector issue.</p></div><div id="comment-40912-info" class="comment-info"><span class="comment-age">(26 Mar '15, 10:53)</span> Amato_C</div></div></div><div id="comment-tools-40856" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-40856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41157"></span>

<div id="answer-container-41157" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41157-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Bug #10557 (EAPOL key message #2 is incorrectly labeled as Message 4 of 4 when WPA Key descriptors are used) is resolved.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '15, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span> </br></p></div></div><div id="comments-container-41157" class="comments-container"><span id="41181"></span><div id="comment-41181" class="comment"><div id="post-41181-score" class="comment-score"></div><div class="comment-text"><p>What is the logic for wireshark to flag EAPOL packet as 1/2/3/4 of 4th packet? There is no such flag as such carried in packet.</p></div><div id="comment-41181-info" class="comment-info"><span class="comment-age">(03 Apr '15, 11:27)</span> Ramprasad</div></div><span id="41182"></span><div id="comment-41182" class="comment"><div id="post-41182-score" class="comment-score"></div><div class="comment-text"><p>It depends whether the key descriptor is defined as WPA (0xFE) or RSN (0x02). New wireless routers/AP's should be utilizing RSN. In that case, the Key Information field within the 802.1X Authentication has certain parameters that define an EAPOL message as 1, 2 ,3 or 4. You can refer to the IEEE 802.11-2012 specification (sections 11.6.6.2 through 11.6.6.5) for these settings. You can download spec from IEEE website.</p></div><div id="comment-41182-info" class="comment-info"><span class="comment-age">(03 Apr '15, 12:34)</span> Amato_C</div></div></div><div id="comment-tools-41157" class="comment-tools"></div><div class="clear"></div><div id="comment-41157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

