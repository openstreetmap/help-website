+++
type = "question"
title = "Help to extract login information from captured data"
description = '''I tried to extract login information of window application game such as login portal and login data, but I am confuse where is it located https://drive.google.com/file/d/0Bwx9g-l32Xo0VTFWQXdEdXJJR2M/view?usp=sharing'''
date = "2017-01-28T02:14:00Z"
lastmod = "2017-01-28T04:52:00Z"
weight = 59115
keywords = [ "application", "login", "wireshark" ]
aliases = [ "/questions/59115" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help to extract login information from captured data](/questions/59115/help-to-extract-login-information-from-captured-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59115-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to extract login information of window application game such as login portal and login data, but I am confuse where is it located</p><p><a href="https://drive.google.com/file/d/0Bwx9g-l32Xo0VTFWQXdEdXJJR2M/view?usp=sharing">https://drive.google.com/file/d/0Bwx9g-l32Xo0VTFWQXdEdXJJR2M/view?usp=sharing</a></p></div><div id="question-tags" class="tags-container tags">application login wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '17, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/78914799f01f3bb0e545d3424bb1a264?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yyk&#39;s gravatar image" /><p>yyk<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yyk has no accepted answers">0%</span></p></div></div><div id="comments-container-59115" class="comments-container"></div><div id="comment-tools-59115" class="comment-tools"></div><div class="clear"></div><div id="comment-59115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59116"></span>

<div id="answer-container-59116" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59116-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A little more context might be helpful to understand what is supposed to happen. We could then focus on expectations to figure out where the information is.</p><p>The trace provided has a single TCP connection with some interesting information - if you right click on of the TCP packets and choose Follow TCP Stream (or use display filter: tcp.stream eq 0),</p><pre><code>POST /growtopia/server_data.php HTTP/1.0
Accept: */*
Host: growtopia1.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 37

version=2%2E44&amp;platform=0&amp;protocol=26HTTP/1.1 200 OK
Date: Sat, 28 Jan 2017 10:00:14 GMT
Server: Apache/2.2.15 (CentOS)
X-Powered-By: PHP/5.3.3
Content-Length: 312
Connection: close
Content-Type: text/html; charset=UTF-8

server|209.59.190.105
port|17092
type|1
**#maint|Server is currently down for `4scheduled maintenance``.  Sadly, this will probably take around four hours.** Follow @growtopiagame.com on twitter for info! #hurryupseth
beta_server|growtopiagame.com
beta_port|27003
beta_type|1
meta|124.13.121.122
RTENDMARKERBS1001</code></pre><p>I <strong>bolded</strong> the interesting piece. Is the issue that you can't get in, so you are trying to troubleshoot? If so, this might be root cause.</p><p>If the issue is something else, please provide more detail. There is some UDP traffic to the same host as the TCP connection so I can't discount that this may have additional information that you may be after. I would expect, however, that login occur over TCP, preferably over HTTPS for encryption, but I see regular port80 HTTP traffic here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '17, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-59116" class="comments-container"><span id="59119"></span><div id="comment-59119" class="comment"><div id="post-59119-score" class="comment-score"></div><div class="comment-text"><p>Additionally, it is highly unlikely the username/password will be submitted in plain text. I am sure when the server application facilitates the login, it will do so after a TLS session is established.</p></div><div id="comment-59119-info" class="comment-info"><span class="comment-age">(28 Jan '17, 13:32)</span> Rooster_50</div></div><span id="59120"></span><div id="comment-59120" class="comment"><div id="post-59120-score" class="comment-score">2</div><div class="comment-text"><p>Please have a first look here: <a href="https://blog.packet-foo.com/2016/07/how-to-use-wireshark-to-steal-passwords/">https://blog.packet-foo.com/2016/07/how-to-use-wireshark-to-steal-passwords/</a></p></div><div id="comment-59120-info" class="comment-info"><span class="comment-age">(28 Jan '17, 13:59)</span> Christian_R</div></div><span id="59179"></span><div id="comment-59179" class="comment"><div id="post-59179-score" class="comment-score"></div><div class="comment-text"><p>Hi, this http request is just load for annoucement, because I can still login even it say server is maintenance. I am not sure how it transfer the data, but there seem like no http/https request doing it, this log is start before login and stop after the game logged in so it should contain the data exchange between server and my computer.</p></div><div id="comment-59179-info" class="comment-info"><span class="comment-age">(31 Jan '17, 07:06)</span> yyk</div></div></div><div id="comment-tools-59116" class="comment-tools"></div><div class="clear"></div><div id="comment-59116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

