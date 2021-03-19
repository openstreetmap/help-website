+++
type = "question"
title = "Ssl/tls application data protocol when using pre master secret"
description = '''Hi I have custom protocol as ssl application data protocol, for which i have my own lua dissector. I want to know if there is a way to set the application data protocol to a protocol other than http, when using the pre master secret file,. thanks gianrico'''
date = "2015-02-10T00:39:00Z"
lastmod = "2015-02-10T02:52:00Z"
weight = 39743
keywords = [ "pre", "ssl", "secret", "master", "pms" ]
aliases = [ "/questions/39743" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ssl/tls application data protocol when using pre master secret](/questions/39743/ssltls-application-data-protocol-when-using-pre-master-secret)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39743-score" class="post-score" title="current number of votes">0</div><span id="post-39743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have custom protocol as ssl application data protocol, for which i have my own lua dissector. I want to know if there is a way to set the application data protocol to a protocol other than http, when using the pre master secret file,.</p><p>thanks gianrico</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pre" rel="tag" title="see questions tagged &#39;pre&#39;">pre</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-secret" rel="tag" title="see questions tagged &#39;secret&#39;">secret</span> <span class="post-tag tag-link-master" rel="tag" title="see questions tagged &#39;master&#39;">master</span> <span class="post-tag tag-link-pms" rel="tag" title="see questions tagged &#39;pms&#39;">pms</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '15, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/6b9ad59bd47afb2fb71373061eac90e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gianrico&#39;s gravatar image" /><p><span>gianrico</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gianrico has no accepted answers">0%</span></p></div></div><div id="comments-container-39743" class="comments-container"></div><div id="comment-tools-39743" class="comment-tools"></div><div class="clear"></div><div id="comment-39743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39752"></span>

<div id="answer-container-39752" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39752-score" class="post-score" title="current number of votes">1</div><span id="post-39752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>as far as I understand the code:</p><p>If you are using a pre-master secret file the "inner" protocol is derived from the standard protocols that have itself registered with the SSL dissector, by calling <strong>ssl_dissector_add()</strong> (see packet-http.c, packet-smtp.c, etc.). So, in your Lua dissector you would have to do the same. Unfortunately <strong>ssl_dissector_add()</strong> is not exposed to the Lua module, meaning you can't do that with the current code.</p><p>To solve your problem a (larger) code change would be required, to add the port and protocol to the pre-master secret file or to expose <strong>ssl_dissector_add()</strong> to Lua, while both approaches would be desirable and probably usefull in certain situations. If you need that and cannot implement it yourself, please file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a>. Add as much information as possible and a link to your question.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Feb '15, 02:53</strong> </span></p></div></div><div id="comments-container-39752" class="comments-container"></div><div id="comment-tools-39752" class="comment-tools"></div><div class="clear"></div><div id="comment-39752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

