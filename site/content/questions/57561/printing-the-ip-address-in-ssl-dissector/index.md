+++
type = "question"
title = "Printing the IP address in SSL dissector"
description = '''I wanted to print the destination IP address of a packet to a file if the decoder variable is created after the cipher key exchange. i.e final output would be a file with a list of ip addresses. To do so, I added code at the function static gint dissect_ssl3_record() fprintf(f,&quot;%s&quot;,address_to_str(NU...'''
date = "2016-11-23T00:33:00Z"
lastmod = "2016-12-05T13:35:00Z"
weight = 57561
keywords = [ "print", "ssl", "findipaddress", "ipaddress", "ssl_decrypt" ]
aliases = [ "/questions/57561" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Printing the IP address in SSL dissector](/questions/57561/printing-the-ip-address-in-ssl-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57561-score" class="post-score" title="current number of votes">0</div><span id="post-57561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to print the destination IP address of a packet to a file if the decoder variable is created after the cipher key exchange. i.e final output would be a file with a list of ip addresses.</p><p>To do so, I added code at the function static gint dissect_ssl3_record()</p><p>fprintf(f,"%s",address_to_str(NULL,(const guint8 *)session-&gt;srv_addr.data));</p><p>I have been unable to print out the IP address in numeric form so far.</p><p>Could someone please point me out how to print the destination ip address correctly in the ssl dissector.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-print" rel="tag" title="see questions tagged &#39;print&#39;">print</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-findipaddress" rel="tag" title="see questions tagged &#39;findipaddress&#39;">findipaddress</span> <span class="post-tag tag-link-ipaddress" rel="tag" title="see questions tagged &#39;ipaddress&#39;">ipaddress</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '16, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/c28011fe6d6c690149158e45cf811175?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mac9393&#39;s gravatar image" /><p><span>mac9393</span><br />
<span class="score" title="36 reputation points">36</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mac9393 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Dec '16, 11:50</strong> </span></p></div></div><div id="comments-container-57561" class="comments-container"></div><div id="comment-tools-57561" class="comment-tools"></div><div class="clear"></div><div id="comment-57561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57878"></span>

<div id="answer-container-57878" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57878-score" class="post-score" title="current number of votes">0</div><span id="post-57878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This should work once you call it after <code>ssl_set_server()</code> has been called. There is also <code>pinfo-&gt;dst</code> and <code>pinfo-&gt;src</code> which might be useful as alternative when you know the side.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '16, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-57878" class="comments-container"></div><div id="comment-tools-57878" class="comment-tools"></div><div class="clear"></div><div id="comment-57878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

