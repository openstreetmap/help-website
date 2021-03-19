+++
type = "question"
title = "VoIP profile"
description = '''Hi all, First question here! Sorry if this has been covered - I couldn&#x27;t find the answer anywhere. I am looking for some advice on setting up a VoIP profile, to really get the most out of my captures. I have been using Wireshark now for approx 3 months and am really starting to find my feet, but hav...'''
date = "2015-02-05T14:51:00Z"
lastmod = "2015-02-07T07:18:00Z"
weight = 39676
keywords = [ "sip", "rtp", "voip" ]
aliases = [ "/questions/39676" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VoIP profile](/questions/39676/voip-profile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39676-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>First question here! Sorry if this has been covered - I couldn't find the answer anywhere.</p><p>I am looking for some advice on setting up a VoIP profile, to really get the most out of my captures.</p><p>I have been using Wireshark now for approx 3 months and am really starting to find my feet, but have a long way to go.</p><p>I am having to install &amp; maintain hosted PBX systems (Gamma Horizon) and PBX onto SIP trunks. Any advice on columns, filtered traffic and things to look out for when it comes to dropped calls, one-way transmission etc.</p><p>Any help would be appreciated. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">sip rtp voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '15, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/293ddb924d4ae89abdb5fc6cc1d8de43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VoidedSquirrel&#39;s gravatar image" /><p>VoidedSquirrel<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VoidedSquirrel has no accepted answers">0%</span></p></div></div><div id="comments-container-39676" class="comments-container"><span id="39690"></span><div id="comment-39690" class="comment"><div id="post-39690-score" class="comment-score"></div><div class="comment-text"><p>I am new to this....</p><p>.... but seem to get lots of views but no responses. Am I doing something wrong????</p><p>Was under the impression this was a lively, helpful community!!!!</p></div><div id="comment-39690-info" class="comment-info"><span class="comment-age">(06 Feb '15, 13:09)</span> VoidedSquirrel</div></div></div><div id="comment-tools-39676" class="comment-tools"></div><div class="clear"></div><div id="comment-39676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39694"></span>

<div id="answer-container-39694" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39694-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Often when a question is asked as generically as this it's difficult to answer. In a way you're really asking "How can I support a SIP-based VoIP network", which is a huge topic of its own.</p><p>Personally I find there's little benefit in customizing too much with profiles for something like SIP since the 'optimal layout' depends too much on what you're looking for in that moment. If you have a specific goal, the tools in Wireshark (like custom columns/sorting, or the different time field types) can help, but you need to start with a question.</p><p>As a 'default', I do set a custom colour rule for SIP traffic just so it stands out over the default for UDP (I make it purple), and I also include SIP errors in my catch-all 'something is wrong or at least cautionary' colour rule that I set above everything else, but those are the only SIP-specific things I would start with, where what columns I'd want to set would depend a lot on what I was trying to do (and why I was opening that packet capture file to begin with).</p><p>Now, for just 'validating a VoIP network', you need to develop a test plan, where Wireshark is just one tool that can be used within the scope of that plan. Examples of things you'd want to validate would be:</p><ul><li>Call setup time</li><li>End-to-end delay of RTP/media</li><li>Jitter</li><li>Capacity of the network to support the calls.</li><li>Network QoS design (queuing model, prioritization, marking/classification, etc.)</li><li>Per-use-case call flow validation</li><li>High-availability/redundancy testing and validation.</li></ul><p>If you are looking at this as an "example call that didn't work", as with any signaling flow the key is to follow the call flow. Where did it break? For your question of what things should be watched out for, I can say with SIP that every vendor seems to do something differently and I've seen it break at just about every possible point, so that question is just too open-ended to answer. I've literally had a case where a UDP port number was dynamically changing for the RTP stream mid-call after a given number of seconds in a call, so there's no quick checklist to cover all the possible bases here - just follow the call flow and make sure your test plan includes all the use-cases you have for the service.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '15, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-39694" class="comments-container"><span id="39695"></span><div id="comment-39695" class="comment"><div id="post-39695-score" class="comment-score"></div><div class="comment-text"><p>That's great - thanks for your help. Much appreciated.</p></div><div id="comment-39695-info" class="comment-info"><span class="comment-age">(07 Feb '15, 11:26)</span> VoidedSquirrel</div></div><span id="39711"></span><div id="comment-39711" class="comment"><div id="post-39711-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-39711-info" class="comment-info"><span class="comment-age">(09 Feb '15, 05:37)</span> Jaap ♦</div></div></div><div id="comment-tools-39694" class="comment-tools"></div><div class="clear"></div><div id="comment-39694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

