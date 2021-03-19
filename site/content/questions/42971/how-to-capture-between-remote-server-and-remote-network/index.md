+++
type = "question"
title = "How to capture between remote server and remote network"
description = '''Hi, I want to capture packets going between a remote server in my VLAN and a remote subnet that is connected to the same core switch as my server. I also want to exclude any traffic coming from/to the server that I have Wireshark running on: Wireshark is on server: 10.250.255.241 I want to capture t...'''
date = "2015-06-08T06:19:00Z"
lastmod = "2015-06-08T08:51:00Z"
weight = 42971
keywords = [ "capture-filter" ]
aliases = [ "/questions/42971" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture between remote server and remote network](/questions/42971/how-to-capture-between-remote-server-and-remote-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42971-score" class="post-score" title="current number of votes">0</div><span id="post-42971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to capture packets going between a remote server in my VLAN and a remote subnet that is connected to the same core switch as my server. I also want to exclude any traffic coming from/to the server that I have Wireshark running on:</p><p>Wireshark is on server: 10.250.255.241</p><p>I want to capture traffic between: 10.250.255.77 and the 10.100.100.xxx network</p><p>I assumed that the capture filter would look like one of these:</p><p>host 10.250.255.77 and net 10.100.100.0/24</p><p>or</p><p>src net 10.100.100.100.0/24 and host 10.250.255.77</p><p>I'm also not sure how to exclude traffic from 10.250.255.241</p><p>The capture is not showing any traffic but there should be lots of traffic between that host and that network.</p><p>What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '15, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/dceb0dbefabbac8e85385fc78d386930?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rdub15&#39;s gravatar image" /><p><span>rdub15</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rdub15 has no accepted answers">0%</span></p></div></div><div id="comments-container-42971" class="comments-container"></div><div id="comment-tools-42971" class="comment-tools"></div><div class="clear"></div><div id="comment-42971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42974"></span>

<div id="answer-container-42974" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42974-score" class="post-score" title="current number of votes">1</div><span id="post-42974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This filter will capture bi-directional traffic between the server and network, while excluding the traffic from your Wireshark machine:</p><p>host 10.250.255.77 and net 10.100.100 and !(host 10.250.255.241)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '15, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-42974" class="comments-container"><span id="42977"></span><div id="comment-42977" class="comment"><div id="post-42977-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Amato_C. The filter you wrote looks like it should work, but it still isn't. Is there anything else I'm not taking into consideration? I'm not very familiar with Wireshark but I know that traffic is passing between that server and that subnet. The server is a fax server and the subnet is for the VOIP switches. We are using FOIP and I know that faxes are being sent and received. I'm very confused as to why I can't capture the packets...</p></div><div id="comment-42977-info" class="comment-info"><span class="comment-age">(08 Jun '15, 08:45)</span> <span class="comment-user userinfo">rdub15</span></div></div><span id="42978"></span><div id="comment-42978" class="comment"><div id="post-42978-score" class="comment-score"></div><div class="comment-text"><p>Let's start with the basics. Maybe your configuration is not correct to capture traffic. Please read the following Wiki: <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>I suspect you are capturing traffic on a switch port which has not been configured as a mirror port.</p></div><div id="comment-42978-info" class="comment-info"><span class="comment-age">(08 Jun '15, 08:51)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-42974" class="comment-tools"></div><div class="clear"></div><div id="comment-42974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

