+++
type = "question"
title = "Man-in-the-middle setup"
description = '''How would I setup a Man-in-the-middle scenario with windows XP. Wireshark is capturing all packets to the man-in-the-middles&#x27;s ip but won&#x27;t pass it through to the end device. It seems I can only capture off one Interface at a time.'''
date = "2010-09-17T06:50:00Z"
lastmod = "2010-09-18T17:48:00Z"
weight = 179
keywords = [ "man-in-the-middle" ]
aliases = [ "/questions/179" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Man-in-the-middle setup](/questions/179/man-in-the-middle-setup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-179-score" class="post-score" title="current number of votes">0</div><span id="post-179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How would I setup a Man-in-the-middle scenario with windows XP. Wireshark is capturing all packets to the man-in-the-middles's ip but won't pass it through to the end device. It seems I can only capture off one Interface at a time.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-man-in-the-middle" rel="tag" title="see questions tagged &#39;man-in-the-middle&#39;">man-in-the-middle</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '10, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/918a6cfb38e1fe2deef3db5357818d34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbajema&#39;s gravatar image" /><p><span>jbajema</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbajema has no accepted answers">0%</span></p></div></div><div id="comments-container-179" class="comments-container"></div><div id="comment-tools-179" class="comment-tools"></div><div class="clear"></div><div id="comment-179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="185"></span>

<div id="answer-container-185" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-185-score" class="post-score" title="current number of votes">2</div><span id="post-185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jbajema has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As @SYNbit points out, Wireshark only captures traffic. It doesn't modify or retransmit them. You should be able to <a href="http://www.windowsnetworking.com/articles_tutorials/wxpbrdge.html">bridge the interfaces in XP</a>, then capture traffic on one of the physical interfaces or on the bridge. On Ubuntu you can <a href="https://help.ubuntu.com/community/NetworkMonitoringBridge">bridge interfaces using brctl</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-185" class="comments-container"></div><div id="comment-tools-185" class="comment-tools"></div><div class="clear"></div><div id="comment-185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="208"></span>

<div id="answer-container-208" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-208-score" class="post-score" title="current number of votes">1</div><span id="post-208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I was distracted by the "man-in-the-middle" title, this usually means some active program doing decryption and re-encryption or some data injection.</p><p>If the whole purpose is to sit in between a connection and capture all the traffic, you might want to <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch">use a switch with port mirroring capabilities</a>. You can than attach your PC with wireshark to the configured mirroring port to see all traffic to/from the system that you want to monitor.</p><p>There are a couple of low-price switches offering you this capability:</p><ul><li><a href="http://www.dual-comm.com/OnlineShop.htm">Dualcomm Model DCGS-2005 (Gb) or DCSW-1005 (100 Mb)</a></li><li><a href="http://www.netgear.com/products/business/switches/prosafe-plus-switches/gs105e.aspx">NetGear gs105e</a></li></ul><p>(For the netgear, check the online forum. It does some strange stuff with icmp that has been solved in a beta release of the software. And it can only be configured with a little windows based program)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '10, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-208" class="comments-container"></div><div id="comment-tools-208" class="comment-tools"></div><div class="clear"></div><div id="comment-208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="180"></span>

<div id="answer-container-180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-180-score" class="post-score" title="current number of votes">0</div><span id="post-180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That is because Wireshark is not man-in-the-middle software and therefore does not forward packets. It's a diagnostics tool to analyze network traffic with.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-180" class="comments-container"><span id="182"></span><div id="comment-182" class="comment"><div id="post-182-score" class="comment-score"></div><div class="comment-text"><p>I don't beleive that is correct as I have seen it done with Ubuntu. I am trying to do the same thing in the windows environment with the exact laptop and external ethernet adapter with no luck.</p></div><div id="comment-182-info" class="comment-info"><span class="comment-age">(17 Sep '10, 08:33)</span> <span class="comment-user userinfo">jbajema</span></div></div></div><div id="comment-tools-180" class="comment-tools"></div><div class="clear"></div><div id="comment-180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="207"></span>

<div id="answer-container-207" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-207-score" class="post-score" title="current number of votes">0</div><span id="post-207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Building the bridge and monitoring it works... for a bit, then blue screens the pc. But at least I can capture the info I require, Thanks gerald</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 21:15</strong></p><img src="https://secure.gravatar.com/avatar/918a6cfb38e1fe2deef3db5357818d34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbajema&#39;s gravatar image" /><p><span>jbajema</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbajema has no accepted answers">0%</span></p></div></div><div id="comments-container-207" class="comments-container"><span id="209"></span><div id="comment-209" class="comment"><div id="post-209-score" class="comment-score"></div><div class="comment-text"><p>Please use "add new comment" to respond to answers. This will keep your response next to the "answer" that you are responding to, while an "answer" will move up and down depending on the votes it gets.</p><p>You can use "More -&gt; Convert to comment" to change your "answer" into a comment...</p></div><div id="comment-209-info" class="comment-info"><span class="comment-age">(18 Sep '10, 00:16)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="216"></span><div id="comment-216" class="comment"><div id="post-216-score" class="comment-score"></div><div class="comment-text"><p>Cool! I hadn't noticed the "Convert to comment" feature! @jbajema I tested it using one of your other answers. Hope that's OK.</p></div><div id="comment-216-info" class="comment-info"><span class="comment-age">(18 Sep '10, 17:48)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-207" class="comment-tools"></div><div class="clear"></div><div id="comment-207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

