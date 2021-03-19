+++
type = "question"
title = "Spike in HTTP + lots of TCP out of order"
description = '''Hi,  Problem: The users experience a frequent disconnection. We have run wireshark on the PC of the user who was complaining. During the capture, he was connected to a few servers (setup explanation coming below) and claims his database connectivity &amp;amp; his SSH connections got disconnected. The wi...'''
date = "2014-10-02T19:56:00Z"
lastmod = "2014-10-14T08:48:00Z"
weight = 36809
keywords = [ "tcp-out-of-order" ]
aliases = [ "/questions/36809" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Spike in HTTP + lots of TCP out of order](/questions/36809/spike-in-http-lots-of-tcp-out-of-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36809-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Problem: The users experience a frequent disconnection. We have run wireshark on the PC of the user who was complaining. During the capture, he was connected to a few servers (setup explanation coming below) and claims his database connectivity &amp; his SSH connections got disconnected. The wireshark capture also shows a lot of HTTP traffic originating from this user going out onto the internet.</p><p>Link to sanitised file: <a href="https://www.cloudshark.org/captures/812a16a5d79a">https://www.cloudshark.org/captures/812a16a5d79a</a></p><p>Setup: UserPC (Wireshark Running) -&gt; Cisco Layer 2 Switch -&gt; CoreSwitch -&gt; IDS/IPS -&gt; Core Firewall -&gt; DMZ Firewall -&gt; Perimeter IDS/IPS -&gt; Perimeter Firewall -&gt; Internet</p><p>User Connections: 1. Connected to servers in the server VLAN (Database, SSH, ERP etc.) 2. Connected to websites on the internet</p><p>Review of Capture: There is a spike in HTTP Traffic for 4-5 seconds. Second 1 - 130000 bytes Second 2 - 160000 bytes Second 3 - 550000 bytes Second 4 - 300000 bytes Second 5 - 150000 bytes</p><p>During this time, there is a spike in TCP out of order packets (mainly due to HTTP). And the user experienced a network issue at this time. How should we analyse this situation?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">tcp-out-of-order</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '14, 19:56</strong></p><img src="https://secure.gravatar.com/avatar/2936d79aee56f6373531797bf8f444bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raymondw&#39;s gravatar image" /><p>raymondw<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raymondw has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Oct '14, 21:25</p></div></div><div id="comments-container-36809" class="comments-container"></div><div id="comment-tools-36809" class="comment-tools"></div><div class="clear"></div><div id="comment-36809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37038"></span>

<div id="answer-container-37038" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37038-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The out of order packets are due to the IDS/FW/Proxy sending to you using a reduced MSS of 1360 while receiving data at a MSS 1460 from the internet. This leads to 2 segments being sent to you: one with 1360 bytes and one with 100 bytes.<br />
The majority of small (100 bytes) segments arrive earlier than the logically preceding 1360 bytes causing lots of gap reports being sent upstream.<br />
I don't see any 'disconnects' in the trace though.<br />
I would suggest to figure out who is adjusting the MSS of your SYN packets to 1360 on their way to the proxy.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '14, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-37038" class="comments-container"></div><div id="comment-tools-37038" class="comment-tools"></div><div class="clear"></div><div id="comment-37038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36814"></span>

<div id="answer-container-36814" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36814-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hard to say without a look at the capture itself, because even though there is a lot of scenario description it does not really help that much. Something like "there is a spike for x seconds" is way to unspecific for any conclusion.</p><p>My advice would be either to post a capture, e.g. at <a href="http://www.cloudshark.org">Cloudshark</a> (sanitize it first if necessary, e.g by using <a href="http://www.tracewrangler.com">TraceWrangler</a>) and have someone here look at it.</p><p>If you can't do that you'll have to look for signs of trouble in your capture, e.g. by searching for TCP reset packets that indicate session problems. The trouble with that is that you need some experience to do that because there are resets that are perfectly normal and expected. You can also try to filter on "tcp.analysis.flags" to see if you have interesting expert symptoms - but still, a skilled analyst is often required to tell which ones are important and which can be ignored.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '14, 03:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-36814" class="comments-container"><span id="36848"></span><div id="comment-36848" class="comment"><div id="post-36848-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper.</p><p>I will sanitize and upload at cloudshark in a day. Thanks for the suggestion.</p><p>I have already seen the "tcp.analysis.flags". I didn't feel there was anything wrong with that. But, will look at it again, just in case.</p></div><div id="comment-36848-info" class="comment-info"><span class="comment-age">(05 Oct '14, 04:11)</span> raymondw</div></div><span id="36911"></span><div id="comment-36911" class="comment"><div id="post-36911-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>I have uploaded the sanitized trace file in cloudshark. Can I send you the link to the file?</p><p>Thanks</p></div><div id="comment-36911-info" class="comment-info"><span class="comment-age">(08 Oct '14, 01:34)</span> raymondw</div></div><span id="36912"></span><div id="comment-36912" class="comment"><div id="post-36912-score" class="comment-score"></div><div class="comment-text"><p>Edit your question with the link.</p></div><div id="comment-36912-info" class="comment-info"><span class="comment-age">(08 Oct '14, 02:37)</span> grahamb ♦</div></div></div><div id="comment-tools-36814" class="comment-tools"></div><div class="clear"></div><div id="comment-36814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

