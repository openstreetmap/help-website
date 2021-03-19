+++
type = "question"
title = "How can I read the whole WLAN?"
description = '''Hey, I&#x27;m new to Wireshark and I want to use it to improve my understanding of networks and protocols. What I want to do is: receive all packages in my WLAN for example packages sent/received by my phone. Is there a way to do that? &quot;Capture all in promiscuous mode&quot; doesn&#x27;t seem to do it. So how can I...'''
date = "2013-06-04T01:55:00Z"
lastmod = "2013-06-04T06:22:00Z"
weight = 21733
keywords = [ "wlan" ]
aliases = [ "/questions/21733" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I read the whole WLAN?](/questions/21733/how-can-i-read-the-whole-wlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21733-score" class="post-score" title="current number of votes">0</div><span id="post-21733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I'm new to Wireshark and I want to use it to improve my understanding of networks and protocols. What I want to do is: receive all packages in my WLAN for example packages sent/received by my phone.</p><p>Is there a way to do that? "Capture all in promiscuous mode" doesn't seem to do it. So how can I get this work? I mean what is a network sniffer good for if you only get the traffic from your own computer?</p><p>PS: I'm on Windows if that matters.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '13, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/2a023d0a408ee39d06205d00ebd7df11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TBJoe&#39;s gravatar image" /><p><span>TBJoe</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TBJoe has no accepted answers">0%</span></p></div></div><div id="comments-container-21733" class="comments-container"></div><div id="comment-tools-21733" class="comment-tools"></div><div class="clear"></div><div id="comment-21733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21734"></span>

<div id="answer-container-21734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21734-score" class="post-score" title="current number of votes">1</div><span id="post-21734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows you'll need an <a href="http://www.riverbed.com/de/products/cascade/wireshark_enhancements/airpcap.php">AirPCAP</a> adapter to capture the whole WLAN, otherwise you'll not see everything, just as you found out yourself. On Linux/MAC OS you could use Wireshark without special hardware as long as your network card can be enabled for monitor mode through the use of additional tools.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '13, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21734" class="comments-container"><span id="21740"></span><div id="comment-21740" class="comment"><div id="post-21740-score" class="comment-score"></div><div class="comment-text"><p>For (a lot) more details see the wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">WLAN capturing</a>.</p></div><div id="comment-21740-info" class="comment-info"><span class="comment-age">(04 Jun '13, 06:22)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-21734" class="comment-tools"></div><div class="clear"></div><div id="comment-21734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

