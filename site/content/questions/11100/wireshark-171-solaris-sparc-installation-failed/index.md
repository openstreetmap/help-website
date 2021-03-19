+++
type = "question"
title = "Wireshark 1.7.1 Solaris Sparc installation failed"
description = '''In file included from packet-coap.c:32: ../../config.h:391:1: &quot;_FILE_OFFSET_BITS&quot; redefined In file included from /usr/include/stdio.h:21,  from packet-coap.c:1: /usr/include/sys/feature_tests.h:187:1: this is the location of the previous definition make[5]: *** [libdissectors_la-packet-coap.lo] Err...'''
date = "2012-05-17T05:39:00Z"
lastmod = "2012-05-17T08:16:00Z"
weight = 11100
keywords = [ "sparc", "solaris", "build", "1.7.1" ]
aliases = [ "/questions/11100" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.7.1 Solaris Sparc installation failed](/questions/11100/wireshark-171-solaris-sparc-installation-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11100-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>In file included from packet-coap.c:32:
../../config.h:391:1: &quot;_FILE_OFFSET_BITS&quot; redefined
In file included from /usr/include/stdio.h:21,
                 from packet-coap.c:1:
/usr/include/sys/feature_tests.h:187:1: this is the location of the previous definition
make[5]: *** [libdissectors_la-packet-coap.lo] Error 1
make[5]: Leaving directory `/Software/wireshark-1.7.1/epan/dissectors&#39;
make[4]: *** [all-recursive] Error 1
make[4]: Leaving directory `/Software/wireshark-1.7.1/epan/dissectors&#39;
make[3]: *** [all] Error 2
make[3]: Leaving directory `/Software/wireshark-1.7.1/epan/dissectors&#39;
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/Software/wireshark-1.7.1/epan&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/Software/wireshark-1.7.1&#39;
make: *** [all] Error 2</code></pre></div><div id="question-tags" class="tags-container tags">sparc solaris build 1.7.1</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '12, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/ff63d6abbb91e67370ca72fa125b2cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="isarana&#39;s gravatar image" /><p>isarana<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="isarana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '12, 06:09</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-11100" class="comments-container"></div><div id="comment-tools-11100" class="comment-tools"></div><div class="clear"></div><div id="comment-11100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11104"></span>

<div id="answer-container-11104" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11104-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This was fixed in r41993. To avoid the problem without upgrading (to SVN) you could delete the "#include&lt;stdio.h&gt;" from packet-coap.c .</p><p>Please do report (preferrably--as this is a Q&amp;A site--via a <a href="https://bugs.wireshark.org">bug report</a>) if you find the problem in any other places.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-11104" class="comments-container"></div><div id="comment-tools-11104" class="comment-tools"></div><div class="clear"></div><div id="comment-11104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

