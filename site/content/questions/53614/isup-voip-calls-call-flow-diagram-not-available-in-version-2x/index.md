+++
type = "question"
title = "ISUP voip calls call-flow diagram not available in version 2.x"
description = '''Hello,  I am able to see ISUP (M3UA) in the call-flow diagrams in last versions of wireshark 2.x. Same capture is being shown properly in versions 1.12.x. Do I need to configure anything special or is this a bug? Thanks. Regards. '''
date = "2016-06-22T10:17:00Z"
lastmod = "2016-07-13T06:47:00Z"
weight = 53614
keywords = [ "voipcalls", "diagram", "isup" ]
aliases = [ "/questions/53614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ISUP voip calls call-flow diagram not available in version 2.x](/questions/53614/isup-voip-calls-call-flow-diagram-not-available-in-version-2x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53614-score" class="post-score" title="current number of votes">0</div><span id="post-53614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am able to see ISUP (M3UA) in the call-flow diagrams in last versions of wireshark 2.x. Same capture is being shown properly in versions 1.12.x.</p><p>Do I need to configure anything special or is this a bug?</p><p>Thanks. Regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-voipcalls" rel="tag" title="see questions tagged &#39;voipcalls&#39;">voipcalls</span> <span class="post-tag tag-link-diagram" rel="tag" title="see questions tagged &#39;diagram&#39;">diagram</span> <span class="post-tag tag-link-isup" rel="tag" title="see questions tagged &#39;isup&#39;">isup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '16, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/bff17dd1803f438476d3122098005102?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="juamargon&#39;s gravatar image" /><p><span>juamargon</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="juamargon has no accepted answers">0%</span></p></div></div><div id="comments-container-53614" class="comments-container"></div><div id="comment-tools-53614" class="comment-tools"></div><div class="clear"></div><div id="comment-53614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53615"></span>

<div id="answer-container-53615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53615-score" class="post-score" title="current number of votes">0</div><span id="post-53615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The M3U sample found on <a href="https://wiki.wireshark.org/SampleCaptures">https://wiki.wireshark.org/SampleCaptures</a> works fine with Wireshark 2.0.4 and 2.1.0 development release (the VoIP flow graph being much nicer with 2.1.0).</p><p>Which version of Wiresahrk are you using? This used to be a problem with the first 2.0 releases but should be fixed now. If not, could you share a capture file?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '16, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-53615" class="comments-container"><span id="54031"></span><div id="comment-54031" class="comment"><div id="post-54031-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>Thanks a lot for your answer. I have checked the sample capture and it works fine in version 2.04. The flow in shown with your parameters. But it is not working with my traces.</p><p>Unfortunately I cannot share the traces I am working on, but to let you know the differences, to decode my call I need to configure MTP3=ANSI and M3UA=RFC4666.</p><p>The ANSI messages are correctly decoded, but when trying to see it as a VOIP call, it is not detected and the graph cannot be shown.</p><p>This works properly in version 1.12.4.</p></div><div id="comment-54031-info" class="comment-info"><span class="comment-age">(13 Jul '16, 04:09)</span> <span class="comment-user userinfo">juamargon</span></div></div><span id="54035"></span><div id="comment-54035" class="comment"><div id="post-54035-score" class="comment-score"></div><div class="comment-text"><p>Without any capture file, we cannot fix the issue. Be aware that a bug can be submitted as private, which means that only Wireshark core developers will have access to the attached capture. let us know if this is acceptable.</p></div><div id="comment-54035-info" class="comment-info"><span class="comment-age">(13 Jul '16, 06:47)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-53615" class="comment-tools"></div><div class="clear"></div><div id="comment-53615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

