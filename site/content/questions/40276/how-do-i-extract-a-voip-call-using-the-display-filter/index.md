+++
type = "question"
title = "How do I extract a VoIP call using the display filter"
description = '''How to extract a single voip call from a pcap with many using the display filter.'''
date = "2015-03-05T03:47:00Z"
lastmod = "2015-03-18T07:32:00Z"
weight = 40276
keywords = [ "voipcalls", "extract", "voip" ]
aliases = [ "/questions/40276" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I extract a VoIP call using the display filter](/questions/40276/how-do-i-extract-a-voip-call-using-the-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40276-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to extract a single voip call from a pcap with many using the display filter.</p></div><div id="question-tags" class="tags-container tags">voipcalls extract voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '15, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/d84edda6d7ff1f34a88b26a9b8fbcc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tarmongaidon&#39;s gravatar image" /><p>tarmongaidon<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tarmongaidon has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Mar '15, 07:33</p></div></div><div id="comments-container-40276" class="comments-container"><span id="40290"></span><div id="comment-40290" class="comment"><div id="post-40290-score" class="comment-score"></div><div class="comment-text"><p>What's wrong with clicking 'Prepare filter' in the first dialog?</p></div><div id="comment-40290-info" class="comment-info"><span class="comment-age">(05 Mar '15, 08:15)</span> Jaap ♦</div></div><span id="40320"></span><div id="comment-40320" class="comment"><div id="post-40320-score" class="comment-score"></div><div class="comment-text"><p>Absolutely nothing Jaap, that's a better way of getting the call ID. Is there an easier way of getting the ssrc value?</p></div><div id="comment-40320-info" class="comment-info"><span class="comment-age">(06 Mar '15, 02:40)</span> tarmongaidon</div></div><span id="40335"></span><div id="comment-40335" class="comment"><div id="post-40335-score" class="comment-score"></div><div class="comment-text"><p>Could you please the text of your question as an answer to the question, and then edit the text of the question as "How do I display one VoIP call in a capture with multiple calls?" or something such as that, so that the actual answer shows up as an answer and this shows up as an <em>answered</em> question; that better fits the way Q&amp;A sites are intended to be used, and would allow alternative answers (e.g., if <a href="http://wiki.wireshark.org/Mate">MATE</a> could be somehow used for this).</p></div><div id="comment-40335-info" class="comment-info"><span class="comment-age">(06 Mar '15, 18:12)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-40276" class="comment-tools"></div><div class="clear"></div><div id="comment-40276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40657"></span>

<div id="answer-container-40657" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40657-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi All,</p><p>Being a VoIP support tech there have been numerous occasions where I've had to extract just one call from a pcap with 100's of calls.</p><p>This is not any easy task. After a lot of googling around I haven't found this process documented yet.</p><p>Having spent a couple of hours on it I've found a way of using the display filter to filter for the ssrc and Call-ID values and thought I'd share this with you guys:</p><p>1 - Open wireshark and find the desired call by navigating to Telephony -&gt; VoIP Calls. Then click the Flow button to get the call flow.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/VoIP_Calls_ehIxspA.JPG" alt="alt text" /></p><p>2 - Click on the Invite (or any other SIP message) and drill down to the message header and copy the call-ID value. Alternatively you could click 'prepare filter' in the above dialog to automagically prepare a filter with the Call-ID.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Call-ID_sP06xod.JPG" alt="alt text" /></p><p>3 - Select an RTP packet on each stream and note down the Synchronization Source identifier (ssrc) value for all streams.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ssrc_exnR4fR.JPG" alt="alt text" /></p><p>4 - Use the following display filter and enter the values copied from the previous steps (or modify the existing filter if you clicked 'prepare filter' above:</p><p>rtcp.senderssrc==[ssrcvalue1] or rtcp.senderssrc==[ssrcvalue2] or rtp.ssrc==[ssrcvalue1] or rtp.ssrc==[ssrcvalue2] or sip.Call-ID==[Call ID]</p><p>5 - Navigate to File -&gt; Export Specified Packets and make sure that the 'Displayed' radio button is highlighted, give it a file name and save the file.</p><p>Note that you might need to decode the UDP packets as RTP when you open the file on another workstation.</p><p>I hope this saves you guys some time, I've been trying to figure this out on and off for a while now. Any suggestions on making the process less of a PITA or better are welcome.</p><p>Peace out :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '15, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/d84edda6d7ff1f34a88b26a9b8fbcc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tarmongaidon&#39;s gravatar image" /><p>tarmongaidon<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tarmongaidon has no accepted answers">0%</span></p></img></div></div><div id="comments-container-40657" class="comments-container"></div><div id="comment-tools-40657" class="comment-tools"></div><div class="clear"></div><div id="comment-40657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

