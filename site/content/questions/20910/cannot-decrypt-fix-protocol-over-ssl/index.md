+++
type = "question"
title = "cannot decrypt Fix protocol over SSL"
description = '''Hello  Im using wireshark 1.6.8 Im tring to decode FIX traffic over TLSV1 So, On the SSL Decrypt dialog we fill the  &amp;lt;-ip-&amp;gt; &amp;lt;-port-&amp;gt; &amp;lt;-FIX-&amp;gt; &amp;lt;-path&#92;to&#92;key-&amp;gt; But after clicking on ok , we get the following error appear  &quot;error in column &#x27;Protocol&#x27;: Could not find dissector for...'''
date = "2013-05-02T09:44:00Z"
lastmod = "2013-05-04T15:14:00Z"
weight = 20910
keywords = [ "ssl", "fix" ]
aliases = [ "/questions/20910" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [cannot decrypt Fix protocol over SSL](/questions/20910/cannot-decrypt-fix-protocol-over-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20910-score" class="post-score" title="current number of votes">0</div><span id="post-20910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>Im using wireshark 1.6.8</p><p>Im tring to decode FIX traffic over TLSV1</p><p>So, On the SSL Decrypt dialog we fill the</p><p>&lt;-ip-&gt;</p><p>&lt;-port-&gt;</p><p>&lt;-FIX-&gt;</p><p>&lt;-path\to\key-&gt;</p><p>But after clicking on ok , we get the following error appear</p><p>"error in column 'Protocol': Could not find dissector for: 'FIX'"</p><p>the same problem also when we write &lt;-fix-&gt; in place of &lt;-FIX-&gt;</p><p>Thanks for help. Sha</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-fix" rel="tag" title="see questions tagged &#39;fix&#39;">fix</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '13, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/bad2b533f7865d800a35877a4a8a5f6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brill&#39;s gravatar image" /><p><span>Brill</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brill has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '13, 16:33</strong> </span></p></div></div><div id="comments-container-20910" class="comments-container"></div><div id="comment-tools-20910" class="comment-tools"></div><div class="clear"></div><div id="comment-20910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20920"></span>

<div id="answer-container-20920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20920-score" class="post-score" title="current number of votes">1</div><span id="post-20920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately decrypting FIX SSL/TLS messages is not (yet) implemented. If you try to add an SSL key for FIX (or fix) in Wireshark 1.9.2, you will get the list of allowed dissectors.</p><pre><code>error in column &#39;Protocol&#39;: Could not find dissector for: &#39;fix&#39;
Valid dissectors are:
&#39;http&#39; TCP 443
&#39;smtp&#39; TCP 465
&#39;ldap&#39; TCP 636
&#39;imap&#39; TCP 993
&#39;pop&#39; TCP 995
&#39;q931.tpkt&#39; TCP 1300
&#39;skinny&#39; TCP 2443
&#39;http&#39; TCP 4433
&#39;sip.tcp&#39; TCP 5061</code></pre><p>These dissectors call <strong>ssl_dissector_add()</strong> during their initialization. The FIX dissector does not do that and thus you get that error message.</p><p>If you need/want that feature, please file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> with a reference to this question.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '13, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20920" class="comments-container"><span id="20923"></span><div id="comment-20923" class="comment"><div id="post-20923-score" class="comment-score"></div><div class="comment-text"><p>Kurt</p><p>Thank you for the information</p><p>Is there any other way to decrypt protocol that arent on the list above ?</p><p>Sha</p></div><div id="comment-20923-info" class="comment-info"><span class="comment-age">(03 May '13, 01:10)</span> <span class="comment-user userinfo">Brill</span></div></div><span id="20927"></span><div id="comment-20927" class="comment"><div id="post-20927-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is there any other way to decrypt protocol that arent on the list above ?</p></blockquote><p>As there is no 'general' way to decrypt SSL/TLS when used within another protocol, you need a special tool that is able to decrypt the FIX protocol. I have not check how FIX uses SSL/TLS. Can you add some information about that?</p></div><div id="comment-20927-info" class="comment-info"><span class="comment-age">(03 May '13, 03:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20929"></span><div id="comment-20929" class="comment"><div id="post-20929-score" class="comment-score"></div><div class="comment-text"><p>You can always use "data" as protocol in the SSL keys list, this will just decrypt the traffic and show the decrypted hex data, wthout any further interpretation.</p></div><div id="comment-20929-info" class="comment-info"><span class="comment-age">(03 May '13, 03:11)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="20931"></span><div id="comment-20931" class="comment"><div id="post-20931-score" class="comment-score"></div><div class="comment-text"><p>Ah, nice! One new thing learned for today ;-)</p></div><div id="comment-20931-info" class="comment-info"><span class="comment-age">(03 May '13, 03:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20933"></span><div id="comment-20933" class="comment"><div id="post-20933-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8625">Bug 8625</a> was opened for this.</p></div><div id="comment-20933-info" class="comment-info"><span class="comment-age">(03 May '13, 06:27)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="20953"></span><div id="comment-20953" class="comment not_top_scorer"><div id="post-20953-score" class="comment-score"></div><div class="comment-text"><p>I dont really know how ssl encrypt fix data. Need to investigate that...</p><p>Thanks for help and solutions</p><p>Shalom</p></div><div id="comment-20953-info" class="comment-info"><span class="comment-age">(04 May '13, 15:14)</span> <span class="comment-user userinfo">Brill</span></div></div></div><div id="comment-tools-20920" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-20920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

