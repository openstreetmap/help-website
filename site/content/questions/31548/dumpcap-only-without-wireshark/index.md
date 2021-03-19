+++
type = "question"
title = "dumpcap only, without wireshark?"
description = '''Hi, I&#x27;m using a single command with dumpcap to trace the network between two host. This command is used in a batch file on Windows and I would like the whole thing to be the smallest possible. I&#x27;m currently using PortableWireshark which is about 56MB. Is there a way to make this even smaller?  I jus...'''
date = "2014-04-05T07:01:00Z"
lastmod = "2014-04-06T15:02:00Z"
weight = 31548
keywords = [ "dumpcap", "portable" ]
aliases = [ "/questions/31548" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [dumpcap only, without wireshark?](/questions/31548/dumpcap-only-without-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31548-score" class="post-score" title="current number of votes">0</div><span id="post-31548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm using a single command with dumpcap to trace the network between two host. This command is used in a batch file on Windows and I would like the whole thing to be the smallest possible. I'm currently using PortableWireshark which is about 56MB. Is there a way to make this even smaller? I just need the package for dumpcap command line and install of WinPcap.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-portable" rel="tag" title="see questions tagged &#39;portable&#39;">portable</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '14, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/fd56717733f15e776ee340e6acbe830f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Javo&#39;s gravatar image" /><p><span>Javo</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Javo has no accepted answers">0%</span></p></div></div><div id="comments-container-31548" class="comments-container"></div><div id="comment-tools-31548" class="comment-tools"></div><div class="clear"></div><div id="comment-31548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31550"></span>

<div id="answer-container-31550" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31550-score" class="post-score" title="current number of votes">1</div><span id="post-31550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Javo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I can tell (by running Process Explorer to see the DLLs used by dumpcap.exe while running) it needs the following DLLs from the Wireshark installation directory:</p><ul><li>libgcrypt-11.dll</li><li>libglib-2-0-0.dll</li><li>libgmodule-2.0-0.dll</li><li>libgpg-error-0.dll</li><li>libintl-8.dll</li><li>libwsutil.dll</li></ul><p>So I guess if you bundle them with dumpcap.exe and a WinPcap installer you should be good to go. I didn't test this myself, though, but I'm pretty sure you can take over from here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '14, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31550" class="comments-container"><span id="31566"></span><div id="comment-31566" class="comment"><div id="post-31566-score" class="comment-score"></div><div class="comment-text"><p>it works like a charm! thanks</p></div><div id="comment-31566-info" class="comment-info"><span class="comment-age">(06 Apr '14, 06:31)</span> <span class="comment-user userinfo">Javo</span></div></div></div><div id="comment-tools-31550" class="comment-tools"></div><div class="clear"></div><div id="comment-31550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31552"></span>

<div id="answer-container-31552" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31552-score" class="post-score" title="current number of votes">0</div><span id="post-31552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you just need a 'low profile' capture tool, <strong><a href="http://www.winpcap.org/windump/install/default.htm">windump</a></strong> is what you should use. You will just need WinPcap and a single windump binary (0.5 Mbyte).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '14, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31552" class="comments-container"><span id="31554"></span><div id="comment-31554" class="comment"><div id="post-31554-score" class="comment-score"></div><div class="comment-text"><p>Not sure, but I don't think windump is able to write the pcap-ng file format, which would make it inferior to dumpcap. I would always recommend to avoid the pcap file format wherever possible.</p></div><div id="comment-31554-info" class="comment-info"><span class="comment-age">(05 Apr '14, 14:14)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="31555"></span><div id="comment-31555" class="comment"><div id="post-31555-score" class="comment-score"></div><div class="comment-text"><p>Neither tcpdump (except on later versions of OS X) nor WinDump can currently write pcap-ng files.</p><p>However, if you're only capturing on one interface, the advantages of pcap-ng over pcap for <em>capturing</em> are somewhat limited, and, if you want to use capabilities such as annotating captures, you can read a pcap file into Wireshark, annotate packets, and then write the capture out as a pcap-ng file.</p><p>So I wouldn't recommend avoiding pcap whenever possible; I'd only recommend avoiding it if you need one or more of pcap-ng's capabilities in the particular use case. If the feature isn't needed, or isn't available, when capturing (dumpcap doesn't, for example, write out per-packet comments), there's no need to avoid pcap format when capturing.</p></div><div id="comment-31555-info" class="comment-info"><span class="comment-age">(05 Apr '14, 14:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="31567"></span><div id="comment-31567" class="comment"><div id="post-31567-score" class="comment-score"></div><div class="comment-text"><p>Why use pcap if pcap-ng is available? Makes little sense to me going for the weaker option... :-)</p><p>I'm not trying to start a war here (we have way too many of those already ;-)), but my rule of thumb is to always use the capture format that preserves the most information from the time of the capture, and pcap should not be that format unless using very outdated capture software.</p></div><div id="comment-31567-info" class="comment-info"><span class="comment-age">(06 Apr '14, 09:01)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="31568"></span><div id="comment-31568" class="comment"><div id="post-31568-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Why use pcap if pcap-ng is available?</p></blockquote><p>If the program that drops fewer packets supports only pcap? Currently, in at least one test on Linux, tcpdump dropped fewer packets than dumpcap, and I suspect the problem isn't Linux-specific. Yes, we should fix that, but, for now....</p><p>In addition, just because pcap-ng <em>can</em> save more information, that doesn't mean it <em>does</em> save more information when you use some particular version of some particular capture program.</p></div><div id="comment-31568-info" class="comment-info"><span class="comment-age">(06 Apr '14, 10:19)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="31577"></span><div id="comment-31577" class="comment"><div id="post-31577-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Not sure, but I don't think windump is able to write the pcap-ng file format,</p></blockquote><p>No, it does not. But the OP requested a method to <strong>minimize the size</strong> of the capture tool footprint. In that respect, it's hard to beat windump ;-) He/she did not mention support for pcap-ng.</p><blockquote><p>I would always recommend to avoid the pcap file format wherever possible.</p></blockquote><p>Hm.. honestly, in the last couple of years I have had <strong>very</strong> few situations where pcap-ng was really needed or helpful. For the 'typical' network troubleshooting situation (I guess 98-99%), pcap-ng does not offer any additional value.</p><p>Don't get me wrong, it's nice to have the additional information about the OS, interfaces, comments and everything else but nothing of these are vital to analyze the problem hidden in the capture file nor do they speed up things.</p></div><div id="comment-31577-info" class="comment-info"><span class="comment-age">(06 Apr '14, 15:02)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-31552" class="comment-tools"></div><div class="clear"></div><div id="comment-31552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

