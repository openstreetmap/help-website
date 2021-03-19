+++
type = "question"
title = "wireshark placement"
description = '''Ok, I am a newbie to wireshark and a little confused on what traffic wireshark captures depending on where it is. Okay, for example I am using wireshark on my desktop PC. I have the usual home network setup. &quot;modem connect to wireless router&quot; &amp;amp; &quot;desktop connected to wireless router&quot;. What traffi...'''
date = "2012-08-17T08:57:00Z"
lastmod = "2012-08-17T09:12:00Z"
weight = 13706
keywords = [ "newbie", "wireshark" ]
aliases = [ "/questions/13706" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark placement](/questions/13706/wireshark-placement)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13706-score" class="post-score" title="current number of votes">0</div><span id="post-13706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok, I am a newbie to wireshark and a little confused on what traffic wireshark captures depending on where it is. Okay, for example I am using wireshark on my desktop PC. I have the usual home network setup. "modem connect to wireless router" &amp; "desktop connected to wireless router". What traffic am I suppose to see? just the traffic coming in on my ethernet port through the switch? No traffic from the ISP?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '12, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/52857dcff5e05dba5f87f9670ead91b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="I_GEEK_IT&#39;s gravatar image" /><p><span>I_GEEK_IT</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="I_GEEK_IT has no accepted answers">0%</span></p></div></div><div id="comments-container-13706" class="comments-container"></div><div id="comment-tools-13706" class="comment-tools"></div><div class="clear"></div><div id="comment-13706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13707"></span>

<div id="answer-container-13707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13707-score" class="post-score" title="current number of votes">0</div><span id="post-13707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll see all packets directed to your MAC address, and broadcast/multicast packets. If someone else is using your router you won't see their unicast packets.</p><p>Since I guess your ISP is allowing you to access the internet you will of course see everything is sent to your PC (or coming from it). Of course you will not see any Layer 2 headers that came from your ISP since they're exchanged by the router for your local segment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '12, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13707" class="comments-container"></div><div id="comment-tools-13707" class="comment-tools"></div><div class="clear"></div><div id="comment-13707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

