+++
type = "question"
title = "Help extracting data from http post"
description = '''I&#x27;m trying to view the communications between a game and it&#x27;s server. I believe it is using some form of UTF8 encoded xml but wireshark is only showing application/octet-stream and I&#x27;m not able to get the text from these files. The server name has xrpc in it, so I&#x27;m assuming it&#x27;s using xrpc or xml-r...'''
date = "2016-11-23T11:04:00Z"
lastmod = "2016-11-24T03:43:00Z"
weight = 57578
keywords = [ "post", "octet-stream", "data", "xml-rpc", "xrpc" ]
aliases = [ "/questions/57578" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help extracting data from http post](/questions/57578/help-extracting-data-from-http-post)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57578-score" class="post-score" title="current number of votes">0</div><span id="post-57578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to view the communications between a game and it's server. I believe it is using some form of UTF8 encoded xml but wireshark is only showing application/octet-stream and I'm not able to get the text from these files. The server name has xrpc in it, so I'm assuming it's using xrpc or xml-rpc.</p><p>Could someone provide guidance on how to extract the payload in clear text instead of having to view it in hex?</p><p><a href="https://www.dropbox.com/s/xanrozfnklt30ng/boot.pcap?dl=0">https://www.dropbox.com/s/xanrozfnklt30ng/boot.pcap?dl=0</a> <a href="https://www.dropbox.com/s/czvzmj59lnfz9ux/boot.pcapng?dl=0">https://www.dropbox.com/s/czvzmj59lnfz9ux/boot.pcapng?dl=0</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-octet-stream" rel="tag" title="see questions tagged &#39;octet-stream&#39;">octet-stream</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-xml-rpc" rel="tag" title="see questions tagged &#39;xml-rpc&#39;">xml-rpc</span> <span class="post-tag tag-link-xrpc" rel="tag" title="see questions tagged &#39;xrpc&#39;">xrpc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '16, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/edda64fc3a2ea1f338d14e668ee134c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="octrevolution&#39;s gravatar image" /><p><span>octrevolution</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="octrevolution has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Nov '16, 11:54</strong> </span></p></div></div><div id="comments-container-57578" class="comments-container"></div><div id="comment-tools-57578" class="comment-tools"></div><div class="clear"></div><div id="comment-57578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57598"></span>

<div id="answer-container-57598" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57598-score" class="post-score" title="current number of votes">0</div><span id="post-57598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like the name XRPC is used both for an XML based RPC protocol as a gaming protocol. I'm sure the latter has been used. A little googling on games and xrpc lays a link with jrpc. From there on I think if you want to extract meaningful data from the communication, all you can do is start reverse engineering the network protocol. This is beyond the scope of this Q&amp;A site.</p><p>If you do have reverse engineered the protocol, you might be able to write dissector-code so that Wireshark can present you with the protocol fields in a meaningful way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '16, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-57598" class="comments-container"></div><div id="comment-tools-57598" class="comment-tools"></div><div class="clear"></div><div id="comment-57598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

