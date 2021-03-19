+++
type = "question"
title = "possible to use the MAC info in the Wireshark manuf file as part of display filter?"
description = '''Is it possible to use the MAC info in the Wireshark manuf file as part of display filter?  i.e. wlan.addr contains Apple This would be much more efficient than building a filter with all 249 MAC prefixes associated with Apple in the manuf file thanks tom'''
date = "2013-09-03T08:51:00Z"
lastmod = "2013-09-03T14:32:00Z"
weight = 24314
keywords = [ "manuf", "display-filter" ]
aliases = [ "/questions/24314" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [possible to use the MAC info in the Wireshark manuf file as part of display filter?](/questions/24314/possible-to-use-the-mac-info-in-the-wireshark-manuf-file-as-part-of-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24314-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to use the MAC info in the Wireshark manuf file as part of display filter?</p><p>i.e. wlan.addr contains Apple</p><p>This would be much more efficient than building a filter with all 249 MAC prefixes associated with Apple in the manuf file</p><p>thanks</p><p>tom</p></div><div id="question-tags" class="tags-container tags">manuf display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '13, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/038f7b79a1448cc73dcc75b47e7d8371?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomh&#39;s gravatar image" /><p>tomh<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomh has no accepted answers">0%</span></p></div></div><div id="comments-container-24314" class="comments-container"></div><div id="comment-tools-24314" class="comment-tools"></div><div class="clear"></div><div id="comment-24314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24317"></span>

<div id="answer-container-24317" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24317-score" class="post-score" title="current number of votes">6</div></div></td><td><div class="item-right"><div class="answer-body"><p>Prior to <a href="http://anonsvn.wireshark.org/viewvc?revision=51742&amp;view=revision">revision 51742</a>, this was not possible; however, I just committed that change so Wireshark should now support it, at least on the development trunk.</p><p>If you're running on a platform for which the <a href="http://buildbot.wireshark.org/trunk/waterfall">buildbots</a> generate installers, then you ought to be able to use an <a href="http://www.wireshark.org/download/automated/">automated build</a> with that revision (or later) once the buildbots successfully create the installers.</p><p>If you're on a platform for which no automated installer exists, then you will have to either build from the automated sources or <a href="http://www.wireshark.org/develop.html">directly from the repository</a>. Or you can wait until 1.12.0 is released next year. Since this would be considered a new feature, it's not going to be backported to 1.10 or 1.8, since no new features go into stable releases.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '13, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24317" class="comments-container"><span id="24345"></span><div id="comment-24345" class="comment"><div id="post-24345-score" class="comment-score"></div><div class="comment-text"><p>Great -- thanks!</p><p>I've downloaded and am now running 1.11.0-SVN-51747 from /trunk for OSX</p><p>What is the syntax for a display filter using the manuf values?</p><p>wlan.addr[0:] matches c0:63:94 is valid and filters correctly</p><p>wlan.addr{0:3] matches Apple is valid but filters out everything (i.e. nothing displayed)</p><p>thanks again</p><p>tom</p></div><div id="comment-24345-info" class="comment-info"><span class="comment-age">(04 Sep '13, 06:33)</span> tomh</div></div><span id="24347"></span><div id="comment-24347" class="comment"><div id="post-24347-score" class="comment-score"></div><div class="comment-text"><p>according to the <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-ieee80211.c?r1=51742&amp;r2=51741&amp;pathrev=51742">source code</a>:</p><blockquote><p>wlan.addr_resolved matches Apple</p></blockquote></div><div id="comment-24347-info" class="comment-info"><span class="comment-age">(04 Sep '13, 06:40)</span> Kurt Knochner ♦</div></div><span id="24350"></span><div id="comment-24350" class="comment"><div id="post-24350-score" class="comment-score"></div><div class="comment-text"><p>Right, there are actually 6 new filters:</p><ul><li><code>wlan.da_resolved</code></li><li><code>wlan.sa_resolved</code></li><li><code>wlan.ra_resolved</code></li><li><code>wlan.ta_resolved</code></li><li><code>wlan.bssid_resolved</code></li><li><code>wlan.addr_resolved</code></li></ul><p>Keep in mind that these filter names may change (or even disappear) in the future. There is a discussion now about improving this even further. In the end, the functionality will still be there, but the implementation may be different and thus so too will the filtering.</p></div><div id="comment-24350-info" class="comment-info"><span class="comment-age">(04 Sep '13, 07:16)</span> cmaynard ♦♦</div></div><span id="24608"></span><div id="comment-24608" class="comment"><div id="post-24608-score" class="comment-score">1</div><div class="comment-text"><p>As per the answer by @cmaynard, this is only in the latest trunk and hasn't been backported to 1.8 or 1.10. Your output indicates a 1.8.2 build.</p><p>Make sure you are building off the master branch.</p></div><div id="comment-24608-info" class="comment-info"><span class="comment-age">(12 Sep '13, 07:55)</span> grahamb ♦</div></div><span id="25192"></span><div id="comment-25192" class="comment"><div id="post-25192-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>I'm using tshark 1.10.2 over my RPi. I'm also very interested in the usage of the Wireshark manuf file as part of display filter... that's why i got the last tshark version.</p><p>Unfortunately after executing the command: tshark -i wlan1 -R "wlan.addr_resolved matches Apple"</p><p>I receive an error due to neither wlan.addr_resolved nor Apple are field or protocol names.</p><p>Could you provide any advice based on your experience?</p><p>Thanks in advance, LeGramo</p></div><div id="comment-25192-info" class="comment-info"><span class="comment-age">(25 Sep '13, 02:12)</span> legramo</div></div></div><div id="comment-tools-24317" class="comment-tools"></div><div class="clear"></div><div id="comment-24317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

