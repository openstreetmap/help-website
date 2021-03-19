+++
type = "question"
title = "How to exclude my traffic ?"
description = '''First of all sorry if this is a dumb question i am somehow unexperienced... i want to search with my network card but filter out my own traffic ... i guess the best would be to use not ip.src == xxx.xxx.xxx.xxx or not ip.addr=xxx.xxx.xxx.xxx maybe it´s possible to do this by MAC of the computer i am...'''
date = "2014-04-17T14:49:00Z"
lastmod = "2015-04-20T09:28:00Z"
weight = 31950
keywords = [ "exclude", "excludemyowntraffic", "sniff", "ip.addr", "ip.src" ]
aliases = [ "/questions/31950" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to exclude my traffic ?](/questions/31950/how-to-exclude-my-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31950-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First of all sorry if this is a dumb question i am somehow unexperienced...</p><p>i want to search with my network card but filter out my own traffic ... i guess the best would be to use <code>not ip.src == xxx.xxx.xxx.xxx</code> or <code>not ip.addr=xxx.xxx.xxx.xxx</code> maybe it´s possible to do this by MAC of the computer i am using ? any more graceful ideas ?(because i have more than 1 MAC i guess) and any ideas how i can prove this ? how can i see that it´s actually foreign traffic in my network ?</p></div><div id="question-tags" class="tags-container tags">exclude excludemyowntraffic sniff ip.addr ip.src</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '14, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/cec615fb40a2b1cb61a1cdb3e1cf11d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="astrionn&#39;s gravatar image" /><p>astrionn<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="astrionn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Apr '14, 17:09</p></div></div><div id="comments-container-31950" class="comments-container"><span id="31963"></span><div id="comment-31963" class="comment"><div id="post-31963-score" class="comment-score"></div><div class="comment-text"><p>okay i tried to exclude my ip address via 'not ip.addr == myip' but still get my data because i dont think that my neighbor visited the same sites like me ...</p></div><div id="comment-31963-info" class="comment-info"><span class="comment-age">(18 Apr '14, 03:38)</span> astrionn</div></div><span id="31964"></span><div id="comment-31964" class="comment"><div id="post-31964-score" class="comment-score"></div><div class="comment-text"><p>okay by now i excluded my ip address with ip.addr adn excluded my MAC´s but still see traffic i did ... what can i do ?</p></div><div id="comment-31964-info" class="comment-info"><span class="comment-age">(18 Apr '14, 05:22)</span> astrionn</div></div><span id="31965"></span><div id="comment-31965" class="comment"><div id="post-31965-score" class="comment-score"></div><div class="comment-text"><p>okay now i guess i did all i could even imagine to do to exclude my traffic and still see my traffic ...</p><p>not ip.addr == xxx.x.xx.xxx and not ip.src == xxx.x.xx.xx and not mac ==xx-xx-xx-xx-xx-xx and not mac ==xx-xx-xx-xx-xx-xx and not ip ==xxx.x.x.x and not ip.dst == xxx.x.xx.xxx and not ip.src == xxx.x.xx.xxx</p><p>i just copy paste this filter ... and i still see my own traffic ...</p></div><div id="comment-31965-info" class="comment-info"><span class="comment-age">(18 Apr '14, 05:36)</span> astrionn</div></div></div><div id="comment-tools-31950" class="comment-tools"></div><div class="clear"></div><div id="comment-31950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31952"></span>

<div id="answer-container-31952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31952-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is usually done by either removing all protocol bindings from the network card (especially IP addresses), or you could filter out your own MAC address. Something like "not ether host <strong>your-MAC-address</strong>".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '14, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31952" class="comments-container"><span id="31957"></span><div id="comment-31957" class="comment"><div id="post-31957-score" class="comment-score"></div><div class="comment-text"><p>okay seems legit thx</p></div><div id="comment-31957-info" class="comment-info"><span class="comment-age">(17 Apr '14, 15:51)</span> astrionn</div></div></div><div id="comment-tools-31952" class="comment-tools"></div><div class="clear"></div><div id="comment-31952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41602"></span>

<div id="answer-container-41602" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41602-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Substitute the "and not" on everything to "or not"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '15, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/40fd710c7f89e3fb3cc7cb0505f6bbc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skiltvakt&#39;s gravatar image" /><p>skiltvakt<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skiltvakt has no accepted answers">0%</span></p></div></div><div id="comments-container-41602" class="comments-container"></div><div id="comment-tools-41602" class="comment-tools"></div><div class="clear"></div><div id="comment-41602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

