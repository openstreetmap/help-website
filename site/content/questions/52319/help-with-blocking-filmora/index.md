+++
type = "question"
title = "Help With Blocking Filmora"
description = '''I have a serial for the video editing software &quot;Filmora&quot; and I am trying to prevent it from accessing the internet. I&#x27;ve blocked my (Win7) firewall for both of the two running executables from Filmora&#x27;s installation directory, but it still connects to the internet and invalidates my (legitimate) reg...'''
date = "2016-05-08T11:57:00Z"
lastmod = "2017-02-24T03:46:00Z"
weight = 52319
keywords = [ "firewall", "filmora", "block", "registration" ]
aliases = [ "/questions/52319" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Help With Blocking Filmora](/questions/52319/help-with-blocking-filmora)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52319-score" class="post-score" title="current number of votes">0</div><span id="post-52319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a serial for the video editing software "Filmora" and I am trying to prevent it from accessing the internet. I've blocked my (Win7) firewall for both of the two running executables from Filmora's installation directory, but it still connects to the internet and invalidates my (legitimate) registration serial.</p><p>So, as a 2nd step (1st being the firewall blocking), I installed "Process Monitor" hoping to find a process/executable that is somehow connecting to the internet from Filmora, but could not. TOO MANY ENTRIES and I really don't know how to read the log very well.</p><p>So, my 3rd idea was to install Wireshark and see if I can identify an "outbound" process/executable that way. I've installed Wireshark a couple of times, but it is even more complex than process monitor, so I thought I'd find a forum (this one) and ask for help.</p><p>What's the best way to use Wireshark to monitor Filmora in order to determine which process is accessing the internet, so I can block it in my firewall? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span> <span class="post-tag tag-link-filmora" rel="tag" title="see questions tagged &#39;filmora&#39;">filmora</span> <span class="post-tag tag-link-block" rel="tag" title="see questions tagged &#39;block&#39;">block</span> <span class="post-tag tag-link-registration" rel="tag" title="see questions tagged &#39;registration&#39;">registration</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '16, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/32cefaf931b9b875490f2262a517c566?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wire_Birch&#39;s gravatar image" /><p><span>Wire_Birch</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wire_Birch has no accepted answers">0%</span></p></div></div><div id="comments-container-52319" class="comments-container"></div><div id="comment-tools-52319" class="comment-tools"></div><div class="clear"></div><div id="comment-52319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52359"></span>

<div id="answer-container-52359" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52359-score" class="post-score" title="current number of votes">0</div><span id="post-52359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I might post a more detailed answer, but for posterity I seemed to have solved my problem. Long story short Wireshark showed a connection to a chinese IP Address, which I investigated and it turns out it's associated with "Wondershare". Blocked the single IP address, which worked for about a day, then it didn't. Fired-up Wireshark a 2nd time and discovered that a different IP address was being used, but it was in the same "block" of IP Addresses, so I blocked the whole range in my firewall (by making a rule), and that seems to have done the trick. Working now for about 2 days. Maybe in a week or so I'll post details on how to build the rule. I want to give it time to make sure it's a durable fix.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '16, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/32cefaf931b9b875490f2262a517c566?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wire_Birch&#39;s gravatar image" /><p><span>Wire_Birch</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wire_Birch has no accepted answers">0%</span></p></div></div><div id="comments-container-52359" class="comments-container"></div><div id="comment-tools-52359" class="comment-tools"></div><div class="clear"></div><div id="comment-52359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59657"></span>

<div id="answer-container-59657" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59657-score" class="post-score" title="current number of votes">0</div><span id="post-59657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I ended up going to my firewall settings (wf.msc in Win 10) and blocking all outbound connections by default. I then re-enabled all my default inbound &amp; outbound rules, added in a few rules for msOutlook, Kerberos, DFS and high TCP/UDP ports, and it seems to have done the trick with preventing any unauthorized program accessing the internet (ahem... Filmora).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '17, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/da119487fddb39e59b64370294ae0fc1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MX6&#39;s gravatar image" /><p><span>MX6</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MX6 has no accepted answers">0%</span></p></div></div><div id="comments-container-59657" class="comments-container"></div><div id="comment-tools-59657" class="comment-tools"></div><div class="clear"></div><div id="comment-59657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

