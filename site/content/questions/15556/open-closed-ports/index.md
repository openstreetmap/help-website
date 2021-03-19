+++
type = "question"
title = "Open closed ports"
description = '''After capturing packets of an nmap scan: nmap –PN –scanflags PSHSYN –g 53 –p 22,80 [target] I found one respond from the target with ACK and RST flags set on port 80 I also found 4 responds from the target with ACK and SYN flags set on port 22 Does it indicate that the ports are open or closed ?  I ...'''
date = "2012-11-05T18:15:00Z"
lastmod = "2012-11-06T01:37:00Z"
weight = 15556
keywords = [ "nmap", "ack", "port", "packet", "syn" ]
aliases = [ "/questions/15556" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Open closed ports](/questions/15556/open-closed-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15556-score" class="post-score" title="current number of votes">0</div><span id="post-15556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After capturing packets of an nmap scan: nmap –PN –scanflags PSHSYN –g 53 –p 22,80 [target] I found one respond from the target with ACK and RST flags set on port 80 I also found 4 responds from the target with ACK and SYN flags set on port 22</p><p>Does it indicate that the ports are open or closed ? I was thinking that if you get a respond with ACK and RST flags set for port 80 it means that it is closed, however I am not sure if port 22 is closed or open. I also do not know why I have one respond packet for port 80(http) but four for port 22(ssh).</p><p>Thanks for your help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nmap" rel="tag" title="see questions tagged &#39;nmap&#39;">nmap</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '12, 18:15</strong></p><img src="https://secure.gravatar.com/avatar/cab9f439bb2eb387864cfe887fed544e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomala&#39;s gravatar image" /><p><span>tomala</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomala has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Nov '12, 18:33</strong> </span></p></div></div><div id="comments-container-15556" class="comments-container"></div><div id="comment-tools-15556" class="comment-tools"></div><div class="clear"></div><div id="comment-15556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15565"></span>

<div id="answer-container-15565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15565-score" class="post-score" title="current number of votes">0</div><span id="post-15565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you get a SYN,ACK for a SYN packet (your nmap scan on port 22), that most certainly means, that the port is open. However, it is hard to say why you get 4 responses without some information about the environment and the full capture file. Maybe nmap sent 4 SYN packets and thus you received 4 SYN,ACK !?!</p><p>If you want to know if the port is open, just open a connection to it. If you see the banner of the ssh daemon, the port is obviously open.</p><p><strong>UPDATE</strong></p><blockquote><p>I also do not know why I have one respond packet for port 80(http) but four for port 22(ssh).</p></blockquote><p>if that was caused by the same nmap scan, there could be "something" between the nmap scanner and the target that generated the answer packets. This "something" could be a firewall with a REJECT rule for port 80 and possibly some SYN Defender module for port 22. However, it would still be unclear why you get 4 answer packets for one SYN packet on port 22. As I said: Without further information about the environment and without the full capture file, it's hard to make any good assumptions.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '12, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Nov '12, 01:43</strong> </span></p></div></div><div id="comments-container-15565" class="comments-container"></div><div id="comment-tools-15565" class="comment-tools"></div><div class="clear"></div><div id="comment-15565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15566"></span>

<div id="answer-container-15566" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15566-score" class="post-score" title="current number of votes">0</div><span id="post-15566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The RST flag on port 80 means it is closed but not firewalled. If you get SYN/ACK flags on port 22 it means it is open and responds to connection requests.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '12, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15566" class="comments-container"><span id="15569"></span><div id="comment-15569" class="comment"><div id="post-15569-score" class="comment-score"></div><div class="comment-text"><p>could'nt it be a firewall with a REJECT rule instead of a DROP rule?</p></div><div id="comment-15569-info" class="comment-info"><span class="comment-age">(06 Nov '12, 01:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15571"></span><div id="comment-15571" class="comment"><div id="post-15571-score" class="comment-score"></div><div class="comment-text"><p>yep, agreed, but that is very uncommon :-)</p></div><div id="comment-15571-info" class="comment-info"><span class="comment-age">(06 Nov '12, 01:37)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-15566" class="comment-tools"></div><div class="clear"></div><div id="comment-15566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

