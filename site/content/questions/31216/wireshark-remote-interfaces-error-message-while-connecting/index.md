+++
type = "question"
title = "Wireshark Remote Interfaces error message while connecting"
description = '''I what to connect with wireshark remote interface to an other computer. On the computer runs pcap. But it don&#x27;t work. Do someone know the reason and a solution? Errormessage: I get the message: &quot;Can&#x27;t get list of interfaces: Loggin failt. Unknown user or password&quot; I what to connect with wireshark re...'''
date = "2014-03-27T07:17:00Z"
lastmod = "2014-03-27T23:50:00Z"
weight = 31216
keywords = [ "interfaces", "remote" ]
aliases = [ "/questions/31216" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Remote Interfaces error message while connecting](/questions/31216/wireshark-remote-interfaces-error-message-while-connecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31216-score" class="post-score" title="current number of votes">0</div><span id="post-31216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I what to connect with wireshark remote interface to an other computer. On the computer runs pcap. But it don't work. Do someone know the reason and a solution?</p><p>Errormessage:</p><p>I get the message: "Can't get list of interfaces: Loggin failt. Unknown user or password" I what to connect with wireshark remote interface to an other computer. On the computer runs pcap. But it don't work. Do someone know the reason and a solution?</p><p>Errormessage:</p><p>I get the message: "Can't get list of interfaces: Login fault. Unknown user or password"</p><p>I have tried the following:</p><ul><li>I have checked Password and User, they were valid and the user is a domain user with admin rights.</li><li>I have tried yo make a remote interface to the local machine where wireshark is running and this works.</li><li>I used the Port: 2002 and there is no virusscanner.</li></ul><p>How can I check that I can use the Port: 2002 ?</p><p>Is there an other common port like 2002 ?</p><p>Where is the reason for the error message ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '14, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/5da1ab99c9c336e772e069c86747135c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dirk%20Lehmann&#39;s gravatar image" /><p><span>Dirk Lehmann</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dirk Lehmann has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Mar '14, 06:40</strong> </span></p></div></div><div id="comments-container-31216" class="comments-container"></div><div id="comment-tools-31216" class="comment-tools"></div><div class="clear"></div><div id="comment-31216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31225"></span>

<div id="answer-container-31225" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31225-score" class="post-score" title="current number of votes">2</div><span id="post-31225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dirk Lehmann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'd check Password and User, they where valid and <strong>the user is a domain user</strong> with admin rights.</p></blockquote><p>rpcapd does not support domain authentication. Please use a local user account with admin privileges.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31225" class="comments-container"><span id="31244"></span><div id="comment-31244" class="comment"><div id="post-31244-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot, youre going right :-)</p></div><div id="comment-31244-info" class="comment-info"><span class="comment-age">(27 Mar '14, 23:50)</span> <span class="comment-user userinfo">Dirk Lehmann</span></div></div></div><div id="comment-tools-31225" class="comment-tools"></div><div class="clear"></div><div id="comment-31225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

