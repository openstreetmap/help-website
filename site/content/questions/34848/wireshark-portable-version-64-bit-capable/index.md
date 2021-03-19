+++
type = "question"
title = "Wireshark portable version - 64 bit capable?"
description = '''I have the latest &quot;Windows PortableApps (32-bit)&quot; installed on my USB stick. It works fine on my XP+SP3 boxes but refuses to run under Win 7 64bit. Is there a way around this? Is it just the WinCap that needs to be 64bit? Any help very welcome as I&#x27;m trying to &quot;retire&quot; my XP boxes. Dave'''
date = "2014-07-23T04:40:00Z"
lastmod = "2014-07-25T00:58:00Z"
weight = 34848
keywords = [ "portable", "wireshark" ]
aliases = [ "/questions/34848" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark portable version - 64 bit capable?](/questions/34848/wireshark-portable-version-64-bit-capable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34848-score" class="post-score" title="current number of votes">0</div><span id="post-34848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the latest "Windows PortableApps (32-bit)" installed on my USB stick.</p><p>It works fine on my XP+SP3 boxes but refuses to run under Win 7 64bit.</p><p>Is there a way around this? Is it just the WinCap that needs to be 64bit?</p><p>Any help very welcome as I'm trying to "retire" my XP boxes.</p><p>Dave</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-portable" rel="tag" title="see questions tagged &#39;portable&#39;">portable</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '14, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/b479520ebfc9692bf3159b7ecb79374e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="softfoot&#39;s gravatar image" /><p><span>softfoot</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="softfoot has no accepted answers">0%</span></p></div></div><div id="comments-container-34848" class="comments-container"><span id="34851"></span><div id="comment-34851" class="comment"><div id="post-34851-score" class="comment-score"></div><div class="comment-text"><p>Hi, I can run the portable version without issue on my Win 7 64bits box. Could you describe what is your issue exactly? Do you have any error message? Does the Wireshark GUI loads but does not display any interface?</p></div><div id="comment-34851-info" class="comment-info"><span class="comment-age">(23 Jul '14, 05:36)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="34892"></span><div id="comment-34892" class="comment"><div id="post-34892-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I should have been clearer.</p><p>When I start WireSharkPortable on XP it automatically installs WinPcap 4.1.3 and then WSP runs normally.</p><p>Under Win7 it never installs WinPcap and when the WSP gui starts I get a popup saying "The NPF driver isnt running" and there are no interfaces listed.</p><p>I dont really want to manually install WinPcap on each of the machines I'm working on.</p><p>WSP is Version 1.10.8 (v1.10.8-2-g52a5244 from master-1.10)</p><p>Dave</p></div><div id="comment-34892-info" class="comment-info"><span class="comment-age">(24 Jul '14, 11:39)</span> <span class="comment-user userinfo">softfoot</span></div></div><span id="34897"></span><div id="comment-34897" class="comment"><div id="post-34897-score" class="comment-score"></div><div class="comment-text"><p>I <em>think</em> WinPcap needs admin rights to be installed. Are you executing WiresharkPortable with elevated privileges (run as administrator)? It UAC activated on your Windows 7 boxes?</p></div><div id="comment-34897-info" class="comment-info"><span class="comment-age">(24 Jul '14, 13:51)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="34905"></span><div id="comment-34905" class="comment"><div id="post-34905-score" class="comment-score"></div><div class="comment-text"><p>That fixed it :-) I had to disable UAC - a shame, but better than the alternative. Bob</p></div><div id="comment-34905-info" class="comment-info"><span class="comment-age">(25 Jul '14, 00:58)</span> <span class="comment-user userinfo">softfoot</span></div></div></div><div id="comment-tools-34848" class="comment-tools"></div><div class="clear"></div><div id="comment-34848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

