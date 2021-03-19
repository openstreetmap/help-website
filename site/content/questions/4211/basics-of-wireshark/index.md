+++
type = "question"
title = "Basics of wireshark"
description = '''Hello,  I have newly started using Wireshark for data capturing, can anybody please tell me what are the basic things one should know to work with wireshark.  For what purpose the manual pages are useful?'''
date = "2011-05-24T23:23:00Z"
lastmod = "2011-05-29T23:32:00Z"
weight = 4211
keywords = [ "beginner" ]
aliases = [ "/questions/4211" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Basics of wireshark](/questions/4211/basics-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4211-score" class="post-score" title="current number of votes">0</div><span id="post-4211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have newly started using Wireshark for data capturing, can anybody please tell me what are the basic things one should know to work with wireshark. For what purpose the manual pages are useful?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '11, 23:23</strong></p><img src="https://secure.gravatar.com/avatar/257c9f9e498193d7ddde57090efe094a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagu072&#39;s gravatar image" /><p><span>sagu072</span><br />
<span class="score" title="35 reputation points">35</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagu072 has no accepted answers">0%</span></p></div></div><div id="comments-container-4211" class="comments-container"></div><div id="comment-tools-4211" class="comment-tools"></div><div class="clear"></div><div id="comment-4211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4212"></span>

<div id="answer-container-4212" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4212-score" class="post-score" title="current number of votes">2</div><span id="post-4212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sagu072 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a really large topics, so here's what I think you should do:</p><ol><li>Familiarize yourself with Wireshark display filters, also context sensitive filtering by using the popup menus</li><li>check out the various statistics (endpoints, conversations, protocol distribution, I/O graph, just to name a few)</li><li>The most important thing you need is knowledge about the protocols you want to analyze. If you don't know how they are supposed to work you won't get much results out of working with Wireshark. So if you don't know the structure and workings of Ethernet, IP, TCP/UDP, ICMP, DHCP, ARP, etc. you should get into that. Otherwise the decodes won't mean much to you.</li></ol><p>It looks like a short list, but believe me, it's not something you can do in one afternoon ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '11, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4212" class="comments-container"><span id="4214"></span><div id="comment-4214" class="comment"><div id="post-4214-score" class="comment-score"></div><div class="comment-text"><p>jasper, Thank you very much jasper, knowing protcols is getting to know the working of tat protocol n message structures only right ? o anything else is important .? If u hv any other suggestion pleas post. Thanks Sagar</p></div><div id="comment-4214-info" class="comment-info"><span class="comment-age">(25 May '11, 00:09)</span> <span class="comment-user userinfo">sagu072</span></div></div><span id="4216"></span><div id="comment-4216" class="comment"><div id="post-4216-score" class="comment-score"></div><div class="comment-text"><p>You need to know message structures first, but also how the protocol works in regard to requests/answers. For example the TCP sequence number/acknowledge number mechanism is something where only knowing the header structure isn't enough - you also need to know how the packets work with each other.</p></div><div id="comment-4216-info" class="comment-info"><span class="comment-age">(25 May '11, 00:21)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="4217"></span><div id="comment-4217" class="comment"><div id="post-4217-score" class="comment-score"></div><div class="comment-text"><p>ok, what are dumpcap, mergecap etc, which are provided in manual pages, for wat purpose they can be used ?</p></div><div id="comment-4217-info" class="comment-info"><span class="comment-age">(25 May '11, 00:33)</span> <span class="comment-user userinfo">sagu072</span></div></div><span id="4219"></span><div id="comment-4219" class="comment"><div id="post-4219-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" into a "comment" as that is how this site works best, see the FAQ)</p></div><div id="comment-4219-info" class="comment-info"><span class="comment-age">(25 May '11, 00:52)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="4221"></span><div id="comment-4221" class="comment"><div id="post-4221-score" class="comment-score"></div><div class="comment-text"><p>@SynBit: thx, I would have done the conversion as well but I don't think I can :-)</p><p>@sagu072: dumpcap is the executable that does the actual capture on your network card. It can either be used separately or automatically through capturing from within Wireshark. Mergecap is used to merge or concatenate multiple tracefiles.</p></div><div id="comment-4221-info" class="comment-info"><span class="comment-age">(25 May '11, 01:14)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="4282"></span><div id="comment-4282" class="comment not_top_scorer"><div id="post-4282-score" class="comment-score"></div><div class="comment-text"><p>hi, i want to know how to decode the data which is in hex dumped format, i mean i want to know what s the exact message flowing through the network by removing the headers of protocol , can u pleas tel me some idea of how i can go to it.</p></div><div id="comment-4282-info" class="comment-info"><span class="comment-age">(29 May '11, 23:32)</span> <span class="comment-user userinfo">sagu072</span></div></div></div><div id="comment-tools-4212" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-4212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4220"></span>

<div id="answer-container-4220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4220-score" class="post-score" title="current number of votes">2</div><span id="post-4220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One good starting point is the book Laura Chappell wrote about <a href="http://www.wiresharkbook.com/">Wirshark Network Analysis</a>. It teches you the basics of how to use Wireshark and also the basics of mostly used protocols.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '11, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4220" class="comments-container"><span id="4222"></span><div id="comment-4222" class="comment"><div id="post-4222-score" class="comment-score"></div><div class="comment-text"><p>is that book s free ? it will be helpful for me if u can paste the link to download the book .</p></div><div id="comment-4222-info" class="comment-info"><span class="comment-age">(25 May '11, 01:16)</span> <span class="comment-user userinfo">sagu072</span></div></div><span id="4224"></span><div id="comment-4224" class="comment"><div id="post-4224-score" class="comment-score"></div><div class="comment-text"><p>Nope, that is not a free book.</p><p>If you want to start with free information you might want to check out the following:</p><ul><li><a href="http://www.wireshark.org/docs/">http://www.wireshark.org/docs/</a></li><li><a href="http://www.wireshark.org/docs/wsug_html_chunked/">The Wireshark User's Guide</a></li><li><a href="http://www.ietf.org/rfc.html">RFC's</a> For the protocols IP, ARP, TCP, UDP, ICMP for starters</li></ul></div><div id="comment-4224-info" class="comment-info"><span class="comment-age">(25 May '11, 01:25)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="4283"></span><div id="comment-4283" class="comment"><div id="post-4283-score" class="comment-score"></div><div class="comment-text"><p>hi, i want to know how to decode the data which is in hex dumped format, i mean i want to know what s the exact message flowing through the network by removing the headers of protocol , can u pleas tel me some idea of how i can go to it.</p></div><div id="comment-4283-info" class="comment-info"><span class="comment-age">(29 May '11, 23:32)</span> <span class="comment-user userinfo">sagu072</span></div></div></div><div id="comment-tools-4220" class="comment-tools"></div><div class="clear"></div><div id="comment-4220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

