+++
type = "question"
title = "Can Wireshark automatically resolve the IP address into host names?"
description = '''Can Wireshark automatically resolve the IP address into host names?'''
date = "2014-11-07T17:52:00Z"
lastmod = "2014-11-07T22:39:00Z"
weight = 37680
keywords = [ "ip", "address", "wireshark" ]
aliases = [ "/questions/37680" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark automatically resolve the IP address into host names?](/questions/37680/can-wireshark-automatically-resolve-the-ip-address-into-host-names)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37680-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can Wireshark automatically resolve the IP address into host names?</p></div><div id="question-tags" class="tags-container tags">ip address wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '14, 17:52</strong></p><img src="https://secure.gravatar.com/avatar/416a674ed40560b7da546111781bff02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolf1937&#39;s gravatar image" /><p>wolf1937<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolf1937 has no accepted answers">0%</span></p></div></div><div id="comments-container-37680" class="comments-container"></div><div id="comment-tools-37680" class="comment-tools"></div><div class="clear"></div><div id="comment-37680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37683"></span>

<div id="answer-container-37683" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37683-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>When you enable name resolution (Edit - Preferences - Name Resolution) <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-106.png" alt="alt text" /></p><p>Wireshark will resolve ip addresses to hostnames when the capture file contains DNS traffic or when you have a hosts file in your profile that maps ip addresses to hostnames.</p><p>You can also 'Use an external name resolver' to resolve the IP addresses using <strong>your DNS</strong> when you open the trace file. This might cause heavy UDP traffic from your machine if you are looking at large captures though so be cautious with this option.<br />
Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-37683" class="comments-container"></div><div id="comment-tools-37683" class="comment-tools"></div><div class="clear"></div><div id="comment-37683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

