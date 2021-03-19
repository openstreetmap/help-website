+++
type = "question"
title = "Stop sniffing after a period of network inactivity"
description = '''I&#x27;m triggering tshark to capture packets when certain events occur. The actions I&#x27;m interested in capturing might last minutes, hours, or even days before ceasing, are on multiple interfaces, arbitrary hosts/IP addresses (public and private) and are captured in unique filenames. Unfortunately there ...'''
date = "2012-05-28T11:02:00Z"
lastmod = "2012-05-28T11:02:00Z"
weight = 11429
keywords = [ "inactivity", "autostop" ]
aliases = [ "/questions/11429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Stop sniffing after a period of network inactivity](/questions/11429/stop-sniffing-after-a-period-of-network-inactivity)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11429-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm triggering tshark to capture packets when certain events occur. The actions I'm interested in capturing might last minutes, hours, or even days before ceasing, are on multiple interfaces, arbitrary hosts/IP addresses (public and private) and are captured in unique filenames.</p><p>Unfortunately there is no magic packet that would signal the end of the event, so I have to figure out a way to stop capturing the stuff (obviously there is not much harm done if I continue to capture traffic, but eventually I'll have to kill off the process! :)) But if tshark hasn't captured any traffic in an hour or whatever, there's no need to continue.</p><p>I could write a little monitor to watch if tshark has written to the capture file lately, but I'm hoping there's some other method that might be simpler.</p><p>I'll note tshark already keeps track of time and traffic as well as how much data is written (e.g. the -a duration:{value,filesize,files} flags), so it should be an easy thing to add on ;)</p><p>Thanks for any suggestions -</p><p>dan</p></div><div id="question-tags" class="tags-container tags">inactivity autostop</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '12, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/d9f7a401ecf122119f58437b055d039d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zenfish&#39;s gravatar image" /><p>zenfish<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zenfish has no accepted answers">0%</span></p></div></div><div id="comments-container-11429" class="comments-container"></div><div id="comment-tools-11429" class="comment-tools"></div><div class="clear"></div><div id="comment-11429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

