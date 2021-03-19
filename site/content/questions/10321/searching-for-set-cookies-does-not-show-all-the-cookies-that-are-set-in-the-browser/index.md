+++
type = "question"
title = "Searching for set cookies  does not show all the cookies that are set in the browser"
description = '''I first cleared all the cookies in my browser. Then I went to www.yahoo.com. Mean while wireshark was capturing. In the search field of the wireshark, I entered http.set_cookie. But the filtered packets do not show all the cookies that are set in the browser. For example, the cookies shown(in wiresh...'''
date = "2012-04-19T22:02:00Z"
lastmod = "2012-04-20T01:11:00Z"
weight = 10321
keywords = [ "capture", "capture-filter", "cookie", "wireshark" ]
aliases = [ "/questions/10321" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Searching for set cookies does not show all the cookies that are set in the browser](/questions/10321/searching-for-set-cookies-does-not-show-all-the-cookies-that-are-set-in-the-browser)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10321-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I first cleared all the cookies in my browser. Then I went to <a href="http://www.yahoo.com">www.yahoo.com</a>. Mean while wireshark was capturing. In the search field of the wireshark, I entered http.set_cookie. But the filtered packets do not show all the cookies that are set in the browser. For example, the cookies shown(in wireshark) in the domain <a href="http://in.yahoo.com">in.yahoo.com</a> is only fpc. Where as in the browser 6 more cookies are set in that domain(like fpps, fpc_s, fpt etc)<br />
Why is this happening? Is wireshark not able to capture all the packets?</p></div><div id="question-tags" class="tags-container tags">capture capture-filter cookie wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '12, 22:02</strong></p><img src="https://secure.gravatar.com/avatar/7e720df07b8a3ef623cf6a7587f21ab8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashwin&#39;s gravatar image" /><p>Ashwin<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashwin has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '12, 22:03</p></div></div><div id="comments-container-10321" class="comments-container"></div><div id="comment-tools-10321" class="comment-tools"></div><div class="clear"></div><div id="comment-10321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10329"></span>

<div id="answer-container-10329" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10329-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark will not be able to capture any set_cookie commands that were sent encrypted over HTTPS. Since some websites will change from HTTP to HTTPS for "sensitive" transactions, please check to see whether there was HTTPS traffic which might have set the cookies. This is especially true if you logged into Yahoo with your ID and password during the session.</p><p>It is also possible for cookies to be set by javascript commands embedded in an HTML page, which your search filter may not detect.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '12, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-10329" class="comments-container"></div><div id="comment-tools-10329" class="comment-tools"></div><div class="clear"></div><div id="comment-10329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

