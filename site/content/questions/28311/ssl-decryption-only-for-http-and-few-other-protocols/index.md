+++
type = "question"
title = "SSL Decryption: only for http and few other protocols"
description = '''Hello Team, I can decrypt SSL inside TCP on different ports. That works fine as long at that is typical protocol like http or smtp or ldap... But i have custom/prioprietary protocol inside that SSL. In the past i did not have any problems with that, i could see binary MSCHAPv2 session inside SSL: ht...'''
date = "2013-12-21T03:19:00Z"
lastmod = "2013-12-21T07:39:00Z"
weight = 28311
keywords = [ "ssl" ]
aliases = [ "/questions/28311" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decryption: only for http and few other protocols](/questions/28311/ssl-decryption-only-for-http-and-few-other-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28311-score" class="post-score" title="current number of votes">0</div><span id="post-28311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Team,</p><p>I can decrypt SSL inside TCP on different ports. That works fine as long at that is typical protocol like http or smtp or ldap...</p><p>But i have custom/prioprietary protocol inside that SSL. In the past i did not have any problems with that, i could see binary MSCHAPv2 session inside SSL: <a href="https://supportforums.cisco.com/servlet/JiveServlet/showImage/38-2724-125782/packet11-mod.png">https://supportforums.cisco.com/servlet/JiveServlet/showImage/38-2724-125782/packet11-mod.png</a></p><p>But right now with version 1.10.3 i do not see it. Debugs reveal some problems - it looks like decoder for specific protocol is mandatory ?. In my configuration i have selected http because i need to select something - but it does not working. In the past i have also used "http" and as you can see on the screenshot wireshark displayed decrypted data anyway.</p><p>How can i achieve the old behavior and decrypt any protocol hidden inside SSL ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '13, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/c57870fba6890fbb620bcbd60ce3185a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="highland7&#39;s gravatar image" /><p><span>highland7</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="highland7 has no accepted answers">0%</span></p></div></div><div id="comments-container-28311" class="comments-container"></div><div id="comment-tools-28311" class="comment-tools"></div><div class="clear"></div><div id="comment-28311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28312"></span>

<div id="answer-container-28312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28312-score" class="post-score" title="current number of votes">0</div><span id="post-28312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try <code>data</code> as protocol instead of <code>http</code>?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '13, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Dec '13, 07:40</strong> </span></p></div></div><div id="comments-container-28312" class="comments-container"></div><div id="comment-tools-28312" class="comment-tools"></div><div class="clear"></div><div id="comment-28312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

