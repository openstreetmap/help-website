+++
type = "question"
title = "Spectralink (SRP) encapsulation"
description = '''Hi, I am analyzing VoIP communications using Spectralink. Wireshark successfully detects IP protocol 119 as Spectralink, unluckily it&#x27;s not able to dissect the data payload. Since there is no encryption, we can see the RTP contents in the bytes detail, but it&#x27;s really hard to create filters on multi...'''
date = "2011-09-09T11:42:00Z"
lastmod = "2011-09-09T23:03:00Z"
weight = 6234
keywords = [ "srp", "spectralink" ]
aliases = [ "/questions/6234" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Spectralink (SRP) encapsulation](/questions/6234/spectralink-srp-encapsulation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6234-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am analyzing VoIP communications using Spectralink. Wireshark successfully detects IP protocol 119 as Spectralink, unluckily it's not able to dissect the data payload. Since there is no encryption, we can see the RTP contents in the bytes detail, but it's really hard to create filters on multiple conversations based on theses HEX values.</p><p>Even if the SRP protocol is quite old, it's still widely used today. I've searched through the site, nobody never created a SRP dissector?</p><p>There might be multiple variations, but I've found a common one with 42 bytes overhead, including 2-byte trailer</p><p>Regards, Laurent</p></div><div id="question-tags" class="tags-container tags">srp spectralink</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '11, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/e177d49ca6cc8f53ee58cb3de1c4fbaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yul_analyzer&#39;s gravatar image" /><p>yul_analyzer<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yul_analyzer has no accepted answers">0%</span></p></div></div><div id="comments-container-6234" class="comments-container"></div><div id="comment-tools-6234" class="comment-tools"></div><div class="clear"></div><div id="comment-6234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6236"></span>

<div id="answer-container-6236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6236-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could wip a LUA dissector together to get the data from the IP proto 119 packets to the RTP dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '11, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6236" class="comments-container"></div><div id="comment-tools-6236" class="comment-tools"></div><div class="clear"></div><div id="comment-6236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6242"></span>

<div id="answer-container-6242" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6242-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Without a specification for the Spectralink Radio Protocol, nobody <em>can</em> create an SRP dissector! Even if such a protocol specification is available, nobody's likely to create it unless either 1) they have the specification and they need the dissector or 2) they have the specification, they're bored, and they don't have anything more fun to do than write a dissector for the protocol. :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '11, 23:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6242" class="comments-container"><span id="6268"></span><div id="comment-6268" class="comment"><div id="post-6268-score" class="comment-score"></div><div class="comment-text"><p>I might try to create a basic dissector, is it possible to call a dissector inside one? ie. inside the SRP dissector, check if the data payload is recognized e.g as a RTP payload?</p></div><div id="comment-6268-info" class="comment-info"><span class="comment-age">(11 Sep '11, 08:00)</span> yul_analyzer</div></div><span id="6273"></span><div id="comment-6273" class="comment"><div id="post-6273-score" class="comment-score"></div><div class="comment-text"><p>Yes. I'll leave it to you to do the "inside the SRP dissector, check if the data payload is recognized e.g as a RTP payload", but, to call the RTP dissector for that:</p><ul><li><p>in your dissector's register_handoff routine, get a handle for the RTP dissector with <code>find_dissector("rtp")</code>;</p></li><li><p>when your dissector wants to dissect payload as RTP, construct a tvbuff for the data payload and use <code>call_dissector()</code> using the handle you got from <code>find_dissector()</code>.</p></li></ul></div><div id="comment-6273-info" class="comment-info"><span class="comment-age">(11 Sep '11, 10:06)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-6242" class="comment-tools"></div><div class="clear"></div><div id="comment-6242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

