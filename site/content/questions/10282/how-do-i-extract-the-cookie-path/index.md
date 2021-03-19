+++
type = "question"
title = "How do I Extract the cookie path?"
description = '''I am using wireshark to extract the cookie details. But wireshark only gives details like name of the cookie and value. How do I read the path tof the cookie for which it is set?'''
date = "2012-04-19T07:30:00Z"
lastmod = "2012-04-19T11:23:00Z"
weight = 10282
keywords = [ "cookies", "http", "wireshark" ]
aliases = [ "/questions/10282" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How do I Extract the cookie path?](/questions/10282/how-do-i-extract-the-cookie-path)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10282-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark to extract the cookie details. But wireshark only gives details like name of the cookie and value.<br />
How do I <strong>read the path</strong> tof the cookie for which it is set?</p></div><div id="question-tags" class="tags-container tags">cookies http wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '12, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/7e720df07b8a3ef623cf6a7587f21ab8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashwin&#39;s gravatar image" /><p>Ashwin<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashwin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-10282" class="comments-container"></div><div id="comment-tools-10282" class="comment-tools"></div><div class="clear"></div><div id="comment-10282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="10285"></span>

<div id="answer-container-10285" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10285-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean the URL for which the cookie was set ("path" being a confusing word here, because that would mean the storage file on a lokal disk instead) you can tell by the URL that was requested together with the cookie. Cookies are set for certain URLs/URIs, so if you see a cookie coming in together with a GET/POST/...-Request, then it is set for that URL. Unfortunately you can't tell the base URL though unless you gather a ton of requests and determine the scope manually.</p><p>For example if you see a cookie for <a href="http://www.test.com/whatever/">http://www.test.com/whatever/</a> you can't tell if the Cookie was set for that exact path, or if it was set for a broader scope of <a href="http://www.test.com">http://www.test.com</a>. But as soon as you see the same cookie coming back for <a href="http://www.test.com">http://www.test.com</a> you know it was.</p><p>It's usually easier to find a packet where the cookie was originally set, and read the scope from there. If you don't have that packet you have to determine it yourself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10285" class="comments-container"></div><div id="comment-tools-10285" class="comment-tools"></div><div class="clear"></div><div id="comment-10285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10284"></span>

<div id="answer-container-10284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10284-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You don't read the path in Wireshark because that information is not transmitted across the network, so it doesn't appear in the data captured by Wireshark. The path to the location where cookies are stored depends on which operating system and browser you are using. A little Googling will turn up the location for your browser and OS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-10284" class="comments-container"></div><div id="comment-tools-10284" class="comment-tools"></div><div class="clear"></div><div id="comment-10284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10295"></span>

<div id="answer-container-10295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10295-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just to complicate things, it is allowable, although not common, for the same cookie name to be set for different URL domains and/or paths, with either the same or a different value. The result is that the browser considers each one to be an independent cookie. So if a cookie named status is set to the value "bar" at <a href="http://www.test.com/,">http://www.test.com/,</a> and a second cookie named status is set to "fu" at <a href="http://www.test.com/whatever/,">http://www.test.com/whatever/,</a> then when your browser goes to the first URL the status cookie will be "bar" but when you go to the second URL the server will get: status=fu <strong>and</strong> status=bar. It is up to the server at that point to figure out what to do!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-10295" class="comments-container"></div><div id="comment-tools-10295" class="comment-tools"></div><div class="clear"></div><div id="comment-10295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

