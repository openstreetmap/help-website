+++
type = "question"
title = "packets out of order"
description = '''Is it common for packets to be out of order when capturing on two interfaces? I have noticed that my packets do not always arrive in the correct order. For instance I may get a DHCP ACK before the DHCP Request. I am just wondering if I should ignore this type of thing or not. Would an aggregating TA...'''
date = "2014-06-23T19:20:00Z"
lastmod = "2014-06-24T05:40:00Z"
weight = 34102
keywords = [ "order", "out-of-order", "time" ]
aliases = [ "/questions/34102" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [packets out of order](/questions/34102/packets-out-of-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34102-score" class="post-score" title="current number of votes">0</div><span id="post-34102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it common for packets to be out of order when capturing on two interfaces?</p><p>I have noticed that my packets do not always arrive in the correct order. For instance I may get a DHCP ACK before the DHCP Request. I am just wondering if I should ignore this type of thing or not.</p><p>Would an aggregating TAP provide better results?</p><p>I am just starting out with Wireshark so my equipment is not ideal. I am using a new MacBook Pro. This MacBook does not have wired ethernet so I am using USB 3.0 to ethernet adapters. I am also using the following network tap. <a href="https://hakshop.myshopify.com/collections/gadgets/products/throwing-star-lan-tap-pro.">https://hakshop.myshopify.com/collections/gadgets/products/throwing-star-lan-tap-pro.</a></p><p>I am assuming the packet order issue has to do with using two interfaces. I am fixing to buy a new TAP so I am wondering if I should get an aggregating tap to solve out of order packet issues or just ignore it.</p><p>I am between Net Optics and Network Instruments. Both companies have aggregating and non-aggregating models.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span> <span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '14, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/3299cadf0717cf9db46cf96e68ecc610?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fishfilet&#39;s gravatar image" /><p><span>fishfilet</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fishfilet has no accepted answers">0%</span></p></div></div><div id="comments-container-34102" class="comments-container"></div><div id="comment-tools-34102" class="comment-tools"></div><div class="clear"></div><div id="comment-34102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34103"></span>

<div id="answer-container-34103" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34103-score" class="post-score" title="current number of votes">0</div><span id="post-34103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>yes, it is common, but you can use the command line tool "reordercap" to fix that. Reordercap is part of the Wireshark distribution. Taps are expensive, so i'm not sure it makes any sense to buy one unless you really need very exact results. Problem with aggregation taps is that they are not always reliable; I had a few issues with them where they didn't provide correct results or even introduced crc errors to a link.</p><p>My advice: reorder your files with reordercap and see if you can work with that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '14, 20:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-34103" class="comments-container"><span id="34104"></span><div id="comment-34104" class="comment"><div id="post-34104-score" class="comment-score"></div><div class="comment-text"><p>I read about reordercap but it functions on the timestamps which are also generally out of order although in a different order than the frames.</p><p>I can deal with the packets being out of order if it's normal. I just wanted to make sure that there are no major problems analyzing trace files because of it.</p><p>If this is something everyone deals with and it's no big deal I'll just get a cheaper tap. I want to get a new one because mine is 10/100 only. Used non-aggregating taps are not to expensive.</p></div><div id="comment-34104-info" class="comment-info"><span class="comment-age">(23 Jun '14, 20:41)</span> <span class="comment-user userinfo">fishfilet</span></div></div><span id="34115"></span><div id="comment-34115" class="comment"><div id="post-34115-score" class="comment-score"></div><div class="comment-text"><p>If you reorder your capture by timestamp you should no longer see answer packets before request packets - if you still do then you capture setup is not working.</p><p>Out-of-order packets are also quite normal on a TCP level if earlier packets arrive later due to buffering and other reasons. But you should (after reordercap) never see packets that can't have been on the network in that order (like an answer being sent before you see the request for it).</p><p>The HakShop TAP is a passive Ethernet TAP, which is why it can only work up to 100 MBit/s. There's no way to built a TAP like that for speeds 1G and up due to technical reasons. BTW, if looking at TAPs also take a look at Garland Technology.</p></div><div id="comment-34115-info" class="comment-info"><span class="comment-age">(24 Jun '14, 05:40)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-34103" class="comment-tools"></div><div class="clear"></div><div id="comment-34103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

