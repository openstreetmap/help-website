+++
type = "question"
title = "To:Wireshark developers :) and all. OSX issues with Wireshark 2.0.1 monitor mode ? ?"
description = '''Hello all, I think OSX has some issue with 2.0.1 especially when trying to sniff in monitor mode.  I do not quite understand the problem but this is my status message unable to set data link type on interface &#x27;en0&#x27; Then on suggestion i started wireshark from terminal implementing the following param...'''
date = "2016-01-14T17:56:00Z"
lastmod = "2016-01-14T18:15:00Z"
weight = 49232
keywords = [ "monitor-mode", "2.0.0" ]
aliases = [ "/questions/49232" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [To:Wireshark developers :) and all. OSX issues with Wireshark 2.0.1 monitor mode ? ?](/questions/49232/towireshark-developers-and-all-osx-issues-with-wireshark-201-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49232-score" class="post-score" title="current number of votes">0</div><span id="post-49232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I think OSX has some issue with 2.0.1 especially when trying to sniff in monitor mode.</p><p>I do not quite understand the problem but this is my status message</p><p>unable to set data link type on interface 'en0'</p><p>Then on suggestion i started wireshark from terminal implementing the following params and to start in monitor mode.</p><p>sudo wireshark -i en1 -k -I -y EN10MB</p><p>This did not solve the issue, i think the preceding stable version is working fine(1.12.9). Will this be the case going forward. How does one overcome this problem ?</p><p>Thanks Bharat C P</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-monitor-mode" rel="tag" title="see questions tagged &#39;monitor-mode&#39;">monitor-mode</span> <span class="post-tag tag-link-2.0.0" rel="tag" title="see questions tagged &#39;2.0.0&#39;">2.0.0</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '16, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/e689f2131ff3f3113d0b2cee2f420ebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BharatNT2IE&#39;s gravatar image" /><p><span>BharatNT2IE</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BharatNT2IE has no accepted answers">0%</span></p></div></div><div id="comments-container-49232" class="comments-container"></div><div id="comment-tools-49232" class="comment-tools"></div><div class="clear"></div><div id="comment-49232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49233"></span>

<div id="answer-container-49233" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49233-score" class="post-score" title="current number of votes">0</div><span id="post-49233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11364">bug 11364</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '16, 18:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49233" class="comments-container"></div><div id="comment-tools-49233" class="comment-tools"></div><div class="clear"></div><div id="comment-49233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

