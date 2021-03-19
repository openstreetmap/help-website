+++
type = "question"
title = "Rpcapd for Fedora 13-64 bit"
description = '''Hello Everyone, I want to know that, is there any package of rpcapd ( for Remote capturing ) for Fedora 13-64 bit? Or any rpcapd package for 64-bit Linux will work on that? Please reply!!'''
date = "2012-09-25T21:28:00Z"
lastmod = "2012-10-01T08:13:00Z"
weight = 14525
keywords = [ "rpcapd", "fedora13" ]
aliases = [ "/questions/14525" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rpcapd for Fedora 13-64 bit](/questions/14525/rpcapd-for-fedora-13-64-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14525-score" class="post-score" title="current number of votes">0</div><span id="post-14525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Everyone,</p><p>I want to know that, is there any package of rpcapd ( for Remote capturing ) for Fedora 13-64 bit? Or any rpcapd package for 64-bit Linux will work on that?</p><p>Please reply!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpcapd" rel="tag" title="see questions tagged &#39;rpcapd&#39;">rpcapd</span> <span class="post-tag tag-link-fedora13" rel="tag" title="see questions tagged &#39;fedora13&#39;">fedora13</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '12, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/e82780891a1e938f0bf3a529adc858a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baila&#39;s gravatar image" /><p><span>baila</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baila has no accepted answers">0%</span></p></div></div><div id="comments-container-14525" class="comments-container"></div><div id="comment-tools-14525" class="comment-tools"></div><div class="clear"></div><div id="comment-14525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14542"></span>

<div id="answer-container-14542" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14542-score" class="post-score" title="current number of votes">0</div><span id="post-14542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To the best of my knowledge rpcapd.exe is part of WinPACP and doesn't exist for linux, so you won't find it in any repositories.</p><p>There are how-to blogs out there that take you through recompiling the daemon for linux (<a href="http://www.pawelko.net/linux/17-Rpcapd-For-Linux">Like Here</a>), but these are not guaranteed to work:</p><p>However, linux does not need rpcapd, from the remote capture section of the wireshark docs:</p><p><strong>Microsoft Windows only</strong></p><p><strong>This dialog and capability is only available on Microsoft Windows. On Linux/Unix you can achieve the same effect (securely) through an SSH tunnel.</strong></p><p>I suggest you google a bit and learn about SSH tunnels, this might be a quick starter for you (<a href="http://blog.nielshorn.net/2010/02/using-wireshark-with-remote-capturing/">Linux Tunnels for Wireshark</a>).</p><p>Cheers,</p><p>Craig.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '12, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/7f557535084abef24cd30661f9daefad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CTNOBLE&#39;s gravatar image" /><p><span>CTNOBLE</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CTNOBLE has no accepted answers">0%</span></p></div></div><div id="comments-container-14542" class="comments-container"><span id="14546"></span><div id="comment-14546" class="comment"><div id="post-14546-score" class="comment-score"></div><div class="comment-text"><p>I am actually working from Local Windows machine!!</p></div><div id="comment-14546-info" class="comment-info"><span class="comment-age">(26 Sep '12, 07:39)</span> <span class="comment-user userinfo">baila</span></div></div><span id="14547"></span><div id="comment-14547" class="comment"><div id="post-14547-score" class="comment-score"></div><div class="comment-text"><p>Have a look at plink.</p><p>Or search around this forum for details on how to run cross-platform captures, I'm sure there was a similar question recently, they pointed to this:</p><p><a href="http://www.winpcap.org/docs/docs_40_2/html/group__remote.html">http://www.winpcap.org/docs/docs_40_2/html/group__remote.html</a></p></div><div id="comment-14547-info" class="comment-info"><span class="comment-age">(26 Sep '12, 07:44)</span> <span class="comment-user userinfo">CTNOBLE</span></div></div><span id="14616"></span><div id="comment-14616" class="comment"><div id="post-14616-score" class="comment-score"></div><div class="comment-text"><p>Hi all,</p><p>I have tried with Fedora 13-32 bit. I have followed the steps mentioned at <a href="http://www.pawelko.net/linux/38-Here">http://www.pawelko.net/linux/38-Here</a> . The rpcapd is started successfully. But when I am trying to get the interface list from my local machine,it shows "Can't get list of interfaces: The other host terminated the connection."</p><p>On another wireshark terminal I found that the authentication is successful with the remote machine. But when the local machine request for the interface list, the remote sends "FIN,ACK" packet.</p><p>Please Help me <span class="__cf_email__" data-cfemail="056a70712445">[email protected]</span>!</p></div><div id="comment-14616-info" class="comment-info"><span class="comment-age">(30 Sep '12, 23:27)</span> <span class="comment-user userinfo">baila</span></div></div><span id="14617"></span><div id="comment-14617" class="comment"><div id="post-14617-score" class="comment-score"></div><div class="comment-text"><p><span>@baila</span>: Did you provide enough capabilities to rpcapd to see any interface?</p></div><div id="comment-14617-info" class="comment-info"><span class="comment-age">(30 Sep '12, 23:52)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="14618"></span><div id="comment-14618" class="comment"><div id="post-14618-score" class="comment-score"></div><div class="comment-text"><p>"enough capabilities" means? I am running by simply "./rpcapd" on remote machine!</p></div><div id="comment-14618-info" class="comment-info"><span class="comment-age">(30 Sep '12, 23:59)</span> <span class="comment-user userinfo">baila</span></div></div><span id="14619"></span><div id="comment-14619" class="comment not_top_scorer"><div id="post-14619-score" class="comment-score"></div><div class="comment-text"><p>it gives the same result while I am running rpcapd on remote machine with NULL authentication!!</p></div><div id="comment-14619-info" class="comment-info"><span class="comment-age">(01 Oct '12, 00:25)</span> <span class="comment-user userinfo">baila</span></div></div><span id="14620"></span><div id="comment-14620" class="comment not_top_scorer"><div id="post-14620-score" class="comment-score"></div><div class="comment-text"><p>To capture on a linux machine you need to be root.</p><p>$ sudo rpcapd</p></div><div id="comment-14620-info" class="comment-info"><span class="comment-age">(01 Oct '12, 01:43)</span> <span class="comment-user userinfo">CTNOBLE</span></div></div><span id="14629"></span><div id="comment-14629" class="comment not_top_scorer"><div id="post-14629-score" class="comment-score"></div><div class="comment-text"><p>I'm refering to <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a></p></div><div id="comment-14629-info" class="comment-info"><span class="comment-age">(01 Oct '12, 08:13)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-14542" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-14542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

