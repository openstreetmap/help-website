+++
type = "question"
title = "Interfaces related question"
description = '''How can I do that wireshark read the interfaces from the /etc/network/interfaces file? I had inserted there a virtual interface and wireshark don&#x27;t see it'''
date = "2013-03-23T06:25:00Z"
lastmod = "2013-03-23T17:25:00Z"
weight = 19768
keywords = [ "interface", "local", "wireshark" ]
aliases = [ "/questions/19768" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Interfaces related question](/questions/19768/interfaces-related-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19768-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I do that wireshark read the interfaces from the /etc/network/interfaces file?</p><p>I had inserted there a virtual interface and wireshark don't see it</p></div><div id="question-tags" class="tags-container tags">interface local wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '13, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/73acd993c6739c4668c05f7b61e971cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mcgiwer&#39;s gravatar image" /><p>Mcgiwer<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mcgiwer has no accepted answers">0%</span></p></div></div><div id="comments-container-19768" class="comments-container"></div><div id="comment-tools-19768" class="comment-tools"></div><div class="clear"></div><div id="comment-19768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19783"></span>

<div id="answer-container-19783" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19783-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark sees interfaces that are reported to it by libpcap/WinPcap; libpcap/WinPcap report whatever interfaces are reported to it by whatever mechanism libpcap/WinPcap uses to find the interfaces, and those mechanisms are OS-dependent.</p><p>None of those mechanisms involve <code>/etc/network/interfaces</code>; they involve asking the OS what interfaces <em>actually exist</em>, not what interfaces are listed in a configuration file used by the OS to set up interfaces (the OS might, for example, not be able to create an interface that's specified in a configuration file, and Wireshark should not offer those non-existent interfaces).</p><p><code>/etc/network/interfaces</code> <a href="http://forums.fedoraforum.org/showthread.php?t=162231">is, apparently, a Debian configuration file</a>.</p><p>libpcap/WinPcap will not report interfaces on which it cannot capture.</p><p>If you do <code>ls /sys/class/net</code>, does your virtual interface show up there?</p><p>If it doesn't, perhaps it wasn't created, even though it's listed in <code>/etc/network/interfaces</code>, so neither Wireshark nor tcpdump nor any other program can see it (it's hard to see something that doesn't exist...).</p><p>If it does show up there, what happens if you do <code>sudo tcpdump -i</code> {virtual interface name}, where {virtual interface name} is the name of your virtual interface? If that fails, perhaps, for some reason, no program can capture on that virtual interface, in which case there's no point in libpcap reporting it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '13, 17:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19783" class="comments-container"></div><div id="comment-tools-19783" class="comment-tools"></div><div class="clear"></div><div id="comment-19783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

