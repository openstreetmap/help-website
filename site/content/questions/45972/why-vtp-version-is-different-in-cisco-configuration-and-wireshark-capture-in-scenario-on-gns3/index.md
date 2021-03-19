+++
type = "question"
title = "Why VTP version is different in cisco configuration and wireshark capture in scenario on GNS3??"
description = '''ESW16 VTP configuration:  ESW4 VTP configuration:  WireShark capture on the link between switches: '''
date = "2015-09-20T06:40:00Z"
lastmod = "2015-09-22T01:24:00Z"
weight = 45972
keywords = [ "vtp" ]
aliases = [ "/questions/45972" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why VTP version is different in cisco configuration and wireshark capture in scenario on GNS3??](/questions/45972/why-vtp-version-is-different-in-cisco-configuration-and-wireshark-capture-in-scenario-on-gns3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45972-score" class="post-score" title="current number of votes">0</div><span id="post-45972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>ESW16 VTP configuration: <img src="https://osqa-ask.wireshark.org/upfiles/ESW16.PNG" alt="alt text" /></p><p>ESW4 VTP configuration: <img src="https://osqa-ask.wireshark.org/upfiles/ESW4.PNG" alt="alt text" /></p><p>WireShark capture on the link between switches:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_hdWiKvm.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vtp" rel="tag" title="see questions tagged &#39;vtp&#39;">vtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '15, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/8752544ec453a6d8e08fdde4d465eca7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MehranBazgir&#39;s gravatar image" /><p><span>MehranBazgir</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MehranBazgir has no accepted answers">0%</span></p></img></div></div><div id="comments-container-45972" class="comments-container"></div><div id="comment-tools-45972" class="comment-tools"></div><div class="clear"></div><div id="comment-45972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45973"></span>

<div id="answer-container-45973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45973-score" class="post-score" title="current number of votes">3</div><span id="post-45973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are using version 1. The "VTP Version" statement in that show command only says what the switch is capable of, meanwhile you can see in the "V2 Mode" statement that it is disabled. Since it is only capable of versions 1 or 2, and version 2 is disabled, you are using version 1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '15, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></img></div></div><div id="comments-container-45973" class="comments-container"><span id="46008"></span><div id="comment-46008" class="comment"><div id="post-46008-score" class="comment-score"></div><div class="comment-text"><p>Thanks, but enabling the VTP version 2 had no effect on the capture result.</p></div><div id="comment-46008-info" class="comment-info"><span class="comment-age">(21 Sep '15, 05:29)</span> <span class="comment-user userinfo">MehranBazgir</span></div></div><span id="46009"></span><div id="comment-46009" class="comment"><div id="post-46009-score" class="comment-score"></div><div class="comment-text"><p>Thank you Quadratic. I modified my configuration and set the VTP version to 2, but the result of capturing was the same as the previous.</p><p>ESW16 new VTP configuration:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ESW16_iY4KTCl.PNG" alt="alt text" /></p><p>ESW4 new VTP configuration:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ESW4_2zhf3vW.PNG" alt="alt text" /></p><p>WireShark capture on the link between switches:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_P2NQLNr.PNG" alt="alt text" /></p></div><div id="comment-46009-info" class="comment-info"><span class="comment-age">(21 Sep '15, 05:29)</span> <span class="comment-user userinfo">MehranBazgir</span></div></div><span id="46043"></span><div id="comment-46043" class="comment"><div id="post-46043-score" class="comment-score">1</div><div class="comment-text"><p>Do the summary advertisements show version 1? I suspect not. :)</p><p>I'm being coy, but there's no difference between a join message in one version or the other. If you're running version 2, you should see it in the summary advertisements though. So, the message is a version 1 message basically. I just double-checked my memory with a real switch and confirmed this - the summaries should be V2, joins are advertised V1.</p></div><div id="comment-46043-info" class="comment-info"><span class="comment-age">(21 Sep '15, 21:20)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="46045"></span><div id="comment-46045" class="comment"><div id="post-46045-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, I got it. :)</p></div><div id="comment-46045-info" class="comment-info"><span class="comment-age">(22 Sep '15, 01:24)</span> <span class="comment-user userinfo">MehranBazgir</span></div></div></div><div id="comment-tools-45973" class="comment-tools"></div><div class="clear"></div><div id="comment-45973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

