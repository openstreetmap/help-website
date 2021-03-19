+++
type = "question"
title = "how to: launch network sniffer application for asdm on mac"
description = '''I use use the Cisco ASDM firewall management software on my mac quite a lot and all is good. I also use Wireshark to review pcap files exported from Firewalls and routers. Under Windows ( :-( ) i could launch the wireshark app directly from using the packet capture wizard. this is set up under &#x27;Pref...'''
date = "2013-08-27T08:34:00Z"
lastmod = "2013-10-15T17:45:00Z"
weight = 24100
keywords = [ "macosx", "x11", "launch", "capture", "wireshark" ]
aliases = [ "/questions/24100" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to: launch network sniffer application for asdm on mac](/questions/24100/how-to-launch-network-sniffer-application-for-asdm-on-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24100-score" class="post-score" title="current number of votes">0</div><span id="post-24100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use use the Cisco ASDM firewall management software on my mac quite a lot and all is good. I also use Wireshark to review pcap files exported from Firewalls and routers.</p><p>Under Windows ( :-( ) i could launch the wireshark app directly from using the packet capture wizard.</p><p>this is set up under 'Preferences' then pointing to the application. it seems a little different on the mac - simply point to wireshark.app doesnt launch the app whatsoever.</p><p>i managed to get the ASDM to launch the app by pointing to the following directory (where i have wireshark located): /Applications/Network Apps/Wireshark.app/Contents/MacOS/Wireshark</p><p>but this merely launch the app and fails to pull the live data (Capture) from within the ASDM.</p><p>hope someone can make sense of this post and assist.</p><p>Many thanks Lee</p><p>i am running the following:</p><p>OS X 10.8.4</p><p>Java 1.6.0_51</p><p>ASDM Launcher version 1.6(64)</p><p>Version 1.10.1 (SVN Rev 50926 from /trunk-1.10)</p><p>XQuartz 2.7.4 (xorg-server 1.13.0)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-x11" rel="tag" title="see questions tagged &#39;x11&#39;">x11</span> <span class="post-tag tag-link-launch" rel="tag" title="see questions tagged &#39;launch&#39;">launch</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '13, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/1c1d1ffd36fe7bb1a4244afc594d14f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leekendrick&#39;s gravatar image" /><p><span>leekendrick</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leekendrick has no accepted answers">0%</span></p></div></div><div id="comments-container-24100" class="comments-container"></div><div id="comment-tools-24100" class="comment-tools"></div><div class="clear"></div><div id="comment-24100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24110"></span>

<div id="answer-container-24110" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24110-score" class="post-score" title="current number of votes">0</div><span id="post-24110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you have a capture file corresponding to a capture that's completed (i.e., <em>not</em> a live capture that's in progress), you could try opening it using the <code>open</code> command, if the capture wizard will let you do that; see <a href="https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/open.1.html">the man page for it</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '13, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '13, 10:51</strong> </span></p></div></div><div id="comments-container-24110" class="comments-container"></div><div id="comment-tools-24110" class="comment-tools"></div><div class="clear"></div><div id="comment-24110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25948"></span>

<div id="answer-container-25948" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25948-score" class="post-score" title="current number of votes">0</div><span id="post-25948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I moved from a Linux environment to Mac. This was really the only remaining issue I had with Mac although there are some fundamental issues that I know that they will not fix. I went to the prompt and typed</p><p>which wireshark</p><p>and it gave me this path.<br />
</p><p>/usr/local/bin/wireshark</p><p>I added it to my Tools --&gt; Preferences section on ASDM and I was off to the races.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '13, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/e89cb08fd00a5b34449c1664f309bf31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manny%20Fernandez&#39;s gravatar image" /><p><span>Manny Fernandez</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manny Fernandez has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-25948" class="comments-container"><span id="25989"></span><div id="comment-25989" class="comment"><div id="post-25989-score" class="comment-score"></div><div class="comment-text"><p>Hi Manny,</p><p>Many thanks for your reply, I am still unable to 'launch network sniffer appication' from the ASDM. I get the following error after following your steps:</p><p>/usr/local/bin/wireshark does not exist. Would you like to open the preferences dialog in order to specify the network sniffer application to use?</p><p>here is the output from which wireshark:</p><p>sh-3.2# which wireshark</p><p>/usr/local/bin/wireshark</p><p>sh-3.2# pwd</p><p>/usr/local/bin</p><p>sh-3.2# ls -l</p><p>total 104</p><p>lrwxr-xr-x 1 root wheel 48 5 Aug 22:00 bbdiff -&gt; /Applications/BBEdit.app/Contents/Helpers/bbdiff</p><p>lrwxr-xr-x 1 root wheel 53 5 Aug 22:00 bbedit -&gt; /Applications/BBEdit.app/Contents/Helpers/bbedit_tool</p><p>lrwxr-xr-x 1 root wheel 48 5 Aug 22:00 bbfind -&gt; /Applications/BBEdit.app/Contents/Helpers/bbfind</p><p>lrwxr-xr-x 1 root wheel 11 2 Aug 23:06 capinfos -&gt; ./wireshark</p><p>lrwxr-xr-x 1 root wheel 11 2 Aug 23:06 dftest -&gt; ./wireshark</p><p>lrwxr-xr-x 1 root wheel 11 2 Aug 23:06 dumpcap -&gt; ./wireshark</p><p>lrwxr-xr-x 1 root wheel 11 2 Aug 23:06 editcap -&gt; ./wireshark</p><p>lrwxr-xr-x 1 root wheel 11 2 Aug 23:06 mergecap -&gt; ./wireshark</p><p>lrwxr-xr-x 1 root wheel 11 2 Aug 23:06 randpkt -&gt; ./wireshark</p><p>lrwxr-xr-x 1 root wheel 11 2 Aug 23:06 rawshark -&gt; ./wireshark</p><p>lrwxr-xr-x 1 root wheel 11 2 Aug 23:06 text2pcap -&gt; ./wireshark</p><p>lrwxr-xr-x 1 root wheel 11 2 Aug 23:06 tshark -&gt; ./wireshark</p><p>-rwxr-xr-x 1 504 staff 482 16 Jul 18:19 wireshark</p><p>sh-3.2#</p><p>hope you help.</p><p>KR Lee</p></div><div id="comment-25989-info" class="comment-info"><span class="comment-age">(15 Oct '13, 01:35)</span> <span class="comment-user userinfo">leekendrick</span></div></div><span id="26030"></span><div id="comment-26030" class="comment"><div id="post-26030-score" class="comment-score"></div><div class="comment-text"><blockquote><p>/usr/local/bin/wireshark does not exist</p></blockquote><p>Well, it <em>does</em> exist, as per your "ls" output, so ASDM is not telling the truth.</p><p>Perhaps it's just too lazy to report the error as "I was not able to run /usr/local/bin/wireshark".</p><p>What happens if you type <code>/usr/local/bin/wireshark</code> from the command line?</p></div><div id="comment-26030-info" class="comment-info"><span class="comment-age">(15 Oct '13, 17:02)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="26034"></span><div id="comment-26034" class="comment"><div id="post-26034-score" class="comment-score"></div><div class="comment-text"><p>From your output, it looks like you did it after a 'sudo su'. when I ran mine, it was from under my user account 'Mannys-MacBook-Pro:~ MyUserName$'</p><p>As guy pointed out, the output does in fact show that you have it and that the OS will launch from that location. I will look at mine again and get right back.</p></div><div id="comment-26034-info" class="comment-info"><span class="comment-age">(15 Oct '13, 17:45)</span> <span class="comment-user userinfo">Manny Fernandez</span></div></div></div><div id="comment-tools-25948" class="comment-tools"></div><div class="clear"></div><div id="comment-25948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

