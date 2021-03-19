+++
type = "question"
title = "wireshark (tshark) 2.3.0 export imf object error, a bug?"
description = '''In this pcap file, if we use &quot;tcp.stream eq 0&quot; as the filter, save text of the stream to a .emf file, we will get a legal mail file. If we use &quot;imf&quot; as the filter, copy text of the &quot;Internet Message Format&quot; and save it to a .emf file, open the emf file we saved, check the content of the attachment, ...'''
date = "2017-03-27T01:59:00Z"
lastmod = "2017-03-27T08:30:00Z"
weight = 60335
keywords = [ "smtp", "bug", "wireshark2.3", "imf" ]
aliases = [ "/questions/60335" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark (tshark) 2.3.0 export imf object error, a bug?](/questions/60335/wireshark-tshark-230-export-imf-object-error-a-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60335-score" class="post-score" title="current number of votes">0</div><span id="post-60335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In <strong><em><a href="https://1drv.ms/u/s!AsKf7JSSLhjigQhefk1LuYEisyWQ">this pcap file</a></em></strong>, if we use "tcp.stream eq 0" as the filter, save text of the stream to a .emf file, we will get a legal mail file.</p><p>If we use "imf" as the filter, copy text of the "Internet Message Format" and save it to a .emf file, open the emf file we saved, check the content of the attachment, we will find the picture is damaged.</p><p>If we use the "export object" to export the imf objects to file, the picture is damaged, too.</p><p>Here are the <strong><em><a href="https://1drv.ms/f/s!AsKf7JSSLhjigQwBjBr4XMJXPyBb">two eml files</a></em></strong> (ok.eml and error.eml), the content of this two files should be the same, but they are not. In the error.eml, we can read:<img src="https://osqa-ask.wireshark.org/upfiles/error_Mo2NbfZ.png" alt="alt text" /> These text are not correct.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-wireshark2.3" rel="tag" title="see questions tagged &#39;wireshark2.3&#39;">wireshark2.3</span> <span class="post-tag tag-link-imf" rel="tag" title="see questions tagged &#39;imf&#39;">imf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '17, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/0bd368bfaf8831f5ba687cb90597d980?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="my3439955&#39;s gravatar image" /><p><span>my3439955</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="my3439955 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Mar '17, 02:43</strong> </span></p></div></div><div id="comments-container-60335" class="comments-container"></div><div id="comment-tools-60335" class="comment-tools"></div><div class="clear"></div><div id="comment-60335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60341"></span>

<div id="answer-container-60341" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60341-score" class="post-score" title="current number of votes">0</div><span id="post-60341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I took a look and it seems that the "Fast Retransmissions" are not handled well by the TCP protocol preference "Do not call subdissectors for error packets". This means they will end up in the IMF data. The "follow TCP stream" output does not contain the extra bytes as they are ignored based on the TCP sequence numbers.</p><p>Could you file a bug-report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> for this? Please attach the file and my comments to the case. Thanks!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '17, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-60341" class="comments-container"><span id="60342"></span><div id="comment-60342" class="comment"><div id="post-60342-score" class="comment-score"></div><div class="comment-text"><p>I'll try what you told, thanks for answer</p></div><div id="comment-60342-info" class="comment-info"><span class="comment-age">(27 Mar '17, 03:36)</span> <span class="comment-user userinfo">my3439955</span></div></div><span id="60349"></span><div id="comment-60349" class="comment"><div id="post-60349-score" class="comment-score"></div><div class="comment-text"><p>bug reported. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13523">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13523</a></p></div><div id="comment-60349-info" class="comment-info"><span class="comment-age">(27 Mar '17, 04:20)</span> <span class="comment-user userinfo">my3439955</span></div></div><span id="60358"></span><div id="comment-60358" class="comment"><div id="post-60358-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-60358-info" class="comment-info"><span class="comment-age">(27 Mar '17, 08:30)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-60341" class="comment-tools"></div><div class="clear"></div><div id="comment-60341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

