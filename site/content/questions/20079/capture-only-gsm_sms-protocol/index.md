+++
type = "question"
title = "capture only gsm_sms protocol"
description = '''Hello! I need to capture only (!!!) gsm_sms protocol from the SS7 stream with the help of the tshark. But unfortunately I could not find any useful information in Internet how to create such filter. Maybe somebody could help me with this? Any examples or links... Any help will be appreciated! Thanks...'''
date = "2013-04-04T06:58:00Z"
lastmod = "2013-04-09T06:23:00Z"
weight = 20079
keywords = [ "gsm_sms", "tshark", "ss7" ]
aliases = [ "/questions/20079" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capture only gsm\_sms protocol](/questions/20079/capture-only-gsm_sms-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20079-score" class="post-score" title="current number of votes">0</div><span id="post-20079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I need to capture only (!!!) gsm_sms protocol from the SS7 stream with the help of the tshark. But unfortunately I could not find any useful information in Internet how to create such filter. Maybe somebody could help me with this? Any examples or links...</p><p>Any help will be appreciated! Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gsm_sms" rel="tag" title="see questions tagged &#39;gsm_sms&#39;">gsm_sms</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-ss7" rel="tag" title="see questions tagged &#39;ss7&#39;">ss7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '13, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/2d7d6eacf9c502b9188b233cb3e1d8ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="domeno&#39;s gravatar image" /><p><span>domeno</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="domeno has no accepted answers">0%</span></p></div></div><div id="comments-container-20079" class="comments-container"></div><div id="comment-tools-20079" class="comment-tools"></div><div class="clear"></div><div id="comment-20079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20218"></span>

<div id="answer-container-20218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20218-score" class="post-score" title="current number of votes">2</div><span id="post-20218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use this (display) filter with tshark:</p><blockquote><p><code>tshark -ni eth0 -R "gsm_sms"</code><br />
</p></blockquote><p>Please replace eth0 with your interface name.</p><p>Unfortunately, you can't write the data stream to a pcap file (Option -w) while you are using a display filter (-R).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20218" class="comments-container"><span id="20232"></span><div id="comment-20232" class="comment"><div id="post-20232-score" class="comment-score"></div><div class="comment-text"><p>To Kurt</p><p>Thanks for the reply. But I have no any problem with the display filters. I need to capture events in the “gsm_sms” protocols and then write them into the files.</p><p>And now I have problem to write correct capture filter for the “gsm_sms” protocol. May be you know how to write correct capture filter for this protocol?</p><p>With best regards.</p></div><div id="comment-20232-info" class="comment-info"><span class="comment-age">(08 Apr '13, 22:16)</span> <span class="comment-user userinfo">domeno</span></div></div><span id="20238"></span><div id="comment-20238" class="comment"><div id="post-20238-score" class="comment-score"></div><div class="comment-text"><p>I don't think there is a way to use a <strong>capture filter</strong> to identify gsm_sms, as the capture filters have no protocol intelligence at the GSM level (only IP, UDP, TCP, etc.), so it would be hard/impossible to detect a gsm_sms message/packet.</p><p>Your best option is to capture everything and then later use Wireshark or tshark to just analyze gsm_sms with a display filter.</p><p>You can also ask the people at <a href="http://openbsc.osmocom.org/trac/wiki/OsmocomOverview">osmocom.org</a> (see <strong>lists</strong>). Maybe they can help or have any further idea. If so, please update here as well for the benefit of all ;-)</p></div><div id="comment-20238-info" class="comment-info"><span class="comment-age">(09 Apr '13, 05:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20218" class="comment-tools"></div><div class="clear"></div><div id="comment-20218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20239"></span>

<div id="answer-container-20239" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20239-score" class="post-score" title="current number of votes">2</div><span id="post-20239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Generally each protocol messages follows a definite structure. You have to decode the frame in order to find the GSM SMS protocol data.</p><p>Generally GSM SMS will have the following sequence, <a href="https://docs.google.com/file/d/0B81y2c59Ta9HRzZqNmZsNXgtVzg/edit?usp=sharing">https://docs.google.com/file/d/0B81y2c59Ta9HRzZqNmZsNXgtVzg/edit?usp=sharing</a></p><p>The 21st byte of M3UA (refer to the above link) will be the indicator for the following protocol. It specifies which protocol message follows M3UA.</p><p>This may give you an idea how to proceed. GSM SMS protocol specifications can be found in ITU-T Q.7xx(not sure which number exactly it is) series of ITU-T. It is available freely.</p><p>No other way other than digging detail in to the frame to find out specific protocol message. I explored this when i tried to find out only ISUP messages. So not sure about GSM SMS. But I hope this will be handy. Will post it here if I find anything else.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '13, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/b2940a37e14d31283e43c55dc07a1fea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manoj%20G&#39;s gravatar image" /><p><span>Manoj G</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manoj G has 2 accepted answers">33%</span></p></div></div><div id="comments-container-20239" class="comments-container"></div><div id="comment-tools-20239" class="comment-tools"></div><div class="clear"></div><div id="comment-20239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

