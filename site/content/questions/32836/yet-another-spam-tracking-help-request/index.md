+++
type = "question"
title = "Yet Another Spam Tracking Help Request"
description = '''We have been black listed a few times this year due to spam. I am trying to help figure out the cause of the issue. We have blocked communications on port 25. We operate a groupwise mail server, and we have blackhole routed the ip address that has been provided to us from the ISP. 172.22.218.222 I a...'''
date = "2014-05-15T12:12:00Z"
lastmod = "2014-05-15T12:12:00Z"
weight = 32836
keywords = [ "blocked", "25", "spam", "port", "wireshark" ]
aliases = [ "/questions/32836" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Yet Another Spam Tracking Help Request](/questions/32836/yet-another-spam-tracking-help-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32836-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have been black listed a few times this year due to spam. I am trying to help figure out the cause of the issue. We have blocked communications on port 25. We operate a groupwise mail server, and we have blackhole routed the ip address that has been provided to us from the ISP. 172.22.218.222</p><p>I am curious how I go about finding the culprit machine in my network. Since we have blocked the transmission on port 25 and we are not operating as an open relay, what should I be looking for exactly? I see in my spam filter that a large amount of email from a specific user is being differed because of our rate control. I can't see where the mail came from or originating ip. I can see who the end user is suppose to be, and the messages that are being sent are blank, at least when I view the email documents in the Barracuda spam filter, there is no content. We have changed the password of the offending user to something complicated but the intrusion still occurs. We have tried removing the account and setting up a new one for the user. This solves the issue for the user, but the spammer soon finds a new user and begins using that account.</p><p>Any help and insight is greatly appreciated!</p><p>My current set up is a wireshark machine and my mail server on a hub together, I am packet capturing everything at the moment, I would like to set up some filters that may help me, or some kind of expression to filter my results. Filtering port 25, has no affect as the port is blocked.</p><p>My next thought is to capture between gateway and firewall, or to port mirror on the main switch, but given that this is a network for education, there is ALWAYS a large amount of traffic to sift through.</p><p>To be honest, I am not sure if the offender is using the server as a relay, or if the machine is located locally, or accessing a machine locally to do it's bidding, this is what I would like to find.</p></div><div id="question-tags" class="tags-container tags">blocked 25 spam port wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '14, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/c0167f47fe549da521296101f49423a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaymes%20Driver&#39;s gravatar image" /><p>Jaymes Driver<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaymes Driver has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 May '14, 12:17</p></div></div><div id="comments-container-32836" class="comments-container"></div><div id="comment-tools-32836" class="comment-tools"></div><div class="clear"></div><div id="comment-32836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

