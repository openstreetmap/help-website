+++
type = "question"
title = "about the capacity of wireshark, so many packets drop"
description = '''I have met some problem with wireshark. my situation is i have a good IBM server,the server&#x27;s configuration is below： CPU: 4 core, xeon 7500, 2.0GHz disk: 10000RPM 600GBytes RAM: 32GBytes Ethernet ports: 1 Gigabit the version of wireshark: 1.6 64bits the OS : Windows 2008 R2  the flow of my data is ...'''
date = "2012-03-08T19:16:00Z"
lastmod = "2012-03-09T06:50:00Z"
weight = 9448
keywords = [ "drop", "capacity", "wireshark" ]
aliases = [ "/questions/9448" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [about the capacity of wireshark, so many packets drop](/questions/9448/about-the-capacity-of-wireshark-so-many-packets-drop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9448-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have met some problem with wireshark. my situation is i have a good IBM server,the server's configuration is below：</p><pre><code>CPU: 4 core, xeon 7500, 2.0GHz
disk: 10000RPM  600GBytes
RAM: 32GBytes
Ethernet ports:  1 Gigabit
the version of wireshark: 1.6 64bits
the OS : Windows 2008 R2</code></pre><p>the flow of my data is 250Mbps more or less, but when i collect the date for one hour, the size of the date collected is just only 95GBytes. So there are about 14Gbytes drop.</p><p>So, who can tell me why , and give me a solution, thanks a lot.</p></div><div id="question-tags" class="tags-container tags">drop capacity wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '12, 19:16</strong></p><img src="https://secure.gravatar.com/avatar/62534523076ca6a3c9484a615ba1e581?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anew_flyfree&#39;s gravatar image" /><p>anew_flyfree<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anew_flyfree has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Mar '12, 23:56</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-9448" class="comments-container"></div><div id="comment-tools-9448" class="comment-tools"></div><div class="clear"></div><div id="comment-9448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9455"></span>

<div id="answer-container-9455" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9455-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First thing to do is try the dumpcap utility: its job is to simply capture packets and do it quickly. It doesn't have all the overhead of the GUI.</p><p>Increasing the capture buffer size (with dumpcap's "-B" command-line argument) may also help.</p><p>If that doesn't help (enough), which I suppose may be the case if you're really talking 250 Mbps, you may need to look into some commercial solutions. Riverbed sponsors Wireshark and also makes products which complement it: for example dealing with high-speed and long-term capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '12, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-9455" class="comments-container"></div><div id="comment-tools-9455" class="comment-tools"></div><div class="clear"></div><div id="comment-9455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

