+++
type = "question"
title = "Runtime Error when try to merge .pcap files (Wireshark crashes)"
description = '''I am trying to merge two small .pcap files but as soon as I click &#x27;Open&#x27; on the second file, I get a Runtime Error, with no further clue as to the cause of the problem. Wireshark crashes and restarts.  This problem has only started today, whereas yesterday I was able to merge files with no problems ...'''
date = "2016-11-24T06:41:00Z"
lastmod = "2016-11-25T06:27:00Z"
weight = 57603
keywords = [ "merge", "runtimeerrorprogram" ]
aliases = [ "/questions/57603" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Runtime Error when try to merge .pcap files (Wireshark crashes)](/questions/57603/runtime-error-when-try-to-merge-pcap-files-wireshark-crashes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57603-score" class="post-score" title="current number of votes">0</div><span id="post-57603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to merge two small .pcap files but as soon as I click 'Open' on the second file, I get a Runtime Error, with no further clue as to the cause of the problem. Wireshark crashes and restarts.<br />
</p><p>This problem has only started today, whereas yesterday I was able to merge files with no problems (in fact today, when I try to re-merge .pcap files that were successfully merged yesterday, I still get the Runtime error, so the source files are fine and not corrupt).<br />
</p><p>I am Running Windows 8.1, 64 bit and Wireshark v2.2.2-0-g775fb08. I have uninstalled and re-installed Wireshark and effected countless reboots but the Runtime Error problem persists.<br />
</p><p>What could I check or change to try and solve this problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-runtimeerrorprogram" rel="tag" title="see questions tagged &#39;runtimeerrorprogram&#39;">runtimeerrorprogram</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '16, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/484fe3cee8e1decc1bea5dc8b3049393?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nigeldom&#39;s gravatar image" /><p><span>nigeldom</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nigeldom has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-57603" class="comments-container"></div><div id="comment-tools-57603" class="comment-tools"></div><div class="clear"></div><div id="comment-57603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57605"></span>

<div id="answer-container-57605" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57605-score" class="post-score" title="current number of votes">0</div><span id="post-57605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is probably a bug in Wireshark. Please open a ticket on <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a> with the pcaps you are trying to merge attached so that we can reproduce the crash and fix it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '16, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Nov '16, 06:45</strong> </span></p></div></div><div id="comments-container-57605" class="comments-container"><span id="57606"></span><div id="comment-57606" class="comment"><div id="post-57606-score" class="comment-score"></div><div class="comment-text"><p>OK, will send over two sample files, although one of my team just managed to merge them without any problems. So I suspect the problem is more with my machine and/or installation, rather than being a problem with the files. Therefore I don't believe you'll be able to reproduce my fault without some extra information - but I don't know what to look for and where.</p></div><div id="comment-57606-info" class="comment-info"><span class="comment-age">(24 Nov '16, 06:50)</span> <span class="comment-user userinfo">nigeldom</span></div></div></div><div id="comment-tools-57605" class="comment-tools"></div><div class="clear"></div><div id="comment-57605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57621"></span>

<div id="answer-container-57621" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57621-score" class="post-score" title="current number of votes">0</div><span id="post-57621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>mergecap [options] -w &lt;outfile&gt;|- &lt;infile&gt; [&lt;infile&gt; ...] doesn't do it for you?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '16, 15:22</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p><span>griff</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span></p></div></div><div id="comments-container-57621" class="comments-container"><span id="57634"></span><div id="comment-57634" class="comment"><div id="post-57634-score" class="comment-score"></div><div class="comment-text"><p>mergecap does work (with the advantage that I can use wildcards on the &lt;infile&gt; list).</p><p>But I still would like to know what I can check to find out why the GUI is not working properly anymore.</p><p>If I were to repeat the uninstall, are there any files I could manually remove that are otherwise left behind, so that when I re-install, I have less memory of the previous installation?</p></div><div id="comment-57634-info" class="comment-info"><span class="comment-age">(25 Nov '16, 04:53)</span> <span class="comment-user userinfo">nigeldom</span></div></div><span id="57635"></span><div id="comment-57635" class="comment"><div id="post-57635-score" class="comment-score"></div><div class="comment-text"><p>You can eventually remove your personal folder found in %APPDATA%\Wireshark (this one is left behind when you uninstall).</p><p>But please provide feedback in the bug 13175 you filled. Michael asked you yesterday if you have Dell Backup and Recover software installed.</p></div><div id="comment-57635-info" class="comment-info"><span class="comment-age">(25 Nov '16, 06:27)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-57621" class="comment-tools"></div><div class="clear"></div><div id="comment-57621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

