+++
type = "question"
title = "Wireshark support for IEEE1722 ?"
description = '''Hello, I am trying to stream MPEG2TS using IEEE1722 protocol. I am referring IEC61883-4 standard to transmit compressed video and monitoring it at the listener end using Wireshark. Now i am facing the following issues and I fell Wireshark AVB dissector does have limitations... 1&amp;gt; As per 1722 stan...'''
date = "2014-10-28T04:31:00Z"
lastmod = "2014-11-14T03:31:00Z"
weight = 37391
keywords = [ "avb" ]
aliases = [ "/questions/37391" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark support for IEEE1722 ?](/questions/37391/wireshark-support-for-ieee1722)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37391-score" class="post-score" title="current number of votes">0</div><span id="post-37391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to stream MPEG2TS using IEEE1722 protocol. I am referring IEC61883-4 standard to transmit compressed video and monitoring it at the listener end using Wireshark. Now i am facing the following issues and I fell Wireshark AVB dissector does have limitations...</p><p>1&gt; As per 1722 standard if SPH = 1 (in CIP# header) than FDF shuold be expanded to 24bit overlapping SYT field. But I can see both SYS and FDF field though SPH = 1 .<br />
2&gt; My format Id = 0x20 which means I am transferring MPEG2TS, but my payload is displayed as audio data having LEVEL and SAMPLE field(as in case of 61883-6).</p><p>Can any one please help me to identify in case I am doing any thing wring</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-avb" rel="tag" title="see questions tagged &#39;avb&#39;">avb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '14, 04:31</strong></p><img src="https://secure.gravatar.com/avatar/8fc96b7bad1059f7eecacdbce4a0e747?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hrusikesh%20Padhy&#39;s gravatar image" /><p><span>Hrusikesh Padhy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hrusikesh Padhy has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-37391" class="comments-container"></div><div id="comment-tools-37391" class="comment-tools"></div><div class="clear"></div><div id="comment-37391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37855"></span>

<div id="answer-container-37855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37855-score" class="post-score" title="current number of votes">0</div><span id="post-37855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>I think that Wireshark is at fault here and currently displays all 1722 data as audio data, regardless of the actual composition of the 61883-Header. I've also implemented a 61883-4 MPEG2-TS-stream via AVB and face the same problem - Wireshark display the payload as audio, despite the fact that the FMT field is set to 0x20.</p><p>Furthermore I've created a custom stream (not using the 61883 interface at all), so I set the 1722 Subtype field to 0x6F (vendor specific) and the Tag field to 0x0, indicating that there's no 61883 header in this packet. Nonetheless, Wireshark interprets the data in my packet as "audio data" and even decodes the first 8 byte of the payload as a 61883 header.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '14, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/45618a9609262fe1c7295ef34944f8fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="clancy688&#39;s gravatar image" /><p><span>clancy688</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="clancy688 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-37855" class="comments-container"><span id="37856"></span><div id="comment-37856" class="comment"><div id="post-37856-score" class="comment-score"></div><div class="comment-text"><p>If you think that Wireshark requires improvement, please raise an item at the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a>, adding a capture file that illustrates the issue.</p></div><div id="comment-37856-info" class="comment-info"><span class="comment-age">(14 Nov '14, 03:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37857"></span><div id="comment-37857" class="comment"><div id="post-37857-score" class="comment-score"></div><div class="comment-text"><p>Hello Graham,</p><p>alright, I'll do that!</p></div><div id="comment-37857-info" class="comment-info"><span class="comment-age">(14 Nov '14, 03:31)</span> <span class="comment-user userinfo">clancy688</span></div></div></div><div id="comment-tools-37855" class="comment-tools"></div><div class="clear"></div><div id="comment-37855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

