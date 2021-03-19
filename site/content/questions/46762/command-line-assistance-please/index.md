+++
type = "question"
title = "Command line assistance please"
description = '''Hopefully this isn&#x27;t a completely stupid q: But I&#x27;m hopeful someone with more knowledge than me will be able to answer this relatively &#x27;easily&#x27;? I wish to create a command line structure which allow me to create a user facing shortcut which does the following. Capture on a specific interface &amp;amp; o...'''
date = "2015-10-20T08:13:00Z"
lastmod = "2015-10-21T04:45:00Z"
weight = 46762
keywords = [ "background", "command-line" ]
aliases = [ "/questions/46762" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Command line assistance please](/questions/46762/command-line-assistance-please)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46762-score" class="post-score" title="current number of votes">0</div><span id="post-46762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hopefully this isn't a completely stupid q: But I'm hopeful someone with more knowledge than me will be able to answer this relatively 'easily'?</p><p>I wish to create a command line structure which allow me to create a user facing shortcut which does the following.</p><p>Capture on a specific interface &amp; output to a rolling set of capture files &amp; for this to happen in the background. I'm troubleshooting an issue &amp; need for the affected user/s to be able to simply start this off.</p><p>Presently I'm kind of stuck at wireshark -b duration:300 files:test -ringbuffer:12 &amp; cannot seem to work out how to set the output file type and/or directory for these to be placed in.</p><p>I can achieve this easily using the main interface, but the idea is for a normal user to simply double click a shortcut &amp; then carry on with their usual activity (with the shark running in the background).</p><p>Any help/guidance would be greatly appreciated! Daniel</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-background" rel="tag" title="see questions tagged &#39;background&#39;">background</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '15, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/12df9c4dd6e272a8d8840bcc398ae05e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danielgilbey&#39;s gravatar image" /><p><span>danielgilbey</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danielgilbey has no accepted answers">0%</span></p></div></div><div id="comments-container-46762" class="comments-container"></div><div id="comment-tools-46762" class="comment-tools"></div><div class="clear"></div><div id="comment-46762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46769"></span>

<div id="answer-container-46769" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46769-score" class="post-score" title="current number of votes">1</div><span id="post-46769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="danielgilbey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Instead of wireshark, please use <strong>dumpcap</strong>, but with the right arguments ;-)</p><p>I never heard of <strong>-ringbuffer:12</strong>, where did you get that from?</p><blockquote><p>dumpcap -ni <strong>interface_id</strong> -w output.pcap -b filesize:10000 -b files:50 -f "host x.x.x.x and port yyyy"</p></blockquote><p>Please replace the <strong>interface_id</strong> with the ID of the interface you want to capture on. <strong>dumpcap -D -M</strong> will tell you.</p><p>That command will write 50 files, each 10 Mbyte large in a ring-buffer style. Meaning: file #51 will overwrite file #1 and so on. The command will <strong>never stop</strong> until you press CTRL-C.</p><p>If you want the command to stop after n seconds, you should use <strong>-b duration:xxxx</strong> instead <strong>-b files</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '15, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Oct '15, 10:23</strong> </span></p></div></div><div id="comments-container-46769" class="comments-container"><span id="46791"></span><div id="comment-46791" class="comment"><div id="post-46791-score" class="comment-score"></div><div class="comment-text"><p>Good morning Kurt,</p><p>Thanks, I've done some (very quick) testing with the method you've described &amp; think this is what I'll end up building out. Greatly appreciated!</p><p>Ref the "-ringbuffer:12" I got that from the help notes I'd found whilst 'googling' about...</p><p>Anyway, thanks again! Daniel</p></div><div id="comment-46791-info" class="comment-info"><span class="comment-age">(21 Oct '15, 01:01)</span> <span class="comment-user userinfo">danielgilbey</span></div></div><span id="46795"></span><div id="comment-46795" class="comment"><div id="post-46795-score" class="comment-score"></div><div class="comment-text"><p>For anyone further interested, this is the .bat that I've come up with regards this.</p><p>start /min cmd.exe /c "dumpcap -ni 2 -w "C:\OutputDirectory\output.pcap" -b filesize:10000 -b files:40"</p></div><div id="comment-46795-info" class="comment-info"><span class="comment-age">(21 Oct '15, 04:13)</span> <span class="comment-user userinfo">danielgilbey</span></div></div><span id="46796"></span><div id="comment-46796" class="comment"><div id="post-46796-score" class="comment-score"></div><div class="comment-text"><p>Thanks and good luck!</p></div><div id="comment-46796-info" class="comment-info"><span class="comment-age">(21 Oct '15, 04:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46769" class="comment-tools"></div><div class="clear"></div><div id="comment-46769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

