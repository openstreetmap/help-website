+++
type = "question"
title = "How to decode MAC-LTE message?"
description = '''I want to decode MAC-LTE message but when I try to decode using tshark it gives the following error. Can&#x27;t dissect LTE MAC frame because no per-frame info was attached!'''
date = "2012-04-04T03:01:00Z"
lastmod = "2012-04-09T04:52:00Z"
weight = 9925
keywords = [ "mac", "tshark", "lte" ]
aliases = [ "/questions/9925" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to decode MAC-LTE message?](/questions/9925/how-to-decode-mac-lte-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9925-score" class="post-score" title="current number of votes">0</div><span id="post-9925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to decode MAC-LTE message but when I try to decode using tshark it gives the following error. Can't dissect LTE MAC frame because no per-frame info was attached!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '12, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/a77eae14872aa3bc6464315b57933f66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ender&#39;s gravatar image" /><p><span>ender</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ender has no accepted answers">0%</span></p></div></div><div id="comments-container-9925" class="comments-container"><span id="9943"></span><div id="comment-9943" class="comment"><div id="post-9943-score" class="comment-score"></div><div class="comment-text"><p>How are the LTE frames stored in the file? Is this a Catapult DCT2000 file (text file), or is it a capture with LTE MAC-over-UDP, or is it something else?</p></div><div id="comment-9943-info" class="comment-info"><span class="comment-age">(04 Apr '12, 14:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="9956"></span><div id="comment-9956" class="comment"><div id="post-9956-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately it is not neither Catapult file nor MAC-over-UDP. It is a just a MAC message without any frames.</p></div><div id="comment-9956-info" class="comment-info"><span class="comment-age">(05 Apr '12, 03:09)</span> <span class="comment-user userinfo">ender</span></div></div></div><div id="comment-tools-9925" class="comment-tools"></div><div class="clear"></div><div id="comment-9925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9959"></span>

<div id="answer-container-9959" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9959-score" class="post-score" title="current number of votes">1</div><span id="post-9959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ender has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The MAC-LTE dissector needs certain context information to be attached to the frame before it can knows how to properly dissect it.</p><p>There is the mac-lte-framed dissector. It currently doesn't have its own DLT, so I've used it with one of the user DLTs (e.g. 147). It still needs to have the context information, which is stored in the same format as the supported MAC-over-UDP format (minus the identifying string that the UDP format uses). You would then need to associate your DLT with the protocol 'mac-lte-framed'. I could post sample code for for writing to this file format to the wiki, if that would help.</p><p>You could use mac-lte-framed, or invent your own format, but you'll still need to attach the context info to each frame ( get_mac_lte_proto_data() and set_mac_lte_proto_data() are available for this and could be called from a plugin if necessary ).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '12, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/4b31b42b2960269c605715bae6547459?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinM&#39;s gravatar image" /><p><span>MartinM</span><br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinM has 3 accepted answers">33%</span></p></div></div><div id="comments-container-9959" class="comments-container"><span id="9960"></span><div id="comment-9960" class="comment"><div id="post-9960-score" class="comment-score"></div><div class="comment-text"><p>(I wanted to edit my comment to note that you would edit the preferences of the USER_DLT dissector to associated mac-lte-framed with a DLT, but couldn't work out how to save my edit...)</p></div><div id="comment-9960-info" class="comment-info"><span class="comment-age">(05 Apr '12, 05:43)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="9961"></span><div id="comment-9961" class="comment"><div id="post-9961-score" class="comment-score"></div><div class="comment-text"><p>If you have edit privs, then it's the little diagonal pen icon next to your name in the comment.</p></div><div id="comment-9961-info" class="comment-info"><span class="comment-age">(05 Apr '12, 07:02)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="9964"></span><div id="comment-9964" class="comment"><div id="post-9964-score" class="comment-score"></div><div class="comment-text"><p><span>@MartinM</span> I would appreciate if you could post sample code.</p></div><div id="comment-9964-info" class="comment-info"><span class="comment-age">(05 Apr '12, 09:35)</span> <span class="comment-user userinfo">ender</span></div></div><span id="9987"></span><div id="comment-9987" class="comment"><div id="post-9987-score" class="comment-score">1</div><div class="comment-text"><p>OK, I uploaded sample code, which should be available here: <a href="http://www.wireshark.org/~martinm/mac_pcap_sample_code.c">http://www.wireshark.org/~martinm/mac_pcap_sample_code.c</a> I will update <a href="http://wiki.wireshark.org/MAC-LTE">http://wiki.wireshark.org/MAC-LTE</a> later today with a link to it.</p></div><div id="comment-9987-info" class="comment-info"><span class="comment-age">(06 Apr '12, 09:02)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="10027"></span><div id="comment-10027" class="comment"><div id="post-10027-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@MartinM</span> I compiled sample code and run it. it created "test1.pcap" file. But when I open it in wireshark, it says "Can't dissect LTE MAC frame because no per-frame info was attached!". Did I miss some steps? (I tested on wireshark 1.7.1-SVN-41918)</p></div><div id="comment-10027-info" class="comment-info"><span class="comment-age">(09 Apr '12, 03:29)</span> <span class="comment-user userinfo">ender</span></div></div><span id="10028"></span><div id="comment-10028" class="comment not_top_scorer"><div id="post-10028-score" class="comment-score"></div><div class="comment-text"><p>Did you configure USER_DLT to use 'mac-lte-framed' rather than 'mac-lte' as the payload protocol? Also you need a pretty recent version of Wireshark, e.g. recent sources, a development snapshot or 1.7.1.</p><p>If both of these are OK, you could send me your test1.pcap to make sure it is the same as the output I get.</p></div><div id="comment-10028-info" class="comment-info"><span class="comment-age">(09 Apr '12, 03:43)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="10029"></span><div id="comment-10029" class="comment not_top_scorer"><div id="post-10029-score" class="comment-score"></div><div class="comment-text"><p>Changing USER_DLT to 'mac-lte-framed' solved my problem. <span>@MartinM</span>, thanks for your help.</p></div><div id="comment-10029-info" class="comment-info"><span class="comment-age">(09 Apr '12, 04:52)</span> <span class="comment-user userinfo">ender</span></div></div></div><div id="comment-tools-9959" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-9959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

