+++
type = "question"
title = "EDITCAP supported format for input files"
description = '''Hello Experts, I am trying to split a large BFR (NI Observer Capture file) to a pcap file. When I use editcap, it gives me error that file format is not supported. Can somebody please tell me what are supported filetypes for input for editcap.  And also is there a good way to convert or split large ...'''
date = "2013-11-14T11:03:00Z"
lastmod = "2013-11-14T14:22:00Z"
weight = 27015
keywords = [ "bfr", "editcap" ]
aliases = [ "/questions/27015" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [EDITCAP supported format for input files](/questions/27015/editcap-supported-format-for-input-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27015-score" class="post-score" title="current number of votes">0</div><span id="post-27015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Experts,</p><p>I am trying to split a large BFR (NI Observer Capture file) to a pcap file. When I use editcap, it gives me error that file format is not supported.</p><p>Can somebody please tell me what are supported filetypes for input for editcap.</p><p>And also is there a good way to convert or split large BFR file.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bfr" rel="tag" title="see questions tagged &#39;bfr&#39;">bfr</span> <span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '13, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/831b5b077f0dd7cb7c2988a29a9cfa63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hkjarral&#39;s gravatar image" /><p><span>hkjarral</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hkjarral has no accepted answers">0%</span></p></div></div><div id="comments-container-27015" class="comments-container"></div><div id="comment-tools-27015" class="comment-tools"></div><div class="clear"></div><div id="comment-27015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27019"></span>

<div id="answer-container-27019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27019-score" class="post-score" title="current number of votes">2</div><span id="post-27019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Which version of Wireshark are you using? Using the <code>205-HTTP.bfr</code> Network Instruments Observer capture file from the Wireshark menagerie, I tried this with <code>editcap</code> from trunk-1.8, trunk-1.10, trunk (svn 53323) as well as 1.10.2, and they all worked. Perhaps you're using an older version of Wireshark? Or perhaps there is a newer version of the Network Instruments Observer file format that Wireshark doesn't yet support? Maybe you could post a small capture file to <a href="http://cloudshark.org/">cloudshark</a> (or some other place of your choosing), so someone could take a look at it?</p><p>Also, what is the exact syntax you are using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27019" class="comments-container"><span id="27020"></span><div id="comment-27020" class="comment"><div id="post-27020-score" class="comment-score"></div><div class="comment-text"><p>You are right I figured it out !</p><p>I have the latest version of wireshark but it still couldn't read the observer file because wireshark supports observer file version upto 9.0 and I have version 15.0 of observer file.</p><p>Thanks for you response.</p></div><div id="comment-27020-info" class="comment-info"><span class="comment-age">(14 Nov '13, 14:17)</span> <span class="comment-user userinfo">hkjarral</span></div></div><span id="27021"></span><div id="comment-27021" class="comment"><div id="post-27021-score" class="comment-score"></div><div class="comment-text"><p>In that case, you should probably <a href="https://bugs.wireshark.org/bugzilla/">file a bug report</a> with a sample observer 15.0 capture file and either a link to the capture file format or a patch to allow Wireshark to read the newer formats.</p></div><div id="comment-27021-info" class="comment-info"><span class="comment-age">(14 Nov '13, 14:22)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-27019" class="comment-tools"></div><div class="clear"></div><div id="comment-27019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

