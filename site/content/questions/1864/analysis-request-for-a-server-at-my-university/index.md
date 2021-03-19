+++
type = "question"
title = "Analysis request - for a server at my University"
description = '''Hello I have many TCP retransmission errors (over 230 during 46 seconds) on a FTP transfer between my home laptop and a remote FTP server at my University and this issue is going for months without being able to find the cause. On any other server, FTP transfer is going strong, so it is not on my la...'''
date = "2011-01-21T13:50:00Z"
lastmod = "2011-01-25T03:09:00Z"
weight = 1864
keywords = [ "ftp", "retransmissions", "analysis" ]
aliases = [ "/questions/1864" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Analysis request - for a server at my University](/questions/1864/analysis-request-for-a-server-at-my-university)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1864-score" class="post-score" title="current number of votes">0</div><span id="post-1864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I have many TCP retransmission errors (over <strong>230</strong> during 46 seconds) on a FTP transfer between my home laptop and a remote FTP server at my University and this issue is going for months without being able to find the cause. On any other server, FTP transfer is going strong, so it is not on my laptop side.</p><p>I captured a 15 MB file in .cap format showing what I just described and maybe more. But I am not an expert in packets analysis and I don't know what to do next. That is why I am asking for your help.</p><p>If you agree to help, please tell me where to upload the captured file and if there is more info needed, I will try to do my best to answer.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '11, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/56983276cbf323b8225333d615cc96dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="masster64&#39;s gravatar image" /><p><span>masster64</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="masster64 has no accepted answers">0%</span></p></div></div><div id="comments-container-1864" class="comments-container"><span id="1868"></span><div id="comment-1868" class="comment"><div id="post-1868-score" class="comment-score"></div><div class="comment-text"><p>If you see a lot of retrans, it's probably a duplex mismatch on that server. You should ask the ops guys to make sure the duplex settings match. (especially if ftp to other servers are consistently good). IT can be due to small tcp window size, but trace file would be required to analyze it. You can always use box.net to host the files. don't forget to chop it to headers using editcap (editcap -s 96 orig_file.pcap new_file.pcap)</p></div><div id="comment-1868-info" class="comment-info"><span class="comment-age">(21 Jan '11, 20:58)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="1899"></span><div id="comment-1899" class="comment"><div id="post-1899-score" class="comment-score"></div><div class="comment-text"><p>I guess you're right about small TCP window. here is what TCP parameters are on server now:</p><p>« SpeedGuide.net TCP Analyzer Results » Tested on: 01.23.2011 18:12 IP address: 141.85.xxx.xx Client OS: Linux Ubuntu</p><p>TCP options string: 020405b40101040201030307 MSS: 1460 MTU: 1500 TCP Window: 5888 (NOT multiple of MSS) RWIN Scaling: 7 bits (2^7=128) Unscaled RWIN : 46 Recommended RWINs: 64240, 128480, 256960, 513920, 1027840 BDP limit (200ms): 236kbps (29KBytes/s) BDP limit (500ms): 94kbps (12KBytes/s) MTU Discovery: ON TTL: 47 Timestamps: OFF SACKs: ON IP ToS: 00000000 (0)</p></div><div id="comment-1899-info" class="comment-info"><span class="comment-age">(23 Jan '11, 15:18)</span> <span class="comment-user userinfo">masster64</span></div></div><span id="1900"></span><div id="comment-1900" class="comment"><div id="post-1900-score" class="comment-score"></div><div class="comment-text"><p>TCP Window: 5888 (NOT multiple of MSS) is waaaay too low for a 100Mbps external bandwith, right ?</p><p>1) Is there a software on Linux to calculate optimal TCP parameters ? Like SG TCP Optimizer on Win32 (http://www.speedguide.net/downloads.php)</p><p>2) Right now I put the following lines in sysctl.conf, issued a sysctl -p command, but nothing changed after reboot :(</p><p>net.core.rmem_default = 256960</p><p>net.core.rmem_max = 1027840</p><p>net.core.wmem_default = 256960</p><p>net.core.wmem_max = 1027840</p><p>net.ipv4.tcp_timestamps = 0</p><p>net.ipv4.tcp_sack = 1</p><p>net.ipv4.tcp_window_scaling = 1</p></div><div id="comment-1900-info" class="comment-info"><span class="comment-age">(23 Jan '11, 15:31)</span> <span class="comment-user userinfo">masster64</span></div></div></div><div id="comment-tools-1864" class="comment-tools"></div><div class="clear"></div><div id="comment-1864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1865"></span>

<div id="answer-container-1865" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1865-score" class="post-score" title="current number of votes">0</div><span id="post-1865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you send the file with <a href="http://www.yousendit.com">YouSendIt</a> or any other file transfer service to my mailbox (see my profile page for the address), I'm more than happy to have a look...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '11, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1865" class="comments-container"><span id="1874"></span><div id="comment-1874" class="comment"><div id="post-1874-score" class="comment-score"></div><div class="comment-text"><p>thank you. I've send it by mail, subject "Analysis file from Wireshark forum".</p></div><div id="comment-1874-info" class="comment-info"><span class="comment-age">(22 Jan '11, 03:48)</span> <span class="comment-user userinfo">masster64</span></div></div><span id="1875"></span><div id="comment-1875" class="comment"><div id="post-1875-score" class="comment-score"></div><div class="comment-text"><p>Converted your answer to a comment. See: http://ask.wireshark.org/questions/292/example-of-how-to-use-askwiresharkorg-and-how-not-to</p></div><div id="comment-1875-info" class="comment-info"><span class="comment-age">(22 Jan '11, 04:21)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="1876"></span><div id="comment-1876" class="comment"><div id="post-1876-score" class="comment-score"></div><div class="comment-text"><p>Hmmm... I did not receive the file yet, it might be too big for normal mail.</p></div><div id="comment-1876-info" class="comment-info"><span class="comment-age">(22 Jan '11, 04:36)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="1877"></span><div id="comment-1877" class="comment"><div id="post-1877-score" class="comment-score"></div><div class="comment-text"><p>I have just tested downloading a big file on server via HTTP. Same issue. So it is not FTP only related. [URL=http://img442.imageshack.us/i/upanddown.jpg/][IMG]http://img442.imageshack.us/img442/4324/upanddown.th.jpg[/IMG][/URL]</p></div><div id="comment-1877-info" class="comment-info"><span class="comment-age">(22 Jan '11, 04:41)</span> <span class="comment-user userinfo">masster64</span></div></div><span id="1878"></span><div id="comment-1878" class="comment"><div id="post-1878-score" class="comment-score"></div><div class="comment-text"><p>I upped it on Megaupload at http://www.megaupload.com/?d=XOLJ929N The above image is at http://img442.imageshack.us/img442/4324/upanddown.jpg</p></div><div id="comment-1878-info" class="comment-info"><span class="comment-age">(22 Jan '11, 04:50)</span> <span class="comment-user userinfo">masster64</span></div></div><span id="1915"></span><div id="comment-1915" class="comment not_top_scorer"><div id="post-1915-score" class="comment-score"></div><div class="comment-text"><p>did you get the file ok ?</p></div><div id="comment-1915-info" class="comment-info"><span class="comment-age">(25 Jan '11, 03:09)</span> <span class="comment-user userinfo">masster64</span></div></div></div><div id="comment-tools-1865" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-1865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

