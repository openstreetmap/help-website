+++
type = "question"
title = "Is there any way to see the codecs used in voip application in wireshark(G729,AMR...)"
description = '''Hello, Is there any way to see the codecs used in VOIP application in wireshark(G729,AMR…). I want to analyse a VOIP appliocation ,in which i can see SIP methods only.I didn&#x27;t find a way to see any codecs used.Also i tried to see RTP packets,which i couldn&#x27;t find(i searched for rtp for filtering)fin...'''
date = "2013-12-24T00:50:00Z"
lastmod = "2013-12-24T15:12:00Z"
weight = 28355
keywords = [ "macosx", "codec", "srtp", "rtp", "wireshark" ]
aliases = [ "/questions/28355" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any way to see the codecs used in voip application in wireshark(G729,AMR...)](/questions/28355/is-there-any-way-to-see-the-codecs-used-in-voip-application-in-wiresharkg729amr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28355-score" class="post-score" title="current number of votes">0</div><span id="post-28355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Is there any way to see the codecs used in VOIP application in wireshark(G729,AMR…).</p><p>I want to analyse a VOIP appliocation ,in which i can see SIP methods only.I didn't find a way to see any codecs used.Also i tried to see RTP packets,which i couldn't find(i searched for rtp for filtering)find.I actuallally made a call from VOIP application and was only able to see SIP protocol.Do anyone have any idea to analyse SRTP on wireshark.I am using MAC system.I couldn't find RTP for the same call.Can anyone help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-codec" rel="tag" title="see questions tagged &#39;codec&#39;">codec</span> <span class="post-tag tag-link-srtp" rel="tag" title="see questions tagged &#39;srtp&#39;">srtp</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '13, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/f8567d265d3a5aca94d6f8922ce91303?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="surajkthomas&#39;s gravatar image" /><p><span>surajkthomas</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="surajkthomas has no accepted answers">0%</span></p></div></div><div id="comments-container-28355" class="comments-container"></div><div id="comment-tools-28355" class="comment-tools"></div><div class="clear"></div><div id="comment-28355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28374"></span>

<div id="answer-container-28374" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28374-score" class="post-score" title="current number of votes">0</div><span id="post-28374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll have to look for the SDP information exchanged between the SIP endpoints. This will tell how the media session is setup. But maybe it's non-standard, otherwise Wireshark would probably have picked it up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '13, 15:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-28374" class="comments-container"></div><div id="comment-tools-28374" class="comment-tools"></div><div class="clear"></div><div id="comment-28374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

