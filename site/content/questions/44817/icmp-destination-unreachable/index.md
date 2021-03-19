+++
type = "question"
title = "ICMP Destination Unreachable"
description = '''Hello everyone, I&#x27;m new to this forum but I hope you can help me. When I try to find Servers in different online games (ARK, DayZ SA,...) I find several servers when I start the game. But after about 400 servers I can&#x27;t find any more servers. After refresh I can&#x27;t find a single server. The network s...'''
date = "2015-08-04T05:19:00Z"
lastmod = "2015-08-05T02:57:00Z"
weight = 44817
keywords = [ "icmp" ]
aliases = [ "/questions/44817" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ICMP Destination Unreachable](/questions/44817/icmp-destination-unreachable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44817-score" class="post-score" title="current number of votes">0</div><span id="post-44817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I'm new to this forum but I hope you can help me.</p><p>When I try to find Servers in different online games (ARK, DayZ SA,...) I find several servers when I start the game. But after about 400 servers I can't find any more servers. After refresh I can't find a single server. The network seems to be really busy since I can't access any Website while the game is still opened.</p><p>So I tried to find out what is going on and used Wireshark. As soon as the game stops I get a bunch of ICMP Destination unreachable entries.</p><p>Turning off my firewall didn't help. I also contacted my ISP but didn't get any reply yet.</p><p>I attached a picture, tell me if you need the Log file</p><p>I hope you can help me with this issue :)</p><p>Thanks! <img src="https://osqa-ask.wireshark.org/upfiles/TrafficLog.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '15, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/05d442bf8c26b4ad262d7b48c9a232d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="th_ke&#39;s gravatar image" /><p><span>th_ke</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="th_ke has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Aug '15, 05:22</strong> </span></p></div></div><div id="comments-container-44817" class="comments-container"></div><div id="comment-tools-44817" class="comment-tools"></div><div class="clear"></div><div id="comment-44817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44823"></span>

<div id="answer-container-44823" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44823-score" class="post-score" title="current number of votes">0</div><span id="post-44823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the meaning of 'Communication Administratively Prohibited'? RFC 1812 states:</p><p><code>Routers SHOULD use Code 13 (Communication Administratively Prohibited) if they administratively filter packets.</code></p><p>This filtering may be dynamic, such as sending too much traffic of some kind, all depending on upstream policy.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '15, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-44823" class="comments-container"><span id="44827"></span><div id="comment-44827" class="comment"><div id="post-44827-score" class="comment-score"></div><div class="comment-text"><p>So its something only the provider can fix? Or is it some setting in my router? Its a FritzBOx 6340 Cable by the way...</p></div><div id="comment-44827-info" class="comment-info"><span class="comment-age">(04 Aug '15, 09:22)</span> <span class="comment-user userinfo">th_ke</span></div></div><span id="44850"></span><div id="comment-44850" class="comment"><div id="post-44850-score" class="comment-score"></div><div class="comment-text"><p>Upstream is any party between you and your destination, which may be multiple parties.</p></div><div id="comment-44850-info" class="comment-info"><span class="comment-age">(05 Aug '15, 00:10)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="44852"></span><div id="comment-44852" class="comment"><div id="post-44852-score" class="comment-score"></div><div class="comment-text"><p>So how can this problem be solved? Do I have any influence on it at all?</p></div><div id="comment-44852-info" class="comment-info"><span class="comment-age">(05 Aug '15, 00:14)</span> <span class="comment-user userinfo">th_ke</span></div></div><span id="44860"></span><div id="comment-44860" class="comment"><div id="post-44860-score" class="comment-score"></div><div class="comment-text"><p>I'd start with a call to Kabel_BW.</p></div><div id="comment-44860-info" class="comment-info"><span class="comment-age">(05 Aug '15, 02:19)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="44862"></span><div id="comment-44862" class="comment"><div id="post-44862-score" class="comment-score"></div><div class="comment-text"><p>Tried it yesterday, no response until now...</p></div><div id="comment-44862-info" class="comment-info"><span class="comment-age">(05 Aug '15, 02:57)</span> <span class="comment-user userinfo">th_ke</span></div></div></div><div id="comment-tools-44823" class="comment-tools"></div><div class="clear"></div><div id="comment-44823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

