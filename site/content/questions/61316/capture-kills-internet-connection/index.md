+++
type = "question"
title = "capture kills internet connection"
description = '''I can&#x27;t figure out why starting capture of my wifi adapter is killing my laptops internet connection. Current version of wireshark was working fine and causing no problems a couple days ago. Admittedly, I was up late hours poking and prodding settings and may have done something to cause this. Closi...'''
date = "2017-05-09T21:29:00Z"
lastmod = "2017-05-10T05:17:00Z"
weight = 61316
keywords = [ "capture", "connection", "kills" ]
aliases = [ "/questions/61316" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [capture kills internet connection](/questions/61316/capture-kills-internet-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61316-score" class="post-score" title="current number of votes">0</div><span id="post-61316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can't figure out why starting capture of my wifi adapter is killing my laptops internet connection. Current version of wireshark was working fine and causing no problems a couple days ago. Admittedly, I was up late hours poking and prodding settings and may have done something to cause this.</p><p>Closing wireshark, closing firefox, turn wifi-off, then back on, resets the connection and internet works again. I can load wireshark, internet keeps working. As soon as I click capture, the browser stops resolving, and no TCP, PORT, HTTP traffic is found in capture. It does scroll all kinds of beacon, etc.. activity from the wifi adapter in capture log.</p><p>This is on OSx v10.12.4. I don't think its my router as a fresh install of wireshark on another computer on this network works properly. I've been playing with PF settings during the same time I played with Wireshark settings, but I're restored PF to default, disabled PF all together, etc.. and the scenario of breaking internet connection is the same.</p><p>Any pointers on where I should start looking? I didn't find much searching google.</p><p>-David</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-kills" rel="tag" title="see questions tagged &#39;kills&#39;">kills</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '17, 21:29</strong></p><img src="https://secure.gravatar.com/avatar/3824e0c5281473468f580f4f10d9f835?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dryasia&#39;s gravatar image" /><p><span>dryasia</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dryasia has no accepted answers">0%</span></p></div></div><div id="comments-container-61316" class="comments-container"></div><div id="comment-tools-61316" class="comment-tools"></div><div class="clear"></div><div id="comment-61316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61320"></span>

<div id="answer-container-61320" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61320-score" class="post-score" title="current number of votes">0</div><span id="post-61320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dryasia has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using the WiFi card to capture <strong>and</strong> communicate with the Internet? Because if you do, the activation of monitor mode is probably the reason why you lose connectivity. WiFi cards are half duplex (either send or receive, not both at the exact same time) and as soon as you tell it to monitor, it will become receive-only full-time, so you can't send requests anymore.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '17, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61320" class="comments-container"><span id="61321"></span><div id="comment-61321" class="comment"><div id="post-61321-score" class="comment-score"></div><div class="comment-text"><p>For more info see the wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">WLAN Capture</a>, in particular the info about the various capture modes.</p></div><div id="comment-61321-info" class="comment-info"><span class="comment-age">(10 May '17, 03:41)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="61325"></span><div id="comment-61325" class="comment"><div id="post-61325-score" class="comment-score"></div><div class="comment-text"><p>That was it, thanks!</p></div><div id="comment-61325-info" class="comment-info"><span class="comment-age">(10 May '17, 05:17)</span> <span class="comment-user userinfo">dryasia</span></div></div></div><div id="comment-tools-61320" class="comment-tools"></div><div class="clear"></div><div id="comment-61320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

