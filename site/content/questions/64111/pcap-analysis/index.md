+++
type = "question"
title = "Pcap analysis"
description = '''Can someone tell me if there is anything malicious in this pcap? https://drive.google.com/open?id=0B1VcVVkZTYTJYTZ0Ny1rZmNwam8 Thankyou so much!'''
date = "2017-10-23T08:07:00Z"
lastmod = "2017-10-24T11:46:00Z"
weight = 64111
keywords = [ "malicious", "pcap" ]
aliases = [ "/questions/64111" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Pcap analysis](/questions/64111/pcap-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64111-score" class="post-score" title="current number of votes">0</div><span id="post-64111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone tell me if there is anything malicious in this pcap?</p><p><a href="https://drive.google.com/open?id=0B1VcVVkZTYTJYTZ0Ny1rZmNwam8">https://drive.google.com/open?id=0B1VcVVkZTYTJYTZ0Ny1rZmNwam8</a></p><p>Thankyou so much!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malicious" rel="tag" title="see questions tagged &#39;malicious&#39;">malicious</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '17, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/42a40141589fe4f48f4a73360ee6474f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subb148&#39;s gravatar image" /><p><span>subb148</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subb148 has no accepted answers">0%</span></p></div></div><div id="comments-container-64111" class="comments-container"></div><div id="comment-tools-64111" class="comment-tools"></div><div class="clear"></div><div id="comment-64111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64113"></span>

<div id="answer-container-64113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64113-score" class="post-score" title="current number of votes">0</div><span id="post-64113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To me it looks as if the 192.168.56.105 is trying to determine what operating system the 192.168.56.107 is running by sending it various weird packets (like TCP packet with no flags at all) and analysing its reaction to them, and maybe it also checks for presence of known protocol stack vulnerabilities the same way.</p><p>Mentioning of <a href="https://nmap.org/">nmap</a> in the HTTP OPTIONS request supports this theory, but it may as well be that the 192.168.56.105 already became a botnet zombie and tries to find an exploitable vulnerability on its network neighbor (possibly using nmap).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '17, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-64113" class="comments-container"><span id="64115"></span><div id="comment-64115" class="comment"><div id="post-64115-score" class="comment-score"></div><div class="comment-text"><p>Thank-you so much :)</p></div><div id="comment-64115-info" class="comment-info"><span class="comment-age">(23 Oct '17, 09:57)</span> <span class="comment-user userinfo">subb148</span></div></div><span id="64117"></span><div id="comment-64117" class="comment"><div id="post-64117-score" class="comment-score"></div><div class="comment-text"><p>If its okay, can you quickly have a look at this as well. <a href="https://drive.google.com/file/d/0B1VcVVkZTYTJdGJnSXVZdm9qaWM/view?usp=sharing">https://drive.google.com/file/d/0B1VcVVkZTYTJdGJnSXVZdm9qaWM/view?usp=sharing</a> , I would love your feedback if this is normal traffic or not :)</p></div><div id="comment-64117-info" class="comment-info"><span class="comment-age">(23 Oct '17, 10:01)</span> <span class="comment-user userinfo">subb148</span></div></div><span id="64118"></span><div id="comment-64118" class="comment"><div id="post-64118-score" class="comment-score"></div><div class="comment-text"><p>Are you sure I'm not doing your homework for you?</p><p>The only thing suspicious here is that when 192.168.56.106 as tcp client connects to 192.168.56.105 as server and then issues bash commands in plaintext and gets them responded, all that without any previous authentication, it connects to port 4440 which IANA lists as unassigned. So it seems that the rsh service on 192.168.56.105 is listening at a non-standard port.</p><p>The reason why I think it is a homework is that 192.168.56.105 acts as a potential attacker in this scenario while it acts as a potential victim in the previous one.</p><p>If it is not a homework, the explanation could be that 192.168.56.106 has became a zombie (by a previously "zombieized" 192.168.56.105) already before this capture has been started, and has been instructed to test rsh communication with 192.168.56.105, thus e.g. verifying that lists of authorized clients for rsh have been successfully modified there.</p></div><div id="comment-64118-info" class="comment-info"><span class="comment-age">(23 Oct '17, 11:02)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="64129"></span><div id="comment-64129" class="comment"><div id="post-64129-score" class="comment-score"></div><div class="comment-text"><p>Omg..you're an absolute legend. Yes it makes complete sense. I'm at Uni and we were asked to find if there was malicious activity for around 100 pcaps. Out of 100, I have 20 which I was not able to figure out if there was anything malicious at all.</p><p>But thankyou so so much! Is there any way you can help me out with the other pcaps? I'm willing to pay you for your time :)</p><p>But thank-you again!</p></div><div id="comment-64129-info" class="comment-info"><span class="comment-age">(23 Oct '17, 14:53)</span> <span class="comment-user userinfo">subb148</span></div></div><span id="64159"></span><div id="comment-64159" class="comment"><div id="post-64159-score" class="comment-score"></div><div class="comment-text"><p>To hire someone is a proper homework solution if you study MBA :-) For IT studies, the proper solution is to look through the captures which seem not to be that big and watch for things like</p><ul><li>opening TCP sessions to many different ports, possibly closing them with FIN or RESET without transferring a single byte of payload,</li><li>sending packets with weird contents (where Wireshark is very helpful as it highlights in yellow and red packets which it cannot decode properly,</li><li>repeated attempts to log in using telnet and/or ssh (because with each attempt the attacker tries a new username/password combination),</li><li>repeated attempts to register using SIP (same case as above),</li><li>tcp session establishment attempts coming from many different IPs (tens of thousands and above) at the same time - these are not conquest attempts but DDoS in progress</li><li>others which I don't know a I am not a cybersecurity expert, so I have no idea about all those exploits like heartbleeding bug where the password was retrieved from victim's storage at the first login attempt rather than tried from a vocabulary list.</li></ul></div><div id="comment-64159-info" class="comment-info"><span class="comment-age">(24 Oct '17, 09:34)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="64163"></span><div id="comment-64163" class="comment not_top_scorer"><div id="post-64163-score" class="comment-score"></div><div class="comment-text"><p>Thankyou so so much!</p></div><div id="comment-64163-info" class="comment-info"><span class="comment-age">(24 Oct '17, 11:46)</span> <span class="comment-user userinfo">subb148</span></div></div></div><div id="comment-tools-64113" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-64113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

