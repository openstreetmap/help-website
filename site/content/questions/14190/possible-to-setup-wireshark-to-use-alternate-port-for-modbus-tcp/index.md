+++
type = "question"
title = "Possible to setup Wireshark to use alternate port for Modbus TCP?"
description = '''Hello -- We have a server setup to act as three separate Modbus &quot;slave servers&quot;. One uses the standard Modbus TCP port 502. The others use ports 503 and 504, respectively. When we use Wireshark to look at network traffic, it has no problem recognizing all port 502 traffic as Modbus TCP protocol. How...'''
date = "2012-09-11T13:11:00Z"
lastmod = "2014-05-22T06:51:00Z"
weight = 14190
keywords = [ "modbus", "protocol", "tcp" ]
aliases = [ "/questions/14190" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Possible to setup Wireshark to use alternate port for Modbus TCP?](/questions/14190/possible-to-setup-wireshark-to-use-alternate-port-for-modbus-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14190-score" class="post-score" title="current number of votes">0</div><span id="post-14190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello -- We have a server setup to act as three separate Modbus "slave servers". One uses the standard Modbus TCP port 502. The others use ports 503 and 504, respectively. When we use Wireshark to look at network traffic, it has no problem recognizing all port 502 traffic as Modbus TCP protocol. However, it does not recognize the other port traffic as Modbus TCP. Is there some "easy" way to configure Wireshark to see 502, 503, and 504 for Modbus TCP? Thanks for any ideas. Regards, Steve</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '12, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/9578c59c1cbb579b64d330ef5a62d766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sreiner&#39;s gravatar image" /><p><span>sreiner</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sreiner has no accepted answers">0%</span></p></div></div><div id="comments-container-14190" class="comments-container"></div><div id="comment-tools-14190" class="comment-tools"></div><div class="clear"></div><div id="comment-14190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14192"></span>

<div id="answer-container-14192" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14192-score" class="post-score" title="current number of votes">0</div><span id="post-14192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could select a packet of one of the flows on those ports and use the popup menu to choose "Decode As" -&gt; "Transport" -&gt; "Modbus/TCP".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '12, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14192" class="comments-container"><span id="32983"></span><div id="comment-32983" class="comment"><div id="post-32983-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>any idea why "Modbus/TCP" is not listed when chosing "Decode As" -&gt; "Transport"?? However, Modbus/TCP packets on port 502 are disected as "Modbus/TCP"</p><p>(Wireshark 1.10.7)</p></div><div id="comment-32983-info" class="comment-info"><span class="comment-age">(22 May '14, 04:31)</span> <span class="comment-user userinfo">Alfonso</span></div></div><span id="32985"></span><div id="comment-32985" class="comment"><div id="post-32985-score" class="comment-score"></div><div class="comment-text"><p>I'll just say "Decode As" ... does show Modbus/TCP for me in Wireshark-1.10.7. I'd suggest trying again. :)</p></div><div id="comment-32985-info" class="comment-info"><span class="comment-age">(22 May '14, 05:55)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="32993"></span><div id="comment-32993" class="comment"><div id="post-32993-score" class="comment-score"></div><div class="comment-text"><p>Well, it does... I was doing "Decode As" on UDP packets. It shows up on TCP, though. What I was trying to decode is our Modbus/TCP broadcasted over UDP.</p><p>Thanks a lot.</p></div><div id="comment-32993-info" class="comment-info"><span class="comment-age">(22 May '14, 06:44)</span> <span class="comment-user userinfo">Alfonso</span></div></div><span id="32996"></span><div id="comment-32996" class="comment"><div id="post-32996-score" class="comment-score">1</div><div class="comment-text"><p>see: <a href="http://ask.wireshark.org/questions/32617/modbusudp-support">modbusudp-support</a></p></div><div id="comment-32996-info" class="comment-info"><span class="comment-age">(22 May '14, 06:51)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-14192" class="comment-tools"></div><div class="clear"></div><div id="comment-14192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

