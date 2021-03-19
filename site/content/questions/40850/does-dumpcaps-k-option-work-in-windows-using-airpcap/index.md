+++
type = "question"
title = "Does dumpcap&#x27;s -k option work in Windows (using AirPcap)?"
description = '''I&#x27;m trying to use dumpcap to capture 802.11 traces on a Windows machine (using an AirPcap Nx). I need to set the wifi channel, but I haven&#x27;t been able to get the -k option to work. Should this work? If so, what is the syntax? If not, is there another alternative?'''
date = "2015-03-25T10:06:00Z"
lastmod = "2015-03-25T18:08:00Z"
weight = 40850
keywords = [ "wifi", "dumpcap", "channel" ]
aliases = [ "/questions/40850" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Does dumpcap's -k option work in Windows (using AirPcap)?](/questions/40850/does-dumpcaps-k-option-work-in-windows-using-airpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40850-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to use dumpcap to capture 802.11 traces on a Windows machine (using an AirPcap Nx). I need to set the wifi channel, but I haven't been able to get the -k option to work. Should this work? If so, what is the syntax? If not, is there another alternative?</p></div><div id="question-tags" class="tags-container tags">wifi dumpcap channel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '15, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/302906ecd01da0af954ac548f5b355b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="V%20Capps&#39;s gravatar image" /><p>V Capps<br />
<span class="score" title="5 reputation points">5</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="V Capps has no accepted answers">0%</span></p></div></div><div id="comments-container-40850" class="comments-container"><span id="40862"></span><div id="comment-40862" class="comment"><div id="post-40862-score" class="comment-score"></div><div class="comment-text"><p>I also tried this on a Mac and couldn't get the -k option to work on that, either.</p></div><div id="comment-40862-info" class="comment-info"><span class="comment-age">(25 Mar '15, 15:41)</span> V Capps</div></div><span id="40863"></span><div id="comment-40863" class="comment"><div id="post-40863-score" class="comment-score"></div><div class="comment-text"><p>Some questions</p><ul><li>what is your Wireshark version</li><li>how did you start dumpcap (all CLI options)</li><li>what is the dumpcap behavior</li></ul></div><div id="comment-40863-info" class="comment-info"><span class="comment-age">(25 Mar '15, 16:48)</span> Kurt Knochner ♦</div></div><span id="40865"></span><div id="comment-40865" class="comment"><div id="post-40865-score" class="comment-score"></div><div class="comment-text"><p>I've tried Wireshark 1.12.3 and 1.12.4.</p><p>I was running dumpcap from the cmd prompt so I could use the ringbuffer option, but I've simplified the options while trying to get -k working. The AirPcap is interface 1.</p><p>When I enter the following, nothing happens, and I immediately get a cmd prompt back: dumpcap -i 1 -k 2427,HT20 -w test.pcap</p><p>If I leave out the "-k 2427,HT20" part, it says, "Capturing on 'AirPcap USB wireless capture adapter nr. 00'", etc. and proceeds to capture packets as expected.</p><p>I've tried several different things for the -k syntax, but they all just return without doing anything. Or, if I use something like "-k 2427" (with no comma), I get the error, "dumpcap: 1: Failed to init ws80211: Operation not permitted".</p></div><div id="comment-40865-info" class="comment-info"><span class="comment-age">(25 Mar '15, 17:38)</span> V Capps</div></div></div><div id="comment-tools-40850" class="comment-tools"></div><div class="clear"></div><div id="comment-40850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40870"></span>

<div id="answer-container-40870" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40870-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to the dumpcap code the wifi channel setting is done through <a href="http://www.infradead.org/~tgr/libnl/">libnl</a> which is only available for Linux, so it won't work on Windows and I don't think that libnl supports AriPcap on Linux (if you tried that as well). So, the dumpcap option -k does nothing on a Windows system.</p><p>You can (probably) set the AriPcap channel on the CLI with a python script (apc-channel.py), and then run dumpcap afterwards.</p><blockquote><p><a href="http://blog.didierstevens.com/2008/06/10/quickpost-wifi-channel-hopping-with-an-airpcap-adapter/">http://blog.didierstevens.com/2008/06/10/quickpost-wifi-channel-hopping-with-an-airpcap-adapter/</a></p></blockquote><p>You'll probably have to modify the script, as it's doing channel hopping by default.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '15, 18:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40870" class="comments-container"><span id="40872"></span><div id="comment-40872" class="comment"><div id="post-40872-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info. I'll take a look at the python script and see if I can modify it to work for what I'm trying to do.</p></div><div id="comment-40872-info" class="comment-info"><span class="comment-age">(25 Mar '15, 20:27)</span> V Capps</div></div><span id="40873"></span><div id="comment-40873" class="comment"><div id="post-40873-score" class="comment-score"></div><div class="comment-text"><p>A few quick modifications to apc-channel.py, and I now have a python script that sets the AirPcap to the specified channel. Thanks for your help!</p></div><div id="comment-40873-info" class="comment-info"><span class="comment-age">(25 Mar '15, 21:20)</span> V Capps</div></div><span id="40876"></span><div id="comment-40876" class="comment"><div id="post-40876-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-40876-info" class="comment-info"><span class="comment-age">(26 Mar '15, 01:36)</span> Kurt Knochner ♦</div></div><span id="40892"></span><div id="comment-40892" class="comment"><div id="post-40892-score" class="comment-score"></div><div class="comment-text"><p>Please file a bug report against <code>dumpcap -k</code>. If an option doesn't work, then it should either be made to work as expected, or it should be removed from being listed and accepted on platforms where it doesn't work.</p></div><div id="comment-40892-info" class="comment-info"><span class="comment-age">(26 Mar '15, 07:07)</span> cmaynard ♦♦</div></div><span id="40919"></span><div id="comment-40919" class="comment"><div id="post-40919-score" class="comment-score"></div><div class="comment-text"><p>Yes, currently -k is Linux-only. Sadly, there do not yet exist libpcap APIs to allow the 802.11 channel to be set in a platform-independent fashion, so Wireshark needs to have its own platform-dependent code to do that, and that code has only been written for Linux so far.</p></div><div id="comment-40919-info" class="comment-info"><span class="comment-age">(26 Mar '15, 14:27)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-40870" class="comment-tools"></div><div class="clear"></div><div id="comment-40870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

