+++
type = "question"
title = "Is it possible to sniff packets from an IP website to all others IP ?"
description = '''Hi, Like it&#x27;s saying in the title, my question is:  is it possible to sniff, with wireshark, any information from an IP website to all of the visitors ? And if the answer is &quot;yes&quot;, how ? plz.  Or, wireshark can just sniff packets beetween our connexion to others ? Thanks, (i&#x27;m a beginner of wireshar...'''
date = "2016-08-29T13:35:00Z"
lastmod = "2016-08-29T14:03:00Z"
weight = 55177
keywords = [ "packets", "sniff", "wireshark" ]
aliases = [ "/questions/55177" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to sniff packets from an IP website to all others IP ?](/questions/55177/is-it-possible-to-sniff-packets-from-an-ip-website-to-all-others-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55177-score" class="post-score" title="current number of votes">0</div><span id="post-55177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Like it's saying in the title, my question is:</p><blockquote><p>is it possible to sniff, with wireshark, any information from an IP website to all of the visitors ? And if the answer is "yes", how ? plz.</p></blockquote><p>Or, wireshark can just sniff packets beetween our connexion to others ?</p><p>Thanks, (i'm a beginner of wireshark), BR, M</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-sniff" rel="tag" title="see questions tagged &#39;sniff&#39;">sniff</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '16, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/66b1114dd74e0d9c432791c84a1b9138?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yawatem&#39;s gravatar image" /><p><span>Yawatem</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yawatem has no accepted answers">0%</span></p></div></div><div id="comments-container-55177" class="comments-container"></div><div id="comment-tools-55177" class="comment-tools"></div><div class="clear"></div><div id="comment-55177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55178"></span>

<div id="answer-container-55178" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55178-score" class="post-score" title="current number of votes">1</div><span id="post-55178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capture location would be key in determining what conversations you see. If you are server side, then you can see from the server's IP(s) out to all the clients if you capture off the server's NIC or if you have a Test Access Port just after the server's NIC. If you are capturing from the client side, you would only see your conversation to the server if you are capturing at the client NIC. Your view of client side conversations will change if you capture elsewhere in the LAN (after router/switch) and have other users in the LAN accessing that same site.</p><p>So short answer is Yes, depending on what you have access to you can capture both views. If capturing server side, depending on utilization/connections/NIC speeds I would recommend not using the Wireshark GUI but using some of the native libraries (dumpcap, tcpdump). Then you can split PCAPs into more manageable sizes that you can use Wireshark to inspect.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '16, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p><span>BruteForce</span><br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span></p></div></div><div id="comments-container-55178" class="comments-container"><span id="55179"></span><div id="comment-55179" class="comment"><div id="post-55179-score" class="comment-score"></div><div class="comment-text"><p>Ok, there is no way for sniffing information from a server to some clients (all of them, by the way), if you haven't got access to the server ? :))</p><p>(thanks for answser) :)</p></div><div id="comment-55179-info" class="comment-info"><span class="comment-age">(29 Aug '16, 14:03)</span> <span class="comment-user userinfo">Yawatem</span></div></div></div><div id="comment-tools-55178" class="comment-tools"></div><div class="clear"></div><div id="comment-55178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

