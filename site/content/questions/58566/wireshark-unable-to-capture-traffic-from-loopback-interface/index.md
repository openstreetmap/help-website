+++
type = "question"
title = "wireshark unable to capture traffic from loopback interface"
description = '''I run a python script from scapy (using my host machine)to send packets to my virtual machine, where wireshark is installed with loopback interface , but wireshark isn&#x27;t receiving any packets although they are sent from scapy successfully , my python script is &amp;gt;&amp;gt;&amp;gt; sendp(IP(dst=&quot;10.0.2.13&quot;)/...'''
date = "2017-01-06T11:11:00Z"
lastmod = "2017-01-06T12:23:00Z"
weight = 58566
keywords = [ "wireshark" ]
aliases = [ "/questions/58566" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark unable to capture traffic from loopback interface](/questions/58566/wireshark-unable-to-capture-traffic-from-loopback-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58566-score" class="post-score" title="current number of votes">0</div><span id="post-58566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I run a python script from scapy (using my host machine)to send packets to my virtual machine, where wireshark is installed with loopback interface , but wireshark isn't receiving any packets although they are sent from scapy successfully , my python script is &gt;&gt;&gt; sendp(IP(dst="10.0.2.13")/ICMP()/"HELLOOOO",count=100)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '17, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/5dfff9736551f2e3b54f636167931f9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lobna&#39;s gravatar image" /><p><span>lobna</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lobna has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '17, 11:13</strong> </span></p></div></div><div id="comments-container-58566" class="comments-container"><span id="58567"></span><div id="comment-58567" class="comment"><div id="post-58567-score" class="comment-score"></div><div class="comment-text"><p>What OS on both host and VM and what version of Wireshark?</p></div><div id="comment-58567-info" class="comment-info"><span class="comment-age">(06 Jan '17, 11:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="58569"></span><div id="comment-58569" class="comment"><div id="post-58569-score" class="comment-score"></div><div class="comment-text"><p>Why do you capture on the loopback, while packets come in on a virtual network interface?</p></div><div id="comment-58569-info" class="comment-info"><span class="comment-age">(06 Jan '17, 12:23)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-58566" class="comment-tools"></div><div class="clear"></div><div id="comment-58566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

