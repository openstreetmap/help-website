+++
type = "question"
title = "undefined reference to `tvb_bcd_dig_to_ep_str&#x27;"
description = '''I&#x27;m compiling the source code with some modification. Before running, my source was built several times successfully, but today when I run it again , there are some errors that I don&#x27;t know what the reason is. I commented out new modification I made today but still failed. I modified a lot in the co...'''
date = "2013-09-25T03:56:00Z"
lastmod = "2013-09-25T09:39:00Z"
weight = 25201
keywords = [ "compiling", "undefined" ]
aliases = [ "/questions/25201" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [undefined reference to \`tvb\_bcd\_dig\_to\_ep\_str'](/questions/25201/undefined-reference-to-tvb_bcd_dig_to_ep_str)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25201-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm compiling the source code with some modification. Before running, my source was built several times successfully, but today when I run it again , there are some errors that I don't know what the reason is. I commented out new modification I made today but still failed. I modified a lot in the code so, it is quite difficult to comment out all of them, one by one to know where the error is. So, I post the messages got from screen to this web, if you have any idea about the reason, or any clue, please suggest me to find out the problem. Thank you very much. Here is the error:</p><pre><code>epan/.libs/libwireshark.so: undefined reference to `tvb_bcd_dig_to_ep_str&#39;
epan/.libs/libwireshark.so: undefined reference to `tvb_get_ephemeral_string&#39;
epan/.libs/libwireshark.so: undefined reference to `tvb_get_ephemeral_unicode_string&#39;
collect2: error: ld returned 1 exit status make[2]:
*** [wireshark] Error 1
 make[2]: Leaving directory `/media/sonnh/Win7_x64/wireshark_print&#39;
 make[1]: *** [all-recursive] Error 1
 make[1]: Leaving directory `/media/sonnh/Win7_x64/wireshark_print&#39;
 make: *** [all] Error 2</code></pre></div><div id="question-tags" class="tags-container tags">compiling undefined</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '13, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p>hoangsonk49<br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div></div><div id="comments-container-25201" class="comments-container"></div><div id="comment-tools-25201" class="comment-tools"></div><div class="clear"></div><div id="comment-25201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25202"></span>

<div id="answer-container-25202" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25202-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably you're working from trunk, and have also updated your working copy? There is currently an effort underway to switch over the memory allocator to the newer wmem allocator, and "ephemeral" is the older type so you may have fallen foul of the changeover. Have a look at the recent developer mailing <a href="http://www.wireshark.org/lists/wireshark-dev/201309/threads.html">list archives</a> for references to wmem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '13, 04:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-25202" class="comments-container"><span id="25204"></span><div id="comment-25204" class="comment"><div id="post-25204-score" class="comment-score"></div><div class="comment-text"><p>Yes, i'm using trunk, so is it possible to handle this problem by using an older source code to ignore the changeover?</p></div><div id="comment-25204-info" class="comment-info"><span class="comment-age">(25 Sep '13, 04:14)</span> hoangsonk49</div></div><span id="25205"></span><div id="comment-25205" class="comment"><div id="post-25205-score" class="comment-score"></div><div class="comment-text"><p>Yes, switch your working copy to the trunk-1.10 branch. That will only get bugfixes, not current development.</p></div><div id="comment-25205-info" class="comment-info"><span class="comment-age">(25 Sep '13, 04:30)</span> grahamb ♦</div></div><span id="25208"></span><div id="comment-25208" class="comment"><div id="post-25208-score" class="comment-score"></div><div class="comment-text"><p>I found a link on the website :<a href="http://wiresharkdownloads.riverbed.com/wireshark/src/wireshark-1.10.2.tar.bz2">link text</a> . is it useful in this case?</p></div><div id="comment-25208-info" class="comment-info"><span class="comment-age">(25 Sep '13, 04:36)</span> hoangsonk49</div></div><span id="25210"></span><div id="comment-25210" class="comment"><div id="post-25210-score" class="comment-score">1</div><div class="comment-text"><p>There are two basic ways of working with the Wireshark source code as discussed in the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcObtain.html">Developers Guide Sect 3.3</a>:</p><ol><li>Use a version control system such as subversion (or git) to retrieve a local copy of the sources, and to then keep that copy up to date with the main Wireshark repository. If you use this method, you should use the trunk-1.10 branch unless you like to live on the bleeding edge where all the development work goes on, in which case use trunk.</li><li>Download a snapshot of the source files, e.g. a tarball, and work with that. Note that using this method it becomes much harder to track any changes that may be made to the main Wireshark source files.</li></ol></div><div id="comment-25210-info" class="comment-info"><span class="comment-age">(25 Sep '13, 05:05)</span> grahamb ♦</div></div></div><div id="comment-tools-25202" class="comment-tools"></div><div class="clear"></div><div id="comment-25202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25225"></span>

<div id="answer-container-25225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25225-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can really easily change your code to adapt to the new API:</p><ul><li>replace the inclusion of epan/emem.h by the inclusion of epan/wmem/wmem.h</li><li>rename tvb_bcd_dig_to_ep_str(XXX) to tvb_bcd_dig_to_wmem_packet_str(XXX)</li><li>rename tvb_get_ephemeral_string(XXX) to tvb_get_string(wmem_packet_scope(), XXX)</li><li>rename tvb_get_ephemeral_unicode_string(XXX) to tvb_get_unicode_string(wmem_packet_scope(), XXX)</li></ul><p>And you are done!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '13, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-25225" class="comments-container"><span id="25255"></span><div id="comment-25255" class="comment"><div id="post-25255-score" class="comment-score"></div><div class="comment-text"><p>problem solved. I checked out the branch 1.10 and no more similar errors. Thanks!</p></div><div id="comment-25255-info" class="comment-info"><span class="comment-age">(25 Sep '13, 18:49)</span> hoangsonk49</div></div></div><div id="comment-tools-25225" class="comment-tools"></div><div class="clear"></div><div id="comment-25225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

