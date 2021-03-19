+++
type = "question"
title = "capture file appears to be damaged or corrupt"
description = '''The capture file appears to be damaged or corrupt. (pcap: File has 65706-byte packet, bigger than the maximum of 65535) Hello,  I am having an issue when trying to debug some voip calls. I capture the errors but the wireshark file is always corrupt with the error at the top of my post.  I have tried...'''
date = "2012-02-09T07:16:00Z"
lastmod = "2014-09-12T13:22:00Z"
weight = 8931
keywords = [ "corrupt", "capture", "file" ]
aliases = [ "/questions/8931" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [capture file appears to be damaged or corrupt](/questions/8931/capture-file-appears-to-be-damaged-or-corrupt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8931-score" class="post-score" title="current number of votes">0</div><span id="post-8931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The capture file appears to be damaged or corrupt. (pcap: File has 65706-byte packet, bigger than the maximum of 65535)</p><p>Hello, I am having an issue when trying to debug some voip calls. I capture the errors but the wireshark file is always corrupt with the error at the top of my post. I have tried using the wireshark GUI and also dumpcap using the following string</p><pre><code>C:\Program Files\Wireshark&gt;dumpcap -b filesize:50000 -wdebug.pcap</code></pre><p>All files that i create are corrupt, even if I set dumpcap to create only a 5mb file this shows as corrupt. I have tried using Wireshark version 1.6.4 and 1.6.5.</p><p>The operating system is Windows 2008 64 bit R2 on VMWare. UAC and Windows Firewall are turned off</p><p>has anyone ever seen this issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-corrupt" rel="tag" title="see questions tagged &#39;corrupt&#39;">corrupt</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '12, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/2dba8b330a87511b68957e6ff5b4c5d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="processflows%20support&#39;s gravatar image" /><p><span>processflows...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="processflows support has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Feb '12, 07:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-8931" class="comments-container"></div><div id="comment-tools-8931" class="comment-tools"></div><div class="clear"></div><div id="comment-8931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="8938"></span>

<div id="answer-container-8938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8938-score" class="post-score" title="current number of votes">2</div><span id="post-8938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you capture the packets on the same system as where you are trying to view them in Wireshark? If not, how did you transfer the file from the capturing system to the Wireshark PC?</p><p>Most times I have seen this message, the files were transferred by FTP, but in ASCII mode instead of BINARY mode. This will mangle the file (as different systems use different line endings and FTP in ASCII mode tries to change byte sequences that look like line-endings).</p><p>So if you did transfer the file with FTP, please enable BINARY mode before sending the file over.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '12, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-8938" class="comments-container"></div><div id="comment-tools-8938" class="comment-tools"></div><div class="clear"></div><div id="comment-8938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8937"></span>

<div id="answer-container-8937" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8937-score" class="post-score" title="current number of votes">0</div><span id="post-8937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems like you might have a version of libpcap (winpcap) that has been modified. You should not see captured packets longer than 65535 bytes. <strong>Try reinstalling winpcap.</strong></p><p>Alternatively, if you have an intentionally modified version of winpcap (perhaps one that supports larger packets), you'll need to adjust the following:</p><p><code>wiretap/libpcap.c</code>, lines 756-771:</p><pre><code>if (hdr-&gt;hdr.incl_len &gt; WTAP_MAX_PACKET_SIZE) {
    /*
     * Probably a corrupt capture file; return an error,
     * so that our caller doesn&#39;t blow up trying to allocate
     * space for an immensely-large packet, and so that
     * the code to try to guess what type of libpcap file
     * this is can tell when it&#39;s not the type we&#39;re guessing
     * it is.
     */
    *err = WTAP_ERR_BAD_FILE;
    if (err_info != NULL) {
        *err_info = g_strdup_printf(&quot;pcap: File has %u-byte packet, bigger than maximum of %u&quot;,
            hdr-&gt;hdr.incl_len, WTAP_MAX_PACKET_SIZE);
    }
    return -1;
}</code></pre><p>and <code>wiretap/wtap.h</code> lines 308-313:</p><pre><code>/*
 * Maximum packet size we&#39;ll support.
 * 65535 is the largest snapshot length that libpcap supports, so we
 * use that.
 */
#define WTAP_MAX_PACKET_SIZE            65535</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '12, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8937" class="comments-container"><span id="8974"></span><div id="comment-8974" class="comment"><div id="post-8974-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the replies, I will get them to uninstall Winpcap. We have uninstalled and reinstalled wireshark but I am wondering if that also fully uninstalled/reinstalled winpcap at the same time. So I will uninstall Winpcap first, then wireshark, do a reboot and then reinstall from a fresh download. all software is direct download from the website with no modifications.</p><p>I dont think its the FTP issue as the files on the machine itself also seem to be corrupt. I did consider unusual partitioning on the server but it seems to be standard NTFS.</p></div><div id="comment-8974-info" class="comment-info"><span class="comment-age">(13 Feb '12, 02:57)</span> <span class="comment-user userinfo">processflows...</span></div></div><span id="8981"></span><div id="comment-8981" class="comment"><div id="post-8981-score" class="comment-score"></div><div class="comment-text"><p>Make sure your installer isn't getting corrupted during the download. It's unlikely, but you should probably do the verification anyway, given the nature of your problem. The 1.6.5 signature is available in the <a href="http://www.wireshark.org/download/SIGNATURES-1.6.5.txt">signatures file</a>. The latest signatures file can always be found on the <a href="http://www.wireshark.org/download.html">downloads page</a>.</p></div><div id="comment-8981-info" class="comment-info"><span class="comment-age">(13 Feb '12, 12:59)</span> <span class="comment-user userinfo">multipleinte...</span></div></div></div><div id="comment-tools-8937" class="comment-tools"></div><div class="clear"></div><div id="comment-8937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36213"></span>

<div id="answer-container-36213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36213-score" class="post-score" title="current number of votes">0</div><span id="post-36213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Updating to the latest version 1.12 (at the moment) resolved the issue for me</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '14, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/09742558cc65d1bab3368c15298fc229?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tesla&#39;s gravatar image" /><p><span>Tesla</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tesla has no accepted answers">0%</span></p></div></div><div id="comments-container-36213" class="comments-container"><span id="36290"></span><div id="comment-36290" class="comment"><div id="post-36290-score" class="comment-score"></div><div class="comment-text"><p>Perhaps Windows was doing TCP segmentation offloading, and delivered packets that actually were reassembled from multiple network packets and that were larger than 65535 bytes. 1.12 increased the maximum packet size to 262144 bytes, and thus didn't complain about those larger packets.</p></div><div id="comment-36290-info" class="comment-info"><span class="comment-age">(12 Sep '14, 13:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-36213" class="comment-tools"></div><div class="clear"></div><div id="comment-36213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

