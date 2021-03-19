+++
type = "question"
title = "How can I note external events?"
description = '''I&#x27;m trying to debug something, a flaky Bluetooth stream, that has a lot of data and relatively rare issues. Ideally, what I&#x27;d like to be able to do is to start Wireshark running and then have a button I can press that will, in real time, insert markers in to the packet capture stream. Then I could g...'''
date = "2014-09-20T11:44:00Z"
lastmod = "2014-09-20T15:57:00Z"
weight = 36484
keywords = [ "events", "mark" ]
aliases = [ "/questions/36484" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I note external events?](/questions/36484/how-can-i-note-external-events)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36484-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to debug something, a flaky Bluetooth stream, that has a lot of data and relatively rare issues. Ideally, what I'd like to be able to do is to start Wireshark running and then have a button I can press that will, in real time, insert markers in to the packet capture stream. Then I could go back and look carefully at the traffic around the time of events.</p><p>Does that exist? And if not, what's the best way to record markers like that and make use of them in Wireshark?</p></div><div id="question-tags" class="tags-container tags">events mark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '14, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/e2a701576a423fb2ec04d5b639899406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wpietri&#39;s gravatar image" /><p>wpietri<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wpietri has no accepted answers">0%</span></p></div></div><div id="comments-container-36484" class="comments-container"></div><div id="comment-tools-36484" class="comment-tools"></div><div class="clear"></div><div id="comment-36484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36485"></span>

<div id="answer-container-36485" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36485-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Nothing such as that exists in Wireshark.</p><p>It might be a useful enhancement. The pcap file format doesn't have any mechanism to support that, but the pcap-ng format, which is the default, is extensible, so we could add, for example, an "external event" block type that contains user-specified text.</p><p>Enhancement requests can be filed at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '14, 15:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-36485" class="comments-container"><span id="36496"></span><div id="comment-36496" class="comment"><div id="post-36496-score" class="comment-score"></div><div class="comment-text"><p>Thanks! That's helpful; there's so much good stuff in Wireshark I have a hard time telling when something definitely isn't there. For now I think I'll just make a little script that logs keypresses with fine-grained timestamps. But that would be a cool feature.</p></div><div id="comment-36496-info" class="comment-info"><span class="comment-age">(21 Sep '14, 14:42)</span> wpietri</div></div><span id="36498"></span><div id="comment-36498" class="comment"><div id="post-36498-score" class="comment-score"></div><div class="comment-text"><p>If you file an enhancement request, that'll at least make a record of it in the bug database, so that people can find it, discuss it, and work on it more easily; please do so if you'd like to have the feature.</p></div><div id="comment-36498-info" class="comment-info"><span class="comment-age">(21 Sep '14, 15:02)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-36485" class="comment-tools"></div><div class="clear"></div><div id="comment-36485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

