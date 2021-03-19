+++
type = "question"
title = "how to remove the VLAN header in wireshark"
description = '''how to remove the VLAN header in wireshark, is there has any operation to remove the vlan header '''
date = "2017-03-07T01:45:00Z"
lastmod = "2017-03-07T05:45:00Z"
weight = 59883
keywords = [ "vlan" ]
aliases = [ "/questions/59883" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to remove the VLAN header in wireshark](/questions/59883/how-to-remove-the-vlan-header-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59883-score" class="post-score" title="current number of votes">0</div><span id="post-59883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to remove the VLAN header in wireshark, is there has any operation to remove the vlan header</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '17, 01:45</strong></p><img src="https://secure.gravatar.com/avatar/853d7093103a60a3b0083b42b705b99e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neil_hao&#39;s gravatar image" /><p><span>neil_hao</span><br />
<span class="score" title="26 reputation points">26</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neil_hao has no accepted answers">0%</span></p></div></div><div id="comments-container-59883" class="comments-container"></div><div id="comment-tools-59883" class="comment-tools"></div><div class="clear"></div><div id="comment-59883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59886"></span>

<div id="answer-container-59886" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59886-score" class="post-score" title="current number of votes">0</div><span id="post-59886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="neil_hao has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is perfectly capable to show you the details of the VLAN header and continue dissection of the rest of the frame. If you are looking at <em>changing</em> the frame and saving that, then Wireshark is not the tool for you. See the <a href="https://wiki.wireshark.org/Tools">Wiki</a> for a long list of tools to work with capture files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '17, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59886" class="comments-container"><span id="59887"></span><div id="comment-59887" class="comment"><div id="post-59887-score" class="comment-score">1</div><div class="comment-text"><p>TraceWrangler can do this, using an anonymization task.</p></div><div id="comment-59887-info" class="comment-info"><span class="comment-age">(07 Mar '17, 05:45)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-59886" class="comment-tools"></div><div class="clear"></div><div id="comment-59886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

