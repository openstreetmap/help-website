+++
type = "question"
title = "IP Addresses and Hostnames in one tshark output"
description = '''I&#x27;ve been trying to get both IP address and hostname with tshark. From Wireshark it is easy, but from tshark I couldn&#x27;t figure out how to do it. &quot;-z ip_hosts,tree&quot; parameter just give the IP Addresses even when I specify &quot;-N n&quot; parameter. How can I get this IP addresses and hostnames together? By th...'''
date = "2015-07-30T07:08:00Z"
lastmod = "2015-07-31T00:39:00Z"
weight = 44638
keywords = [ "ip", "resolve", "tshark", "hostname." ]
aliases = [ "/questions/44638" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [IP Addresses and Hostnames in one tshark output](/questions/44638/ip-addresses-and-hostnames-in-one-tshark-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44638-score" class="post-score" title="current number of votes">0</div><span id="post-44638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been trying to get both IP address and hostname with tshark. From Wireshark it is easy, but from tshark I couldn't figure out how to do it. "-z ip_hosts,tree" parameter just give the IP Addresses even when I specify "-N n" parameter. How can I get this IP addresses and hostnames together?</p><p>By the way -z hosts does not give all IPs and hostnames, sometimes does not give anything at all.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-resolve" rel="tag" title="see questions tagged &#39;resolve&#39;">resolve</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-hostname." rel="tag" title="see questions tagged &#39;hostname.&#39;">hostname.</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/e38b402a5635b121c60c316fcfca8da1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xmikro&#39;s gravatar image" /><p><span>xmikro</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xmikro has no accepted answers">0%</span></p></div></div><div id="comments-container-44638" class="comments-container"></div><div id="comment-tools-44638" class="comment-tools"></div><div class="clear"></div><div id="comment-44638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44640"></span>

<div id="answer-container-44640" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44640-score" class="post-score" title="current number of votes">0</div><span id="post-44640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xmikro has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try the -T and -e options. For example:</p><p>-T fields -e ip.addr</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '15, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44640" class="comments-container"><span id="44669"></span><div id="comment-44669" class="comment"><div id="post-44669-score" class="comment-score"></div><div class="comment-text"><p>Thanks! <code>tshark -T fields -e ip.dst_host -e ip.dst</code> is just what I wanted. But do you have any idea why <code>-z hosts</code> parameter does not work?</p></div><div id="comment-44669-info" class="comment-info"><span class="comment-age">(31 Jul '15, 00:39)</span> <span class="comment-user userinfo">xmikro</span></div></div></div><div id="comment-tools-44640" class="comment-tools"></div><div class="clear"></div><div id="comment-44640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

