+++
type = "question"
title = "Detecting Wireshark usage"
description = '''Is it possible to determine if Wireshark is being used on my network. I&#x27;ve found Wireshark installed on an office machine and would like to know if there is a way for me to determine if this machine is being used to capture packets on our network short of manually searching for saved captures on the...'''
date = "2013-04-08T13:52:00Z"
lastmod = "2013-04-08T14:50:00Z"
weight = 20201
keywords = [ "usage", "detecting", "wireshark" ]
aliases = [ "/questions/20201" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Detecting Wireshark usage](/questions/20201/detecting-wireshark-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20201-score" class="post-score" title="current number of votes">0</div><span id="post-20201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to determine if Wireshark is being used on my network. I've found Wireshark installed on an office machine and would like to know if there is a way for me to determine if this machine is being used to capture packets on our network short of manually searching for saved captures on the machine. It would be best if I didn't have to have access to the actual machine running Wireshark to determine it. Even if I have to use Wireshark on another node to determine if they are using it.</p><p>Please any help with this would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-detecting" rel="tag" title="see questions tagged &#39;detecting&#39;">detecting</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '13, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/b4cd2827e535678dc7f1d0bb640a17e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="networking&#39;s gravatar image" /><p><span>networking</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="networking has no accepted answers">0%</span></p></div></div><div id="comments-container-20201" class="comments-container"></div><div id="comment-tools-20201" class="comment-tools"></div><div class="clear"></div><div id="comment-20201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="20202"></span>

<div id="answer-container-20202" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20202-score" class="post-score" title="current number of votes">1</div><span id="post-20202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't detect a fully passive sniffer on the network, with "fully passive" meaning that the PC running Wireshark (or any other sniffing software) uses a network card with its TCP/IP stack disabled. That way the card will only listen and never talk, so you can't spot it on the network.</p><p>If the network card is not completely passive you could try to detect if it is running in promiscuous mode, e.g. be using nmap: <a href="http://nmap.org/nsedoc/scripts/sniffer-detect.html">http://nmap.org/nsedoc/scripts/sniffer-detect.html</a></p><p>What you can do is examine PCs that have Wireshark installed to see if they created capture files in the past, but that is IT forensics and not network related; it also requires the quite special skill set of a computer forensics specialist.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20202" class="comments-container"></div><div id="comment-tools-20202" class="comment-tools"></div><div class="clear"></div><div id="comment-20202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20203"></span>

<div id="answer-container-20203" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20203-score" class="post-score" title="current number of votes">1</div><span id="post-20203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See also: <a href="http://security.stackexchange.com/questions/3630/how-to-find-out-that-a-nic-is-in-promiscuous-mode-on-a-lan">http://security.stackexchange.com/questions/3630/how-to-find-out-that-a-nic-is-in-promiscuous-mode-on-a-lan</a> . It lists 3 methods of detecting NICs in promiscuous mode (needed to capture packets of other machines).</p><p>Also please note that if you are on a switched network, the office PC with Wireshark on it will only see packets to/from itself and broadcasts/multicasts. In order for the PC to see other peoples traffic, it might run tools that do <a href="http://en.wikipedia.org/wiki/ARP_spoofing">arp poisoning</a> and you will be able to see that on your network when you mirror the traffic on the switch port to this office PC. You will have to run wireshark on another system to make the arp poisoning visible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20203" class="comments-container"></div><div id="comment-tools-20203" class="comment-tools"></div><div class="clear"></div><div id="comment-20203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20205"></span>

<div id="answer-container-20205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20205-score" class="post-score" title="current number of votes">0</div><span id="post-20205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>see my answer to a similar question</p><blockquote><p><code>http://ask.wireshark.org/questions/14351/detectprevent-wireshark</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 14:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20205" class="comments-container"></div><div id="comment-tools-20205" class="comment-tools"></div><div class="clear"></div><div id="comment-20205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

