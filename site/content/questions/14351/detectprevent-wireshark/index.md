+++
type = "question"
title = "detect/prevent wireshark?"
description = '''Someone on my network have wireshark. Can someone tell me how i can detect if he capturing my pc-internet packets? I mean detect or prevent wireshark of doing it.'''
date = "2012-09-18T09:30:00Z"
lastmod = "2015-06-03T22:46:00Z"
weight = 14351
keywords = [ "detection", "prevent" ]
aliases = [ "/questions/14351" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [detect/prevent wireshark?](/questions/14351/detectprevent-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14351-score" class="post-score" title="current number of votes">0</div><span id="post-14351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Someone on my network have wireshark. Can someone tell me how i can detect if he capturing my pc-internet packets? I mean detect or prevent wireshark of doing it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-detection" rel="tag" title="see questions tagged &#39;detection&#39;">detection</span> <span class="post-tag tag-link-prevent" rel="tag" title="see questions tagged &#39;prevent&#39;">prevent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '12, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/4eba89ce26147df94447b1d1911f0c79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Johnny&#39;s gravatar image" /><p><span>Johnny</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Johnny has no accepted answers">0%</span></p></div></div><div id="comments-container-14351" class="comments-container"></div><div id="comment-tools-14351" class="comment-tools"></div><div class="clear"></div><div id="comment-14351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="14361"></span>

<div id="answer-container-14361" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14361-score" class="post-score" title="current number of votes">2</div><span id="post-14361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Basically you can detect if a system on the <strong>same subnet</strong> is running a sniffer, if some conditions are fulfilled (see below).</p><p>Reason: If the system runs the sniffer, its interface will be in promiscuous mode. The test works like this: Send a ping with the correct IP address into the network but with a wrong mac address. The sniffing host will answer the ping packet, as it will receive every packet in promiscuous mode. There is a ready-to use script in nmap to support this detection.</p><blockquote><p><code>http://nmap.org/nsedoc/scripts/sniffer-detect.html</code><br />
</p></blockquote><p>HOWEVER: This method only works if,</p><ul><li>the sniffing host is on the same Layer2 network</li><li>the sniffing host does not have a firewall that blocks incoming icmp packets</li><li>the sniffing host does the sniffing with an interface that has TCP/IP enabled, and thus is able to answer the ICMP packet.</li></ul><p>BTW: There is no reliable way to prevent the use of a sniffer on a network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '12, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Sep '12, 13:27</strong> </span></p></div></div><div id="comments-container-14361" class="comments-container"></div><div id="comment-tools-14361" class="comment-tools"></div><div class="clear"></div><div id="comment-14361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14358"></span>

<div id="answer-container-14358" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14358-score" class="post-score" title="current number of votes">0</div><span id="post-14358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't usually detect Wireshark or any other sniffer that is passively capturing packets on your network, and most of the time that is not a problem at all. In today's switched networks, other PCs do not see your packets, because the switch will simply not forward them to any other node than the one it has to be delivered to. That is, as long as there is no SPAN port running (Switched Port ANalyzer) on the switch, and nobody uses hacking techniques like ARP cache poisoning etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '12, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14358" class="comments-container"></div><div id="comment-tools-14358" class="comment-tools"></div><div class="clear"></div><div id="comment-14358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42871"></span>

<div id="answer-container-42871" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42871-score" class="post-score" title="current number of votes">0</div><span id="post-42871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Doesn't stop them from running it on a server if they have access, or from sniffing their own link and accessing data or running client apps while monitoring. For that matter, they could be running tshark, dumpcap, or tcpdump.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 22:46</strong></p><img src="https://secure.gravatar.com/avatar/f0950f468133c72b3e15e65edf5db5ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lucidcryotank&#39;s gravatar image" /><p><span>Lucidcryotank</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lucidcryotank has one accepted answer">50%</span></p></div></div><div id="comments-container-42871" class="comments-container"></div><div id="comment-tools-42871" class="comment-tools"></div><div class="clear"></div><div id="comment-42871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

