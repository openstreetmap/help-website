+++
type = "question"
title = "No interfaces found by Wireshark 2.0 on El Capitan (OS X 10.11.2)"
description = '''I cannot get Wireshark to see network interfaces when I start it under El Capitan 10.11.2'''
date = "2016-01-18T15:56:00Z"
lastmod = "2016-01-22T06:26:00Z"
weight = 49340
keywords = [ "wireshark", "2.0", "elcapitan", "networkinterfaces" ]
aliases = [ "/questions/49340" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No interfaces found by Wireshark 2.0 on El Capitan (OS X 10.11.2)](/questions/49340/no-interfaces-found-by-wireshark-20-on-el-capitan-os-x-10112)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49340-score" class="post-score" title="current number of votes">1</div><span id="post-49340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I cannot get Wireshark to see network interfaces when I start it under El Capitan 10.11.2</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-2.0" rel="tag" title="see questions tagged &#39;2.0&#39;">2.0</span> <span class="post-tag tag-link-elcapitan" rel="tag" title="see questions tagged &#39;elcapitan&#39;">elcapitan</span> <span class="post-tag tag-link-networkinterfaces" rel="tag" title="see questions tagged &#39;networkinterfaces&#39;">networkinterfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '16, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/db34ddf09a756387a7928eb33dadb2fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boilermaker&#39;s gravatar image" /><p><span>Boilermaker</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boilermaker has no accepted answers">0%</span></p></div></div><div id="comments-container-49340" class="comments-container"><span id="49344"></span><div id="comment-49344" class="comment"><div id="post-49344-score" class="comment-score"></div><div class="comment-text"><p>What does the command <code>ls -l /dev/bpf*</code> print?</p></div><div id="comment-49344-info" class="comment-info"><span class="comment-age">(18 Jan '16, 19:03)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="49405"></span><div id="comment-49405" class="comment"><div id="post-49405-score" class="comment-score"></div><div class="comment-text"><p>I accidentally sent my response via email only. Here is what I found:</p><pre><code>bash-3.2# pwd
/dev
bash-3.2# ls -l bpf* print?
ls: print?: No such file or directory
crw-------  1 root  wheel   23,   0 Jan 14 23:18 bpf0
crw-------  1 root  wheel   23,   1 Jan 14 23:18 bpf1
crw-------  1 root  wheel   23,   2 Jan 19 05:38 bpf2
crw-------  1 root  wheel   23,   3 Jan 18 17:38 bpf3
crw-------  1 root  wheel   23,   4 Jan 14 23:18 bpf4
bash-3.2#</code></pre><p>What should the permissions be?</p></div><div id="comment-49405-info" class="comment-info"><span class="comment-age">(20 Jan '16, 08:51)</span> <span class="comment-user userinfo">Boilermaker</span></div></div></div><div id="comment-tools-49340" class="comment-tools"></div><div class="clear"></div><div id="comment-49340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49407"></span>

