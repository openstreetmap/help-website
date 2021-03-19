+++
type = "question"
title = "Why am I getting AppleTalk Packets (Zone Information Protocol) in my scan"
description = '''Hello, I am on a LAN that has no Apple equipment I ran a 15 min. Baseline scan on my LAN and found some ZIP (AppleTalk) stuff. There are no Apple devices on my network so why am I getting this protocol on my network? '''
date = "2014-09-12T11:24:00Z"
lastmod = "2014-09-12T14:46:00Z"
weight = 36279
keywords = [ "appletalk", "zip" ]
aliases = [ "/questions/36279" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why am I getting AppleTalk Packets (Zone Information Protocol) in my scan](/questions/36279/why-am-i-getting-appletalk-packets-zone-information-protocol-in-my-scan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36279-score" class="post-score" title="current number of votes">0</div><span id="post-36279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am on a LAN that has no Apple equipment I ran a 15 min. Baseline scan on my LAN and found some ZIP (AppleTalk) stuff. There are no Apple devices on my network so why am I getting this protocol on my network?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/InterestingProtocols.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-appletalk" rel="tag" title="see questions tagged &#39;appletalk&#39;">appletalk</span> <span class="post-tag tag-link-zip" rel="tag" title="see questions tagged &#39;zip&#39;">zip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '14, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p><span>Beldum</span><br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></img></div></div><div id="comments-container-36279" class="comments-container"></div><div id="comment-tools-36279" class="comment-tools"></div><div class="clear"></div><div id="comment-36279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36280"></span>

<div id="answer-container-36280" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36280-score" class="post-score" title="current number of votes">2</div><span id="post-36280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jasper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Those frames usually originate from print servers, mostly embedded devices that are part of networked printers theses days. You should check all printers to see if they have AppleTalk enabled and disable it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '14, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36280" class="comments-container"><span id="36282"></span><div id="comment-36282" class="comment"><div id="post-36282-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, how did you know those kind of messages are usually associated with and originate from print servers? I think you are right though. Thanks once again!</p></div><div id="comment-36282-info" class="comment-info"><span class="comment-age">(12 Sep '14, 11:36)</span> <span class="comment-user userinfo">Beldum</span></div></div><span id="36283"></span><div id="comment-36283" class="comment"><div id="post-36283-score" class="comment-score">1</div><div class="comment-text"><p>well, nobody is using AppleTalk anymore, and those printers are always the reason why that protocol shows up every once in a while. So it wasn't from your screenshot but from 10 years of experience in network analysis that I diagnosed (well, guessed) that cause.</p><p>BTW if my answer helped, you might want accept it with the check mark button on the left ;-)</p></div><div id="comment-36283-info" class="comment-info"><span class="comment-age">(12 Sep '14, 11:40)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="36284"></span><div id="comment-36284" class="comment"><div id="post-36284-score" class="comment-score"></div><div class="comment-text"><p>Jasper, I'm a noob to this forum, I thumbed up your answer, but I have no idea how to mark it as the correct answer.</p></div><div id="comment-36284-info" class="comment-info"><span class="comment-age">(12 Sep '14, 11:54)</span> <span class="comment-user userinfo">Beldum</span></div></div><span id="36285"></span><div id="comment-36285" class="comment"><div id="post-36285-score" class="comment-score"></div><div class="comment-text"><p>Jasper, just a quick question, is port 1900 safe? It seems that I am getting SSDP traffic on my LAN.</p></div><div id="comment-36285-info" class="comment-info"><span class="comment-age">(12 Sep '14, 12:00)</span> <span class="comment-user userinfo">Beldum</span></div></div><span id="36286"></span><div id="comment-36286" class="comment"><div id="post-36286-score" class="comment-score">1</div><div class="comment-text"><p>No worries, it's not a problem, and we were all noobs at one point in time ;-)</p><p>Port 1900 is often used by service discovery protocols to see what kind of services a node offers. This is also often seen with print servers.</p></div><div id="comment-36286-info" class="comment-info"><span class="comment-age">(12 Sep '14, 12:06)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="36287"></span><div id="comment-36287" class="comment not_top_scorer"><div id="post-36287-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper you are very understanding lol. Based on my LAN baseline scan, with the ZIP and SSDP protocol messages coming from my print server, does that mean my network is at risk? I know that 192.168.10.1 source IP address is sending a multicast message to 239.255.255.250. That is the SSDP protocol on port 1900. Is that something I should be worried about?</p></div><div id="comment-36287-info" class="comment-info"><span class="comment-age">(12 Sep '14, 12:14)</span> <span class="comment-user userinfo">Beldum</span></div></div><span id="36291"></span><div id="comment-36291" class="comment not_top_scorer"><div id="post-36291-score" class="comment-score"></div><div class="comment-text"><p>Normally not, no, since that is a private LAN and not accessible from the outside. Plus, there should be a firewall protecting the network from external access.</p></div><div id="comment-36291-info" class="comment-info"><span class="comment-age">(12 Sep '14, 14:46)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-36280" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-36280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

