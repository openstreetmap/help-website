+++
type = "question"
title = "Difference between RST/ACK and RST responses in a Null scan"
description = '''From what I have researched so far on NULL scans, there are 2 conflicting answers regarding the results of the NULL scan. In a NULL scan, some sources state that if RST/ACK response is received from the server, that means the server is closed. However, other sources state RST/ACK as only RST. Is the...'''
date = "2012-12-22T08:33:00Z"
lastmod = "2012-12-23T18:12:00Z"
weight = 17164
keywords = [ "port-scanning", "port" ]
aliases = [ "/questions/17164" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Difference between RST/ACK and RST responses in a Null scan](/questions/17164/difference-between-rstack-and-rst-responses-in-a-null-scan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17164-score" class="post-score" title="current number of votes">0</div><span id="post-17164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From what I have researched so far on NULL scans, there are 2 conflicting answers regarding the results of the NULL scan.</p><p>In a NULL scan, some sources state that if RST/ACK response is received from the server, that means the server is closed.</p><p>However, other sources state RST/ACK as only RST. Is there a difference between the 2 of them ?</p><p>Thanks =) .</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-port-scanning" rel="tag" title="see questions tagged &#39;port-scanning&#39;">port-scanning</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '12, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/9b52984d9786885d47fe81e43d8591ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinged&#39;s gravatar image" /><p><span>Dinged</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinged has no accepted answers">0%</span></p></div></div><div id="comments-container-17164" class="comments-container"><span id="17168"></span><div id="comment-17168" class="comment"><div id="post-17168-score" class="comment-score"></div><div class="comment-text"><p>how does your Null scan look like? Which tool did you use?</p></div><div id="comment-17168-info" class="comment-info"><span class="comment-age">(22 Dec '12, 09:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17170"></span><div id="comment-17170" class="comment"><div id="post-17170-score" class="comment-score"></div><div class="comment-text"><p>Hmm I didn't actually perform the NULL scan, I am currently trying to do some read up on NULL scans and encountered different answers. Some books state it as such,"This is an advanced scan that may be able to pass through firewalls undetected or modified. Null scan has all flags off or not set. It only works on Unix systems. Closed ports will return a RST flag." while others state it as a RST/ACK flag &gt;&gt; see image <a href="http://i.imgur.com/7FKeM.png">http://i.imgur.com/7FKeM.png</a></p></div><div id="comment-17170-info" class="comment-info"><span class="comment-age">(22 Dec '12, 09:22)</span> <span class="comment-user userinfo">Dinged</span></div></div><span id="17172"></span><div id="comment-17172" class="comment"><div id="post-17172-score" class="comment-score"></div><div class="comment-text"><p>well, don't (blindly) believe what's written in books. Try yourself. That will also help you to understand the whole thing much better. Grab <a href="http://nmap.org/">nmap</a> and Wireshark and test how different operating systems react ;-)</p><p>Furthermore, listen to the advice of <span>@Jasper</span>.</p></div><div id="comment-17172-info" class="comment-info"><span class="comment-age">(22 Dec '12, 09:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17173"></span><div id="comment-17173" class="comment"><div id="post-17173-score" class="comment-score"></div><div class="comment-text"><p>Haha you've a point =) . Guess I should do some hands-on..</p></div><div id="comment-17173-info" class="comment-info"><span class="comment-age">(22 Dec '12, 09:32)</span> <span class="comment-user userinfo">Dinged</span></div></div><span id="17174"></span><div id="comment-17174" class="comment"><div id="post-17174-score" class="comment-score"></div><div class="comment-text"><p>Yep, there nothing to loose, other than a few minutes/hours of your live ;-)</p></div><div id="comment-17174-info" class="comment-info"><span class="comment-age">(22 Dec '12, 09:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17164" class="comment-tools"></div><div class="clear"></div><div id="comment-17164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17165"></span>

<div id="answer-container-17165" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17165-score" class="post-score" title="current number of votes">1</div><span id="post-17165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dinged has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are so many different TCP stacks out there, so everything is possible, especially when it comes to scanning systems with invalid flags set or not set. Usually, all packets coming from systems that do not intentionally fool around with packet details (like the one doing the scan) have the ACK flag set unless it is the initial SYN packet of the three way handshake.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '12, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17165" class="comments-container"><span id="17171"></span><div id="comment-17171" class="comment"><div id="post-17171-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the information. So whether is it a RST/ACK or a RST packet being sent from the server is dependent on the TCP stacks and the usual case would be a RST/ACK result right ?</p></div><div id="comment-17171-info" class="comment-info"><span class="comment-age">(22 Dec '12, 09:25)</span> <span class="comment-user userinfo">Dinged</span></div></div><span id="17213"></span><div id="comment-17213" class="comment"><div id="post-17213-score" class="comment-score"></div><div class="comment-text"><p>yes, it is dependent on the TCP stack implementation, and since there is no case in the TCP RFC stating what to do when a packet with no flags arrives, it is quite impossible to predict the reaction. I'd not be surprised if you get a mix of RST, RST/ACK or even no packet at all when testing various targets.</p></div><div id="comment-17213-info" class="comment-info"><span class="comment-age">(23 Dec '12, 18:12)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-17165" class="comment-tools"></div><div class="clear"></div><div id="comment-17165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

