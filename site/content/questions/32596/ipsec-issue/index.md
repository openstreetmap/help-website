+++
type = "question"
title = "IPSEC Issue"
description = '''Hello All! I am not a packet analyst by far and I am trying to track down an issue we are having with IPSec and the creation of a secure tunnel over our network.  We have a dynamic port/address NAT rule in place that NATs all of the ip addresses in one location to a public IP address. We are trying ...'''
date = "2014-05-07T07:07:00Z"
lastmod = "2014-05-07T07:07:00Z"
weight = 32596
keywords = [ "ipsec-nat-t", "4500", "nat", "ipsec" ]
aliases = [ "/questions/32596" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IPSEC Issue](/questions/32596/ipsec-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32596-score" class="post-score" title="current number of votes">0</div><span id="post-32596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All! I am not a packet analyst by far and I am trying to track down an issue we are having with IPSec and the creation of a secure tunnel over our network.</p><p>We have a dynamic port/address NAT rule in place that NATs all of the ip addresses in one location to a public IP address. We are trying to get a signal booster that is installed on our network to talk to towers outside our network. It looks like traffic is getting to the firewall but not the booster, but I have allowances on our firewall for ports 500 and 4500 and I can see that traffic is being allowed.</p><p>When I do a packet capture, (from the firewall) I can't read the results well enough to understand where the hangup is. I can see a packet that looks like it comes from our public ip address to the external address that is coming across as destination unreachable (port unreachable). The source port is ipsec-nat-t (4500). But does that mean that the firewall is blocking the port, even though traffic to and from that port is allowed? What should I be looking for to determine what the root cause of this stopage is?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipsec-nat-t" rel="tag" title="see questions tagged &#39;ipsec-nat-t&#39;">ipsec-nat-t</span> <span class="post-tag tag-link-4500" rel="tag" title="see questions tagged &#39;4500&#39;">4500</span> <span class="post-tag tag-link-nat" rel="tag" title="see questions tagged &#39;nat&#39;">nat</span> <span class="post-tag tag-link-ipsec" rel="tag" title="see questions tagged &#39;ipsec&#39;">ipsec</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '14, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/1dab2050f14ec07c291322e2c3156a6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LostInTheParadigm&#39;s gravatar image" /><p><span>LostInThePar...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LostInTheParadigm has no accepted answers">0%</span></p></div></div><div id="comments-container-32596" class="comments-container"></div><div id="comment-tools-32596" class="comment-tools"></div><div class="clear"></div><div id="comment-32596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

