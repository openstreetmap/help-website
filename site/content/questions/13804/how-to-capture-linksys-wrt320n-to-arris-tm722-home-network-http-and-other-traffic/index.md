+++
type = "question"
title = "HOW TO capture linksys wrt320n to arris tm722 home network HTTP and other traffic"
description = '''Hi WireShark community, I am new to wireshark and network monitoring in general, but not new to software and computer technology. I&#x27;m a software engineer with over 20 years experience, but have never dropped down this low in the weeds before. My goal is to use WireShark to capture all outbound web t...'''
date = "2012-08-21T17:54:00Z"
lastmod = "2012-08-22T00:07:00Z"
weight = 13804
keywords = [ "traffic", "modem", "http", "router" ]
aliases = [ "/questions/13804" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [HOW TO capture linksys wrt320n to arris tm722 home network HTTP and other traffic](/questions/13804/how-to-capture-linksys-wrt320n-to-arris-tm722-home-network-http-and-other-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13804-score" class="post-score" title="current number of votes">0</div><span id="post-13804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi WireShark community,</p><p>I am new to wireshark and network monitoring in general, but not new to software and computer technology. I'm a software engineer with over 20 years experience, but have never dropped down this low in the weeds before.</p><p>My goal is to use WireShark to capture all outbound web traffic going between my linksys/cisco wrt320n router and the comcast arris tm722 cable modem.</p><p>I want to be able to capture sending IP + destination IP/host + complete URL, along with a timestamp - then, ideally, log it to file.</p><p><strong>is this possible?</strong> or, not without additional software/hardware</p><p>Thanks in advance, Bob</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-modem" rel="tag" title="see questions tagged &#39;modem&#39;">modem</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '12, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/006972f7da88197cfbadb33f2c2d6d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bderemer&#39;s gravatar image" /><p><span>bderemer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bderemer has no accepted answers">0%</span></p></div></div><div id="comments-container-13804" class="comments-container"></div><div id="comment-tools-13804" class="comment-tools"></div><div class="clear"></div><div id="comment-13804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13810"></span>

<div id="answer-container-13810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13810-score" class="post-score" title="current number of votes">0</div><span id="post-13810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the topology between router and cable modem is ethernet it should be simple, but you might need to add a piece of hardware in between them - for example a hub (a real one, meaning a half duplex device, not a "switching hub") or a mini switch with port mirroring capabilities.</p><p>See also <a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '12, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13810" class="comments-container"></div><div id="comment-tools-13810" class="comment-tools"></div><div class="clear"></div><div id="comment-13810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

