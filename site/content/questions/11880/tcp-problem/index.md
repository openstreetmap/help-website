+++
type = "question"
title = "TCP problem"
description = '''![alt text][1] [1]: imgur.com&quot; /&amp;gt; This one capture at site B. I try to understand this. After [SYN], the server at site A just keep pushing the data to server at site B, but I did not see any [ACK] back at site B. I only see the Window size 92 but with unknown scaling. They communicate over satel...'''
date = "2012-06-13T16:38:00Z"
lastmod = "2012-06-18T16:58:00Z"
weight = 11880
keywords = [ "tcp" ]
aliases = [ "/questions/11880" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP problem](/questions/11880/tcp-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11880-score" class="post-score" title="current number of votes">0</div><span id="post-11880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>![alt text][1]</p><p>[1]: <a href="http://imgur.com/Kpgep"><img src="http://i.imgur.com/Kpgep.jpg" title="Hosted by &lt;a href=" />imgur.com</a>" /&gt;</p><p>This one capture at site B. I try to understand this. After [SYN], the server at site A just keep pushing the data to server at site B, but I did not see any [ACK] back at site B. I only see the Window size 92 but with unknown scaling. They communicate over satellite link. Any body can point out what going on? Is it due to the nature of Satellite link ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '12, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/2d16b30b269cb74533a6c723643a82f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pixaround&#39;s gravatar image" /><p><span>pixaround</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pixaround has no accepted answers">0%</span></p></img></div></div><div id="comments-container-11880" class="comments-container"><span id="12033"></span><div id="comment-12033" class="comment"><div id="post-12033-score" class="comment-score"></div><div class="comment-text"><p>Did you see any packets at all going from B to A? Such as the SYN-ACK at the start of the TCP connection? Is it possible that your capture interface is just not capturing packets originating at B?</p><p>The main difference about a Satellite link is that because of its long latency the TCP window will need to be negotiated to a much higher value than needed on a shorter link carrying the same number of bits per second.</p></div><div id="comment-12033-info" class="comment-info"><span class="comment-age">(18 Jun '12, 16:21)</span> <span class="comment-user userinfo">inetdog</span></div></div></div><div id="comment-tools-11880" class="comment-tools"></div><div class="clear"></div><div id="comment-11880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12035"></span>

<div id="answer-container-12035" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12035-score" class="post-score" title="current number of votes">0</div><span id="post-12035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>satellite links exist in different types. Two (among others) are:</p><ul><li>Two-way satellite communication (up-/download via satellite)</li><li>One-way receive, with terrestrial transmit (download via satellite, upload via Modem, ISDN, GPRS, 3G etc.)</li></ul><p>The third packet from the bottom ACKs the receipt of some bytes. If you don't see that data in Wireshark (your screenshot indicates that), there are two possible reasons:</p><ul><li>There is something wrong with your wireshark setup (hard to tell without further information)</li><li>OR, you see only one half of the communication, as the other half takes a different "route" (Modem, ISDN, 3G) that Wireshark is unable to see.</li></ul><p>Based on the information you provided, I assume the later.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '12, 17:36</strong> </span></p></div></div><div id="comments-container-12035" class="comments-container"></div><div id="comment-tools-12035" class="comment-tools"></div><div class="clear"></div><div id="comment-12035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

