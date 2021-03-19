+++
type = "question"
title = "WS not capturing packets on NW"
description = '''I&#x27;m running Kali on Virtualbox, and when I run WS it only captures traffic from my VM, like if I open Mozilla it&#x27;ll only capture traffic from Mozilla through Kali. My question is, how can I point WS to capture traffic from my network as a whole? Thank you.'''
date = "2017-07-29T12:11:00Z"
lastmod = "2017-07-30T21:58:00Z"
weight = 63240
keywords = [ "virtualbox", "kali-linux", "wireshark" ]
aliases = [ "/questions/63240" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WS not capturing packets on NW](/questions/63240/ws-not-capturing-packets-on-nw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63240-score" class="post-score" title="current number of votes">0</div><span id="post-63240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running Kali on Virtualbox, and when I run WS it only captures traffic from my VM, like if I open Mozilla it'll only capture traffic from Mozilla through Kali.</p><p>My question is, how can I point WS to capture traffic from my network as a whole?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-virtualbox" rel="tag" title="see questions tagged &#39;virtualbox&#39;">virtualbox</span> <span class="post-tag tag-link-kali-linux" rel="tag" title="see questions tagged &#39;kali-linux&#39;">kali-linux</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '17, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/78a1bbbf7825d9ee151640405f1495f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jtl369&#39;s gravatar image" /><p><span>jtl369</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jtl369 has no accepted answers">0%</span></p></div></div><div id="comments-container-63240" class="comments-container"><span id="63242"></span><div id="comment-63242" class="comment"><div id="post-63242-score" class="comment-score"></div><div class="comment-text"><p>The answer depends on many factors:</p><ul><li><p>do you want to capture on<br />
a) wireless or<br />
b) wired interface?</p></li><li><p>if wired, do you want to capture traffic of<br />
ba) other virtual machines running on the same host or<br />
bb) other physical machines and eventually virtual machines running on other hosts than the one hosting your Kali VM?</p></li></ul></div><div id="comment-63242-info" class="comment-info"><span class="comment-age">(30 Jul '17, 02:42)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="63248"></span><div id="comment-63248" class="comment"><div id="post-63248-score" class="comment-score"></div><div class="comment-text"><p>My physical machine is currently connected via wireless, I want to capture wireless packets of other physical machines on the network.</p></div><div id="comment-63248-info" class="comment-info"><span class="comment-age">(30 Jul '17, 17:22)</span> <span class="comment-user userinfo">jtl369</span></div></div></div><div id="comment-tools-63240" class="comment-tools"></div><div class="clear"></div><div id="comment-63240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63250"></span>

<div id="answer-container-63250" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63250-score" class="post-score" title="current number of votes">1</div><span id="post-63250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want to capture wireless packets of other physical machines on the network.</p></blockquote><p>According to <a href="https://www.virtualbox.org/manual/ch06.html#network_bridged">virtualbox documentation on networking</a>, there is currently no way to achieve that goal. To capture 3rd party wireless traffic, a wireless network card has to run in monitoring mode, which is not possible for guests on Virtualbox as they cannot achieve full and exclusive control over the wireless hardware.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '17, 21:58</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-63250" class="comments-container"></div><div id="comment-tools-63250" class="comment-tools"></div><div class="clear"></div><div id="comment-63250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

