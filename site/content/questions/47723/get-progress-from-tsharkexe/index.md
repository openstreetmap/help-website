+++
type = "question"
title = "get progress from tshark.exe"
description = '''I have a set of Windows batch files that create specifically formatted .txt files by running tshark on pre-existing captures with some preset filter settings. Sometimes I am running on very large files and I do not know if tshark is still running or has frozen up. Is there a way to get a text progre...'''
date = "2015-11-18T08:19:00Z"
lastmod = "2015-11-19T02:15:00Z"
weight = 47723
keywords = [ "progress", "tshark" ]
aliases = [ "/questions/47723" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [get progress from tshark.exe](/questions/47723/get-progress-from-tsharkexe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47723-score" class="post-score" title="current number of votes">0</div><span id="post-47723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a set of Windows batch files that create specifically formatted .txt files by running tshark on pre-existing captures with some preset filter settings. Sometimes I am running on very large files and I do not know if tshark is still running or has frozen up. Is there a way to get a text progress bar or percentage complete reported back to the command line?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-progress" rel="tag" title="see questions tagged &#39;progress&#39;">progress</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '15, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/7aa31b10303327434572773aabbc9b2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trashman&#39;s gravatar image" /><p><span>Trashman</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trashman has no accepted answers">0%</span></p></div></div><div id="comments-container-47723" class="comments-container"></div><div id="comment-tools-47723" class="comment-tools"></div><div class="clear"></div><div id="comment-47723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47724"></span>

<div id="answer-container-47724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47724-score" class="post-score" title="current number of votes">0</div><span id="post-47724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately for you there isn't.</p><p>How would you propose that tshark would output the progress when it's also outputting the results of the dissection for your text files?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '15, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47724" class="comments-container"><span id="47725"></span><div id="comment-47725" class="comment"><div id="post-47725-score" class="comment-score"></div><div class="comment-text"><p>I suppose your point is that text file output is only available by redirecting stdout to a text file using "&gt;" therefore anything output by tshark is going to go to that text file. I can see why it's not currently available.</p><p>Ideally, I guess, txt would be a format option for the output file designated in -w. Perhaps an auto-detect if the file has a .txt extension, or perhaps a different flag, such as -wt if you want text output. Then tshark could output progress to the standard output while it outputs the data to that file and you could see the progress update as it writes the file.</p></div><div id="comment-47725-info" class="comment-info"><span class="comment-age">(18 Nov '15, 10:24)</span> <span class="comment-user userinfo">Trashman</span></div></div><span id="47741"></span><div id="comment-47741" class="comment"><div id="post-47741-score" class="comment-score"></div><div class="comment-text"><p>I think there's two different scenarios here, the first when performing live capture, is that progress is displayed with packet counts\dissection, and the second, in your use case, when processing an existing capture file.</p><p>For the latter I think it would be possible to add another flag to indicate where the dissected output should go and then print the progress to stdout.</p><p>Please raise an enhancement request on the Wireshark <a href="https://bugs.wireshark.org">Bugzilla</a> for this. Patches gratefully accepted.</p></div><div id="comment-47741-info" class="comment-info"><span class="comment-age">(19 Nov '15, 02:15)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-47724" class="comment-tools"></div><div class="clear"></div><div id="comment-47724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

