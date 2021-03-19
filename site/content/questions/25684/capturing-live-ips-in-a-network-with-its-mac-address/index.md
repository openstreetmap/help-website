+++
type = "question"
title = "Capturing live IP&#x27;s in a network with its MAC Address?"
description = '''Is it possible to capture all live IP Address in a network along with its MAC Address?? If yes, can someone explain me the way to acheive this task pls? Thank you.'''
date = "2013-10-06T17:33:00Z"
lastmod = "2013-10-07T08:18:00Z"
weight = 25684
keywords = [ "ipaddress", "mac-address" ]
aliases = [ "/questions/25684" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing live IP's in a network with its MAC Address?](/questions/25684/capturing-live-ips-in-a-network-with-its-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25684-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to capture all live IP Address in a network along with its MAC Address?? If yes, can someone explain me the way to acheive this task pls? Thank you.</p></div><div id="question-tags" class="tags-container tags">ipaddress mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '13, 17:33</strong></p><img src="https://secure.gravatar.com/avatar/b41802fe7f333c0b2b2b68be7da4f757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karthick&#39;s gravatar image" /><p>Karthick<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karthick has no accepted answers">0%</span></p></div></div><div id="comments-container-25684" class="comments-container"></div><div id="comment-tools-25684" class="comment-tools"></div><div class="clear"></div><div id="comment-25684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25688"></span>

<div id="answer-container-25688" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25688-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It depends almost entirely on how you define "network". Normally, if you run wireshark on your own computer, you will only see your own traffic, between your computer and the switch. If you're talking about your local broadcast domain, you may be able to 'mirror' all traffic transiting your local switch over to a 'SPAN' port on that switch and monitor all the traffic there using wireshark. In either case, wireshark will by default capture both the IP and MAC addresses of all the traffic that it sees. Simply fire up wireshark, select the network interface in use, and click "start". For information on SPAN ports, see the documentation provided by the switch vendor.<br />
</p><p>If you define 'network' as everything in your building or campus, then it becomes a much more difficult proposition, and would generally require access to resources on other switches not commonly available to the average end-user.</p><p>I'm ignoring for the purposes of this discussion tools like ettercap which would allow you to poison a given switch CAM table to re-direct certain traffic so that you can see it. Google "ettercap" if you wish to pursue that angle.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '13, 19:47</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p>griff<br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span> </br></p></div></div><div id="comments-container-25688" class="comments-container"><span id="25689"></span><div id="comment-25689" class="comment"><div id="post-25689-score" class="comment-score"></div><div class="comment-text"><p>thank you.</p></div><div id="comment-25689-info" class="comment-info"><span class="comment-age">(06 Oct '13, 21:30)</span> Karthick</div></div><span id="25700"></span><div id="comment-25700" class="comment"><div id="post-25700-score" class="comment-score"></div><div class="comment-text"><p>as soon as your "network" has routers: no, you probably can't do that, because MACs are "hidden" behind routers - they are only visible in the local broadcast segment. So unless you capture everywhere in all broadcast zones you won't be able to map all IPs to their MACs.</p></div><div id="comment-25700-info" class="comment-info"><span class="comment-age">(07 Oct '13, 00:55)</span> Jasper ♦♦</div></div></div><div id="comment-tools-25688" class="comment-tools"></div><div class="clear"></div><div id="comment-25688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25716"></span>

<div id="answer-container-25716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25716-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to capture all live IP Address in a network along with its MAC Address?</p></blockquote><p>Not really, as 'live' does not mean a system will also send and/or receive data. In that case the system might be alive, but still invisible for you.</p><p>A network capture tool is not an ideal solution for this kind of problem. As others have already answered: You will detect those systems that are local to your capture device (remote also possible with certain capture setups), including their MAC address, however you will only see those systems that are communicating while you capture data.</p><p>I suggest to use a network scanner to identify all live systems on the local network (including their MAC address + much more information about those systems). There are many tools out there, so I'll name only two:</p><ul><li><a href="http://www.softperfect.com/products/networkscanner/">Softperfect Network Scanner</a></li><li><a href="http://www.nmap.org">nmap</a></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25716" class="comments-container"><span id="51531"></span><div id="comment-51531" class="comment"><div id="post-51531-score" class="comment-score"></div><div class="comment-text"><p>hello kurt can you please help me how to change source coulumn so i can only see IP address as i am seeing MAC address when i try to copy file from source to destination. [email protected]</p></div><div id="comment-51531-info" class="comment-info"><span class="comment-age">(09 Apr '16, 05:24)</span> aliimran63</div></div></div><div id="comment-tools-25716" class="comment-tools"></div><div class="clear"></div><div id="comment-25716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

