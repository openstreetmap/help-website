+++
type = "question"
title = "Seeing only management and control frames on 802.11"
description = '''I&#x27;m capturing in monitor mode, but I&#x27;m not seeing any packets where the header claims it&#x27;s a data.'''
date = "2013-07-22T17:53:00Z"
lastmod = "2013-07-24T23:47:00Z"
weight = 23274
keywords = [ "802.11" ]
aliases = [ "/questions/23274" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Seeing only management and control frames on 802.11](/questions/23274/seeing-only-management-and-control-frames-on-80211)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23274-score" class="post-score" title="current number of votes">0</div><span id="post-23274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm capturing in monitor mode, but I'm not seeing any packets where the header claims it's a data.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '13, 17:53</strong></p><img src="https://secure.gravatar.com/avatar/d387f094ffe1d9ae09b727e98754370b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andyhuang&#39;s gravatar image" /><p><span>andyhuang</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andyhuang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jul '13, 18:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23274" class="comments-container"><span id="23275"></span><div id="comment-23275" class="comment"><div id="post-23275-score" class="comment-score"></div><div class="comment-text"><p>This is a separate question - the person who asked the question where you added an "answer" that's actually a question never said whether the problem was that they didn't see any data frames or that they saw data frames but they were only dissected as 802.11, not, for example, as HTTP over TCP over IP.</p><p>If you're truly having the <em>first</em> problem, that means that you're seeing 802.11 management and control frames, but no data frames, according to the Frame Control field - i.e., the "Type:" subfield of the Frame Control field is either "Management frame" or "Control frame", never "Data frame".</p><p>If you're seeing frames where the Frame Control field "Type" subfield says "Data frame", then you're <em>not</em> having the first problem from that question, you're having the <em>second</em> problem from that question.</p></div><div id="comment-23275-info" class="comment-info"><span class="comment-age">(22 Jul '13, 18:16)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="23310"></span><div id="comment-23310" class="comment"><div id="post-23310-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I have the FIRST problem, never see "Data frame". My AP is not encrypted， wireshark version is 1.10.0. I can capture beacon frames and control frames.</p></div><div id="comment-23310-info" class="comment-info"><span class="comment-age">(23 Jul '13, 19:16)</span> <span class="comment-user userinfo">andyhuang</span></div></div></div><div id="comment-tools-23274" class="comment-tools"></div><div class="clear"></div><div id="comment-23274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23311"></span>

<div id="answer-container-23311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23311-score" class="post-score" title="current number of votes">0</div><span id="post-23311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's probably a driver or adapter problem then. You'd have to ask the adapter vendor or the driver writer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 20:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23311" class="comments-container"><span id="23321"></span><div id="comment-23321" class="comment"><div id="post-23321-score" class="comment-score"></div><div class="comment-text"><p>I found that when I put the adapter in monitor mode in advance by using iwconfig tools, wireshark can capture all the packages with mac802.11 header in prom mode. But when I use the "monitor mode" checkbox in wireshark, it has the problem described above.Isn't it weird?</p></div><div id="comment-23321-info" class="comment-info"><span class="comment-age">(24 Jul '13, 02:37)</span> <span class="comment-user userinfo">andyhuang</span></div></div><span id="23336"></span><div id="comment-23336" class="comment"><div id="post-23336-score" class="comment-score"></div><div class="comment-text"><p>I infer from "iwconfig tools" that this is on Linux; what type of adapter is it, and what does <code>ldd /usr/lib/libpcap.so</code> print?</p></div><div id="comment-23336-info" class="comment-info"><span class="comment-age">(24 Jul '13, 10:33)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="23350"></span><div id="comment-23350" class="comment"><div id="post-23350-score" class="comment-score"></div><div class="comment-text"><p>Yes, I'm on debian wheezy. The adapter is AR242x/AR542x.</p><pre><code>    #ldd /usr/lib/x86_64-linux-gnu/libpcap.so
    linux-vdso.so.1 =&gt;  (0x00007fff37d7e000)
    libc.so.6 =&gt; /lib/x86_64-linux-gnu/libc.so.6 (0x00007f8b8ece8000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f8b8f0db000)</code></pre></div><div id="comment-23350-info" class="comment-info"><span class="comment-age">(24 Jul '13, 17:32)</span> <span class="comment-user userinfo">andyhuang</span></div></div><span id="23351"></span><div id="comment-23351" class="comment"><div id="post-23351-score" class="comment-score"></div><div class="comment-text"><p>OK, libpcap is not built with libnl, which means the monitor-mode support doesn't work as well as it should. (libpcap needs to talk to netlink directly, so that distributions don't get to choose whether it'll use net link for monitor-mode support or not. That's another project on my overloaded wish list; note that whatever code it uses to talk to netlink must be BSD-licensed....)</p><p>It <em>probably</em> has a mac80211 driver, but, as libpcap isn't using libnl, it can't create a mon0 VAP and capture on it, so it's probably relying on some old ioctls that might get undone by "helpful" software.</p><p>The checkbox in Wireshark will probably not work until I get around to making libpcap talk directly to netlink, that version of libpcap ends up in an official release, and it gets picked up by various Linux distributions.</p></div><div id="comment-23351-info" class="comment-info"><span class="comment-age">(24 Jul '13, 18:11)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="23353"></span><div id="comment-23353" class="comment"><div id="post-23353-score" class="comment-score"></div><div class="comment-text"><p>I'm totally confused now. If the monitor-mode isn't supported well in my situation, how could wireshark capture 802.11 management and control frames? Moreover in the help of iwconfig tools, wireshark seems to work normally, are the packages captured reliable then, or may some other packages be missing?</p></div><div id="comment-23353-info" class="comment-info"><span class="comment-age">(24 Jul '13, 21:29)</span> <span class="comment-user userinfo">andyhuang</span></div></div><span id="23354"></span><div id="comment-23354" class="comment not_top_scorer"><div id="post-23354-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If the monitor-mode isn't supported well in my situation, how could wireshark capture 802.11 management and control frames?</p></blockquote><p>Because not being able to capture data frames in monitor mode doesn't count as performing "well".</p><blockquote><p>Moreover in the help of iwconfig tools, wireshark seems to work normally, are the packages captured reliable then</p></blockquote><p>They're probably captured as reliably as the hardware allows.</p></div><div id="comment-23354-info" class="comment-info"><span class="comment-age">(24 Jul '13, 23:47)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-23311" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-23311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

