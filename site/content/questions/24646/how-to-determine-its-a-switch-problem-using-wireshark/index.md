+++
type = "question"
title = "How to determine it&#x27;s a switch problem using wireshark."
description = '''Hi There, Network background: I got a call from a company to troubleshoot many issues including poor connectivity in sections of their office. The network setup was pretty simple, ISP to router, router to cisco smb 200 managed switch, from it an up link to another cisco smb 16 port switch (not manag...'''
date = "2013-09-13T06:56:00Z"
lastmod = "2013-09-14T14:04:00Z"
weight = 24646
keywords = [ "switchednetwork", "switch", "slow" ]
aliases = [ "/questions/24646" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to determine it's a switch problem using wireshark.](/questions/24646/how-to-determine-its-a-switch-problem-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24646-score" class="post-score" title="current number of votes">-1</div><span id="post-24646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There, Network background: I got a call from a company to troubleshoot many issues including poor connectivity in sections of their office. The network setup was pretty simple, ISP to router, router to cisco smb 200 managed switch, from it an up link to another cisco smb 16 port switch (not managed) in another room, and finally from it an uplink to another cisco sbm 200 switch in another room (not managed). Users connected to the managed switch (the one connected to the router) had no issues. The rest of the office (those connected via uplink) experienced awful network issues, to be exact network was slow.</p><p>From the problem area I had network connection and was able to browse the web but at an unacceptable performance. I ran wireshark and notice a lot of retransmission and many small windows size value and unknown windows scaling value.</p><p>After verifying that the the uplinks and port settings were working fine I decided to swap the cisco smb 16 port with another one unit, once it did it magic happened and everything worked fine.</p><p>The questions I have is: What could've been the best way to use wireshark for troubleshooting this issue? what should I have looked into wireshark to find out that the switch was the issue? Should I have installed wireshark on different sections of the network and capture communication two way communication instead? I'm glad the problem is fixed but now that i'm reviewing the issue I realized I missed something in the capture that would've pointed me to the root cause.</p><p>Thanks in advanced...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-switchednetwork" rel="tag" title="see questions tagged &#39;switchednetwork&#39;">switchednetwork</span> <span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '13, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/f07c12721752c973bcb5b312cc845489?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kjzd28b&#39;s gravatar image" /><p><span>kjzd28b</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kjzd28b has no accepted answers">0%</span></p></div></div><div id="comments-container-24646" class="comments-container"><span id="24675"></span><div id="comment-24675" class="comment"><div id="post-24675-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I realized <strong>I missed something in the capture</strong> that would've pointed me to the root cause.</p></blockquote><p>I don't think so.</p><p>Obviously it depends on the problem within the switch, but usually you won't see a direct indicator in the capture file, other than TCP retransmissions and that could have been caused by everything in the network.</p><p>The correct think to do, is already described by <span>@Jasper</span>.</p></div><div id="comment-24675-info" class="comment-info"><span class="comment-age">(14 Sep '13, 04:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24646" class="comment-tools"></div><div class="clear"></div><div id="comment-24646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24647"></span>

<div id="answer-container-24647" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24647-score" class="post-score" title="current number of votes">2</div><span id="post-24647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Usually, I'd move the sniffer through the network path (from bad to good), and capture (if possible) on both sides of the device in question. If the device is a switch I'd use network TAPs on both sides because I can't trust the SPAN ports on the device I don't trust (transitive mistrust, so to speak :-)) Then comes the (sometimes) hard part: compare the two traces to see what went in, and what came out. It helps to narrow it down to a single bad connection to quickly find it in both traces.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24647" class="comments-container"><span id="24681"></span><div id="comment-24681" class="comment"><div id="post-24681-score" class="comment-score"></div><div class="comment-text"><p>thanks jasper and kurt,</p><p>i think that considering the retransmission issue helps isolate the issue to a L1 or L2. I didn't have network taps with me and the faulty switch wasn't managed so I couldn't span the port. Japer, when you capture on both sides and compare the traces you have tons of data from everyone on both sides of the switch, what do you look at to narrow it down?<br />
</p></div><div id="comment-24681-info" class="comment-info"><span class="comment-age">(14 Sep '13, 07:41)</span> <span class="comment-user userinfo">kjzd28b</span></div></div><span id="24691"></span><div id="comment-24691" class="comment"><div id="post-24691-score" class="comment-score"></div><div class="comment-text"><p>I'd use a specific PC to do some tests from the "bad" location. This way I can narrow the traces down to IP and (often) a few ports. Finding TCP conversations is not that hard - filter both on the same IP and port pairs, and use the absolute sequence numbers to match packets.</p></div><div id="comment-24691-info" class="comment-info"><span class="comment-age">(14 Sep '13, 14:04)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-24647" class="comment-tools"></div><div class="clear"></div><div id="comment-24647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

