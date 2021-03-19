+++
type = "question"
title = "prism ultralite trace to wireshark"
description = '''how can i convert a trace taken in prism ultralite to a wireshark readable format? the trace is saved in text format and when i run text2pcap it is only writing 16 bytes of a packet. also i would like to know a way to convert a wan trace with l2 protocol say ppp having first 2 bytes as FF 03 into an...'''
date = "2010-12-17T23:50:00Z"
lastmod = "2010-12-18T00:47:00Z"
weight = 1392
keywords = [ "text2pcap" ]
aliases = [ "/questions/1392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [prism ultralite trace to wireshark](/questions/1392/prism-ultralite-trace-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1392-score" class="post-score" title="current number of votes">0</div><span id="post-1392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can i convert a trace taken in prism ultralite to a wireshark readable format? the trace is saved in text format and when i run text2pcap it is only writing 16 bytes of a packet. also i would like to know a way to convert a wan trace with l2 protocol say ppp having first 2 bytes as FF 03 into an ethernet packet is there a program to do this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-text2pcap" rel="tag" title="see questions tagged &#39;text2pcap&#39;">text2pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '10, 23:50</strong></p><img src="https://secure.gravatar.com/avatar/fb62c26a883814378050872f2e4bc2fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xbobby&#39;s gravatar image" /><p><span>xbobby</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xbobby has no accepted answers">0%</span></p></div></div><div id="comments-container-1392" class="comments-container"></div><div id="comment-tools-1392" class="comment-tools"></div><div class="clear"></div><div id="comment-1392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1393"></span>

<div id="answer-container-1393" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1393-score" class="post-score" title="current number of votes">0</div><span id="post-1393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Recently text2pcap functionality has been added in Wireshark and there are quite a few options there which might help you out. You can download a development version from <a href="http://www.wireshark.org/download/automated/">http://www.wireshark.org/download/automated/</a>. You can then select "File =&gt; import".</p><p>If this does not help you, you can need to preprocess your text output to match a format that can be used by the import function.</p><p>Or you could file an enhancement request on https://bugzilla.wireshark.org asking for the "Prism Ultralite" file format to be included as supported filetype (at least for reading). PLease make sure you attach some tracefiles showing different encapsulation types. Of course it then all depends on when a developer finds the interest and time to write the code for it. If you feel up to it, you could write the code yourself and submit a patch to be included too :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '10, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1393" class="comments-container"></div><div id="comment-tools-1393" class="comment-tools"></div><div class="clear"></div><div id="comment-1393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

