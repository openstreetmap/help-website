+++
type = "question"
title = "What is this? Destination port: cc-tracking"
description = '''I am trying to test my friends proxy to make sure his IP cant be pulled, and the IP 74.38.140.80 keeps popping up with the destination port cc-tracking. Every other skype IP gives a 5 digit destination port, but this IP and port just lurk around and dont belong to anyone that I know of. Anyone know ...'''
date = "2014-02-09T02:14:00Z"
lastmod = "2014-02-09T08:04:00Z"
weight = 29566
keywords = [ "skype" ]
aliases = [ "/questions/29566" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is this? Destination port: cc-tracking](/questions/29566/what-is-this-destination-port-cc-tracking)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29566-score" class="post-score" title="current number of votes">0</div><span id="post-29566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to test my friends proxy to make sure his IP cant be pulled, and the IP 74.38.140.80 keeps popping up with the destination port cc-tracking. Every other skype IP gives a 5 digit destination port, but this IP and port just lurk around and dont belong to anyone that I know of. Anyone know what the destination port means, or why even with my skype filter on it is getting through everytime? PLZ HELP!! :D Much thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-skype" rel="tag" title="see questions tagged &#39;skype&#39;">skype</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '14, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/c46fc5a8b4af6a9370ed868b12666758?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skratch&#39;s gravatar image" /><p><span>Skratch</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skratch has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Feb '14, 02:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29566" class="comments-container"></div><div id="comment-tools-29566" class="comment-tools"></div><div class="clear"></div><div id="comment-29566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29567"></span>

<div id="answer-container-29567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29567-score" class="post-score" title="current number of votes">1</div><span id="post-29567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A lot of tcp and udp ports are "allocated" for specific applications by <a href="http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt">IANA</a>, so Wireshark will show the application that is "allocated" for that port. In your case, cc-tracking is registered for tcp and udp port 4870.</p><p>Note that just because a port is "allocated" for an application doesn't mean all traffic using that port is the registered application, other applications are free to use the port if they wish on the understanding that they may encounter difficulties if the registered application is actually running.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '14, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-29567" class="comments-container"><span id="29571"></span><div id="comment-29571" class="comment"><div id="post-29571-score" class="comment-score"></div><div class="comment-text"><p>Ok that helps a little bit, its just weird that it popped up randomly today, everytime I have used Wireshark in the past month this IP and Port has never appeared. And all of a sudden it is popping up everytime I start the program, and it doesn't belong to anybody in the skype call. Just not sure where it is coming from, or if something changed to make it appear, such as a program I might have running that is causing it to show up. Your thoughts? (not crazy tech savy, so the simpler the terms the better!)</p></div><div id="comment-29571-info" class="comment-info"><span class="comment-age">(09 Feb '14, 03:02)</span> <span class="comment-user userinfo">Skratch</span></div></div><span id="29576"></span><div id="comment-29576" class="comment"><div id="post-29576-score" class="comment-score"></div><div class="comment-text"><p>If the IP address is one used by your machine then I would agree that it's down to a process running on your machine. You don't say what OS you're running, but using command line programs such as netstat can show what processes are using a port.</p></div><div id="comment-29576-info" class="comment-info"><span class="comment-age">(09 Feb '14, 08:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-29567" class="comment-tools"></div><div class="clear"></div><div id="comment-29567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

