+++
type = "question"
title = "Not capturing POST requests"
description = '''Hi - relative Wireshark noob, but experienced computer scientist. I&#x27;m managing a large wireless network and have set Wireshark to capture all packets. After capturing approximately 1 million across a wide variety of users, our security team wanted to check HTTP POST requests.  Using the filter: http...'''
date = "2015-01-26T11:57:00Z"
lastmod = "2015-01-26T12:18:00Z"
weight = 39407
keywords = [ "post", "http.request.method", "noob" ]
aliases = [ "/questions/39407" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Not capturing POST requests](/questions/39407/not-capturing-post-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39407-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi - relative Wireshark noob, but experienced computer scientist.</p><p>I'm managing a large wireless network and have set Wireshark to capture all packets. After capturing approximately 1 million across a wide variety of users, our security team wanted to check HTTP POST requests.<br />
</p><p>Using the filter: http.request.method == "POST"</p><p>yielded ZERO results. Now, I am 100% certain that there were POST requests (I issued them personally from non-HTTPS). I was able to find the corresponding GET for each missing POST.</p><p>So, any ideas why I would be seeing absolutely no POST requests? Again, I'm new with Wireshark, but I do know that the POST requests were issued.</p><p>Thanks for the help.</p><p>-TB</p></div><div id="question-tags" class="tags-container tags">post http.request.method noob</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '15, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/c2a6cad1a8bf4db49d22a743bf0c26b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trollerboy&#39;s gravatar image" /><p>trollerboy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trollerboy has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39407" class="comments-container"></div><div id="comment-tools-39407" class="comment-tools"></div><div class="clear"></div><div id="comment-39407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39409"></span>

<div id="answer-container-39409" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39409-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, if you find "GET" requests for each location where you think there should be a "POST" you have found your problem (if there should be "POST"s instead) - because in HTTP, there is <strong>either</strong> "GET" <strong>or</strong> "POST" (or other request types). There is no "GET for POST" mechanism (maybe I misread your statement, but it looked to me this either/or may not be clear).</p><p>Are you sure there must be "POST" requests? You should see that request type as form tag action parameter, otherwise they're all "GET".</p><p>How did you "issue" your "POST" requests? You can only create them with form actions, or when using a tool like Fiddler, which can force that kind of request type. Using bookmarks, reloading pages, using links etc. are all "GET".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '15, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jan '15, 12:19</p></div></div><div id="comments-container-39409" class="comments-container"><span id="39412"></span><div id="comment-39412" class="comment"><div id="post-39412-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply, Jasper.<br />
</p><p>I used a post testing site (posttestserver.com) using the full URI as below:</p><p><a href="http://posttestserver.com/post.php?dump&amp;html&amp;dir=henry&amp;status_code=202&amp;sleep=2">http://posttestserver.com/post.php?dump&amp;html&amp;dir=henry&amp;status_code=202&amp;sleep=2</a></p><p>While I follow your train of thought, I think it is highly unlikely that after capturing over 1 million packets from across 40 simultaneous users, that I would get no POST requests to show.</p><p>I welcome and value your continued insight.</p><p>-TB</p></div><div id="comment-39412-info" class="comment-info"><span class="comment-age">(26 Jan '15, 12:41)</span> trollerboy</div></div><span id="39413"></span><div id="comment-39413" class="comment"><div id="post-39413-score" class="comment-score"></div><div class="comment-text"><p>It can happen if nobody fills out a form. My guess is that over 99% of all http requests are "GET" requests.</p><p>If you called that URL in a browser it will result in a "GET" request. Just calling your PHP script "post" does not make it a "POST" action. You need to put a form in it, with a "POST" action.</p><p>I created a test page for you with a "POST" form here:</p><p><a href="http://www.packet-foo.com/test/index.htm">http://www.packet-foo.com/test/index.htm</a></p><p>Try running Wireshark while using the button. You should see a POST request.</p></div><div id="comment-39413-info" class="comment-info"><span class="comment-age">(26 Jan '15, 12:52)</span> Jasper ♦♦</div></div><span id="39415"></span><div id="comment-39415" class="comment"><div id="post-39415-score" class="comment-score"></div><div class="comment-text"><p>Sure enough - you were correct! Thanks so much for making that little test page. It was exactly what I needed. You are a scholar and a gentleman.</p><p>Best regards,</p><p>-TB</p></div><div id="comment-39415-info" class="comment-info"><span class="comment-age">(26 Jan '15, 15:17)</span> trollerboy</div></div><span id="39416"></span><div id="comment-39416" class="comment"><div id="post-39416-score" class="comment-score"></div><div class="comment-text"><p>You're welcome, and thank you. You might want to accept my answer with the green check mark button next to it on the left to mark it accordingly for others to find.</p></div><div id="comment-39416-info" class="comment-info"><span class="comment-age">(26 Jan '15, 15:23)</span> Jasper ♦♦</div></div></div><div id="comment-tools-39409" class="comment-tools"></div><div class="clear"></div><div id="comment-39409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

