+++
type = "question"
title = "Proxy authentication failure. Want to find out which machine."
description = '''I installed wireshark in my proxy server. I want to know which client is throwing out bad password. Is there away I can use wireshark to find out which client it is ?'''
date = "2017-03-14T15:42:00Z"
lastmod = "2017-03-15T07:26:00Z"
weight = 60076
keywords = [ "proxy", "wireshark" ]
aliases = [ "/questions/60076" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Proxy authentication failure. Want to find out which machine.](/questions/60076/proxy-authentication-failure-want-to-find-out-which-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60076-score" class="post-score" title="current number of votes">0</div><span id="post-60076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed wireshark in my proxy server. I want to know which client is throwing out bad password. Is there away I can use wireshark to find out which client it is ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '17, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/e1a7ee5ff8bf06b83d650710e1f51013?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnynot&#39;s gravatar image" /><p><span>gnynot</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnynot has no accepted answers">0%</span></p></div></div><div id="comments-container-60076" class="comments-container"><span id="60077"></span><div id="comment-60077" class="comment"><div id="post-60077-score" class="comment-score"></div><div class="comment-text"><p>I'm using NTLM authentication. I see that ntlmssp.auth.username == user1 doesn't help with anything am I using wrong syntax?</p></div><div id="comment-60077-info" class="comment-info"><span class="comment-age">(14 Mar '17, 17:26)</span> <span class="comment-user userinfo">gnynot</span></div></div><span id="60089"></span><div id="comment-60089" class="comment"><div id="post-60089-score" class="comment-score"></div><div class="comment-text"><p>Is your proxy a HTTP proxy?</p><p>Is your connection to the proxy dissected as HTTP? Maybe you have to use 'Decode as' HTTP first?</p><p>If the connection is dissected as HTTP, 'ntlmssp.auth.username==foobar' lists the packets with a NTLM auth for user foobar (at least with my setup).</p></div><div id="comment-60089-info" class="comment-info"><span class="comment-age">(15 Mar '17, 07:26)</span> <span class="comment-user userinfo">Uli</span></div></div></div><div id="comment-tools-60076" class="comment-tools"></div><div class="clear"></div><div id="comment-60076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

