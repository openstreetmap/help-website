+++
type = "question"
title = "VOIP:  Why do DTMF events not show up on Wireshark capture"
description = '''Why do DTMF events (pressing key on phone) not show up in Wireshark capture of a Cisco IP phone. I press various keys during the phone menu after a call connects, but they don&#x27;t show up. The call and menu choices were successfully completed.'''
date = "2013-02-19T07:41:00Z"
lastmod = "2013-02-19T08:20:00Z"
weight = 18733
keywords = [ "dtmf", "voip" ]
aliases = [ "/questions/18733" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [VOIP: Why do DTMF events not show up on Wireshark capture](/questions/18733/voip-why-do-dtmf-events-not-show-up-on-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18733-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why do DTMF events (pressing key on phone) not show up in Wireshark capture of a Cisco IP phone. I press various keys during the phone menu after a call connects, but they don't show up. The call and menu choices were successfully completed.</p></div><div id="question-tags" class="tags-container tags">dtmf voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '13, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/395bb5a2adb2218f4661e5093af43380?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RAS&#39;s gravatar image" /><p>RAS<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RAS has no accepted answers">0%</span></p></div></div><div id="comments-container-18733" class="comments-container"></div><div id="comment-tools-18733" class="comment-tools"></div><div class="clear"></div><div id="comment-18733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18738"></span>

<div id="answer-container-18738" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18738-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Some questions:</p><ol><li>what is your Wireshark version?</li><li>do you encrypt the SIP and RTP communication?</li></ol><p>Some hints:</p><p>If there are DTMF signals in SIP INFO packets, you will find them with this Display filter (uppercase M is intentional!): <code>sip.Method == INFO</code>. See the following capture file: <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=DTMFsipinfo.pcap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=DTMFsipinfo.pcap</a></p><p>If there are DTMF signals in RTP EVENT packets, you will find them with this Display filter: <code>rtpevent</code>. See the following capture file: <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=SIP_DTMF2.cap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=SIP_DTMF2.cap</a></p><p>If there are DTMF signals <strong>inband</strong> in the RTP audio stream, then they are just audio signals and your won't see them in Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '13, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Feb '13, 08:21</p></div></div><div id="comments-container-18738" class="comments-container"><span id="18740"></span><div id="comment-18740" class="comment"><div id="post-18740-score" class="comment-score"></div><div class="comment-text"><p>Your suggestion above was correct - I found them using sip.Method == INFO . Thank you for the help!</p></div><div id="comment-18740-info" class="comment-info"><span class="comment-age">(19 Feb '13, 08:43)</span> RAS</div></div></div><div id="comment-tools-18738" class="comment-tools"></div><div class="clear"></div><div id="comment-18738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18734"></span>

<div id="answer-container-18734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18734-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on how the Cisco phone or system works it could send the key press evnts as out of band signaling or as tones in the RTP stream or RTP evnts you have to know which method is beeing used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '13, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-18734" class="comments-container"><span id="18735"></span><div id="comment-18735" class="comment"><div id="post-18735-score" class="comment-score"></div><div class="comment-text"><p>I have tried "SIP INFO" (out of band) and "Inband" DTMF Transmit types and still nothing shows up in Wireshark. I search the capture for "DTMF" and no results appear.</p></div><div id="comment-18735-info" class="comment-info"><span class="comment-age">(19 Feb '13, 08:11)</span> RAS</div></div><span id="18737"></span><div id="comment-18737" class="comment"><div id="post-18737-score" class="comment-score"></div><div class="comment-text"><p>Well then chanses are that the tone is sent in the voice channel.</p></div><div id="comment-18737-info" class="comment-info"><span class="comment-age">(19 Feb '13, 08:17)</span> Anders ♦</div></div></div><div id="comment-tools-18734" class="comment-tools"></div><div class="clear"></div><div id="comment-18734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

