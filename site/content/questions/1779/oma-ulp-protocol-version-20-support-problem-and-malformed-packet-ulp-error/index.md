+++
type = "question"
title = "OMA ULP Protocol version 2.0 support problem and Malformed Packet: ULP error"
description = '''Hi, community, I&#x27;m using 1.4.3 to trace the ULP message between two testing nodes, but found that it will report Malformed Packet: ULP error. [Malformed Packet: ULP] Expert Info (Error/Malformed): Malformed Packet (Exception occurred) Message: Malformed Packet (Exception occurred) Severity level: Er...'''
date = "2011-01-17T22:41:00Z"
lastmod = "2011-01-19T20:45:00Z"
weight = 1779
keywords = [ "dissector", "error" ]
aliases = [ "/questions/1779" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OMA ULP Protocol version 2.0 support problem and Malformed Packet: ULP error](/questions/1779/oma-ulp-protocol-version-20-support-problem-and-malformed-packet-ulp-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1779-score" class="post-score" title="current number of votes">0</div><span id="post-1779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, community, I'm using 1.4.3 to trace the ULP message between two testing nodes, but found that it will report Malformed Packet: ULP error.</p><p>[Malformed Packet: ULP] Expert Info (Error/Malformed): Malformed Packet (Exception occurred) Message: Malformed Packet (Exception occurred) Severity level: Error Group: Malformed</p><p>even the msisdn part cannot be decoded successfully, does anyone know the ULP protocol version supported in 1.4.3?</p><p>0000 00 26 02 00 00 c0 00 41 90 1c 44 c9 53 ff ff ff 0010 ff ff ff fc 05 55 03 37 40 05 80 03 84 40 0f 00 0020 b0 00 28 64 00 80</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '11, 22:41</strong></p><img src="https://secure.gravatar.com/avatar/725b10af90ffbbe2613a815466f70267?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eyimjia&#39;s gravatar image" /><p><span>eyimjia</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eyimjia has no accepted answers">0%</span></p></div></div><div id="comments-container-1779" class="comments-container"></div><div id="comment-tools-1779" class="comment-tools"></div><div class="clear"></div><div id="comment-1779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1780"></span>

<div id="answer-container-1780" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1780-score" class="post-score" title="current number of votes">1</div><span id="post-1780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="eyimjia has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the asn1 spec in wireshark/asn1/ulp -- Taken from OMA UserPlane Location Protocol -- http://www.openmobilealliance.org/technical/release_program/docs/SUPL/V2_0-20080627-C/OMA-TS-ULP-V2_0-20080627-C.pdf You could open a bug report at https://bugs.wireshark.org/bugzilla/ including a small capture file ilusstrating the problem. You could also try a development version from http://www.wireshark.org/download/automated/</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '11, 23:01</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-1780" class="comments-container"><span id="1784"></span><div id="comment-1784" class="comment"><div id="post-1784-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply, I've tried the latest development version, but it still doesn't ok, I'm not sure it's a bug or a protocol compliance issue, because the protocl version I'm using is OMA-TS-ULP-V2_0-20100806-D, more elements are added compared with 20080627-C, the error was reported on a common element that I've checked no change happened between the version I'm using and the version WireShark supports. Do you have information whether Wireshark will have any plan to upgrade the ULP version?</p></div><div id="comment-1784-info" class="comment-info"><span class="comment-age">(18 Jan '11, 01:00)</span> <span class="comment-user userinfo">eyimjia</span></div></div><span id="1793"></span><div id="comment-1793" class="comment"><div id="post-1793-score" class="comment-score">1</div><div class="comment-text"><p>Hi, No plans exist to upgrade any protocol, it all depends on contributors intrested in doing the updates. You could extract the asn.1 from teh OMA spec like here http://anonsvn.wireshark.org/viewvc/trunk/asn1/ulp/ attach it to a bug report and some one might update the dissector. BTW ther seems to be a version 3 as well. If you include your failing trace some one might figure out what the problem is. Regards Anders</p></div><div id="comment-1793-info" class="comment-info"><span class="comment-age">(18 Jan '11, 11:58)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="1823"></span><div id="comment-1823" class="comment"><div id="post-1823-score" class="comment-score"></div><div class="comment-text"><p>Please refer to https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5593 if you meet similar problem.</p></div><div id="comment-1823-info" class="comment-info"><span class="comment-age">(19 Jan '11, 20:45)</span> <span class="comment-user userinfo">eyimjia</span></div></div></div><div id="comment-tools-1780" class="comment-tools"></div><div class="clear"></div><div id="comment-1780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

