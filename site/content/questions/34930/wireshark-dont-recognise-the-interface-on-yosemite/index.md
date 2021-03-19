+++
type = "question"
title = "Wireshark don&#x27;t recognise the interface on yosemite"
description = '''Hi All, the current version 1.8.15 and the developer version 1.12.0rc3 don&#x27;t recognize the interface when you install it on Yosemite OS X 10.10 Beta 1. I have try with XQuartz 2.7.6 and Wireshark 1.8.15 and XQuartz 2.7.7_rc1 with Wireshark 1.12.0rc3 no effect. Please help me to fix this issue All th...'''
date = "2014-07-27T02:32:00Z"
lastmod = "2014-08-20T09:04:00Z"
weight = 34930
keywords = [ "xquartz", "wireshark", "yosemite" ]
aliases = [ "/questions/34930" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark don't recognise the interface on yosemite](/questions/34930/wireshark-dont-recognise-the-interface-on-yosemite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34930-score" class="post-score" title="current number of votes">1</div><span id="post-34930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>the current version 1.8.15 and the developer version 1.12.0rc3 don't recognize the interface when you install it on Yosemite OS X 10.10 Beta 1.</p><p>I have try with XQuartz 2.7.6 and Wireshark 1.8.15 and XQuartz 2.7.7_rc1 with Wireshark 1.12.0rc3 no effect.</p><p>Please help me to fix this issue</p><p>All the Best</p><p>DAVIDE RISI <span class="__cf_email__" data-cfemail="d7a5bea4be97bab2f9b4b8ba">[email protected]</span></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xquartz" rel="tag" title="see questions tagged &#39;xquartz&#39;">xquartz</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-yosemite" rel="tag" title="see questions tagged &#39;yosemite&#39;">yosemite</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '14, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/b01c35d0fd9d530f8ed08c0cee47e1de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daviderisi&#39;s gravatar image" /><p><span>daviderisi</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daviderisi has no accepted answers">0%</span></p></div></div><div id="comments-container-34930" class="comments-container"></div><div id="comment-tools-34930" class="comment-tools"></div><div class="clear"></div><div id="comment-34930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35631"></span>

<div id="answer-container-35631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35631-score" class="post-score" title="current number of votes">0</div><span id="post-35631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm having the same problem. You can work around it by running wireshark via the terminal and using sudo. so you'd do</p><pre><code>sudo wireshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/72c4c8155e5614f945bb86e1346a77a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbergoon&#39;s gravatar image" /><p><span>jbergoon</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbergoon has no accepted answers">0%</span></p></div></div><div id="comments-container-35631" class="comments-container"><span id="35632"></span><div id="comment-35632" class="comment"><div id="post-35632-score" class="comment-score"></div><div class="comment-text"><p>Don't run Wireshark as root. There are millions of lines of code in Wireshark that may be susceptible to the very network traffic you're capturing. In the mean-time does the released version of 1.12 work any better?</p></div><div id="comment-35632-info" class="comment-info"><span class="comment-age">(20 Aug '14, 08:58)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="35633"></span><div id="comment-35633" class="comment"><div id="post-35633-score" class="comment-score"></div><div class="comment-text"><p>No change on 1.12 ... Still cannot get any interfaces. also when doing ls -l /dev/bpf* it shows those owned root group wheel ...</p><p><code>ls -l /dev/bpf* crw-rw----  1 root  wheel   23,   0 Aug 20 10:13 /dev/bpf0 crw-rw----  1 root  wheel   23,   1 Aug 19 08:04 /dev/bpf1 crw-rw----  1 root  wheel   23,   2 Aug 20 09:30 /dev/bpf2 crw-rw----  1 root  wheel   23,   3 Aug 20 08:17 /dev/bpf3 crw-------  1 root  wheel   23,   4 Aug 20 08:17 /dev/bpf4</code></p><p>chmodBPF appears to be installed though.</p><p>sudo launchctl list | egrep ChmodBPF Password: - 0 org.wireshark.ChmodBPF</p></div><div id="comment-35633-info" class="comment-info"><span class="comment-age">(20 Aug '14, 09:04)</span> <span class="comment-user userinfo">jbergoon</span></div></div></div><div id="comment-tools-35631" class="comment-tools"></div><div class="clear"></div><div id="comment-35631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

