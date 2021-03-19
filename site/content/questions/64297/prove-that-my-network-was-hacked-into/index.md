+++
type = "question"
title = "Prove that my network was hacked into"
description = '''Hi guys and girls, like the title says I have to prove that my network was hacked into and data was exfiltrated. I&#x27;m a total newbie on this program with about 6 hours in watching tutorials and messing around with it. It&#x27;s for my Ethical hacking class and any comments on where to start first or what ...'''
date = "2017-10-27T09:57:00Z"
lastmod = "2017-10-28T01:12:00Z"
weight = 64297
keywords = [ "filter", "packets", "protocol", "beginner" ]
aliases = [ "/questions/64297" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Prove that my network was hacked into](/questions/64297/prove-that-my-network-was-hacked-into)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64297-score" class="post-score" title="current number of votes">0</div><span id="post-64297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys and girls, like the title says I have to prove that my network was hacked into and data was exfiltrated. I'm a total newbie on this program with about 6 hours in watching tutorials and messing around with it. It's for my Ethical hacking class and any comments on where to start first or what I should be on the lookout for would be greatly appreciated. Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '17, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/68904afe1842e03bc0ed2f62300814ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fame346&#39;s gravatar image" /><p><span>fame346</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fame346 has no accepted answers">0%</span></p></div></div><div id="comments-container-64297" class="comments-container"></div><div id="comment-tools-64297" class="comment-tools"></div><div class="clear"></div><div id="comment-64297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64306"></span>

<div id="answer-container-64306" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64306-score" class="post-score" title="current number of votes">0</div><span id="post-64306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Bad news - Wireshark can only show you what is/was going on while a network traffic capture is/was running. So if your network has been hacked into for a one-time theft of data and that theft has already been completed, capturing network traffic any time after that cannot give you any clue about what has happened.</p><p>If you do have network captures from the suspected time of being hacked, you may use Wireshark to analyse them. But even in that case, it is normally close to impossible to find out the ultimate destination of the stolen data / ultimate source of the attack, as the IP addresses you eventually find to be involved are typically just proxies (whose admins have no clue that they were used for the attack as these boxes have themselves been also hacked before).</p><p>If some machines in your network got infected by malware and e.g. act as proxies for further attacks as described above, capturing the traffic and analysing it may highlight that - if you are lucky enough to be capturing while the malware is active.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '17, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-64306" class="comments-container"><span id="64309"></span><div id="comment-64309" class="comment"><div id="post-64309-score" class="comment-score"></div><div class="comment-text"><p>First off thank you for the response. As for the network capture my teacher did say the provided capture that was given to me was during the time that the network may or may not have been infiltrated. To give you an idea of how large this file is it's 148mb of pure network traffic. Is there any anomalies that I should look out for?</p></div><div id="comment-64309-info" class="comment-info"><span class="comment-age">(27 Oct '17, 14:51)</span> <span class="comment-user userinfo">fame346</span></div></div><span id="64317"></span><div id="comment-64317" class="comment"><div id="post-64317-score" class="comment-score"></div><div class="comment-text"><p>With such traffic volume I'd take the other way round, filter out everything that obviously is not malicious (e.g. hacking of a network cannot start from an ARP packet as only local machines can send ARP), and then filter out other things which seem normal.</p><p>Unless the network contains some servers made accessible from outside, a hacker needs to trick one of the machines in the network into actively downloading the malware as part of a web page (so usually the web server in the internet must be hacked first and its pages then contain some malicious scripts), or as part of an executable file which the user executes either after actively downloading it or after receiving it as an e-mail attachment.</p><p>So the whole exercise is to see from the capture how the network is organised (i.e. are there any connections initiated from outside the subnet? If so, there are servers made available for access from the internet), check every single traffic flow for type and, if capable of transferring code, for detailed contents. Audio and video streams or files may also contain malware as they may exploit bugs of popular media players, but I wouldn't expect this kind of attack in a school assignment.</p><p>Another approach is to observe order of things happening. If after finishing an SSL session (where you have no clue about the contents of the data being transferred) the receiving machine in that session starts doing funny things, like sending DNS queries with weird fqdns and then setting up connections to them, it can be an indicator of it just running a piece of malware. The mere fact that a web server uses SSL doesn't guarantee that it could not be hacked.</p><p>Good luck and let us know whether it was of any use.</p></div><div id="comment-64317-info" class="comment-info"><span class="comment-age">(28 Oct '17, 01:12)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-64306" class="comment-tools"></div><div class="clear"></div><div id="comment-64306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

