+++
type = "question"
title = "User monitoring"
description = '''Hi, I&#x27;ve been asked to monitor/log the internet usage during work hours of about a dozen employees. I want to leave it capturing for a few days but don&#x27;t want run out of memory/space.  My current idea is to capture only DNS traffic, which should give me most of what I need. Is there a better way to ...'''
date = "2013-09-09T05:26:00Z"
lastmod = "2013-09-09T06:18:00Z"
weight = 24475
keywords = [ "monitoring", "user" ]
aliases = [ "/questions/24475" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [User monitoring](/questions/24475/user-monitoring)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24475-score" class="post-score" title="current number of votes">0</div><span id="post-24475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've been asked to monitor/log the internet usage during work hours of about a dozen employees. I want to leave it capturing for a few days but don't want run out of memory/space.</p><p>My current idea is to capture only DNS traffic, which should give me most of what I need. Is there a better way to capture or a better app/method?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-monitoring" rel="tag" title="see questions tagged &#39;monitoring&#39;">monitoring</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '13, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/171d719ac7ad5773800f573d545474ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nt40lanman&#39;s gravatar image" /><p><span>nt40lanman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nt40lanman has no accepted answers">0%</span></p></div></div><div id="comments-container-24475" class="comments-container"></div><div id="comment-tools-24475" class="comment-tools"></div><div class="clear"></div><div id="comment-24475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24477"></span>

<div id="answer-container-24477" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24477-score" class="post-score" title="current number of votes">0</div><span id="post-24477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My current idea is to capture only DNS traffic, which should give me most of what I need.</p></blockquote><p>that just tells you that 'something' on a system requested name resolution. It could be a ping on the CLI, it could be the user surfing (HTTP(s)), it could any other protocol to that server, etc.. So, based on the DNS information you have no valid data about the internet <strong>usage</strong> of those users. If the system uses the local DNS cache, you won't see any internet usage at all, until the DNS cache entry times out.</p><blockquote><p>I want to leave it capturing for a few days but don't want run out of memory/space.</p></blockquote><p>that's the biggest problem if you want to use Wireshark. Wireshark is a great protocol analyzer and network troubleshooting tool, but it is not very good at (realtime) monitoring for long periods of time.</p><p>So, either you run dumpcap (no RAM problems) or you head for another (monitoring) tool. See <a href="http://www.winpcap.org/misc/links.htm">tools in the Links section of WinPcap</a> (e.g. assniffer, iNetWatcher, and similar). On Linux, <a href="http://ngrep.sourceforge.net/">ngrep</a> can be useful or maybe <a href="http://www.xplico.org/">xplico</a>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '13, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24477" class="comments-container"></div><div id="comment-tools-24477" class="comment-tools"></div><div class="clear"></div><div id="comment-24477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

