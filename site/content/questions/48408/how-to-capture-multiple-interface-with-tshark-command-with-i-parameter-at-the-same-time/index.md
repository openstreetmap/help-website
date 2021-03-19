+++
type = "question"
title = "how to capture multiple interface with tshark command with -i parameter at the same time?"
description = '''how to capture multiple interface with tshark command with -i parameter at the same time? we have two interface: eth2 and eth3 , and we want to capture all of the messages in eth2 and eth3, how to do that with tshark CLI?'''
date = "2015-12-09T21:14:00Z"
lastmod = "2015-12-11T12:11:00Z"
weight = 48408
keywords = [ "interfaces", "multiple", "tshark" ]
aliases = [ "/questions/48408" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture multiple interface with tshark command with -i parameter at the same time?](/questions/48408/how-to-capture-multiple-interface-with-tshark-command-with-i-parameter-at-the-same-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48408-score" class="post-score" title="current number of votes">0</div><span id="post-48408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to capture multiple interface with tshark command with -i parameter at the same time? we have two interface: eth2 and eth3 , and we want to capture all of the messages in eth2 and eth3, how to do that with tshark CLI?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '15, 21:14</strong></p><img src="https://secure.gravatar.com/avatar/f8d41d226443162a87ad7a4e42be3c7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tayi&#39;s gravatar image" /><p><span>tayi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tayi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Dec '15, 02:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48408" class="comments-container"></div><div id="comment-tools-48408" class="comment-tools"></div><div class="clear"></div><div id="comment-48408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48409"></span>

<div id="answer-container-48409" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48409-score" class="post-score" title="current number of votes">0</div><span id="post-48409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Determine your interface numbers with "tshark -D"</p><p>Example: eth2 = 1 and eth3=2</p><p>Use following syntax: C:&gt;tshark -i 1 -i 2</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '15, 22:04</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-48409" class="comments-container"><span id="48412"></span><div id="comment-48412" class="comment"><div id="post-48412-score" class="comment-score"></div><div class="comment-text"><p>thanks, one more question, i used tshark -i eth2 -i eth3 before, but always some packages lost, what is the difference?</p></div><div id="comment-48412-info" class="comment-info"><span class="comment-age">(10 Dec '15, 00:00)</span> <span class="comment-user userinfo">tayi</span></div></div><span id="48440"></span><div id="comment-48440" class="comment"><div id="post-48440-score" class="comment-score"></div><div class="comment-text"><p>??? It's hard to say without seeing what you did. Could you have possibly not entered the adapter name exactly as it is on your machine?</p></div><div id="comment-48440-info" class="comment-info"><span class="comment-age">(10 Dec '15, 18:29)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="48459"></span><div id="comment-48459" class="comment"><div id="post-48459-score" class="comment-score"></div><div class="comment-text"><blockquote><p>ne more question, i used tshark -i eth2 -i eth3 before, but always some packages lost, what is the difference?</p></blockquote><p>There is no difference. The <code>-D</code> flag, and the ability to specify an interface by number as well as name, originally appeared in WinPcap, because network interface names are long ugly strings on NT 5 (Windows 2000) and later; tcpdump and Wireshark picked it up. <code>-D</code> is also useful on UN*Xes; the ability to specify an interface by number is less useful on UN*Xes, because the interface names are short and somewhat sensible names, such as <code>eth0</code> or <code>en0</code> or....</p><p>The packets being lost is a different matter; using interface numbers rather than names will not make any difference.</p></div><div id="comment-48459-info" class="comment-info"><span class="comment-age">(11 Dec '15, 12:11)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-48409" class="comment-tools"></div><div class="clear"></div><div id="comment-48409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

