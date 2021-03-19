+++
type = "question"
title = "How to dissect T1 Circuit Emulation CEM Traffic?"
description = '''Can wireshark interpret the CEM traffic, I have the below topology R1 -- T1 ---- R2 ---- CEM xConnect over ethernet ---- R3 --- T1 R4 I am capturing the packets between R2 - R3 and I want to see the T1 alarms, CEM header etc But all I see is raw data after the xconnect label Is there a way or any ex...'''
date = "2016-08-24T20:29:00Z"
lastmod = "2016-08-25T05:00:00Z"
weight = 55102
keywords = [ "cem", "t1" ]
aliases = [ "/questions/55102" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to dissect T1 Circuit Emulation CEM Traffic?](/questions/55102/how-to-dissect-t1-circuit-emulation-cem-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55102-score" class="post-score" title="current number of votes">0</div><span id="post-55102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can wireshark interpret the CEM traffic, I have the below topology</p><p>R1 -- T1 ---- R2 ---- CEM xConnect over ethernet ---- R3 --- T1 R4</p><p>I am capturing the packets between R2 - R3 and I want to see the T1 alarms, CEM header etc But all I see is raw data after the xconnect label Is there a way or any extension to make wireshark interpret this</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cem" rel="tag" title="see questions tagged &#39;cem&#39;">cem</span> <span class="post-tag tag-link-t1" rel="tag" title="see questions tagged &#39;t1&#39;">t1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '16, 20:29</strong></p><img src="https://secure.gravatar.com/avatar/57d7e47a498572ea4b8c895061aaeaca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vaibhav&#39;s gravatar image" /><p><span>vaibhav</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vaibhav has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '16, 05:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55102" class="comments-container"></div><div id="comment-tools-55102" class="comment-tools"></div><div class="clear"></div><div id="comment-55102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55113"></span>

<div id="answer-container-55113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55113-score" class="post-score" title="current number of votes">0</div><span id="post-55113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Dissector of almost any protocol can be added to Wireshark using C or Lua, but you need to know the protocol specification or, if not available, gather sufficient data to reverse engineer it. For Circuit over Packet, several standards exist, and Cisco may be using one of them as well as their proprietary one. Enough capture data and knowledge of the original payload which was coming from the TDM side (i.e. which timeslots were idle and which had a call on them during the capture) should reveal the truth. But this only applies if compression is switched off, otherwise you have to decompress the data before analysing the Circuit over Packet frame structure, which may require some reverse engineering as well.</p><p>The next question, however, is what you want to do with the extracted payload? The logical view of T1 is a bundle of point-to-point byte streams. The contents of most of them is not further structured (voice call), or carries some kind of direct serial data (common channel signalling, G4 fax or other digital services), or carries some kind of serial data modulated onto an analogue carrier (modem, G3 fax). To process any of these, you would need to place a tap at the output of the basic dissector, collecting the bytes belonging to your stream from the individual CoP frames and rendering them in some form (an .au file, for example) for further processing.</p><p>As for the T1 alarms - depending on the CoP standard used, the alarms may be either detected at the router performing the encapsulation and sent as logical signals over the packet network instead of the normal payload-carrying packets (to save bandwidth), or the encapsulating router may just transparently forward the contents of the T1. In the latter case, you'd e.g. have to process several (tens of) frames to conclude that there is AIS in the T1.</p><p>All in all, while Wireshark is a great tool to help you in the reverse engineering, I doubt whether it makes sense to implement all the analysis layers as given above into it. In fact, my doubt was so deep that I've decided to receive and parse the CoP packets using a task-specific application, so I can e.g. interpret the CCS to identify start and end of a call on a given timeslot, save each call into a separate .au file, and save the CCS into a pcap file so that I could use Wireshark to read it. But your application may be completely different (CAS for example, or digital services on the timeslots) so writing your own tailor-made application is probably your best way forward.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '16, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55113" class="comments-container"></div><div id="comment-tools-55113" class="comment-tools"></div><div class="clear"></div><div id="comment-55113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

