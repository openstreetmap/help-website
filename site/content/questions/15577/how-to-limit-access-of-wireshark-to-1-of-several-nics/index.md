+++
type = "question"
title = "how to limit access of wireshark to 1 of several nics"
description = '''how can i limit wiresharks activity to 1 particular ethernet nic of several on a given station? we&#x27;re in a classroom situation and we have 1 nic connected to a network which is local to the classroom. another nic is connected to the campus network. i don&#x27;t want the class to have the option of sniffi...'''
date = "2012-11-06T04:49:00Z"
lastmod = "2012-11-06T05:05:00Z"
weight = 15577
keywords = [ "access", "nic", "limiting" ]
aliases = [ "/questions/15577" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to limit access of wireshark to 1 of several nics](/questions/15577/how-to-limit-access-of-wireshark-to-1-of-several-nics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15577-score" class="post-score" title="current number of votes">0</div><span id="post-15577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can i limit wiresharks activity to 1 particular ethernet nic of several on a given station? we're in a classroom situation and we have 1 nic connected to a network which is local to the classroom. another nic is connected to the campus network. i don't want the class to have the option of sniffing on the campus network. tnx ams</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-limiting" rel="tag" title="see questions tagged &#39;limiting&#39;">limiting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '12, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/7dce81d8dffe89e75e60b3fc49965947?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jct%20netlabs&#39;s gravatar image" /><p><span>jct netlabs</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jct netlabs has no accepted answers">0%</span></p></div></div><div id="comments-container-15577" class="comments-container"><span id="15578"></span><div id="comment-15578" class="comment"><div id="post-15578-score" class="comment-score"></div><div class="comment-text"><p>What is the OS of these computers? With Windows you're out of luck...</p></div><div id="comment-15578-info" class="comment-info"><span class="comment-age">(06 Nov '12, 05:04)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-15577" class="comment-tools"></div><div class="clear"></div><div id="comment-15577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15579"></span>

<div id="answer-container-15579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15579-score" class="post-score" title="current number of votes">0</div><span id="post-15579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately that's not possible without a change to the code of Wireshark. See my answer in the question below:</p><blockquote><p><code>http://ask.wireshark.org/questions/14067/limit-interface</code><br />
</p></blockquote><p>Furthermore: Even if you could limit Wireshark to listen to one specific interface, your students could just swap the network cables and would then still be able to capture traffic on the campus network.</p><p>So, what can you do:</p><ul><li>build a virtual lab in vmware (or KVM, Xen, etc.) and let the students connect to the capturing machine via RDP, VNC or any other remote desktop software. You can easily separate the virtual lab network from the campus network in a virtual environment.</li><li>don't care too much about the students sniffing the campus network. They can do that anyway, if they bring their own laptop to the campus ;-)</li><li>don't care too much about the students sniffing the campus network, as they will only see their own traffic and broadcast traffic if they are connected to a switch, unless the students use some arp spoofing/flooding tools (maybe you even teach them how to use those kind of tools in your course). So, you should just forbid using those tools on the campus network, as they can severely disrupt the network operation.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '12, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Nov '12, 05:39</strong> </span></p></div></div><div id="comments-container-15579" class="comments-container"></div><div id="comment-tools-15579" class="comment-tools"></div><div class="clear"></div><div id="comment-15579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

