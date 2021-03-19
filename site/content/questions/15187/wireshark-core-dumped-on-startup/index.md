+++
type = "question"
title = "Wireshark core dumped on startup"
description = '''Hi! I have a problem that wireshark crashes on startup. After this problem I tried to uninstall it completely and to delete all files regarding wireshark (after &quot;find / | grep -i wireshark&quot;) and then reinstall it but that did not help. The first step I guess would be to locate the core dump but I ca...'''
date = "2012-10-23T05:18:00Z"
lastmod = "2012-10-27T06:41:00Z"
weight = 15187
keywords = [ "core", "startup", "dump" ]
aliases = [ "/questions/15187" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark core dumped on startup](/questions/15187/wireshark-core-dumped-on-startup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15187-score" class="post-score" title="current number of votes">0</div><span id="post-15187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I have a problem that wireshark crashes on startup. After this problem I tried to uninstall it completely and to delete all files regarding wireshark (after "find / | grep -i wireshark") and then reinstall it but that did not help. The first step I guess would be to locate the core dump but I cannot find it - where could it be located?</p><pre><code>[[email protected] ~]$ wireshark 
Segmentation fault (core dumped)
[[email protected] ~]$ uname -a
Linux LVALTP0650 3.6.2-4.fc17.x86_64 #1 SMP Wed Oct 17 02:43:21 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux
[[email protected] ~]$ wireshark -v
wireshark 1.6.10 (SVN Rev Unknown from unknown)</code></pre><p>I am using Fedora 17. Please help me because I cannot work;)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-core" rel="tag" title="see questions tagged &#39;core&#39;">core</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '12, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/bd4e5a8da561e4305bc2a06569e388db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JacKal&#39;s gravatar image" /><p><span>JacKal</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JacKal has no accepted answers">0%</span></p></div></div><div id="comments-container-15187" class="comments-container"><span id="15189"></span><div id="comment-15189" class="comment"><div id="post-15189-score" class="comment-score"></div><div class="comment-text"><p>some questions:</p><ul><li>where did you get the binary from? The Fedora repository or some rpm repository on the internet?</li><li>do you get the same error, if you run wireshark as root (not recommended, just for this test!)?</li></ul></div><div id="comment-15189-info" class="comment-info"><span class="comment-age">(23 Oct '12, 05:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15190"></span><div id="comment-15190" class="comment"><div id="post-15190-score" class="comment-score"></div><div class="comment-text"><ul><li>sudo yum install wireshark*</li><li>if I "su -" then wiresharl still core dumps</li></ul><p>Before this wireshark worked ok and or a few days I did not use it. Maybe it is important to say that I have used BleachBit to clean my pc - maybe that has left some impact.</p></div><div id="comment-15190-info" class="comment-info"><span class="comment-age">(23 Oct '12, 05:52)</span> <span class="comment-user userinfo">JacKal</span></div></div><span id="15192"></span><div id="comment-15192" class="comment"><div id="post-15192-score" class="comment-score"></div><div class="comment-text"><p>O.K. what is the output of these commands.</p><ul><li>ldd `which wireshark`</li><li>strace -f -o wireshark.trc wireshark</li></ul><p>Please post the output of the first command and the file wireshark.trc somewhere (maybe <a href="http://pastebin.com">pastebin.com</a>) and add the links to your answer.</p></div><div id="comment-15192-info" class="comment-info"><span class="comment-age">(23 Oct '12, 05:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15193"></span><div id="comment-15193" class="comment"><div id="post-15193-score" class="comment-score"></div><div class="comment-text"><ul><li><a href="http://pastebin.com/8bi1VtTJ">http://pastebin.com/8bi1VtTJ</a></li><li><a href="http://pastebin.com/pqhu6ysZ">http://pastebin.com/pqhu6ysZ</a></li></ul><p>I hope this will do.</p></div><div id="comment-15193-info" class="comment-info"><span class="comment-age">(23 Oct '12, 06:06)</span> <span class="comment-user userinfo">JacKal</span></div></div></div><div id="comment-tools-15187" class="comment-tools"></div><div class="clear"></div><div id="comment-15187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15219"></span>

<div id="answer-container-15219" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15219-score" class="post-score" title="current number of votes">2</div><span id="post-15219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JacKal has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://bugzilla.redhat.com/show_bug.cgi?id=866471">Bugzilla Bug #866471</a></p><p>Quote: Try removing abrt-addon-python. Abrt supplies a dissector, that imports a library with the same symbol defined as libsmi has.</p><p>Hopefully this works</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '12, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/66f0113757db223d03f69d01d48f54b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew3726&#39;s gravatar image" /><p><span>Andrew3726</span><br />
<span class="score" title="62 reputation points">62</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew3726 has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Oct '12, 04:05</strong> </span></p></div></div><div id="comments-container-15219" class="comments-container"><span id="15226"></span><div id="comment-15226" class="comment"><div id="post-15226-score" class="comment-score"></div><div class="comment-text"><p>Thanks - that really worked!</p><p>When I was looking where did Wireshark dumped that core I found abrt-harvest-vmcore but did not thought about it more.</p></div><div id="comment-15226-info" class="comment-info"><span class="comment-age">(24 Oct '12, 06:22)</span> <span class="comment-user userinfo">JacKal</span></div></div><span id="15313"></span><div id="comment-15313" class="comment"><div id="post-15313-score" class="comment-score"></div><div class="comment-text"><p>All work fine, now!</p></div><div id="comment-15313-info" class="comment-info"><span class="comment-age">(27 Oct '12, 06:41)</span> <span class="comment-user userinfo">redscc</span></div></div></div><div id="comment-tools-15219" class="comment-tools"></div><div class="clear"></div><div id="comment-15219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15220"></span>

<div id="answer-container-15220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15220-score" class="post-score" title="current number of votes">1</div><span id="post-15220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I had the same issue, with the latest updates from the repositories.</p><p>I went to the wireshark site and downloaded the source tar ball and built it from there.</p><p>It's quite simple, extract the contents and run ./configure &amp;&amp; make</p><p>It goes through everything on your system that is required and will stop and let you know if it needs something that isn't there...just do a yum search and then yum install on those packages.</p><p>The build does take a little while, but like I said....it works :) (This could be the last case scenario, if nothing else works).</p><p>Edit: Last thing you might need to do, is allow your user to access the dumpcap, try this: <a href="https://blog.wireshark.org/2010/02/running-wireshark-as-you/">https://blog.wireshark.org/2010/02/running-wireshark-as-you/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '12, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/2e43a36f9d3ab34231dbc677d6542ab7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spies&#39;s gravatar image" /><p><span>Spies</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spies has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Oct '12, 04:53</strong> </span></p></div></div><div id="comments-container-15220" class="comments-container"></div><div id="comment-tools-15220" class="comment-tools"></div><div class="clear"></div><div id="comment-15220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

