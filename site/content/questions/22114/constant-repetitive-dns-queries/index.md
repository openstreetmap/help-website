+++
type = "question"
title = "Constant Repetitive DNS Queries"
description = '''My computer is running Windows 7 pro. When I perform a live capture on my network interface, I see constant DNS queries asking for the mail server at www.yahoo.com. After restarting the machine, logging in, and immediately starting Wireshark, I still see these queries - probably once every 2 or 3 se...'''
date = "2013-06-17T05:20:00Z"
lastmod = "2013-06-24T04:11:00Z"
weight = 22114
keywords = [ "dns" ]
aliases = [ "/questions/22114" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Constant Repetitive DNS Queries](/questions/22114/constant-repetitive-dns-queries)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22114-score" class="post-score" title="current number of votes">0</div><span id="post-22114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My computer is running Windows 7 pro. When I perform a live capture on my network interface, I see constant DNS queries asking for the mail server at www.yahoo.com. After restarting the machine, logging in, and immediately starting Wireshark, I still see these queries - probably once every 2 or 3 seconds. Has anyone seen anything like this before?<br />
</p><p>Note: I am trying to reply to your comments, but Akismet thinks all of my comments are spam. What am I doing wrong?</p><p>I am only seeing local network protocols and the DNS queries, but I have not done a capture for an extended period.</p><p>I mean MX queries for www.yahoo.com.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '13, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/b8afbe7a108b0f6f38898d009a125ea4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SR584&#39;s gravatar image" /><p><span>SR584</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SR584 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jun '13, 06:55</strong> </span></p></div></div><div id="comments-container-22114" class="comments-container"><span id="22115"></span><div id="comment-22115" class="comment"><div id="post-22115-score" class="comment-score"></div><div class="comment-text"><p>Do you have any other traffic besides these DNS Queries? Outbound SMTP connections for example?</p></div><div id="comment-22115-info" class="comment-info"><span class="comment-age">(17 Jun '13, 06:16)</span> <span class="comment-user userinfo">pfuender</span></div></div><span id="22117"></span><div id="comment-22117" class="comment"><div id="post-22117-score" class="comment-score"></div><div class="comment-text"><blockquote><p>DNS queries asking for <strong>the mail server</strong> at <strong>www.yahoo.com</strong></p></blockquote><p>What do you mean by that? A records for www.yahoo.com or MX records for yahoo.com (or www.yahoo.com)??</p></div><div id="comment-22117-info" class="comment-info"><span class="comment-age">(17 Jun '13, 06:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22114" class="comment-tools"></div><div class="clear"></div><div id="comment-22114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22119"></span>

<div id="answer-container-22119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22119-score" class="post-score" title="current number of votes">0</div><span id="post-22119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I mean MX queries for www.yahoo.com.</p></blockquote><p>as far as I can see, there are no MX records for <strong>www.</strong>yahoo.com. So, if you see those requests in your capture file, there is some software on your system that is either misconfigured or that is trying to do something it shouldn't.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '13, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22119" class="comments-container"><span id="22176"></span><div id="comment-22176" class="comment"><div id="post-22176-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, for your answer. I would still like to know which program is producing these DNS queries, but I have been unable to do so at this point. I suppose no harm is being done.</p><p>Sean</p></div><div id="comment-22176-info" class="comment-info"><span class="comment-age">(19 Jun '13, 09:27)</span> <span class="comment-user userinfo">SR584</span></div></div><span id="22244"></span><div id="comment-22244" class="comment"><div id="post-22244-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I would still like to know which program is producing these DNS queries</p></blockquote><p>hard to figure out, as the program will just call the DNS resolver API on your Windows system and then all DNS request are generated by the resolver of the system, so in a capture file, you will never be able to figure out what program triggers those DNS queries. You will need a Windows system API monitor tool to monitor calls to the DNS resolver API. Please google that.</p></div><div id="comment-22244-info" class="comment-info"><span class="comment-age">(22 Jun '13, 02:30)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22247"></span><div id="comment-22247" class="comment"><div id="post-22247-score" class="comment-score"></div><div class="comment-text"><p>I believe NetMon can tell you what process belongs to what packets (or vice versa)</p></div><div id="comment-22247-info" class="comment-info"><span class="comment-age">(22 Jun '13, 16:36)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="22272"></span><div id="comment-22272" class="comment"><div id="post-22272-score" class="comment-score"></div><div class="comment-text"><p>I guess you mean Microsoft Network Monitor and its capability to show the process name that owns a connection.</p><p>However, as I said, the DNS request will not be issued by any user process (browser, etc.) but by the system DNS resolver library. And thus NetMon is also unable to show which process triggered the DNS query. I just tested it, and NetMon shows <strong>&lt;unknown&gt;</strong> as process name for DNS queries. So, if you want to know who triggered certain DNS queriey, you need either a way of debugging the system DNS resolver library or a system API call tracer.</p></div><div id="comment-22272-info" class="comment-info"><span class="comment-age">(24 Jun '13, 04:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22119" class="comment-tools"></div><div class="clear"></div><div id="comment-22119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

