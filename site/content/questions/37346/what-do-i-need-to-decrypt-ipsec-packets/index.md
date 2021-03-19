+++
type = "question"
title = "What do I need to decrypt IPsec packets?"
description = '''I have a virtual network setup of 2 ubuntu and 2 IPFire with a fifth virtual machine on which I installed Wireshark, I named that VM &quot;Sniffer&quot;. Each ubuntu is connected to an IPFire which acts as a gateway connected to another network which is exactly the same. I have been able to monitor the packet...'''
date = "2014-10-26T05:52:00Z"
lastmod = "2014-10-26T15:21:00Z"
weight = 37346
keywords = [ "decryption", "ipsec" ]
aliases = [ "/questions/37346" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What do I need to decrypt IPsec packets?](/questions/37346/what-do-i-need-to-decrypt-ipsec-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37346-score" class="post-score" title="current number of votes">0</div><span id="post-37346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a virtual network setup of 2 ubuntu and 2 IPFire with a fifth virtual machine on which I installed Wireshark, I named that VM "Sniffer". Each ubuntu is connected to an IPFire which acts as a gateway connected to another network which is exactly the same. I have been able to monitor the packets flowing from network 1 to network 2, including IPsec ESP packets, put I have no idea on how can I decrypt this packets through Wireshark. What do I need to do or have to decrypt IPsec packets using Wireshark?</p><p>I am using IKEv2 ESP Encryption.</p><p>I just need to be put on the road :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-ipsec" rel="tag" title="see questions tagged &#39;ipsec&#39;">ipsec</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '14, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/61a216e4d6ffe0b3d4a2b06f15caac8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mohamed%20Ahmed&#39;s gravatar image" /><p><span>Mohamed Ahmed</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mohamed Ahmed has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Oct '14, 06:15</strong> </span></p></div></div><div id="comments-container-37346" class="comments-container"></div><div id="comment-tools-37346" class="comment-tools"></div><div class="clear"></div><div id="comment-37346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37347"></span>

<div id="answer-container-37347" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37347-score" class="post-score" title="current number of votes">2</div><span id="post-37347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mohamed Ahmed has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the wiki page for <a href="http://wiki.wireshark.org/ESP">esp</a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '14, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Oct '14, 06:56</strong> </span></p></div></div><div id="comments-container-37347" class="comments-container"><span id="37349"></span><div id="comment-37349" class="comment"><div id="post-37349-score" class="comment-score"></div><div class="comment-text"><p>To be honest, I have seen it but not read it. But it seems that the only way I can decrypt ESP packets using Wireshark is by providing it with the security parameters of the tunnel, so it doesn't allow me to crack IPsec without an insider knowledge of the security tunnel being inspected. Is that the correct understanding of the situation?</p></div><div id="comment-37349-info" class="comment-info"><span class="comment-age">(26 Oct '14, 08:11)</span> <span class="comment-user userinfo">Mohamed Ahmed</span></div></div><span id="37350"></span><div id="comment-37350" class="comment"><div id="post-37350-score" class="comment-score">2</div><div class="comment-text"><p>Yes this is correct.</p></div><div id="comment-37350-info" class="comment-info"><span class="comment-age">(26 Oct '14, 08:34)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="37351"></span><div id="comment-37351" class="comment"><div id="post-37351-score" class="comment-score">3</div><div class="comment-text"><p>If you could simply decrypt the packets off the wire, with no information other than the packets themselves, that would kind of defeat the purpose of ESP and encryption altogether. :)</p></div><div id="comment-37351-info" class="comment-info"><span class="comment-age">(26 Oct '14, 09:29)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="37352"></span><div id="comment-37352" class="comment"><div id="post-37352-score" class="comment-score"></div><div class="comment-text"><p>Yes, I thought so. But I guess everything is cracked by the NSA, but we don't have their tools :)</p></div><div id="comment-37352-info" class="comment-info"><span class="comment-age">(26 Oct '14, 10:30)</span> <span class="comment-user userinfo">Mohamed Ahmed</span></div></div></div><div id="comment-tools-37347" class="comment-tools"></div><div class="clear"></div><div id="comment-37347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37354"></span>

<div id="answer-container-37354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37354-score" class="post-score" title="current number of votes">0</div><span id="post-37354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Additionally to the wiki, you could check/read my answer to a similar question.</p><blockquote><p><a href="https://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets">https://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '14, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37354" class="comments-container"></div><div id="comment-tools-37354" class="comment-tools"></div><div class="clear"></div><div id="comment-37354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

