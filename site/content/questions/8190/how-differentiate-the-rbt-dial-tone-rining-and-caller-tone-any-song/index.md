+++
type = "question"
title = "How Differentiate the RBT Dial Tone (Rining) and Caller tone (any song)"
description = '''Dear Sir/Madam, Here i want to ask question regarding the Trace capture difference betweent the RBT of dial tone and caller tone(song), the scenario is basically Partey A call to Party B, during the begining of Part A call to party B call setup Party B set caller tone instead of Rining Bell hear by ...'''
date = "2012-01-02T09:52:00Z"
lastmod = "2012-01-02T12:34:00Z"
weight = 8190
keywords = [ "laps" ]
aliases = [ "/questions/8190" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How Differentiate the RBT Dial Tone (Rining) and Caller tone (any song)](/questions/8190/how-differentiate-the-rbt-dial-tone-rining-and-caller-tone-any-song)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8190-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Sir/Madam,</p><p>Here i want to ask question regarding the Trace capture difference betweent the RBT of dial tone and caller tone(song), the scenario is basically Partey A call to Party B, during the begining of Part A call to party B call setup Party B set caller tone instead of Rining Bell hear by Party A as a Song Tone not getting ringing bell, so here i want to know, where we can found the difference between ringing RBT and Caller tone in Wireshark trace packets and also pls provide the details where we see difference with example so we can differencitae the route qulaity is this route better or not.</p><p>Your prompt reponse highly apprcitaed</p><p>Thanks and Regards, VOIPNET</p></div><div id="question-tags" class="tags-container tags">laps</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '12, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/bce36c5aea20afd053a183d6ae06fbf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Voipnet&#39;s gravatar image" /><p>Voipnet<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Voipnet has no accepted answers">0%</span></p></div></div><div id="comments-container-8190" class="comments-container"><span id="8194"></span><div id="comment-8194" class="comment"><div id="post-8194-score" class="comment-score"></div><div class="comment-text"><p>kindly help me! if any body knows pls answer my question</p></div><div id="comment-8194-info" class="comment-info"><span class="comment-age">(02 Jan '12, 10:49)</span> Voipnet</div></div></div><div id="comment-tools-8190" class="comment-tools"></div><div class="clear"></div><div id="comment-8190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8196"></span>

<div id="answer-container-8196" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8196-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can only make an educated guess what you are trying to ask here. This is what I think is the gist of it:</p><ul><li>Party A calls Party B</li><li>Party B causes Party A to hear a song instead of the expected ringing tone</li></ul><p>Assuming SIP signaling, one would look for SDP payloads in the SIP packets exchanged during call setup, which open a media path from Party B to Party A. This then defines the RTP flow containing 'far end ringing' being your 'song'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '12, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8196" class="comments-container"><span id="8232"></span><div id="comment-8232" class="comment"><div id="post-8232-score" class="comment-score"></div><div class="comment-text"><p>And that's if the carrier even allows that feature.</p></div><div id="comment-8232-info" class="comment-info"><span class="comment-age">(05 Jan '12, 08:32)</span> EricKnaus</div></div></div><div id="comment-tools-8196" class="comment-tools"></div><div class="clear"></div><div id="comment-8196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