<div id="answer-container-49407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49407-score" class="post-score" title="current number of votes">1</div><span id="post-49407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I remember hearing concerns about possible security issues with this command, but after every reboot I type</p><p>sudo chmod 644 /dev/bpf*</p><p>I am then prompted for my admin password. After that, all interfaces appear in Wireshark...until the next reboot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '16, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/65f2bd527c8926a7afc27914aa2b6e67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MisterFalcon&#39;s gravatar image" /><p><span>MisterFalcon</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MisterFalcon has no accepted answers">0%</span></p></div></div><div id="comments-container-49407" class="comments-container"><span id="49436"></span><div id="comment-49436" class="comment"><div id="post-49436-score" class="comment-score"></div><div class="comment-text"><p>Yes that worked!! Thanks!!! Now the interfaces can be seen!</p><p>Here is what I did based on your suggestion:</p><pre><code>bash-3.2# ls -l bpf*
crw-------  1 root  wheel   23,   0 Jan 20 12:42 bpf0
crw-------  1 root  wheel   23,   1 Jan 20 12:42 bpf1
crw-------  1 root  wheel   23,   2 Jan 21 00:42 bpf2
crw-------  1 root  wheel   23,   3 Jan 20 12:42 bpf3
crw-------  1 root  wheel   23,   4 Jan 20 12:42 bpf4
crw-------  1 root  wheel   23,   5 Jan 20 12:42 bpf5
bash-3.2# chmod 644 bpf*
bash-3.2# ls -l bpf*
crw-r--r--  1 root  wheel   23,   0 Jan 20 12:42 bpf0
crw-r--r--  1 root  wheel   23,   1 Jan 20 12:42 bpf1
crw-r--r--  1 root  wheel   23,   2 Jan 21 00:42 bpf2
crw-r--r--  1 root  wheel   23,   3 Jan 20 12:42 bpf3
crw-r--r--  1 root  wheel   23,   4 Jan 20 12:42 bpf4
crw-r--r--  1 root  wheel   23,   5 Jan 20 12:42 bpf5
bash-3.2#</code></pre><p>I wish Apple would reverse their SIP policy and allow user to install legitimite devices and applications such as wireshark, without dancing around permissions</p></div><div id="comment-49436-info" class="comment-info"><span class="comment-age">(21 Jan '16, 10:17)</span> <span class="comment-user userinfo">Boilermaker</span></div></div><span id="49437"></span><div id="comment-49437" class="comment"><div id="post-49437-score" class="comment-score"></div><div class="comment-text"><p>I just installed Wireshark on an El Capitan 10.11.2 virtual machine, and, after installing Wireshark, there were a lot more BPF devices, they all had permission rw-rw----, and were owned by group access_bpf, all of which is as it's supposed to be.</p><p>This persists across a reboot.</p><p>Uninstalling Wireshark (complete with uninstalling the launchd service that sets the BPF permissions at boot time), updating to 10.11.3, and installing Wireshark had the same result.</p><p>SIP was turned on during the entire process, so it's not as if it's what's getting in the way.</p><p>What does the command <code>ls -l /Library/LaunchDaemons/</code> print on your machines?</p></div><div id="comment-49437-info" class="comment-info"><span class="comment-age">(21 Jan '16, 11:12)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="49451"></span><div id="comment-49451" class="comment"><div id="post-49451-score" class="comment-score"></div><div class="comment-text"><p>Mine shows 'org.wireshark.ChmodBPF.plist'.</p><p>But the therein referenced '/Library/Application Support/Wireshark' directory is owned by user:group '504:wheel' who is definitely not on this system?</p><p>Seems to work though, since after reboot I can have interfaces to capture from.</p></div><div id="comment-49451-info" class="comment-info"><span class="comment-age">(22 Jan '16, 04:35)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="49453"></span><div id="comment-49453" class="comment"><div id="post-49453-score" class="comment-score"></div><div class="comment-text"><p>On mine - El Capitan 10.11.2, both before and after entering the chmod 644 /dev/bpf* command I see</p><pre><code>$ ls -l /Library/LaunchDaemons/
total 48
-rw-r--r--  1 root  wheel  462 24 Apr  2014 com.adobe.fpsaud.plist
[email protected] 1 root  wheel  818 15 Dec 07:53 com.google.keystone.daemon.plist
-rw-r--r--  1 root  wheel  572 17 Nov 10:21 com.oracle.JavaInstallHelper.plist
lrwxr-xr-x  1 root  wheel  103 12 Nov  2014 com.oracle.java.Helper-Tool.plist -&gt; /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Resources/com.oracle.java.Helper-Tool.plist
-rw-r--r--  1 root  wheel  588  7 Sep 09:56 com.oracle.java.JavaUpdateHelper.plist
-rw-r--r--  1 root  wheel  670 16 Oct 04:48 org.macosforge.xquartz.privileged_startx.plist
$</code></pre><p>How does one completely uninstall wireshark and he launchd service as mentioned on OSX?</p></div><div id="comment-49453-info" class="comment-info"><span class="comment-age">(22 Jan '16, 06:26)</span> <span class="comment-user userinfo">MisterFalcon</span></div></div></div><div id="comment-tools-49407" class="comment-tools"></div><div class="clear"></div><div id="comment-49407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

