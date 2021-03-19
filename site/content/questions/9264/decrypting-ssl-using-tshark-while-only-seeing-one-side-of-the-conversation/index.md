+++
type = "question"
title = "decrypting ssl using tshark while only seeing one side of the conversation"
description = '''Hello, Been bashing my brain trying to find a solution to decrypting ssl traffic using tshark when I only have access to one side of the conversation. The traffic I see is asymmetric so I will never see the response from the ssl handshake leaving my network as it leaves out of another network pipe. ...'''
date = "2012-02-27T23:49:00Z"
lastmod = "2012-03-04T03:27:00Z"
weight = 9264
keywords = [ "ssl" ]
aliases = [ "/questions/9264" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [decrypting ssl using tshark while only seeing one side of the conversation](/questions/9264/decrypting-ssl-using-tshark-while-only-seeing-one-side-of-the-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9264-score" class="post-score" title="current number of votes">0</div><span id="post-9264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Been bashing my brain trying to find a solution to decrypting ssl traffic using tshark when I only have access to one side of the conversation. The traffic I see is asymmetric so I will never see the response from the ssl handshake leaving my network as it leaves out of another network pipe. Would it be possible to sniff the traffic having the private/pub keys or would I require full visibility into the TCP session?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '12, 23:49</strong></p><img src="https://secure.gravatar.com/avatar/9354f19d7b6f14c9459f34a1cb622f36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="divious1&#39;s gravatar image" /><p><span>divious1</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="divious1 has no accepted answers">0%</span></p></div></div><div id="comments-container-9264" class="comments-container"></div><div id="comment-tools-9264" class="comment-tools"></div><div class="clear"></div><div id="comment-9264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9341"></span>

<div id="answer-container-9341" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9341-score" class="post-score" title="current number of votes">1</div><span id="post-9341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK that is not possible. You need information from both sides of the conversation to be able to decrypt the traffic. The things that pop into mind are:</p><ul><li>You need the ServerHello message from the server to know which cipher was chosen</li><li>You need the ClientKeyExchange from the client to extract the pre-master secret to extract the bulk-encryption key for each specific SSL session</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '12, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9341" class="comments-container"></div><div id="comment-tools-9341" class="comment-tools"></div><div class="clear"></div><div id="comment-9341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

