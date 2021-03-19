+++
type = "question"
title = "How to know that RTP dynamic payload type carries video or voice codec ?"
description = '''Hello I&#x27;m newbie here.  I need to know about RTP payload type. I&#x27;ve got dynamic RTP payload type on my wireshark when I did video call using yahoo messenger. Then it appears many RTP protocols and the info shows: PT=DynamicRTP-Type-123  and also PT=DynamicRTP-Type-97 Since it dynamic payload type, h...'''
date = "2013-05-23T08:20:00Z"
lastmod = "2013-05-23T08:25:00Z"
weight = 21415
keywords = [ "analyze", "dynamic", "rtp", "payload" ]
aliases = [ "/questions/21415" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to know that RTP dynamic payload type carries video or voice codec ?](/questions/21415/how-to-know-that-rtp-dynamic-payload-type-carries-video-or-voice-codec)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21415-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I'm newbie here. I need to know about RTP payload type. I've got dynamic RTP payload type on my wireshark when I did video call using yahoo messenger.</p><p>Then it appears many RTP protocols and the info shows: PT=DynamicRTP-Type-123 and also PT=DynamicRTP-Type-97</p><p>Since it dynamic payload type, how could I know which RTP protocol carries video packets and which carries voice packets? CMIIW Thanks in advance :)</p></div><div id="question-tags" class="tags-container tags">analyze dynamic rtp payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '13, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/ae04a5bb0f41c19e53fcd87ccf89cfb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sekar&#39;s gravatar image" /><p>sekar<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sekar has no accepted answers">0%</span></p></div></div><div id="comments-container-21415" class="comments-container"></div><div id="comment-tools-21415" class="comment-tools"></div><div class="clear"></div><div id="comment-21415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21416"></span>

<div id="answer-container-21416" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21416-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to see the setup of the RTP where the codec is "assigned" a payload type, or possibly guess from the RTP packets. Video should transfer much more data. But you still ned the setup info to know which codec is beeing used it is quite possible proprietarry codecs are beeing used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-21416" class="comments-container"><span id="21479"></span><div id="comment-21479" class="comment"><div id="post-21479-score" class="comment-score"></div><div class="comment-text"><p>well, thanks anders. 1. Yes I notice that payloadtype-123 are much more than type-97. I think that my video (which is motion-JPEG) was fragmented into packets since it has same timestamp. Am I right?</p><ol><li><p>Where could I find 'setup info'? Because I've read sooo much articles and I found that dynamic payload type 96-127 are unassigned.</p></li><li><p>Does it possible for me to replay the audio from my video call?</p></li></ol><p>Soorryy for asking too much. Need your help :)</p></div><div id="comment-21479-info" class="comment-info"><span class="comment-age">(26 May '13, 07:58)</span> sekar</div></div><span id="21483"></span><div id="comment-21483" class="comment"><div id="post-21483-score" class="comment-score"></div><div class="comment-text"><p>Hi, I hvae no idea how yahoo Messenger works or what protocols it uses to set up video calls. In SIP SDP is used to describe the media session beeing set up if you look at the packets around the time of the actual setup of the call can anything be sen there(in plain text)? Without knowing what protocols and codecs Yahoo Messenger uses it will be very hard to do what you want.</p></div><div id="comment-21483-info" class="comment-info"><span class="comment-age">(26 May '13, 12:49)</span> Anders ♦</div></div></div><div id="comment-tools-21416" class="comment-tools"></div><div class="clear"></div><div id="comment-21416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

