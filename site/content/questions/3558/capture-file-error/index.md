+++
type = "question"
title = "Capture file error"
description = '''Wireshark Virtual machine capture seems to be corrupt.  I&#x27;m trying to debug a performance isse and keep recieved the following error. &quot;The capture file appears to be damaged or corrupt. (pcap: file has 65590-byte packet, bigger than the maximum of 65535&quot;. Even though wireshark says the capture is co...'''
date = "2011-04-18T06:52:00Z"
lastmod = "2011-04-19T05:10:00Z"
weight = 3558
keywords = [ "pcap", "error" ]
aliases = [ "/questions/3558" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture file error](/questions/3558/capture-file-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3558-score" class="post-score" title="current number of votes">0</div><span id="post-3558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark Virtual machine capture seems to be corrupt. I'm trying to debug a performance isse and keep recieved the following error. "The capture file appears to be damaged or corrupt. (pcap: file has 65590-byte packet, bigger than the maximum of 65535". Even though wireshark says the capture is correct, the system appears to be functioning propoerly, i.e it is transferring data to a backup server. The wireshark version is 1.4.5. Can anybody point out what I might be doing wrong? I'm capturing in promiscuous mode with a buffer size of 2 megabytes with update list in real time not selected.Tthe system running Wireshark is using a VMware vmxnet3 netowrk device.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/f8f8258bb589f84d3d95b8dced6c902f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jadechen&#39;s gravatar image" /><p><span>jadechen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jadechen has no accepted answers">0%</span></p></div></div><div id="comments-container-3558" class="comments-container"><span id="3564"></span><div id="comment-3564" class="comment"><div id="post-3564-score" class="comment-score"></div><div class="comment-text"><p>My system is a 64 bit version of Windows R2 sp1 and I tried the "old Stable release 1.2.16" and still got the same wireshark crash. Any other suggestions would be appreciated. I'm trying to debug a backup applcations from a VM to a Physical system where the windows size always is in the 500 byte range (so it's ver slow), but in all my traces I never see the TCP options fields either set Sel Acks, or Windows scaling.</p></div><div id="comment-3564-info" class="comment-info"><span class="comment-age">(18 Apr '11, 07:34)</span> <span class="comment-user userinfo">jadechen</span></div></div><span id="3567"></span><div id="comment-3567" class="comment"><div id="post-3567-score" class="comment-score"></div><div class="comment-text"><p>Can you provide the capture via a bug report?</p><p>See Help ! About Wireshark ! Folders to see the directory in which the capture files are stored.</p><p>Or alternatively: use dumpcap to do the capture (using -w to specify the output file). (I'm presuming that an error will be reported when Wireshark or capinfos tries to read that file).</p></div><div id="comment-3567-info" class="comment-info"><span class="comment-age">(18 Apr '11, 07:46)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="3569"></span><div id="comment-3569" class="comment"><div id="post-3569-score" class="comment-score"></div><div class="comment-text"><p>Trying to figure out how to add a bug. I think I have the capture file called wiresharkXXXXa00800. I looked through the current bug list and didn't see anything that looked familiar.</p></div><div id="comment-3569-info" class="comment-info"><span class="comment-age">(18 Apr '11, 08:45)</span> <span class="comment-user userinfo">jadechen</span></div></div></div><div id="comment-tools-3558" class="comment-tools"></div><div class="clear"></div><div id="comment-3558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3559"></span>

<div id="answer-container-3559" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3559-score" class="post-score" title="current number of votes">0</div><span id="post-3559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's a significant problem with the most recent Wireshark 1.4.5 release.</p><p>See: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5837">Bug 5837</a></p><p>Altho your problem sounds like something different, please try using Wireshark 1.4.4 to see if the problem still persists.</p><p>(Windows 32-bit Wireshark 1.4.4 can be downloaded @ <a href="http://www.wireshark.org/download/win32/">Windows Wireshark 32 bit 1.4.4</a>)</p><p>If the problem persists with Wireshark 1.4.4, please file a bug report @ bugs.wireshark.org attaching a (short) capture file showing the problem.</p><p>If necessary, the attachment can be marked private so only the Wireshark core developers will have access.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '11, 07:24</strong> </span></p></div></div><div id="comments-container-3559" class="comments-container"></div><div id="comment-tools-3559" class="comment-tools"></div><div class="clear"></div><div id="comment-3559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3588"></span>

<div id="answer-container-3588" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3588-score" class="post-score" title="current number of votes">0</div><span id="post-3588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you transferring the file by FTP from the system on which you created it to a system on which you want to view it in Wireshark? If so, please make sure you use binary mode, otherwise some magic is done on what FTP believe are line endings, but is in fact just binary data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3588" class="comments-container"><span id="3603"></span><div id="comment-3603" class="comment"><div id="post-3603-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately I wasn't using ftp. the Crash occurs during collection. I turned update in real time and tried various buffer sizes. During a capture, I see the capture hand, i.e. stop collecting packets. When I the stop the capture I get the message about the 65590 to big error.</p><p>I've tried to enter a bug report but the process in not intuitively obvious to the casual observer. The system rejects what I put something in hte "named tag" field or when I hit commit on bugzilla.</p><p>Today, I'm going to collect with a fluke and try to use wireshark for the analysis.</p></div><div id="comment-3603-info" class="comment-info"><span class="comment-age">(19 Apr '11, 04:33)</span> <span class="comment-user userinfo">jadechen</span></div></div><span id="3604"></span><div id="comment-3604" class="comment"><div id="post-3604-score" class="comment-score"></div><div class="comment-text"><p>Can you give some more details on your capture setup? Is the Wireshark VM the one receiving/transmitting production traffic as well, or did you set up a dedicated capture VM that captures traffic of the production VM? I suspect you might have large send offload trouble if you are in fact capturing on the same machine that sends/receives the production traffic. I could verify this if I know your capture scenario a little better.</p></div><div id="comment-3604-info" class="comment-info"><span class="comment-age">(19 Apr '11, 05:10)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-3588" class="comment-tools"></div><div class="clear"></div><div id="comment-3588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

