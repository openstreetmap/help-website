+++
type = "question"
title = "Wireless interface isn&#x27;t shown in Wireshark"
description = '''I&#x27;m trying to capture on my laptop (Linux) packets, that goes through the wireless card. Wireshark shoes only the capture interfaces: bluetooth0, randpkt and udpdump. wlan0 isn&#x27;t shown. I used this and it worked. But is there a way that mon0 (or wlan0) will appear in Wireshark and I can use it norma...'''
date = "2017-09-01T09:44:00Z"
lastmod = "2017-09-03T11:23:00Z"
weight = 63547
keywords = [ "wireless", "interface", "wireshark" ]
aliases = [ "/questions/63547" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireless interface isn't shown in Wireshark](/questions/63547/wireless-interface-isnt-shown-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63547-score" class="post-score" title="current number of votes">0</div><span id="post-63547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture on my laptop (Linux) packets, that goes through the wireless card. Wireshark shoes only the capture interfaces: bluetooth0, randpkt and udpdump. wlan0 isn't shown.</p><p>I used <a href="https://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version">this</a> and it worked. But is there a way that mon0 (or wlan0) will appear in Wireshark and I can use it normally and not having to do the "sudo tcpdump..." and then "wireshark -nr..." any time I want to capture?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '17, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/6f8c87647d8b6d05957166dbbf7029ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharp_pilot&#39;s gravatar image" /><p><span>sharp_pilot</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharp_pilot has no accepted answers">0%</span></p></div></div><div id="comments-container-63547" class="comments-container"><span id="63550"></span><div id="comment-63550" class="comment"><div id="post-63550-score" class="comment-score"></div><div class="comment-text"><p>1) What happens if you run tcpdump on mon0/wlan0 <em>without</em> sudo?</p><p>2) What Linux distribution is this?</p></div><div id="comment-63550-info" class="comment-info"><span class="comment-age">(01 Sep '17, 14:27)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="63552"></span><div id="comment-63552" class="comment"><div id="post-63552-score" class="comment-score"></div><div class="comment-text"><p>1) tcpdump: mon0: You don't have permission to capture on that device (socket: Operation not permitted)</p><p>2) Mint</p><p>I tried <code>sudo wireshark</code> and it showing me all the interfaces that way, but is it safe to use it with root privileges?</p><p>I tried this:</p><p><a href="https://askubuntu.com/questions/74059/how-do-i-run-wireshark-with-root-privileges">https://askubuntu.com/questions/74059/how-do-i-run-wireshark-with-root-privileges</a></p><p>but it isn't helping the tcpdump nor the wireshark to show all interfaces.</p></div><div id="comment-63552-info" class="comment-info"><span class="comment-age">(01 Sep '17, 23:08)</span> <span class="comment-user userinfo">sharp_pilot</span></div></div><span id="63554"></span><div id="comment-63554" class="comment"><div id="post-63554-score" class="comment-score"></div><div class="comment-text"><p>(I installed wireshark by building the source and not via <code>apt-get</code>. So is <code>sudo dpkg-reconfigure wireshark-common</code> the way to activate that or should I do something else?)</p></div><div id="comment-63554-info" class="comment-info"><span class="comment-age">(02 Sep '17, 22:46)</span> <span class="comment-user userinfo">sharp_pilot</span></div></div><span id="63555"></span><div id="comment-63555" class="comment"><div id="post-63555-score" class="comment-score"></div><div class="comment-text"><p>I did this: <a href="https://wiki.wireshark.org/CaptureSetup/CapturePrivileges">https://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a></p><p>And when I run <code>/usr/bin/dumpcap -D</code> it shows me all interfaces. great.</p><p>But when I do <code>dumpcap -D</code> it shows me only <code>1. bluetooth0</code>.</p><p>And when I call <code>wireshark</code> it again doesn't show me all interfaces.</p><p>Any Idea how to make wireshark show all interfaces now?</p></div><div id="comment-63555-info" class="comment-info"><span class="comment-age">(02 Sep '17, 23:07)</span> <span class="comment-user userinfo">sharp_pilot</span></div></div></div><div id="comment-tools-63547" class="comment-tools"></div><div class="clear"></div><div id="comment-63547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63556"></span>

<div id="answer-container-63556" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63556-score" class="post-score" title="current number of votes">0</div><span id="post-63556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sharp_pilot has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I installed wireshark by building the source</p></blockquote><p>If you built using the <code>configure</code> script, you need to run the configure script with <code>--enable-setcap-install</code> - and you may have to install it with <code>make install</code>, and <em>that</em> may require that you install it with <code>sudo make install</code>. Then run the installed version, not the version in your build tree. That <em>should</em> make dumpcap run with the right privileges.</p><p>If you build using CMake, you need to run CMake with <code>-DENABLE_CAP=ON</code>, and you might again have to install.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '17, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-63556" class="comments-container"><span id="63559"></span><div id="comment-63559" class="comment"><div id="post-63559-score" class="comment-score"></div><div class="comment-text"><p>When I run <code>stat /usr/local/bin/wireshark</code> I see:</p><p><code>Access: (0755/-rwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)</code></p><p>So it just installed it as root? And it run it has root now when I call <code>wireshark</code>?</p><p>How should I restrict that?</p></div><div id="comment-63559-info" class="comment-info"><span class="comment-age">(03 Sep '17, 03:46)</span> <span class="comment-user userinfo">sharp_pilot</span></div></div><span id="63560"></span><div id="comment-63560" class="comment"><div id="post-63560-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>So it just installed it as root?</p></blockquote><p>Yes.</p><blockquote><p>And it run it has root now when I call wireshark?</p></blockquote><p>No. Running a program whose executable image file is owned by root does not cause the program to run as root. Try running <code>stat</code> on, for example, <code>/bin/sh</code> or <code>/bin/cat</code>. That happens only if the executable image file has the set-UID bit set; if that were the case, <code>stat</code> would report <code>-rwsr-x-rx</code> - note the "s".</p><p><em>Wireshark</em> isn't what needs elevated privileges to capture on Linux; <em>dumpcap</em> is. And <code>--enable-setcap-install</code> shouldn't cause dumpcap's executable image file to be set-UID root, it should just cause it to have the <code>cap_net_admin</code> and <code>cap_net_raw</code> capabilities, so that the process running dumpcap has the <code>CAP_NET_ADMIN</code> and <code>CAP_NET_RAW</code> capabilities. The file capabilities are set with the <a href="http://man7.org/linux/man-pages/man8/setcap.8.html">setcap</a> command; you can see what capabilities a file has by using the <a href="http://man7.org/linux/man-pages/man8/getcap.8.html">getcap</a> command.</p></div><div id="comment-63560-info" class="comment-info"><span class="comment-age">(03 Sep '17, 11:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-63556" class="comment-tools"></div><div class="clear"></div><div id="comment-63556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

