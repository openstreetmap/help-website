+++
type = "question"
title = "Wireshark doesn&#x27;t see my interface"
description = '''Hello all, I&#x27;ve used Wireshark many times in the past in both Windows and Linux. I can spell TCP/IP but I am no expert. On my blazing 750 MHz Linux (2.6.32) Ubuntu (Lucid Lynx 10.04 LTS) machine, Wireshark does not list my NIC card. I expected to see eth0 listed, but it&#x27;s not. I am on the machine no...'''
date = "2011-08-24T19:37:00Z"
lastmod = "2017-06-23T05:24:00Z"
weight = 5861
keywords = [ "interface", "capture" ]
aliases = [ "/questions/5861" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't see my interface](/questions/5861/wireshark-doesnt-see-my-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5861-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all, I've used Wireshark many times in the past in both Windows and Linux. I can spell TCP/IP but I am no expert. On my blazing 750 MHz Linux (2.6.32) Ubuntu (Lucid Lynx 10.04 LTS) machine, Wireshark does not list my NIC card. I expected to see eth0 listed, but it's not. I am on the machine now making this post, so it is active and working. BTW, eth0 is the only NIC card in the machine. Wireshark lists no interfaces. Did I miss a .conf file somewhere? -Shawn</p></div><div id="question-tags" class="tags-container tags">interface capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '11, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/30a8eb714c16011a9a75b2a96097176b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shawnerz&#39;s gravatar image" /><p>Shawnerz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shawnerz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Aug '11, 14:34</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5861" class="comments-container"></div><div id="comment-tools-5861" class="comment-tools"></div><div class="clear"></div><div id="comment-5861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5866"></span>

<div id="answer-container-5866" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5866-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds like you may not have set permissions so that you can capture as a non-root user. Check the <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">CaptureSetup/CapturePrivileges</a> page and <code>/usr/share/doc/wireshark-common/README.Debian</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '11, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-5866" class="comments-container"><span id="5896"></span><div id="comment-5896" class="comment"><div id="post-5896-score" class="comment-score"></div><div class="comment-text"><p>Multiple, OK, I wen to Users and Groups in Ubuntu, created a group called 'wireshark' and added myself to the group. Rebooted (Windows habit, sorry) but Wireshark still didn't see the interface.</p><p>Then, I went to /user/bin/wireshark and did a sudo ./wireshark, put in my password, and Wireshark saw eth0 and worked great. But on start, WS gave me warning that WS shouldn't be run as root.</p><p>Running as root worked but I get the feeling that I'm doing something wrong. Shouldn't I be able to run WS from Ubuntu's Applications | Internet menu? Thanks, -Shawn</p></div><div id="comment-5896-info" class="comment-info"><span class="comment-age">(26 Aug '11, 17:51)</span> Shawnerz</div></div><span id="5897"></span><div id="comment-5897" class="comment"><div id="post-5897-score" class="comment-score">1</div><div class="comment-text"><p>Why did you add the "wireshark" group? Did <code>/usr/share/doc/wireshark-common/README.Debian</code> says something about that, or was that from <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">CaptureSetup/CapturePrivileges</a>? If it was from CaptureSetup/CapturePrivileges, note that the "Limiting capture permission to only one group" instructions tell you to do a lot more than just add a "wireshark" group and add yourself to it - read it again and do <em>all</em> of the steps, including the "setcap" step.</p></div><div id="comment-5897-info" class="comment-info"><span class="comment-age">(26 Aug '11, 19:19)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5866" class="comment-tools"></div><div class="clear"></div><div id="comment-5866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62254"></span>

<div id="answer-container-62254" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62254-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>run this command: <code>sudo apt-get install snmp-mibs-downloader</code> .. and you should be fine</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '17, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/f0c0c02ff27f2b52906fbcc1354c20e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scofieldzg&#39;s gravatar image" /><p>scofieldzg<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scofieldzg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '17, 05:25</p></div></div><div id="comments-container-62254" class="comments-container"><span id="62256"></span><div id="comment-62256" class="comment"><div id="post-62256-score" class="comment-score"></div><div class="comment-text"><p>are you sure it belongs here?</p></div><div id="comment-62256-info" class="comment-info"><span class="comment-age">(23 Jun '17, 06:36)</span> sindy</div></div><span id="62257"></span><div id="comment-62257" class="comment"><div id="post-62257-score" class="comment-score"></div><div class="comment-text"><p>For sure, it is written in the captureprivilihes, but also wireshark should run under su</p></div><div id="comment-62257-info" class="comment-info"><span class="comment-age">(23 Jun '17, 06:40)</span> scofieldzg</div></div><span id="62258"></span><div id="comment-62258" class="comment"><div id="post-62258-score" class="comment-score"></div><div class="comment-text"><p>Somehow a combination of</p><ul><li><p>an answer which sounds like black magic (why on earth should installation of another package, not related to Wireshark, solve the issue of <code>dumpcap</code> not being run with the right privileges, which is the root cause why the interfaces are not visible)</p></li><li><p>the fact that the question is 6 years old</p></li></ul><p>made me think that you may have been answering a different question actually.</p></div><div id="comment-62258-info" class="comment-info"><span class="comment-age">(23 Jun '17, 06:46)</span> sindy</div></div><span id="62259"></span><div id="comment-62259" class="comment"><div id="post-62259-score" class="comment-score"></div><div class="comment-text"><p>Isnt that what is mentioned here? <a href="https://anonscm.debian.org/viewvc/collab-maint/ext-maint/wireshark/trunk/debian/README.Debian?view=markup">https://anonscm.debian.org/viewvc/collab-maint/ext-maint/wireshark/trunk/debian/README.Debian?view=markup</a></p></div><div id="comment-62259-info" class="comment-info"><span class="comment-age">(23 Jun '17, 06:50)</span> scofieldzg</div></div><span id="62260"></span><div id="comment-62260" class="comment"><div id="post-62260-score" class="comment-score"></div><div class="comment-text"><p>Exactly. That's why I was so confused about your reference to <code>snmp-mibs-downloader</code>.</p></div><div id="comment-62260-info" class="comment-info"><span class="comment-age">(23 Jun '17, 07:11)</span> sindy</div></div><span id="62267"></span><div id="comment-62267" class="comment not_top_scorer"><div id="post-62267-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Isnt that what is mentioned here?</p></blockquote><p>Yes, but it's not mentioned <em>in the context of getting Wireshark to list your interfaces</em>. The manual for a car might talk about both changing the oil and changing the tires, but changing the oil if you have a flat tire probably won't help.</p></div><div id="comment-62267-info" class="comment-info"><span class="comment-age">(23 Jun '17, 10:53)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-62254" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-62254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

