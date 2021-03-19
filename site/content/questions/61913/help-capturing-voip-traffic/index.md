+++
type = "question"
title = "Help capturing VoIP traffic"
description = '''Configured a monitor port on the switch. Connected to this port. Only seeing Local IP traffic Anyone help me configure this as I most be doing something wrong.'''
date = "2017-06-09T09:36:00Z"
lastmod = "2017-06-13T06:30:00Z"
weight = 61913
keywords = [ "voice", "sip", "voip", "rtp" ]
aliases = [ "/questions/61913" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help capturing VoIP traffic](/questions/61913/help-capturing-voip-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61913-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Configured a monitor port on the switch. Connected to this port. Only seeing Local IP traffic</p><p>Anyone help me configure this as I most be doing something wrong.</p></div><div id="question-tags" class="tags-container tags">voice sip voip rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '17, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/7afec5dc1baa9a14b27abc5b4889684f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lslifkin&#39;s gravatar image" /><p>lslifkin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lslifkin has no accepted answers">0%</span></p></div></div><div id="comments-container-61913" class="comments-container"><span id="61917"></span><div id="comment-61917" class="comment"><div id="post-61917-score" class="comment-score"></div><div class="comment-text"><p>'The switch' is a rather generic indication of the networking equipment we are supposed to help you with... Last time I checked we're not psychic, so you've got to tell us exactly what you're working with and what you're doing.</p></div><div id="comment-61917-info" class="comment-info"><span class="comment-age">(09 Jun '17, 10:14)</span> Jaap ♦</div></div><span id="61920"></span><div id="comment-61920" class="comment"><div id="post-61920-score" class="comment-score"></div><div class="comment-text"><p>The switch is a HPE 1920 48Port PoE+ switch. Port 23 has been configured as the Monitor Port. When I start a capture, it seems that 90% of all traffic is the laptop that I am connected to. Want to exclude that in the capture and look to get VoIP traffic logged</p></div><div id="comment-61920-info" class="comment-info"><span class="comment-age">(09 Jun '17, 12:00)</span> lslifkin</div></div><span id="61921"></span><div id="comment-61921" class="comment"><div id="post-61921-score" class="comment-score"></div><div class="comment-text"><p>This may be obvious but make sure: - Span port is correctly configured - In wireshark make sure you enable promiscuous mode on the capturing interface</p><p>You may want to remove any capture filters just in case there's an error in it.</p></div><div id="comment-61921-info" class="comment-info"><span class="comment-age">(09 Jun '17, 12:12)</span> jerioux</div></div></div><div id="comment-tools-61913" class="comment-tools"></div><div class="clear"></div><div id="comment-61913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61985"></span>

<div id="answer-container-61985" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61985-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In addition to defining a monitor port - the port(s) to monitor - you have to define a mirror port (where to send the traffic). Something like:</p><pre><code>; Monitor these ports
interface 3-4,7-9,18,27,31,37
   monitor
   exit
; Send the data to here
mirror-port 24</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '17, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/efd6c87b3ea03d76a316e1bc5cf19a07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbAtAffirmed&#39;s gravatar image" /><p>dbAtAffirmed<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbAtAffirmed has no accepted answers">0%</span></p></div></div><div id="comments-container-61985" class="comments-container"></div><div id="comment-tools-61985" class="comment-tools"></div><div class="clear"></div><div id="comment-61985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

