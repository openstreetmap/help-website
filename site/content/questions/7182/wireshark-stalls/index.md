+++
type = "question"
title = "Wireshark stalls"
description = '''Wireshark will capture without stalling on my windows vista 32 bit OS, only once, if I install it, and directly after, when installation is finished, click the option to launch wireshark (as part of the GUI panel of the installer). Once I exit wireshark, and re enter the program, it will consistentl...'''
date = "2011-11-01T12:29:00Z"
lastmod = "2011-11-01T14:01:00Z"
weight = 7182
keywords = [ "windows", "vista", "stall" ]
aliases = [ "/questions/7182" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark stalls](/questions/7182/wireshark-stalls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7182-score" class="post-score" title="current number of votes">0</div><span id="post-7182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark will capture without stalling on my windows vista 32 bit OS, only once, if I install it, and directly after, when installation is finished, click the option to launch wireshark (as part of the GUI panel of the installer). Once I exit wireshark, and re enter the program, it will consistently stall, and crash, upon any attempt to capture. So if I want to use wireshark again after the first time it worked directly following installation, I am forced to uninstall, reinstall, and launch it directly from the installation panel after installation finishes, for it to only work once before I close it again.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-vista" rel="tag" title="see questions tagged &#39;vista&#39;">vista</span> <span class="post-tag tag-link-stall" rel="tag" title="see questions tagged &#39;stall&#39;">stall</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '11, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/49f47caf6f6bcac15faff47677079dcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmu2101&#39;s gravatar image" /><p><span>jmu2101</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmu2101 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Nov '11, 12:31</strong> </span></p></div></div><div id="comments-container-7182" class="comments-container"><span id="7183"></span><div id="comment-7183" class="comment"><div id="post-7183-score" class="comment-score"></div><div class="comment-text"><p>Try running <code>wireshark</code> in a command prompt to see if there is any error output:</p><pre><code>cd &quot;C:\Program Files\Wireshark&quot;
wireshark.exe</code></pre></div><div id="comment-7183-info" class="comment-info"><span class="comment-age">(01 Nov '11, 12:50)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="7185"></span><div id="comment-7185" class="comment"><div id="post-7185-score" class="comment-score"></div><div class="comment-text"><p>no error output when I do this. Again it just loads wireshark like normal, i start capturing on the ethernet interface, and it stalls after 4 seconds, and windows closes the program. It will only work after clicking the launch button following installation.</p></div><div id="comment-7185-info" class="comment-info"><span class="comment-age">(01 Nov '11, 12:57)</span> <span class="comment-user userinfo">jmu2101</span></div></div></div><div id="comment-tools-7182" class="comment-tools"></div><div class="clear"></div><div id="comment-7182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7187"></span>

<div id="answer-container-7187" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7187-score" class="post-score" title="current number of votes">0</div><span id="post-7187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Problem solved. In Windows Vista you have to run wireshark as an administrator. Just Right Click on the wireshark icon or wherever the application is located, and click, 'run as administrator', otherwise it will hang when you try to capture from an internet connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '11, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/49f47caf6f6bcac15faff47677079dcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmu2101&#39;s gravatar image" /><p><span>jmu2101</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmu2101 has no accepted answers">0%</span></p></div></div><div id="comments-container-7187" class="comments-container"></div><div id="comment-tools-7187" class="comment-tools"></div><div class="clear"></div><div id="comment-7187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

