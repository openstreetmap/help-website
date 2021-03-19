+++
type = "question"
title = "Wireshark with openflow"
description = '''Hello, I am facing problems in using wireshark with openflow. I am currently running on 14.04.1-Ubuntu with wireshark 1.10.6. I need to check openflow protocol for the installed version of wireshark. I tried may ways to install plugins but no luck. Below are the steps I followed:  sudo apt-get insta...'''
date = "2016-05-13T03:22:00Z"
lastmod = "2016-05-13T04:07:00Z"
weight = 52497
keywords = [ "wireshark" ]
aliases = [ "/questions/52497" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark with openflow](/questions/52497/wireshark-with-openflow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52497-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am facing problems in using wireshark with openflow. I am currently running on 14.04.1-Ubuntu with wireshark 1.10.6.</p><p>I need to check openflow protocol for the installed version of wireshark. I tried may ways to install plugins but no luck. Below are the steps I followed:</p><ol><li>sudo apt-get install libgtk2.0-dev</li><li>export WIRESHARK=/usr/include/wireshark</li><li>cd of-dissector/src</li><li>sudo scons install <code>scons: Reading SConscript files ...     ### ERROR: You need to set the WIRESHARK environment variable to the location of your wireshark include directory.     ### ERROR: (such that epan/packet.h is a valid include path)</code></li></ol><p>Though env variable set correctly, it is throwing me above error.</p><pre><code>[email protected]:~/of-dissector/src$ echo $WIRESHARK
/usr/include/wireshark/</code></pre><p>Can anyone please throw some light on this issue step by step?</p><p>Thanks, Basavaraj</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '16, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/03dce3409a3ade018b9c4db5e0aba443?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Basavaraj&#39;s gravatar image" /><p>Basavaraj<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Basavaraj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 May '16, 03:27</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-52497" class="comments-container"><span id="52498"></span><div id="comment-52498" class="comment"><div id="post-52498-score" class="comment-score"></div><div class="comment-text"><p>Where did you get this openflow dissector from?</p></div><div id="comment-52498-info" class="comment-info"><span class="comment-age">(13 May '16, 03:24)</span> grahamb ♦</div></div><span id="52500"></span><div id="comment-52500" class="comment"><div id="post-52500-score" class="comment-score"></div><div class="comment-text"><p>I got it from <a href="https://bitbucket.org/barnstorm/of-dissector.">https://bitbucket.org/barnstorm/of-dissector.</a></p></div><div id="comment-52500-info" class="comment-info"><span class="comment-age">(13 May '16, 03:49)</span> Basavaraj</div></div><span id="52502"></span><div id="comment-52502" class="comment"><div id="post-52502-score" class="comment-score"></div><div class="comment-text"><p>It might be easier to install a newer version of Wireshark with openflow support built in from <a href="https://launchpad.net/~wireshark-dev/+archive/ubuntu/stable">https://launchpad.net/~wireshark-dev/+archive/ubuntu/stable</a></p></div><div id="comment-52502-info" class="comment-info"><span class="comment-age">(13 May '16, 04:01)</span> Anders ♦</div></div><span id="52504"></span><div id="comment-52504" class="comment"><div id="post-52504-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response. @Anders: I installed latest wireshark using the link you shared. But when I launch wireshark, I get error: [email protected]:~$ sudo wireshark QXcbConnection: Failed to get the primary output of the screen XIO: fatal IO error 2 (No such file or directory) on X server "localhost:13.0" after 176 requests (176 known processed) with 0 events remaining.</p><p>Any pointer from your side?</p></div><div id="comment-52504-info" class="comment-info"><span class="comment-age">(13 May '16, 04:40)</span> Basavaraj</div></div><span id="52505"></span><div id="comment-52505" class="comment"><div id="post-52505-score" class="comment-score"></div><div class="comment-text"><p>If you are running over x use the legacy version wireshark-gtk</p></div><div id="comment-52505-info" class="comment-info"><span class="comment-age">(13 May '16, 04:46)</span> Anders ♦</div></div></div><div id="comment-tools-52497" class="comment-tools"></div><div class="clear"></div><div id="comment-52497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52503"></span>

<div id="answer-container-52503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52503-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Plus that dissector appears to be for old versions of openflow and uses a very non-standard (for Wireshark) build system (scons).</p><p>If you want support for that dissector, you'll have to go to the author.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '16, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52503" class="comments-container"></div><div id="comment-tools-52503" class="comment-tools"></div><div class="clear"></div><div id="comment-52503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

