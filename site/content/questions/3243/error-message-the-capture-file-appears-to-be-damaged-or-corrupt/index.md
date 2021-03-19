+++
type = "question"
title = "Error message: The capture file appears to be damaged or corrupt"
description = '''I have tried both versions of Wireshark (1.2.15 and 1.4.4). I have installed the 32 bit version on a Windows XP PC running service pack3 and the 64 bit version on a Windows 7 PC (running Windows 7 Enterprise with service pack 1). I have a snoop capture file from a SUN 35220 machine running Solaris 1...'''
date = "2011-03-31T07:40:00Z"
lastmod = "2017-10-27T13:45:00Z"
weight = 3243
keywords = [ "corrupt", "damaged" ]
aliases = [ "/questions/3243" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Error message: The capture file appears to be damaged or corrupt](/questions/3243/error-message-the-capture-file-appears-to-be-damaged-or-corrupt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3243-score" class="post-score" title="current number of votes">0</div><span id="post-3243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried both versions of Wireshark (1.2.15 and 1.4.4). I have installed the 32 bit version on a Windows XP PC running service pack3 and the 64 bit version on a Windows 7 PC (running Windows 7 Enterprise with service pack 1). I have a snoop capture file from a SUN 35220 machine running Solaris 10. If I open the capture file on the XP machine using Wireshark it opens correctly and displays the data correctly (it is primarily SCTP/M3ua). If I open the same capture file on the Windows 7 machine the wireshark loads 4 packets and puts up a message box with the following message: The capture file appears to be damaged or corrupt. (snoop: File has 1174405120-byte packet, bigger than maximum of 65535)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-corrupt" rel="tag" title="see questions tagged &#39;corrupt&#39;">corrupt</span> <span class="post-tag tag-link-damaged" rel="tag" title="see questions tagged &#39;damaged&#39;">damaged</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '11, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/fe95833133c89ad4320497019f3c1f5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="britdave&#39;s gravatar image" /><p><span>britdave</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="britdave has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Mar '11, 15:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-3243" class="comments-container"></div><div id="comment-tools-3243" class="comment-tools"></div><div class="clear"></div><div id="comment-3243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3244"></span>

<div id="answer-container-3244" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3244-score" class="post-score" title="current number of votes">3</div><span id="post-3244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, please check whether the snoop file on the XP system is <strong>exactly</strong> the same as on the Win7 box (you can do a MD5 checksum). The most common source of these errors is when the file is transferred by FTP in ASCII mode.</p><p>If the files are the same, please make sure you use the same version of Wireshark on both systems, there might be a problem in one of the Wireshark versions (either already solved or recently introduced).</p><p>If there is still a difference between the two systems, please check your preferences whether there is a difference there. Ideally you would delete all preferences on both systems to start with all default settings.</p><p>If the problem still exists on Win7 (or now exist on both systems), please open a bug report on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and attach the tracefile so that the problem can be investigated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '11, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3244" class="comments-container"><span id="3245"></span><div id="comment-3245" class="comment"><div id="post-3245-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick response. I thought I had checked everything. I have a new FTP program and used it to transfer the files to the Windows 7 machine. I deleted the files and used the command line FTP on the Windows 7 pc with the bin switch set.I can now open the file in wireshark. Again, thanks for the timely response.</p></div><div id="comment-3245-info" class="comment-info"><span class="comment-age">(31 Mar '11, 08:07)</span> <span class="comment-user userinfo">britdave</span></div></div><span id="7505"></span><div id="comment-7505" class="comment"><div id="post-7505-score" class="comment-score"></div><div class="comment-text"><p>I have run into this error message consistently when trying to view capture files recorded on a linux system with tcpdump. In this specific case the linux box is a VM within OpenVZ.</p><p>I had taken these steps to confirm the file wasn't corrupt: -verified it was entirely readable using tcpdump on 3 different systems: the original linux machine, another physical linux machine, and my mac os 10.7 -re-transferred using usb stick, and verified file sizes</p><p>I have observed the same bug when using wireshark on all 3 machines: windows, mac os 10.7, and on ubuntu. Sorry, didn't grab the versions of wireshark on all 3, but I believe they were all very recent (post 1.6)</p><p>Bug? Thanks, Shawn</p></div><div id="comment-7505-info" class="comment-info"><span class="comment-age">(18 Nov '11, 09:25)</span> <span class="comment-user userinfo">shawncarroll</span></div></div><span id="7507"></span><div id="comment-7507" class="comment"><div id="post-7507-score" class="comment-score"></div><div class="comment-text"><p>Shawn, your problem is probably a completely different problem, as you transferred your file between UN*X boxes and didn't transfer it with FTP. I'd suggest <a href="https://bugs.wireshark.org/bugzilla/">filing a bug</a>, giving the exact error message (including the size numbers), and attaching the capture file.</p></div><div id="comment-7507-info" class="comment-info"><span class="comment-age">(18 Nov '11, 10:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="64307"></span><div id="comment-64307" class="comment"><div id="post-64307-score" class="comment-score"></div><div class="comment-text"><p>I'd like to second SYN-bit's answer. I encountered the same error as the OP, in my case after transferring a packet capture from a Check Point firewall to a TFTP server. Apparently the default TFTP mode on the firewall is ASCII, but when I manually changed it to binary, I was then able to view the capture in Wireshark.</p></div><div id="comment-64307-info" class="comment-info"><span class="comment-age">(27 Oct '17, 13:45)</span> <span class="comment-user userinfo">eldaar</span></div></div></div><div id="comment-tools-3244" class="comment-tools"></div><div class="clear"></div><div id="comment-3244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10698"></span>

<div id="answer-container-10698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10698-score" class="post-score" title="current number of votes">0</div><span id="post-10698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might use <a href="http://f00l.de/pcapfix/">pcapfix</a> which trys to repair the corrupted packets to make your file readable with wireshark again. But I think the cause of your issue will stay the same... any bug or transfer problem. Maybe the output of the tool and kind of corruption will help you identifying a possible reason for the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '12, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/3bd81edc96c5877d644377567c344e6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="creeq&#39;s gravatar image" /><p><span>creeq</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="creeq has no accepted answers">0%</span></p></div></div><div id="comments-container-10698" class="comments-container"></div><div id="comment-tools-10698" class="comment-tools"></div><div class="clear"></div><div id="comment-10698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

