+++
type = "question"
title = "Router sending packet(s) out every 5 seconds / bandwidth is not compromised"
description = '''Hi folks, I have a dd-wrt mini router (Linksys WRT54GS v7) which I am worried may be compromised. It is sending out a packet every 5 seconds somewhere despite the fact that my WiFi is disabled (everything is hard-wired here) and all machines are either off or unplugged. The simple topology would be:...'''
date = "2013-09-20T15:00:00Z"
lastmod = "2013-09-20T15:49:00Z"
weight = 25057
keywords = [ "router", "packets", "dd-wrt", "compromised", "sending" ]
aliases = [ "/questions/25057" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Router sending packet(s) out every 5 seconds / bandwidth is not compromised](/questions/25057/router-sending-packets-out-every-5-seconds-bandwidth-is-not-compromised)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25057-score" class="post-score" title="current number of votes">0</div><span id="post-25057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks, I have a dd-wrt mini router (Linksys WRT54GS v7) which I am worried may be compromised. It is sending out a packet every 5 seconds somewhere despite the fact that my WiFi is disabled (everything is hard-wired here) and all machines are either off or unplugged.</p><p>The simple topology would be:</p><p>Router --&gt; Modem --&gt; DSLam --&gt; net provider [The modem is an old SpeedStream DSL modem.]</p><p>I know that it is not an internal network issue (i.e. not inside the LAN) since all computers are unplugged or off when packets are still being sent out.</p><p>I called my net provider but the network admin did not want to take the time to diagnose the issue even though I think this would be the quickest way to diagnose what is going on.</p><p>So my question is what would be the best way to diagnose this problem? How would I go about diagnosing it myself? I would like to know what type of packets the router is sending out.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-dd-wrt" rel="tag" title="see questions tagged &#39;dd-wrt&#39;">dd-wrt</span> <span class="post-tag tag-link-compromised" rel="tag" title="see questions tagged &#39;compromised&#39;">compromised</span> <span class="post-tag tag-link-sending" rel="tag" title="see questions tagged &#39;sending&#39;">sending</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '13, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/40c1421ef08969a1e5f60c999b44849d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bongoman&#39;s gravatar image" /><p><span>Bongoman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bongoman has no accepted answers">0%</span></p></div></div><div id="comments-container-25057" class="comments-container"><span id="25058"></span><div id="comment-25058" class="comment"><div id="post-25058-score" class="comment-score"></div><div class="comment-text"><p>how do you know the router sends packets every 5 seconds?</p></div><div id="comment-25058-info" class="comment-info"><span class="comment-age">(20 Sep '13, 15:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-25057" class="comment-tools"></div><div class="clear"></div><div id="comment-25057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25059"></span>

<div id="answer-container-25059" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25059-score" class="post-score" title="current number of votes">0</div><span id="post-25059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How would I go about diagnosing it myself?</p></blockquote><p>Log into the router via ssh and run <a href="http://emtunc.org/blog/04/2011/installing-tcpdump-on-dd-wrt-wrt54gl/">tcpdump on dd-wrt</a></p><blockquote><p>tcpdump -ni eth0 not port 22</p></blockquote><p>Maybe eth0 is not the right interface. Please check with <strong>ifconfig</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '13, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25059" class="comments-container"></div><div id="comment-tools-25059" class="comment-tools"></div><div class="clear"></div><div id="comment-25059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

