+++
type = "question"
title = "capture at multiple interface in Wireshark 1.7 development release"
description = '''Could some pls tell me if it is possible to start wireshark 1.7 ( dev version ) from command line with multiple interfaces specified ? I could start a capture from a single interface from command line but not multiple interfaces.  I tried these but nothing worked sudo wireshark -i eth1 -i /tmp/pipe ...'''
date = "2012-01-10T22:47:00Z"
lastmod = "2012-01-11T11:21:00Z"
weight = 8314
keywords = [ "development", "wireshark1.7" ]
aliases = [ "/questions/8314" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture at multiple interface in Wireshark 1.7 development release](/questions/8314/capture-at-multiple-interface-in-wireshark-17-development-release)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8314-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could some pls tell me if it is possible to start wireshark 1.7 ( dev version ) from command line with multiple interfaces specified ? I could start a capture from a single interface from command line but not multiple interfaces.</p><p>I tried these but nothing worked</p><pre><code>sudo wireshark -i eth1 -i /tmp/pipe

sudo wireshark -k -i eth1 -i /tmp/pipe</code></pre><p>For the above wireshark started but displayed some error information for dumpcap that "--t option is invalid." But i did not specific "-t" in the command line.</p><p>Some pls tell me what the issue is ??</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags">development wireshark1.7</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '12, 22:47</strong></p><img src="https://secure.gravatar.com/avatar/83e04f89cabcf71f8efd2238a88905ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="v%20j&#39;s gravatar image" /><p>v j<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="v j has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '12, 00:09</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-8314" class="comments-container"><span id="8315"></span><div id="comment-8315" class="comment"><div id="post-8315-score" class="comment-score"></div><div class="comment-text"><p>To quote Michael Tuexen's answer when the same question was asked on the wireshark-dev mailing list:</p><blockquote><p>What does dumpcap -t do?</p><p>The -t option is supported on the current developer version (svn head) on my system.</p></blockquote><p>I will ask some additional questions:</p><ul><li><p>Did you build this from source, or is it the 1.7.0 release from the Wireshark download page, or is it one of the automated builds?</p></li><li><p>If you built it from source, did you modify it?</p></li><li><p>If you built it from source, are you running it from the build directory or from a <code>make install</code>?</p></li></ul></div><div id="comment-8315-info" class="comment-info"><span class="comment-age">(11 Jan '12, 00:08)</span> Guy Harris ♦♦</div></div><span id="8323"></span><div id="comment-8323" class="comment"><div id="post-8323-score" class="comment-score"></div><div class="comment-text"><p>dumpcap -t throws invalid option error.</p><p>I built wireshark from source</p><p>No I did not modify the code</p><p>i am running it from build directory</p></div><div id="comment-8323-info" class="comment-info"><span class="comment-age">(11 Jan '12, 04:40)</span> v j</div></div></div><div id="comment-tools-8314" class="comment-tools"></div><div class="clear"></div><div id="comment-8314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8330"></span>

<div id="answer-container-8330" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8330-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, there was a required change made to <a href="http://anonsvn.wireshark.org/viewvc/trunk/dumpcap.c?r1=39751&amp;r2=39775">dumpcap.c</a> after 1.7.0 was released, so you will need to download and build one of the more recent <a href="http://www.wireshark.org/download/automated/src/">automated sources</a> in order for this to work, or you could manually apply the change to the 1.7.0 dumpcap.c file yourself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '12, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '12, 11:22</p></div></div><div id="comments-container-8330" class="comments-container"></div><div id="comment-tools-8330" class="comment-tools"></div><div class="clear"></div><div id="comment-8330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

