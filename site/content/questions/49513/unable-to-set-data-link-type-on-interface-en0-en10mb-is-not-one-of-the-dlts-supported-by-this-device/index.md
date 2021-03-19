+++
type = "question"
title = "Unable to set data link type on interface &#x27;en0&#x27; (EN10MB is not one of the DLTs supported by this device)."
description = '''Hello, I am using Wireshark on a 2014 MacBook Pro running El Capitan (OS X 10.11.3). Wireshark will not capture in monitor mode on my Wi-Fi en0 interface. It works fine when not in monitor mode. When I enable monitor mode in the Capture Interfaces dialog and click Start, I get this error message:  U...'''
date = "2016-01-25T15:32:00Z"
lastmod = "2016-01-29T11:45:00Z"
weight = 49513
keywords = [ "osx", "elcapitan", "monitor", "monitor-mode", "wifi" ]
aliases = [ "/questions/49513" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to set data link type on interface 'en0' (EN10MB is not one of the DLTs supported by this device).](/questions/49513/unable-to-set-data-link-type-on-interface-en0-en10mb-is-not-one-of-the-dlts-supported-by-this-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49513-score" class="post-score" title="current number of votes">0</div><span id="post-49513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am using Wireshark on a 2014 MacBook Pro running El Capitan (OS X 10.11.3). Wireshark will not capture in monitor mode on my Wi-Fi en0 interface. It works fine when not in monitor mode. When I enable monitor mode in the Capture Interfaces dialog and click Start, I get this error message:</p><blockquote><p>Unable to set data link type on interface 'en0' (EN10MB is not one of the DLTs supported by this device).</p></blockquote><p>How can I fix this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-elcapitan" rel="tag" title="see questions tagged &#39;elcapitan&#39;">elcapitan</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-monitor-mode" rel="tag" title="see questions tagged &#39;monitor-mode&#39;">monitor-mode</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '16, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/0d6e5c289d6f8bc1d0d8cfd5566e0607?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sixstring95&#39;s gravatar image" /><p><span>sixstring95</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sixstring95 has one accepted answer">100%</span></p></div></div><div id="comments-container-49513" class="comments-container"></div><div id="comment-tools-49513" class="comment-tools"></div><div class="clear"></div><div id="comment-49513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49629"></span>

<div id="answer-container-49629" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49629-score" class="post-score" title="current number of votes">0</div><span id="post-49629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sixstring95 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After playing around with Wireshark a little, I figured out that if I set my NIC into monitor mode in Wireshark and start a capture I still receive the error message. However, if I completely quit Wireshark and then restart it, I can capture in monitor mode with no problems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '16, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/0d6e5c289d6f8bc1d0d8cfd5566e0607?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sixstring95&#39;s gravatar image" /><p><span>sixstring95</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sixstring95 has one accepted answer">100%</span></p></div></div><div id="comments-container-49629" class="comments-container"></div><div id="comment-tools-49629" class="comment-tools"></div><div class="clear"></div><div id="comment-49629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49514"></span>

<div id="answer-container-49514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49514-score" class="post-score" title="current number of votes">0</div><span id="post-49514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By learning enough of the twisty little maze of classes, all different, that is Qt, and fixing <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11364">bug 11364</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '16, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49514" class="comments-container"></div><div id="comment-tools-49514" class="comment-tools"></div><div class="clear"></div><div id="comment-49514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

