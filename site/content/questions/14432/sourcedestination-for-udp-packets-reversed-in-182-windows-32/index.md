+++
type = "question"
title = "Source/Destination for UDP packets reversed in 1.8.2 windows 32"
description = '''I&#x27;ve been using Ethereal/Wireshark for many years. Today I&#x27;ve been using Wireshark 1.8.2 to look at UDP packets between an embedded device I am developing and a PC. Everything works OK, except the Source and Destination IP addresses seem to be swapped on the display. Actually the TCP source/destinat...'''
date = "2012-09-21T08:03:00Z"
lastmod = "2012-09-21T09:58:00Z"
weight = 14432
keywords = [ "source", "destination", "swapped" ]
aliases = [ "/questions/14432" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Source/Destination for UDP packets reversed in 1.8.2 windows 32](/questions/14432/sourcedestination-for-udp-packets-reversed-in-182-windows-32)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14432-score" class="post-score" title="current number of votes">0</div><span id="post-14432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been using Ethereal/Wireshark for many years. Today I've been using Wireshark 1.8.2 to look at UDP packets between an embedded device I am developing and a PC. Everything works OK, except the Source and Destination IP addresses seem to be swapped on the display. Actually the TCP source/destination seem swapped as well. When looking at the Ethernet II header display, the source and Destination are swapped there as well.</p><p>Win XP 32bit.</p><p>The ICMP (ping) display looks fine</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-swapped" rel="tag" title="see questions tagged &#39;swapped&#39;">swapped</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '12, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/90e80f51d992773defbce0d38f40f5ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithHam&#39;s gravatar image" /><p><span>KeithHam</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithHam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Sep '12, 08:52</strong> </span></p></div></div><div id="comments-container-14432" class="comments-container"></div><div id="comment-tools-14432" class="comment-tools"></div><div class="clear"></div><div id="comment-14432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14434"></span>

<div id="answer-container-14434" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14434-score" class="post-score" title="current number of votes">0</div><span id="post-14434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you say that the IP addresses, the TCP source/destination, and the Ethernet addresses are ALL swapped, it sounds like they all match the appropriate device. So, when Wireshark says that a particular packet is FROM the PC and TO the embedded device, what makes you think that it's really the other way around? Is it possible that you've accidentally dragged either the source or destination columns so that the destination column is before the source column?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '12, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-14434" class="comments-container"><span id="14438"></span><div id="comment-14438" class="comment"><div id="post-14438-score" class="comment-score"></div><div class="comment-text"><p>I share your concern. I have a massive headache today, so I am wondering about my fitness for any useful thought. That said, and considering Wireshark has been working flawlessly for me for over 10 years, operator error is a valid consideration.</p><p>I know what data is supposed to be flowing from one device to the other. The PC requests data (small packets), the Coldfire sends big packets of UDP data back. And that is exactly what I am seeing now (I.E I screwed up, and I apologize)</p><p>So please close this issue, this is (as I suspected,) my fault and I apologize for any wasted time. And thanks for the reply.</p></div><div id="comment-14438-info" class="comment-info"><span class="comment-age">(21 Sep '12, 09:58)</span> <span class="comment-user userinfo">KeithHam</span></div></div></div><div id="comment-tools-14434" class="comment-tools"></div><div class="clear"></div><div id="comment-14434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

