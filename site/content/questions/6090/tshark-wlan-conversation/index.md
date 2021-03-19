+++
type = "question"
title = "tshark wlan conversation"
description = '''How do I collect wlan conversation statistic using tshark? And not connected (authenticated) to the (wireless) LAN, in promiscuous mode. Tried: tshark -qz conv,wlan but wlan is not supported with tshark. wlan is supported with wireshark... wireshark -k -i 1 -a duration:20 -z conv,wlan but the statis...'''
date = "2011-09-05T03:57:00Z"
lastmod = "2011-09-05T12:13:00Z"
weight = 6090
keywords = [ "conversation", "wlan", "tshark" ]
aliases = [ "/questions/6090" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark wlan conversation](/questions/6090/tshark-wlan-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6090-score" class="post-score" title="current number of votes">0</div><span id="post-6090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I collect wlan conversation statistic using tshark? And not connected (authenticated) to the (wireless) LAN, in promiscuous mode. Tried: tshark -qz conv,wlan but wlan is not supported with tshark.<br />
wlan is supported with wireshark... wireshark -k -i 1 -a duration:20 -z conv,wlan but the statistic can not be captured (or piped) to a file. If connected to wlan or lan, then following works well... tshark -qz conv,eth I suspect I need to build a version of tshark that supports wlan? Not a great solution for me.<br />
Any thoughts?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '11, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/e7be376b4785406601ccd297c4ce207a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joseph_blumberg&#39;s gravatar image" /><p><span>joseph_blumberg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joseph_blumberg has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-6090" class="comments-container"></div><div id="comment-tools-6090" class="comment-tools"></div><div class="clear"></div><div id="comment-6090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6099"></span>

<div id="answer-container-6099" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6099-score" class="post-score" title="current number of votes">0</div><span id="post-6099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>File a bug noting that some, but not all, of the conv, taps supported by Wireshark are supported by TShark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '11, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6099" class="comments-container"></div><div id="comment-tools-6099" class="comment-tools"></div><div class="clear"></div><div id="comment-6099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

