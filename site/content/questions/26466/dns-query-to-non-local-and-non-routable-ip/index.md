+++
type = "question"
title = "DNS query to non local and non routable IP"
description = '''I noticed by accident my computer is sending DNS queries to 192.168.1.1 despite it&#x27;s on a class A internal network (10.0.0.0). The queries goes to the firewalls mac-adress, the firewalls IP i 10.0.0.1. I don&#x27;t have 192.168.1.1 registered as a dns server in my network settings. I guess the query goes...'''
date = "2013-10-28T07:54:00Z"
lastmod = "2013-10-29T10:47:00Z"
weight = 26466
keywords = [ "dns" ]
aliases = [ "/questions/26466" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [DNS query to non local and non routable IP](/questions/26466/dns-query-to-non-local-and-non-routable-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26466-score" class="post-score" title="current number of votes">0</div><span id="post-26466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I noticed by accident my computer is sending DNS queries to 192.168.1.1 despite it's on a class A internal network (10.0.0.0).</p><p>The queries goes to the firewalls mac-adress, the firewalls IP i 10.0.0.1.</p><p>I don't have 192.168.1.1 registered as a dns server in my network settings.</p><p>I guess the query goes to the firewall because it's the default gateway and there's no static route to a 192.168.1.10 subnet? But how do I find out what and why on my computer is sending the queries to this class C address?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '13, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/66d07eb13a386219967adce3aaeb7386?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Molotch&#39;s gravatar image" /><p><span>Molotch</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Molotch has no accepted answers">0%</span></p></div></div><div id="comments-container-26466" class="comments-container"><span id="26478"></span><div id="comment-26478" class="comment"><div id="post-26478-score" class="comment-score"></div><div class="comment-text"><p>what is your client OS and version?</p></div><div id="comment-26478-info" class="comment-info"><span class="comment-age">(28 Oct '13, 08:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26487"></span><div id="comment-26487" class="comment"><div id="post-26487-score" class="comment-score"></div><div class="comment-text"><p>Windows 7 x64 Enterprise with SP1.</p></div><div id="comment-26487-info" class="comment-info"><span class="comment-age">(28 Oct '13, 13:31)</span> <span class="comment-user userinfo">Molotch</span></div></div></div><div id="comment-tools-26466" class="comment-tools"></div><div class="clear"></div><div id="comment-26466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26490"></span>

<div id="answer-container-26490" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26490-score" class="post-score" title="current number of votes">1</div><span id="post-26490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Molotch has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But how do I find out what and why on my computer is sending the queries to this class C address?</p></blockquote><p>this is nothing you can solve with Wireshark, as every program on your Windows will call system APIs for DNS resolution. Thus every DNS query will be created by some system component and you will not be able to figure out which program triggered the DNS query (originally) just by looking at the network capture, as there is no information in the DNS packets about the originator.</p><p>See also here: <a href="http://ask.wireshark.org/questions/26171/how-can-i-determine-which-application-is-sending-dns-queries-to-my-bind-server?page=1&amp;focusedAnswerId=26234#26234">http://ask.wireshark.org/questions/26171/how-can-i-determine-which-application-is-sending-dns-queries-to-my-bind-server?page=1&amp;focusedAnswerId=26234#26234</a></p><p>So, on Windows you have the following options:</p><ul><li>dump the whole network configuration and check if there is a reference to 192.168.1.1</li></ul><blockquote><p>netsh dump | find "192.168.1.1"<br />
ipconfig /a | find "192.168.1.1"<br />
</p></blockquote><ul><li>search the registry for 192.168.1.1</li><li>Take a look a the DNS queries and the names in those queries. Maybe there are typical names that can help to identify a certain tool/software on your system.</li><li>get a API call tracer/monitor (<a href="https://www.google.com/?q=windows+api+monitor">search google</a>) and try to watch calls to the DNS resolver API</li><li>Try to use the new <a href="http://technet.microsoft.com/en-us/library/jj649776.aspx">Microsoft Message Analyzer</a> to find the process that triggers the DNS queries (not sure if that would work)</li></ul><p>Besides that, there is not much you can do on Windows, at least I don't know more than the things listed above.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Oct '13, 14:37</strong> </span></p></div></div><div id="comments-container-26490" class="comments-container"><span id="26522"></span><div id="comment-26522" class="comment"><div id="post-26522-score" class="comment-score"></div><div class="comment-text"><p>Thank you for a good answer. I'll try your suggestions and see what I can find out.</p></div><div id="comment-26522-info" class="comment-info"><span class="comment-age">(29 Oct '13, 10:47)</span> <span class="comment-user userinfo">Molotch</span></div></div></div><div id="comment-tools-26490" class="comment-tools"></div><div class="clear"></div><div id="comment-26490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

