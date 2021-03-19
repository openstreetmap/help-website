+++
type = "question"
title = "LLMNR flood"
description = '''Hello all,  I need help on LLMNR ...  I have cases in my office, almost all office network connections down.  when I checked using wireshark, wireshark shows that the LLMNR protocol full fill my network.  I am a beginner to network and use wireshark, I do not know what to do.  Please give me suggest...'''
date = "2014-04-03T02:25:00Z"
lastmod = "2014-04-14T22:59:00Z"
weight = 31464
keywords = [ "llmnr" ]
aliases = [ "/questions/31464" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LLMNR flood](/questions/31464/llmnr-flood)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31464-score" class="post-score" title="current number of votes">0</div><span id="post-31464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I need help on LLMNR ... I have cases in my office, almost all office network connections down. when I checked using wireshark, wireshark shows that the LLMNR protocol full fill my network. I am a beginner to network and use wireshark, I do not know what to do. Please give me suggestions to solve the problem.</p><p>Thx B4</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-llmnr" rel="tag" title="see questions tagged &#39;llmnr&#39;">llmnr</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '14, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/6094ea48590496672560a28e6ffb3f73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kapten&#39;s gravatar image" /><p><span>Kapten</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kapten has no accepted answers">0%</span></p></div></div><div id="comments-container-31464" class="comments-container"></div><div id="comment-tools-31464" class="comment-tools"></div><div class="clear"></div><div id="comment-31464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31531"></span>

<div id="answer-container-31531" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31531-score" class="post-score" title="current number of votes">1</div><span id="post-31531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Disable LLMNR if you don't use it.</p><p>Link Local Multicast Name Resolution (LLMNR) is a protocol defined in RFC 4795 that allows both IPv6 and IPv4 hosts to perform name resolution for the names of neighboring computers without requiring a DNS server or DNS client configuration.</p><p>You can disable LLMNR requests via group policy.</p><p>Group Policy = Computer Configuration\Administrative Templates\Network\DNS Client\Turn off Multicast Name Resolution. (Enabled = Don't use LLMNR, Disabled = Use LLMNR)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '14, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-31531" class="comments-container"><span id="31743"></span><div id="comment-31743" class="comment"><div id="post-31743-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much roland, This time we have disable LLMNR on some pc.. But i'am still have a homework, which is why it could happen ...what's wrong with LLMNR ?</p></div><div id="comment-31743-info" class="comment-info"><span class="comment-age">(10 Apr '14, 21:07)</span> <span class="comment-user userinfo">Kapten</span></div></div><span id="31744"></span><div id="comment-31744" class="comment"><div id="post-31744-score" class="comment-score"></div><div class="comment-text"><p>The following may (or may not) be relevant:</p><p><a href="http://ask.wireshark.org/questions/14940/excessive-llmnr-packets-from-one-workstation">excessive llmnr packets from one workstation</a></p></div><div id="comment-31744-info" class="comment-info"><span class="comment-age">(10 Apr '14, 21:19)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="31745"></span><div id="comment-31745" class="comment"><div id="post-31745-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure .... My current network is 10.10.xx/16, everything is running normally, until my friend configure ip alias on a notebook (Win 7) with ip 192.168.10.29/24, then our network down. LLMNR queries are not random, only focused on one host with OS win 7, and we do not configure PAC on his browser.</p></div><div id="comment-31745-info" class="comment-info"><span class="comment-age">(10 Apr '14, 23:36)</span> <span class="comment-user userinfo">Kapten</span></div></div><span id="31746"></span><div id="comment-31746" class="comment"><div id="post-31746-score" class="comment-score"></div><div class="comment-text"><p>Full with this : 192.168.10.29 224.0.0.252 LLMNR 66 Standard query 0xcfd3 A PC57-1 . . . .</p></div><div id="comment-31746-info" class="comment-info"><span class="comment-age">(10 Apr '14, 23:44)</span> <span class="comment-user userinfo">Kapten</span></div></div><span id="31759"></span><div id="comment-31759" class="comment"><div id="post-31759-score" class="comment-score"></div><div class="comment-text"><p>If you remove the IP alias do you see the same behaviour? Is it another version of Win 7?</p><p>Check the registry:</p><blockquote><p>HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient \EnableMulticast</p></blockquote></div><div id="comment-31759-info" class="comment-info"><span class="comment-age">(11 Apr '14, 13:05)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="31814"></span><div id="comment-31814" class="comment not_top_scorer"><div id="post-31814-score" class="comment-score"></div><div class="comment-text"><p>If ip alias removed, there are some LLMNR protocol appeared queries PC57-1, but it doesn't make my network down. I don't know this is normal or not. Sorry, I was wrong, NB with ip alias using Win 7 Pro(OEM), and PC57-1 using OS Win 8.0.</p></div><div id="comment-31814-info" class="comment-info"><span class="comment-age">(14 Apr '14, 22:59)</span> <span class="comment-user userinfo">Kapten</span></div></div></div><div id="comment-tools-31531" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-31531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

