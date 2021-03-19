+++
type = "question"
title = "Missing Network Adaptor List - No interface found error"
description = '''My question is similar to others posted but the suggested solutions did not solve my issue. I have a machine that was just re-imaged with Windows 7 Enterprise Service Pack 1. I downloaded and installed Wireshark Version 2.2.3 (v2.2.3-0-g57531cd) and WinCap 4.1.3. The error message &quot;No interfaces fou...'''
date = "2017-01-20T06:26:00Z"
lastmod = "2017-01-20T07:11:00Z"
weight = 58905
keywords = [ "nic", "adapter", "networkinterface", "networkinterfaces" ]
aliases = [ "/questions/58905" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing Network Adaptor List - No interface found error](/questions/58905/missing-network-adaptor-list-no-interface-found-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58905-score" class="post-score" title="current number of votes">0</div><span id="post-58905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My question is similar to others posted but the suggested solutions did not solve my issue. I have a machine that was just re-imaged with Windows 7 Enterprise Service Pack 1. I downloaded and installed Wireshark Version 2.2.3 (v2.2.3-0-g57531cd) and WinCap 4.1.3.</p><p>The error message "No interfaces found" is displayed where the network adapter list should be. In Windows, I opened up Device Manager and under Network adapters five adapters are listed. I have an active adapter, which is plugged into the company LAN.</p><p>In Wireshark I opened the ‘Capture’ menu and selected ‘Options’. The Capture Interfaces dialog box opens and no adapter entries are displayed in any of the three tab windows or when I select the Manage Interfaces button in the lower right corner of the dialog box. I’ve uninstalled Wireshark and re-installed, the problem did not go away. Any suggestions would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-adapter" rel="tag" title="see questions tagged &#39;adapter&#39;">adapter</span> <span class="post-tag tag-link-networkinterface" rel="tag" title="see questions tagged &#39;networkinterface&#39;">networkinterface</span> <span class="post-tag tag-link-networkinterfaces" rel="tag" title="see questions tagged &#39;networkinterfaces&#39;">networkinterfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '17, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/f44f48b822c61087c90d498cefaeea4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dkollodge&#39;s gravatar image" /><p><span>dkollodge</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dkollodge has no accepted answers">0%</span></p></div></div><div id="comments-container-58905" class="comments-container"><span id="58907"></span><div id="comment-58907" class="comment"><div id="post-58907-score" class="comment-score"></div><div class="comment-text"><p>Did you install WinPcap along with the wireshark install? check Programs and Features for WinPcap.</p><p>Next, what does the following command produce when run from a command or PowerShell prompt?</p><pre><code>path\to\Wireshark\dumpcap.exe -D</code></pre></div><div id="comment-58907-info" class="comment-info"><span class="comment-age">(20 Jan '17, 06:53)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-58905" class="comment-tools"></div><div class="clear"></div><div id="comment-58905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58908"></span>

<div id="answer-container-58908" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58908-score" class="post-score" title="current number of votes">0</div><span id="post-58908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Of course, once you post a question you figure it out.</p><p>My solution was to right click on the Wireshark program icon and select "Run as administrator". The adapter list was then populated. It appears that I only needed to do this the once. Now, I can click the program icon and the Wireshark populates the list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '17, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/f44f48b822c61087c90d498cefaeea4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dkollodge&#39;s gravatar image" /><p><span>dkollodge</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dkollodge has no accepted answers">0%</span></p></div></div><div id="comments-container-58908" class="comments-container"><span id="58914"></span><div id="comment-58914" class="comment"><div id="post-58914-score" class="comment-score"></div><div class="comment-text"><p>This has come up a few times before, with no real answer as to why it's necessary in some cases. I've <em>NEVER</em> had to do this on many installs.</p><p>Note that Wireshark should never actually be run as Administrator (or root), see the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/CapturePrivileges">Capture Privileges</a>.</p><p>You might also want to check the situation after a reboot.</p></div><div id="comment-58914-info" class="comment-info"><span class="comment-age">(20 Jan '17, 07:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-58908" class="comment-tools"></div><div class="clear"></div><div id="comment-58908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

