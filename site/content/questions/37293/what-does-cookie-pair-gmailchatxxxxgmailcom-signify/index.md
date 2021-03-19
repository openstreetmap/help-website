+++
type = "question"
title = "What does cookie pair: gmailchat=XXXX@gmail.com signify"
description = '''I&#x27;ve just recently started playing around with Wireshark using pre-captures pcap files and running through various scenarios. At the moment I am attempting to find identifying data for an ip address - I can see facebook sessions and gmail sessions using the filter ip.addr=&quot;xxx.xxx.xxx.xxx&quot; &amp;amp;&amp;amp...'''
date = "2014-10-22T10:53:00Z"
lastmod = "2014-11-16T02:39:00Z"
weight = 37293
keywords = [ "chat", "gmail" ]
aliases = [ "/questions/37293" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What does cookie pair: <span class="__cf_email__" cfemail="bfd8d2ded6d3dcd7decb82e7e7e7e7ffd8d2ded6d391dcd0d2">\[email protected\]</span> signify](/questions/37293/what-does-cookie-pair-gmailchatxxxxgmailcom-signify)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37293-score" class="post-score" title="current number of votes">0</div><span id="post-37293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've just recently started playing around with Wireshark using pre-captures pcap files and running through various scenarios. At the moment I am attempting to find identifying data for an ip address - I can see facebook sessions and gmail sessions using the filter ip.addr="xxx.xxx.xxx.xxx" &amp;&amp; http.request.method == "POST", but being encrypted I am unable to view their username.</p><p>However, looking through the HTTP POST packets for gmail I see a packet entry under the cookie as "Cookie Pair: <span class="__cf_email__" data-cfemail="66010b070f0a050e07125b0c090826010b070f0a4805090b">[email protected]</span>". My question - does this cookie pair indicate the user that is logged in to Gmail? Or is it indicating a chat started between the person logged in <em>with</em> the <span class="__cf_email__" data-cfemail="3d5752537d5a505c5451135e5250">[email protected]</span>?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-chat" rel="tag" title="see questions tagged &#39;chat&#39;">chat</span> <span class="post-tag tag-link-gmail" rel="tag" title="see questions tagged &#39;gmail&#39;">gmail</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '14, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/412080f78b9947b637ec0e4e8f3b41a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moriarty&#39;s gravatar image" /><p><span>moriarty</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moriarty has no accepted answers">0%</span></p></div></div><div id="comments-container-37293" class="comments-container"></div><div id="comment-tools-37293" class="comment-tools"></div><div class="clear"></div><div id="comment-37293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37884"></span>

<div id="answer-container-37884" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37884-score" class="post-score" title="current number of votes">1</div><span id="post-37884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could you trace your own google account chatting with someone else? Then you could check the cookies in your own traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '14, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-37884" class="comments-container"></div><div id="comment-tools-37884" class="comment-tools"></div><div class="clear"></div><div id="comment-37884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

