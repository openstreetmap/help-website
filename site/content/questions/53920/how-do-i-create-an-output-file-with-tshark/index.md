+++
type = "question"
title = "how do I create an output file with tshark?"
description = '''I am trying to create an output file with tshark. I have read the help command output, but I think I am missunderstanding something. I get file could not be opened, and permission denied. Does the output argument -w not write a file and output to that file?  When I run the command .&#92;tshark.exe -c 10...'''
date = "2016-07-07T17:58:00Z"
lastmod = "2016-07-07T19:42:00Z"
weight = 53920
keywords = [ "tshark" ]
aliases = [ "/questions/53920" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how do I create an output file with tshark?](/questions/53920/how-do-i-create-an-output-file-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53920-score" class="post-score" title="current number of votes">0</div><span id="post-53920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to create an output file with tshark. I have read the help command output, but I think I am missunderstanding something. I get file could not be opened, and permission denied. Does the output argument -w not write a file and output to that file? When I run the command <code>.\tshark.exe -c 100 -i 6 -w test</code> I get a prompt for the administrator password, which I then provide, but it fails anyhow. Heres a picture. <img src="https://osqa-ask.wireshark.org/upfiles/save.PNG" alt="alt text" /> How do I create an output file when running tshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 17:58</strong></p><img src="https://secure.gravatar.com/avatar/b997637a56fa3812bb5146b3786ee488?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eric%20Lovejoy&#39;s gravatar image" /><p><span>Eric Lovejoy</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eric Lovejoy has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53920" class="comments-container"></div><div id="comment-tools-53920" class="comment-tools"></div><div class="clear"></div><div id="comment-53920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53921"></span>

<div id="answer-container-53921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53921-score" class="post-score" title="current number of votes">1</div><span id="post-53921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By specifying, as the argument to the <code>-w</code> flag, a pathname to a file in a directory to which you have write permission.</p><p>You probably don't have write permission to <code>c:\Program Files\Wireshark</code>. Try either running in a directory to which you have permission (which means you might have to specify the full path to tshark in the command, i.e. <code>c:\Program FIles\Wireshark\Tshark.exe</code>; you might have to quote that, as it contains a space), or specifying a full path to the <code>-w</code> argument, e.g. <code>c:\my\directory\test</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '16, 19:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-53921" class="comments-container"></div><div id="comment-tools-53921" class="comment-tools"></div><div class="clear"></div><div id="comment-53921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

