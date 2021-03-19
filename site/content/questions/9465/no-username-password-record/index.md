+++
type = "question"
title = "No Username Password Record"
description = '''I recently downloaded Wireshark to monitor my son&#x27;s internet activity, which has been suspicious lately. He has his Facebook Password saved to the computer, but not his e-mail&#x27;s (I have a feeling they might be the same). Wireshark is recording packets, but when I log into his Facebook, all the Packe...'''
date = "2012-03-10T11:43:00Z"
lastmod = "2012-03-10T17:03:00Z"
weight = 9465
keywords = [ "username", "capture", "password", "packet" ]
aliases = [ "/questions/9465" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [No Username Password Record](/questions/9465/no-username-password-record)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9465-score" class="post-score" title="current number of votes">0</div><span id="post-9465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently downloaded Wireshark to monitor my son's internet activity, which has been suspicious lately. He has his Facebook Password saved to the computer, but not his e-mail's (I have a feeling they might be the same). Wireshark is recording packets, but when I log into his Facebook, all the Packet information is in Wireshark except for Username and Password when I go to "Follow TCP Stream." In fact, Username and Password are not appearing for any site after logging in. I even tried plugging an Ethernet cord directly into the computer from the modem after wireless did not work. Please help.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-username" rel="tag" title="see questions tagged &#39;username&#39;">username</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '12, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/4f54682ca1b77499fe7f9d4482472328?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cats10&#39;s gravatar image" /><p><span>cats10</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cats10 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-9465" class="comments-container"></div><div id="comment-tools-9465" class="comment-tools"></div><div class="clear"></div><div id="comment-9465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9467"></span>

<div id="answer-container-9467" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9467-score" class="post-score" title="current number of votes">1</div><span id="post-9467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From an experiment I just did, logging out from Facebook and logging back in, it appears that the login process is - not surprisingly - done over SSL/TLS-encapsulated HTTP ("https"), but the process of browsing Facebook, at least, is done over regular HTTP (I never post to Facebook, so I don't know whether that's done with regular or SSL/TLS-encapsulated HTTP).</p><p>This means that the user name and password are probably sent over port 443 rather than port 80, so it's not in the same TCP stream as the rest of the Facebook traffic and thus won't show up in Follow TCP Stream.</p><p>In addition, it means that it's encrypted; Wireshark can decrypt SSL/TLS-encapsulated traffic, if enough information is supplied - see <a href="http://wiki.wireshark.org/SSL">the Wireshark Wiki page on SSL</a> - but that might require you to get some information from your son's computer. (It's encrypted to prevent people from doing exactly what you're trying to do - capture private information such as passwords. Your traffic to a Web site could, if not SSL/TLS-encapsulated, be sniffed, in principle, by, for example, somebody at your ISP.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '12, 17:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9467" class="comments-container"></div><div id="comment-tools-9467" class="comment-tools"></div><div class="clear"></div><div id="comment-9467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9466"></span>

<div id="answer-container-9466" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9466-score" class="post-score" title="current number of votes">0</div><span id="post-9466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a packet analyser not a network monitor. Having said that, it can be used to determine log on credentials for web sites, but only if those websites don't use any form of security when logging in. AFAIK Facebook has optional security enabled on a per-account basis. Email accounts, especially web based ones, usually have security enabled.</p><p>See this previous question and the answers regarding facebook logins: <a href="http://ask.wireshark.org/questions/4903/using-wireshark-to-detect-facebook-login-and-chat">facebook logins</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '12, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9466" class="comments-container"></div><div id="comment-tools-9466" class="comment-tools"></div><div class="clear"></div><div id="comment-9466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

