+++
type = "question"
title = "Wireshark can&#x27;t see Mac wireless interface"
description = '''Hey, I&#x27;m trying to monitor my wireless network but I can&#x27;t see the interface in the capture options. Network Utility lists it as active, and it is active under the Preferences -&amp;gt; Network pane. Am I missing something?'''
date = "2011-12-06T20:34:00Z"
lastmod = "2011-12-07T11:27:00Z"
weight = 7811
keywords = [ "wireless", "interface", "macintosh" ]
aliases = [ "/questions/7811" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark can't see Mac wireless interface](/questions/7811/wireshark-cant-see-mac-wireless-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7811-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I'm trying to monitor my wireless network but I can't see the interface in the capture options.</p><p>Network Utility lists it as active, and it is active under the Preferences -&gt; Network pane.</p><p>Am I missing something?</p></div><div id="question-tags" class="tags-container tags">wireless interface macintosh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '11, 20:34</strong></p><img src="https://secure.gravatar.com/avatar/bb0dd8c140ac683baf24b6438c825c87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ASGR&#39;s gravatar image" /><p>ASGR<br />
<span class="score" title="20 reputation points">20</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ASGR has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Dec '11, 08:50</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-7811" class="comments-container"><span id="7815"></span><div id="comment-7815" class="comment"><div id="post-7815-score" class="comment-score"></div><div class="comment-text"><p>Can you see <em>any</em> interfaces? (I assume, from "Network Utility", that "mac" means "Mac", as in what used to be called "Macintoshes", so, for example, you would probably have <code>en0</code> and <code>en1</code> and <code>lo0</code> interfaces, at least; Network Utility might not show you <code>lo0</code>, as it doesn't correspond to any real hardware or, in fact, to anything that can be used to communicate with another machine, but it <em>is</em> a network interface at the software layer, and you can capture on it.)</p></div><div id="comment-7815-info" class="comment-info"><span class="comment-age">(07 Dec '11, 00:21)</span> Guy Harris ♦♦</div></div><span id="7818"></span><div id="comment-7818" class="comment"><div id="post-7818-score" class="comment-score"></div><div class="comment-text"><p>Thanks for reply.</p><p>Yes. Both en0 and lo0 are listed as selectable interfaces and are capable of capturing packets from, but it's en1 that refuses to be identified. I also tested WS with a wireless network connected with the status of the wireless network as active and still nothing.</p><p>Network Utility listed the interfaces as you described. I had it working before but I get the feeling that I had to do something specific like running WS from root?</p></div><div id="comment-7818-info" class="comment-info"><span class="comment-age">(07 Dec '11, 05:11)</span> ASGR</div></div><span id="7827"></span><div id="comment-7827" class="comment"><div id="post-7827-score" class="comment-score"></div><div class="comment-text"><p>In order to see any interfaces, <code>dumpcap</code> needs to be running with a user and group ID that have read access to the <code>/dev/bpf</code><em>N</em> devices. With the standard Wireshark 1.6.x installation for Mac OS X Snow Leopard, that happens. This doesn't depend on the interface; if you see any interfaces at all, you're running with the right privilege.</p><p>However, the interface has to be "up"; what does <code>/sbin/ifconfig -a</code> print?</p></div><div id="comment-7827-info" class="comment-info"><span class="comment-age">(07 Dec '11, 10:00)</span> Guy Harris ♦♦</div></div><span id="7829"></span><div id="comment-7829" class="comment"><div id="post-7829-score" class="comment-score"></div><div class="comment-text"><p>Below is the output for wireless interface only...</p><pre><code>en1: flags=8822&lt;BROADCAST,SMART,SIMPLEX,MULTICAST&gt; mtu 1500
        ether (output withheld)
        media: autoselect (&lt;unknown type&gt;) status: inactive
        supported media: autoselect</code></pre></div><div id="comment-7829-info" class="comment-info"><span class="comment-age">(07 Dec '11, 10:46)</span> ASGR</div></div></div><div id="comment-tools-7811" class="comment-tools"></div><div class="clear"></div><div id="comment-7811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7830"></span>

<div id="answer-container-7830" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7830-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've just changed the ownership of /dev/bpf* to the same user as WireShark and all the interfaces are now available including firewire and wireless.</p><p>I was relying on accessing /dev/bpf* through group privileges that had rw- but it doesn't seem to like this.</p><p>For prosperity... Use an admin account to run wireshark and give the /dev/bpf* files the same user with rw- privileges.</p><p>Confirmed that it is now working. Thanks for your help.</p><p>A.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '11, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/bb0dd8c140ac683baf24b6438c825c87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ASGR&#39;s gravatar image" /><p>ASGR<br />
<span class="score" title="20 reputation points">20</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ASGR has no accepted answers">0%</span></p></div></div><div id="comments-container-7830" class="comments-container"><span id="7831"></span><div id="comment-7831" class="comment"><div id="post-7831-score" class="comment-score"></div><div class="comment-text"><p>I'm still surprised you even saw <code>en0</code> and <code>lo0</code> if you didn't have access to <code>/dev/bpf*</code>.</p><p>What version of Mac OS X are you running? What version of Wireshark are you running? How did you install that version of Wireshark? As indicated, at least on Snow Leopard, the Wireshark installer should give you access to <code>/dev/bpf*</code> by adding you to the <code>access_bpf</code> group and adding a startup item to make all the BPF devices that exist at start-up time readable and writable by that group; that works on my machine, for example.</p></div><div id="comment-7831-info" class="comment-info"><span class="comment-age">(07 Dec '11, 11:24)</span> Guy Harris ♦♦</div></div><span id="7832"></span><div id="comment-7832" class="comment"><div id="post-7832-score" class="comment-score"></div><div class="comment-text"><p>And does the wireless interface still not have the UP flag set now that you can capture on it?</p></div><div id="comment-7832-info" class="comment-info"><span class="comment-age">(07 Dec '11, 11:26)</span> Guy Harris ♦♦</div></div><span id="7836"></span><div id="comment-7836" class="comment"><div id="post-7836-score" class="comment-score"></div><div class="comment-text"><p>I'm just as surprised... The owner:group was set to 'root:wheel' with rw-rw----. That seemed to work for en0 and lo0 but not for fw0 or en1.</p><p>After changing the owner:group to 'root:admin' with the same rw-rw----, Wireshark now recognises all interfaces available.</p><p>I'm running OSX 10.5.8 with Wireshark 1.6.4 that was installed by the packaged installer. After looking through the StartUpItems, nothing seems to be out-of-order. All items have 'root:wheel' so it should all be executed properly. But yet it seemed to fail to change the group!</p></div><div id="comment-7836-info" class="comment-info"><span class="comment-age">(07 Dec '11, 12:11)</span> ASGR</div></div></div><div id="comment-tools-7830" class="comment-tools"></div><div class="clear"></div><div id="comment-7830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7833"></span>

<div id="answer-container-7833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7833-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The wireless interface did not have the UP flag according to <code>ifconfig</code>, so it was not available for capture. If you can capture on it now, it probably has the UP flag set.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '11, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7833" class="comments-container"><span id="7837"></span><div id="comment-7837" class="comment"><div id="post-7837-score" class="comment-score"></div><div class="comment-text"><p>It certainly has...</p><p>en1: flags=8823&lt;up,broadcast,smart,simplex,multicast&gt; mtu 1500 ether (...) media: autoselect (&lt;unknown type=""&gt;) status: inactive supported media: autoselect</p><p>... and the status changes to active.</p></div><div id="comment-7837-info" class="comment-info"><span class="comment-age">(07 Dec '11, 12:20)</span> ASGR</div></div><span id="7839"></span><div id="comment-7839" class="comment"><div id="post-7839-score" class="comment-score"></div><div class="comment-text"><p>I've double checked the access and permissions and it does seem to look like the problem was in there somewhere.</p><p>Also I may have not pressed the 'Apply' button to get the 'UP' flag on the interface. Apple can have an inconsistent UI sometimes.</p></div><div id="comment-7839-info" class="comment-info"><span class="comment-age">(07 Dec '11, 13:20)</span> ASGR</div></div></div><div id="comment-tools-7833" class="comment-tools"></div><div class="clear"></div><div id="comment-7833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

