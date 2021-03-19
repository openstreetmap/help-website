+++
type = "question"
title = "Sniff IP of a mac-adress, help with filter"
description = '''Hi, I have a NAS connected to a switch. From that same switch I have a wireless router connected. I want to know the IP of my NAS by sniffing it. I have the MAC address of the NAS but I need the IP to be able to connect to it. I am on a laptop now connected wirelessly to the router.  What filter do ...'''
date = "2013-02-05T07:54:00Z"
lastmod = "2013-02-05T13:21:00Z"
weight = 18321
keywords = [ "filter", "mac", "sniff" ]
aliases = [ "/questions/18321" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Sniff IP of a mac-adress, help with filter](/questions/18321/sniff-ip-of-a-mac-adress-help-with-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18321-score" class="post-score" title="current number of votes">0</div><span id="post-18321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a NAS connected to a switch. From that same switch I have a wireless router connected. I want to know the IP of my NAS by sniffing it. I have the MAC address of the NAS but I need the IP to be able to connect to it.</p><p>I am on a laptop now connected wirelessly to the router. What filter do I use to be able to sniff the IP of the NAS?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-sniff" rel="tag" title="see questions tagged &#39;sniff&#39;">sniff</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '13, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/7bdbe55f3a7189ae7726dc1448ad77bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aDonis&#39;s gravatar image" /><p><span>aDonis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aDonis has no accepted answers">0%</span></p></div></div><div id="comments-container-18321" class="comments-container"></div><div id="comment-tools-18321" class="comment-tools"></div><div class="clear"></div><div id="comment-18321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18323"></span>

<div id="answer-container-18323" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18323-score" class="post-score" title="current number of votes">1</div><span id="post-18323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Filter won't help you here, since you'll not be able to capture any packet unless the NAS broadcasts something. The switch will only send packets to you that the NAS directs at your MAC, which it probably will not if you haven't accessed it (which you need the IP address for). Maybe it will broadcast something when you boot it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '13, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-18323" class="comments-container"></div><div id="comment-tools-18323" class="comment-tools"></div><div class="clear"></div><div id="comment-18323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18324"></span>

<div id="answer-container-18324" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18324-score" class="post-score" title="current number of votes">1</div><span id="post-18324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am on a laptop now connected wirelessly to the router. What filter do I use to be able to sniff the IP of the NAS?</p></blockquote><p>Please connect the laptop to another switch port and start Wireshark on the laptop. Then power cycle the NAS. If you are "lucky" the OS of the NAS will send out a <a href="http://wiki.wireshark.org/Gratuitous_ARP">gratuitous ARP</a> after the IP stack was initialized. That gratuituous ARP packet will contain the IP address of the NAS.</p><p>You will <strong>not</strong> see that packet while you are connected to the <strong>router</strong> via wlan/wifi!! So, you need to connect the laptop directly to the switch.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '13, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Feb '13, 13:21</strong> </span></p></div></div><div id="comments-container-18324" class="comments-container"></div><div id="comment-tools-18324" class="comment-tools"></div><div class="clear"></div><div id="comment-18324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

