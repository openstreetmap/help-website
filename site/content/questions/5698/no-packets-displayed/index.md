+++
type = "question"
title = "No Packets displayed"
description = '''Hey there, i got a wired problem. I think i figured out how to use Wireshark, i can capture my own packets. But now I want to capture packets of my Ipod which is on the WLAN too. I have a Macbook Pro mid 2010 and Im running in Monitor Mode to get all the traffic, it also seems to capture packets. Th...'''
date = "2011-08-13T09:13:00Z"
lastmod = "2011-08-18T06:53:00Z"
weight = 5698
keywords = [ "displayed", "packets", "capturing" ]
aliases = [ "/questions/5698" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No Packets displayed](/questions/5698/no-packets-displayed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5698-score" class="post-score" title="current number of votes">1</div><span id="post-5698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there, i got a wired problem.</p><p>I think i figured out how to use Wireshark, i can capture my own packets. But now I want to capture packets of my Ipod which is on the WLAN too.</p><p>I have a Macbook Pro mid 2010 and Im running in Monitor Mode to get all the traffic, it also seems to capture packets. The number at the bottom which says "Packets" increases with the time but "Displayed" is always 0.</p><p>On my macbook it works, but trying to do it on the wlan doesnt. Did I do anything wrong?</p><p>Thanks for your help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-displayed" rel="tag" title="see questions tagged &#39;displayed&#39;">displayed</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-capturing" rel="tag" title="see questions tagged &#39;capturing&#39;">capturing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '11, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/ffe158c2c3a90c8d1b9969bc65efbf93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrBonsai&#39;s gravatar image" /><p><span>MrBonsai</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrBonsai has no accepted answers">0%</span></p></div></div><div id="comments-container-5698" class="comments-container"><span id="5700"></span><div id="comment-5700" class="comment"><div id="post-5700-score" class="comment-score"></div><div class="comment-text"><p>Do you have a display filter? If so, what is the filter?</p></div><div id="comment-5700-info" class="comment-info"><span class="comment-age">(13 Aug '11, 13:13)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-5698" class="comment-tools"></div><div class="clear"></div><div id="comment-5698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5739"></span>

<div id="answer-container-5739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5739-score" class="post-score" title="current number of votes">2</div><span id="post-5739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I am not an expert, but i think i can give you a tip.</p><p>To see packets sent by devices different that the one where wireshark is installed, you need to perfform a MITM(Man In The Middle) attack.</p><p>This means that your MacBook(The Man in The Middle in this case) attack the network(Ussing Arp Poissoning technique), and place it self between the iPhone and the Access point used to go to the internet.</p><p><img src="http://www.wlanbook.com/wp-content/uploads/2007/04/mitm.jpg" alt="alt text" /></p><p>Once you become the man in the middle, turn on wireshark capture at your NIC to see the traffic.</p><p>I recommend you to google around for MITM and ARP Poisoning. Also you will need some other gadgets besides wireshark, have a look at <a href="http://ettercap.sourceforge.net/">Ettercap</a></p><p>I don't know if this technique will work, when an iPhone device is involved, i never tried. But i see no reason why not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '11, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/251b4a8e3088f26eeadd3550e205818d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sfrj&#39;s gravatar image" /><p><span>sfrj</span><br />
<span class="score" title="74 reputation points">74</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sfrj has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Aug '11, 06:53</strong> </span></p></div></div><div id="comments-container-5739" class="comments-container"></div><div id="comment-tools-5739" class="comment-tools"></div><div class="clear"></div><div id="comment-5739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

