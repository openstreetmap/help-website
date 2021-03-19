+++
type = "question"
title = "IPX traffic question"
description = '''I have been using Tshark on an Ubuntu server for some time now. I just noticed the other day that if I do a capture using -i any, I have a pile of IPX traffic that is seen. I have looked at the source and dest addresses and they do not seem to be listed in my database of machines on my network. Howe...'''
date = "2012-05-10T08:57:00Z"
lastmod = "2012-05-10T18:05:00Z"
weight = 10900
keywords = [ "interface", "ipx", "any", "wireshark" ]
aliases = [ "/questions/10900" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IPX traffic question](/questions/10900/ipx-traffic-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10900-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been using Tshark on an Ubuntu server for some time now. I just noticed the other day that if I do a capture using -i any, I have a pile of IPX traffic that is seen. I have looked at the source and dest addresses and they do not seem to be listed in my database of machines on my network. However under the Linux Cooked Capture, there are mac address there that correspond with machines on my network. Machines rang from Novell OES servers, Windows servers and workstations, Linux, and MAC OS X for operating systems. Now what I find funny, is if I run a capture using eth0, eth1, eth2, or lo I do not see any IPX traffic at all. Any thoughts or ideas where this is coming from, and how I can trace it back to a system and disable IPX on that system? Any help is appreciated.</p></div><div id="question-tags" class="tags-container tags">interface ipx any wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '12, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/779b9b847542d579c05157a6139704a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jjalbert&#39;s gravatar image" /><p>jjalbert<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jjalbert has no accepted answers">0%</span></p></div></div><div id="comments-container-10900" class="comments-container"></div><div id="comment-tools-10900" class="comment-tools"></div><div class="clear"></div><div id="comment-10900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10909"></span>

<div id="answer-container-10909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10909-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There may be something going wrong with the Linux cooked header or Wireshark's parsing of it or something related. It's probably better to <a href="https://bugs.wireshark.org/bugzilla/">file a bug report</a> and attach a small capture file that depicts the IPX traffic so someone could take a look at it and determine if there's a problem or not, and if so, apply a fix for it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '12, 18:05</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-10909" class="comments-container"></div><div id="comment-tools-10909" class="comment-tools"></div><div class="clear"></div><div id="comment-10909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

