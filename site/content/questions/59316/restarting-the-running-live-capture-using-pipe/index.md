+++
type = "question"
title = "Restarting the running live capture using PIPE"
description = '''I am feeding the traffic of a network to Wireshark using named Pipe. I am sending data in a PCAP format by sending the global header along with packet header and data. However, When I try to restart the capture I am getting &quot;Unrecognized libcap format&quot; error. Is there any way to know that wireshark ...'''
date = "2017-02-09T21:05:00Z"
lastmod = "2017-02-12T22:45:00Z"
weight = 59316
keywords = [ "pipe" ]
aliases = [ "/questions/59316" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Restarting the running live capture using PIPE](/questions/59316/restarting-the-running-live-capture-using-pipe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59316-score" class="post-score" title="current number of votes">0</div><span id="post-59316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am feeding the traffic of a network to Wireshark using named Pipe. I am sending data in a PCAP format by sending the global header along with packet header and data. However, When I try to restart the capture I am getting "Unrecognized libcap format" error. Is there any way to know that wireshark has been restarted and disconnected from the pipe by which I can create a new pipe and send header formats again?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '17, 21:05</strong></p><img src="https://secure.gravatar.com/avatar/9cddb17b67b25733bc8b6ff94e6bc236?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharief&#39;s gravatar image" /><p><span>sharief</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharief has no accepted answers">0%</span></p></div></div><div id="comments-container-59316" class="comments-container"><span id="59334"></span><div id="comment-59334" class="comment"><div id="post-59334-score" class="comment-score"></div><div class="comment-text"><p>Can you share the command you are using to start the pipe? Is a named pipe necessary, or can you directly pipe the output of the capture to wireshark, even over an ssh tunnel if necessary?</p></div><div id="comment-59334-info" class="comment-info"><span class="comment-age">(10 Feb '17, 08:17)</span> <span class="comment-user userinfo">Lemurshark</span></div></div><span id="59359"></span><div id="comment-59359" class="comment"><div id="post-59359-score" class="comment-score"></div><div class="comment-text"><p>Thank you jon</p><p>I am using &lt;path&gt;/bin/wireshark -i &lt;named_pipe&gt; to start the PIPE. In my case named pipe is necessary as I have to store the data in a file which can not be done through a pipe. Am I thinking wrong here ? Please suggest whether I can provide with Pipe also ?</p></div><div id="comment-59359-info" class="comment-info"><span class="comment-age">(12 Feb '17, 22:45)</span> <span class="comment-user userinfo">sharief</span></div></div></div><div id="comment-tools-59316" class="comment-tools"></div><div class="clear"></div><div id="comment-59316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

