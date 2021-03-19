+++
type = "question"
title = "Capture and Store voice traffic into a Database"
description = '''I am looking for a expert Wireshark Developer to help me in customizing Wireshark.  I want to create an add-on application to Wireshark to collect the data packets related to each individual telephone call, convert the packets into individual audio files (one audio file per telephone call) and then ...'''
date = "2013-02-03T12:37:00Z"
lastmod = "2013-02-05T13:52:00Z"
weight = 18261
keywords = [ "sip", "rtp", "developer" ]
aliases = [ "/questions/18261" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture and Store voice traffic into a Database](/questions/18261/capture-and-store-voice-traffic-into-a-database)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18261-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for a expert Wireshark Developer to help me in customizing Wireshark.</p><p>I want to create an add-on application to Wireshark to collect the data packets related to each individual telephone call, convert the packets into individual audio files (one audio file per telephone call) and then store (and retrieve) the audio files from a Database. This should run on a Linux platform.</p><p>Brian Gatza [email protected] 847-783-0490 ext 113</p></div><div id="question-tags" class="tags-container tags">sip rtp developer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '13, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/c6dabb0fb442fb5057d4b2fcbba8ef61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bgatza&#39;s gravatar image" /><p>bgatza<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bgatza has no accepted answers">0%</span></p></div></div><div id="comments-container-18261" class="comments-container"><span id="18657"></span><div id="comment-18657" class="comment"><div id="post-18657-score" class="comment-score"></div><div class="comment-text"><p>Everyone - thank you for all of your assistance, it has been very helpful and has saved me from going off in the wrong direction.</p><p>Thanks, again Brian</p></div><div id="comment-18657-info" class="comment-info"><span class="comment-age">(15 Feb '13, 08:47)</span> bgatza</div></div><span id="18660"></span><div id="comment-18660" class="comment"><div id="post-18660-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-18660-info" class="comment-info"><span class="comment-age">(15 Feb '13, 09:04)</span> grahamb ♦</div></div></div><div id="comment-tools-18261" class="comment-tools"></div><div class="clear"></div><div id="comment-18261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18263"></span>

<div id="answer-container-18263" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18263-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Don't do it. Go for a real VoIP recorder.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '13, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18263" class="comments-container"><span id="18276"></span><div id="comment-18276" class="comment"><div id="post-18276-score" class="comment-score"></div><div class="comment-text"><p>I trust and appreciate your answer. Could you clarify what the downsides of using Wireshark in this manner would be? Thank you</p></div><div id="comment-18276-info" class="comment-info"><span class="comment-age">(04 Feb '13, 05:40)</span> bgatza</div></div><span id="18329"></span><div id="comment-18329" class="comment"><div id="post-18329-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Could you clarify what the downsides of using Wireshark in this manner would be</p></blockquote><p>a lot of coding work ;-)</p></div><div id="comment-18329-info" class="comment-info"><span class="comment-age">(05 Feb '13, 13:46)</span> Kurt Knochner ♦</div></div><span id="18333"></span><div id="comment-18333" class="comment"><div id="post-18333-score" class="comment-score"></div><div class="comment-text"><p>Just <em>one</em> example of an issue:</p><p>Using Wireshark to dissect and store info as you indicate would presumably mean that Wireshark would need to run for extended periods of time.</p><p>This is a non-starter. Wireshark proper accumulates state (and uses additional memory) as it dissects and thus will eventually run out of memory.</p></div><div id="comment-18333-info" class="comment-info"><span class="comment-age">(05 Feb '13, 14:05)</span> Bill Meier ♦♦</div></div><span id="18336"></span><div id="comment-18336" class="comment"><div id="post-18336-score" class="comment-score"></div><div class="comment-text"><p>What they said. From a distance it looks nice, Wireshark can capture, decode SIP and RTP, extract audio. All nice. But if you look more closely it's like a Swiss army knife. Yes it can get the job done, but it's not convenient, hell not even practical (think of sticking the knife in your nose while you try to look through the magnifying glass). Now you are looking at 'molding it into submission', to do that one job automagically. The architecture is just not a good fit. What you need is to identify the required features (capture, protocol analysis, etc) and look for that tool: a VoIP recorder.</p></div><div id="comment-18336-info" class="comment-info"><span class="comment-age">(05 Feb '13, 15:08)</span> Jaap ♦</div></div></div><div id="comment-tools-18263" class="comment-tools"></div><div class="clear"></div><div id="comment-18263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18330"></span>

<div id="answer-container-18330" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18330-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I suggest to take a look at the following open source SIP capture solution. It probably does all you need.</p><blockquote><p>HOMER SIP Capture Server: <a href="http://www.sipcapture.org/">http://www.sipcapture.org/</a></p></blockquote><p>If you need the RTP data (audio files), you better take a look at one of these tools</p><blockquote><p><a href="http://oreka.sourceforge.net/">http://oreka.sourceforge.net/</a><br />
<a href="http://sourceforge.net/projects/our/?source=navbar">http://sourceforge.net/projects/our/?source=navbar</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '13, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Feb '13, 14:38</p></div></div><div id="comments-container-18330" class="comments-container"></div><div id="comment-tools-18330" class="comment-tools"></div><div class="clear"></div><div id="comment-18330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

