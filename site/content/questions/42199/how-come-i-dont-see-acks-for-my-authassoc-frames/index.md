+++
type = "question"
title = "How come I don&#x27;t see Acks for my Auth/Assoc frames?"
description = '''Aren&#x27;t all unicast frames supposed to be Ack&#x27;d? I never see Acks for Authentication and Association frames. Am I missing something?'''
date = "2015-05-07T16:21:00Z"
lastmod = "2015-05-08T11:31:00Z"
weight = 42199
keywords = [ "802.11" ]
aliases = [ "/questions/42199" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How come I don't see Acks for my Auth/Assoc frames?](/questions/42199/how-come-i-dont-see-acks-for-my-authassoc-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42199-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Aren't all unicast frames supposed to be Ack'd? I never see Acks for Authentication and Association frames. Am I missing something?</p></div><div id="question-tags" class="tags-container tags">802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '15, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/24fad929236ae147d8ccfb56847888ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elin05&#39;s gravatar image" /><p>elin05<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elin05 has no accepted answers">0%</span></p></div></div><div id="comments-container-42199" class="comments-container"></div><div id="comment-tools-42199" class="comment-tools"></div><div class="clear"></div><div id="comment-42199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42229"></span>

<div id="answer-container-42229" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42229-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>To answer your question: Aren't all unicast frames supposed to be Ack'd?</p><p>Yes, assuming a DCF/EDCA channel access method is being implemented in your WLAN. Nearly all WLAN’s utilize DCF and/or EDCA methods. Assuming we have a DCF, then “all individually addressed traffic uses immediate positive acknowledgment (ACK frame) where retransmission is scheduled by the sender if no ACK is received.” Reference IEEE-2012 specification, section 9.3.1. Also, the station does not send an ACK frame in response to an Action NoAck frame. Saying all that, please refer to this link for an expected WiFi association exchange: <a href="https://drive.google.com/file/d/0B80gG9wZvGF0ZU5Wd2xSTnluQ0U/view?usp=sharing">https://drive.google.com/file/d/0B80gG9wZvGF0ZU5Wd2xSTnluQ0U/view?usp=sharing</a></p><p>To answer your main question: How come I don't see Acks for my Auth/Assoc frames?</p><p>This could be a result of many different factors:</p><ol><li>Noisy or busy RF environment = your adapter cannot capture all the traffic that exists on the channel</li><li>Driver is dumping certain frames before delivering to host</li><li>A capture filter is removing ACK frames = not likely if you are seeing ACK frames for Data</li></ol><p>From experience, a majority of my captures do not show ACK frames for the Authentication and Association frames. The capture provided in the link was performed in a RF shielded room with no other 2.4GHz interfering devices present. It also was done with a known working adapter/driver combination.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '15, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-42229" class="comments-container"><span id="42230"></span><div id="comment-42230" class="comment"><div id="post-42230-score" class="comment-score"></div><div class="comment-text"><p>Why do all the frames in your capture show 0x0 FCS? (They were all flagged by my color filter wlan.fcs_bad==1)</p></div><div id="comment-42230-info" class="comment-info"><span class="comment-age">(08 May '15, 12:13)</span> elin05</div></div><span id="42231"></span><div id="comment-42231" class="comment"><div id="post-42231-score" class="comment-score"></div><div class="comment-text"><p>That is definitely my WiFi adapter driver stripping the FCS and replacing it with zeros. On another WiFi adapter driver, I see the correct FCS. But some of the ACK's are missing.</p></div><div id="comment-42231-info" class="comment-info"><span class="comment-age">(08 May '15, 12:20)</span> Amato_C</div></div><span id="42236"></span><div id="comment-42236" class="comment"><div id="post-42236-score" class="comment-score"></div><div class="comment-text"><p>"But some of the ACK's are missing." Why are your ACKs missing? Could it be for the same reason as mine?</p></div><div id="comment-42236-info" class="comment-info"><span class="comment-age">(08 May '15, 14:28)</span> elin05</div></div><span id="42242"></span><div id="comment-42242" class="comment"><div id="post-42242-score" class="comment-score"></div><div class="comment-text"><p>In my case, the only difference is the WiFi adapter and driver.</p></div><div id="comment-42242-info" class="comment-info"><span class="comment-age">(08 May '15, 18:08)</span> Amato_C</div></div></div><div id="comment-tools-42229" class="comment-tools"></div><div class="clear"></div><div id="comment-42229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

