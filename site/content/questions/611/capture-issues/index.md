+++
type = "question"
title = "capture issues"
description = '''I had been running wireshark successfully for some time. In late august, a microsoft update to my XP operating system locked my computer up and I had no alternative but to start from scratch and reload my operating system and all the programs that I was using. Since then, I cannot get Wireshark to w...'''
date = "2010-10-24T20:45:00Z"
lastmod = "2010-10-26T20:53:00Z"
weight = 611
keywords = [ "baffled" ]
aliases = [ "/questions/611" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture issues](/questions/611/capture-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-611-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I had been running wireshark successfully for some time. In late august, a microsoft update to my XP operating system locked my computer up and I had no alternative but to start from scratch and reload my operating system and all the programs that I was using. Since then, I cannot get Wireshark to work. My wireless works properly but when I try a wireshark packet capture I get the following message:</p><pre><code>&quot; Capture session could not be initiated( failed to set hardware filter to promiscuous mode)
  Please check that &quot;\ Device\NPF_{ 5F7A801C-C89A-41FB-91CD-E9AE11B86C59}&quot; is the
 proper interface. &quot;</code></pre><p>The hardware has been set to promiscuous mode so the first line is wrong. I know something is set wrong but I can't figure out what.</p><pre><code>                                          Baffled</code></pre></div><div id="question-tags" class="tags-container tags">baffled</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '10, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/18a41fcf382d249d328dbb0862cca43f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baffled&#39;s gravatar image" /><p>Baffled<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baffled has no accepted answers">0%</span></p></div></div><div id="comments-container-611" class="comments-container"><span id="616"></span><div id="comment-616" class="comment"><div id="post-616-score" class="comment-score"></div><div class="comment-text"><p>Did you also try to (re)install WinPcap?<br />
You can download the latest stable WinPcap version 4.1.2 <a href="http://www.winpcap.org/install/default.htm">here</a>.</p><p>Try to run:<br />
$ wireshark -i 3 -o "capture.prom_mode: TRUE" -k</p></div><div id="comment-616-info" class="comment-info"><span class="comment-age">(25 Oct '10, 06:00)</span> joke</div></div><span id="648"></span><div id="comment-648" class="comment"><div id="post-648-score" class="comment-score"></div><div class="comment-text"><p>I have reinstalled WinPcap 4.1.2 and an older version of WinPcap. Both had no effect. Also no luck with the running the suggested command. Thanks for the attempt Joke. Baffled</p></div><div id="comment-648-info" class="comment-info"><span class="comment-age">(25 Oct '10, 20:46)</span> Baffled</div></div><span id="649"></span><div id="comment-649" class="comment"><div id="post-649-score" class="comment-score"></div><div class="comment-text"><p>Can you go into Capture Options and turn off promiscuous mode and then try the capture? If that's the problem then you should get an error message.</p><p>When you select Capture &gt; Interfaces do you see your adapter and does it seem to indicate it sees traffic?</p></div><div id="comment-649-info" class="comment-info"><span class="comment-age">(25 Oct '10, 21:05)</span> lchappell ♦</div></div><span id="694"></span><div id="comment-694" class="comment"><div id="post-694-score" class="comment-score"></div><div class="comment-text"><p>Laura I tried turning off promiscuous mode as you suggested and Wireshark begins capturing packets normally without any error message. As for my adapter, it is listed as an interface and it does appear to be seeing traffic.</p><pre><code>                           Baffled</code></pre></div><div id="comment-694-info" class="comment-info"><span class="comment-age">(26 Oct '10, 19:53)</span> Baffled</div></div><span id="762"></span><div id="comment-762" class="comment"><div id="post-762-score" class="comment-score"></div><div class="comment-text"><p>Guy As it turns out, this is a computer specific issue. When my system crashed and I reloaded everything, I must have updated my wireless driver. While the new driver would work for everything else, it would not run Wireshark in promiscuous mode. By rolling back my driver to a previous version, the problems went away. I hadn't thought to try this earlier. Thanks to everyone for the suggestions anyway. Baffled</p></div><div id="comment-762-info" class="comment-info"><span class="comment-age">(31 Oct '10, 16:46)</span> Baffled</div></div></div><div id="comment-tools-611" class="comment-tools"></div><div class="clear"></div><div id="comment-611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="696"></span>

<div id="answer-container-696" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-696-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is almost certainly a WinPcap problem; it probably got an error from the WinPcap driver. Try capturing with <a href="http://www.winpcap.org/windump/default.htm">WinDump</a> - without the "-p" flag, so that it tries to turn promiscuous mode on - and see whether it reports the same error. If so, this is definitely a WinPcap error, and you'll need to <a href="http://www.winpcap.org/bugs.htm">report it to the WinPcap developers</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 20:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-696" class="comments-container"></div><div id="comment-tools-696" class="comment-tools"></div><div class="clear"></div><div id="comment-696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

