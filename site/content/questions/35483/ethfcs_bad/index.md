+++
type = "question"
title = "eth.fcs_bad"
description = '''I use Wireshark V1.12.0 On a first platform, at different times, I record the same flow with a lot of frames with a eth.fcs_bad status ! I build a second identic platform in my office. With another PC, WIRESHARK 1.12.0, I see the same flow with a lot of frames with a eth.fcs_bad status ! On this sec...'''
date = "2014-08-14T08:42:00Z"
lastmod = "2014-08-19T04:23:00Z"
weight = 35483
keywords = [ "eth.fcs_bad" ]
aliases = [ "/questions/35483" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [eth.fcs\_bad](/questions/35483/ethfcs_bad)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35483-score" class="post-score" title="current number of votes">0</div><span id="post-35483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use Wireshark V1.12.0 On a first platform, at different times, I record the same flow with a lot of frames with a eth.fcs_bad status !</p><p>I build a second identic platform in my office. With another PC, WIRESHARK 1.12.0, I see the same flow with a lot of frames with a eth.fcs_bad status !</p><p>On this second platform I check this flow with another sniffer. I don't see theses eth.fcs_bad frames. What appends ?</p><p>Do you know this problem ?</p><p>Thank you for your help.</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-eth.fcs_bad" rel="tag" title="see questions tagged &#39;eth.fcs_bad&#39;">eth.fcs_bad</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '14, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/d5bf853f57ad4cc7b8b4a617cea4ca3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EURO59&#39;s gravatar image" /><p><span>EURO59</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EURO59 has no accepted answers">0%</span></p></div></div><div id="comments-container-35483" class="comments-container"></div><div id="comment-tools-35483" class="comment-tools"></div><div class="clear"></div><div id="comment-35483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35484"></span>

<div id="answer-container-35484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35484-score" class="post-score" title="current number of votes">0</div><span id="post-35484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you should turn off checking the FCS in the Ethernet dissector settings, because your frames most likely do not contain the FCS anyway. Only some hardware analyzers record those; normal PCs with standard NICs don't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '14, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35484" class="comments-container"><span id="35509"></span><div id="comment-35509" class="comment"><div id="post-35509-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>(normal PCs with standard NICs don't)</p></blockquote><p>...although some NICs can be configured to do so, and some drivers might do so. (I put the whole "heuristically determine whether there's an FCS or not" mechanism in because the Mac I was using at the time at work <em>did</em> include the FCS in incoming frames.)</p></div><div id="comment-35509-info" class="comment-info"><span class="comment-age">(15 Aug '14, 14:44)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="35567"></span><div id="comment-35567" class="comment"><div id="post-35567-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thank you for your answers</p><p>Of course if I switch off the eth.check-fcs there is no eth.fcs-bad frames anymore...</p><p>In my case my file records one TCP connection with MODBUS application protocol TCP connection is OK, MODBUS DATA are exchanged in each WAY Nearly 20 % of frames are in eth.fcs-bad. I don't understand why only PSH,ACK TCP frames from client to server have all an eth.fcs-bad status ! Note that theses frames have no data then they are short and have a padding</p><p>What do you think about that ?</p><p>Best regards</p></div><div id="comment-35567-info" class="comment-info"><span class="comment-age">(19 Aug '14, 04:11)</span> <span class="comment-user userinfo">EURO59</span></div></div><span id="35568"></span><div id="comment-35568" class="comment"><div id="post-35568-score" class="comment-score"></div><div class="comment-text"><p>Probably the heuristics mentioned by Guy thinks that the padding are the FCS</p></div><div id="comment-35568-info" class="comment-info"><span class="comment-age">(19 Aug '14, 04:23)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-35484" class="comment-tools"></div><div class="clear"></div><div id="comment-35484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

