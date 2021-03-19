+++
type = "question"
title = "Spotting botnet command &amp; control"
description = '''I was reading this article (http://www.technologyreview.com/computing/37311/?p1=MstRcnt&amp;amp;a=f) about spotting botnet command &amp;amp; control boxes. It seems to me you could also use the wireshark filter: dns.flags.rcode == 3 If you received a lot of failures as this filter should show, that would wa...'''
date = "2011-04-19T05:51:00Z"
lastmod = "2011-04-20T12:30:00Z"
weight = 3606
keywords = [ "botnets" ]
aliases = [ "/questions/3606" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Spotting botnet command & control](/questions/3606/spotting-botnet-command-control)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3606-score" class="post-score" title="current number of votes">1</div><span id="post-3606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was reading this article (http://www.technologyreview.com/computing/37311/?p1=MstRcnt&amp;a=f) about spotting botnet command &amp; control boxes. It seems to me you could also use the wireshark filter: dns.flags.rcode == 3 If you received a lot of failures as this filter should show, that would warrant further investigation. Thoughts anyone?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-botnets" rel="tag" title="see questions tagged &#39;botnets&#39;">botnets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '11, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/3a22303bd948b6cb232874f271c074fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobertM&#39;s gravatar image" /><p><span>RobertM</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobertM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Apr '11, 05:52</strong> </span></p></div></div><div id="comments-container-3606" class="comments-container"></div><div id="comment-tools-3606" class="comment-tools"></div><div class="clear"></div><div id="comment-3606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3644"></span>

<div id="answer-container-3644" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3644-score" class="post-score" title="current number of votes">2</div><span id="post-3644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume that your referring to the study published by Texas A&amp;M University at <a href="http://www.ee.tamu.edu/~reddy/papers/imc2010-yadav.pdf">http://www.ee.tamu.edu/~reddy/papers/imc2010-yadav.pdf</a></p><p>IMHO Wireshark is a tool to analyze generic network traffic and not a tool to detect botnet C&amp;C traffic. Detecting - and stopping - this traffic would more be a job for an intrusion detection / prevention system.</p><p>Alas, detecting C&amp;C traffic is not that easy: We found malicious and c&amp;c traffic also in ICMP, HTTP, and other protocols.</p><p>Just relying on the display filter dns.flags.rcode == 3 delivers a bunch of false positives, if you look for C&amp;C traffic. About every network with Windows workstations will generate a ton of queries for hostnames like WPAD (possibly multiple queries when name devolution is used).</p><p>DNS return code 3 can also be seen in large quantities for queries to spamhaus.org or a hashserver at trendmicro.com. To me these queries (or the return codes) are nothing to worry about.</p><p>Any other ideas?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-3644" class="comments-container"><span id="3651"></span><div id="comment-3651" class="comment"><div id="post-3651-score" class="comment-score"></div><div class="comment-text"><p>I fully understand your position, packethunter and I agree. I only mentioned this as an example that if you were getting a lot (let's say over 20) failed dns responses in a short amount of time from one machine in your network, that might alert an administrator to a possible(!) infection that would warrant looking into the errors further. I didn't mean to suggest using wireshark as a IDS or IPS. I suggested its use as another tool in hunting down C&amp;C in your network.</p></div><div id="comment-3651-info" class="comment-info"><span class="comment-age">(20 Apr '11, 12:15)</span> <span class="comment-user userinfo">SovereignMoney</span></div></div><span id="3653"></span><div id="comment-3653" class="comment"><div id="post-3653-score" class="comment-score"></div><div class="comment-text"><p>Sure. Wireshark is an excellent tool if you know what you are looking for.</p><p>Just remember that there are several techniques to sneak information through all security mechanisms that can be purchased for money.</p><p>Unfortunately we don't have a button like "find all problems" - yet.</p><p>Keep on hunting!</p></div><div id="comment-3653-info" class="comment-info"><span class="comment-age">(20 Apr '11, 12:30)</span> <span class="comment-user userinfo">packethunter</span></div></div></div><div id="comment-tools-3644" class="comment-tools"></div><div class="clear"></div><div id="comment-3644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

