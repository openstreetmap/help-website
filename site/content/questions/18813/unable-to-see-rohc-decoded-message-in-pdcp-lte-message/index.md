+++
type = "question"
title = "Unable to see ROHC decoded message in pdcp-lte message"
description = '''I am not able to see any ROHC fields on applying filter pdcp-lte. I tried the filter pdcp-lte.rohc but no messages showed up on applying this filter. Is there any separate dissector for ROHC decoding, apart from the standard pdcp-lte package? I am using wireshark verion 1.4.0 on linux.'''
date = "2013-02-22T06:33:00Z"
lastmod = "2013-02-27T22:18:00Z"
weight = 18813
keywords = [ "pdcp-lte", "rohc" ]
aliases = [ "/questions/18813" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to see ROHC decoded message in pdcp-lte message](/questions/18813/unable-to-see-rohc-decoded-message-in-pdcp-lte-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18813-score" class="post-score" title="current number of votes">0</div><span id="post-18813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am not able to see any ROHC fields on applying filter pdcp-lte. I tried the filter pdcp-lte.rohc but no messages showed up on applying this filter. Is there any separate dissector for ROHC decoding, apart from the standard pdcp-lte package? I am using wireshark verion 1.4.0 on linux.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pdcp-lte" rel="tag" title="see questions tagged &#39;pdcp-lte&#39;">pdcp-lte</span> <span class="post-tag tag-link-rohc" rel="tag" title="see questions tagged &#39;rohc&#39;">rohc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '13, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/720847714158bc9b404e15ad9c0159a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dr1&#39;s gravatar image" /><p><span>dr1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dr1 has no accepted answers">0%</span></p></div></div><div id="comments-container-18813" class="comments-container"><span id="18816"></span><div id="comment-18816" class="comment"><div id="post-18816-score" class="comment-score"></div><div class="comment-text"><p>You should probably try a development release or at least 1.8</p></div><div id="comment-18816-info" class="comment-info"><span class="comment-age">(22 Feb '13, 08:37)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-18813" class="comment-tools"></div><div class="clear"></div><div id="comment-18813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18830"></span>

<div id="answer-container-18830" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18830-score" class="post-score" title="current number of votes">0</div><span id="post-18830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>PDCP LTE dissector did include some ROHC dissection in Wireshark 1.4.0 (while starting from Wireshark 1.8.0, ROHC is a separate dissector), but you must activate ROHC options in PDCP-LTE preferences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '13, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-18830" class="comments-container"><span id="18922"></span><div id="comment-18922" class="comment"><div id="post-18922-score" class="comment-score"></div><div class="comment-text"><p>any idea how to activate the ROHC options in 1.4.0??</p></div><div id="comment-18922-info" class="comment-info"><span class="comment-age">(27 Feb '13, 02:31)</span> <span class="comment-user userinfo">dr1</span></div></div><span id="18930"></span><div id="comment-18930" class="comment"><div id="post-18930-score" class="comment-score"></div><div class="comment-text"><p>Edit -&gt; Preferences -&gt; Protocols -&gt; PDCP-LTE -&gt; Attempt to decode ROHC data. Note that ROHC support is only partial.</p></div><div id="comment-18930-info" class="comment-info"><span class="comment-age">(27 Feb '13, 08:49)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="18955"></span><div id="comment-18955" class="comment"><div id="post-18955-score" class="comment-score"></div><div class="comment-text"><p>I already enabled this preference but I still cant see the ROHC message. (Though it is a compressed profile 1 packet)</p></div><div id="comment-18955-info" class="comment-info"><span class="comment-age">(27 Feb '13, 21:57)</span> <span class="comment-user userinfo">dr1</span></div></div><span id="18956"></span><div id="comment-18956" class="comment"><div id="post-18956-score" class="comment-score"></div><div class="comment-text"><p>Is there any tweaking required in the wireshark code?</p></div><div id="comment-18956-info" class="comment-info"><span class="comment-age">(27 Feb '13, 21:57)</span> <span class="comment-user userinfo">dr1</span></div></div><span id="18957"></span><div id="comment-18957" class="comment"><div id="post-18957-score" class="comment-score"></div><div class="comment-text"><p>According to the source code of 1.4.0, the PDCP LTE dissector is just able to identify that it is a type 1 packet without dissecting it. And it will only work if the PDCP LTE dissector is called from the DCT2000 dissector so as to set the PDCP info structure. By using Wireshark development version (<a href="https://www.wireshark.org/download/automated/)">https://www.wireshark.org/download/automated/)</a> you will be able to perform a better dissection, especially if your capture contains the IR packet. Profiles supported are uncompressed, RTP/UDP/IP and UDP/IP. If you can share your pcap file, it would allow to enhance the ROHC dissection if needed.</p></div><div id="comment-18957-info" class="comment-info"><span class="comment-age">(27 Feb '13, 22:18)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-18830" class="comment-tools"></div><div class="clear"></div><div id="comment-18830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

