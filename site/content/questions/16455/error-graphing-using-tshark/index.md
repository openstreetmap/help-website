+++
type = "question"
title = "Error Graphing Using TShark"
description = '''I&#x27;m getting a strange error running the following Tshark command in Windows Command Prompt: tshark -q -r capture.cap -t ad -z io,stat,10,ip.src==213.248.117.35 &amp;gt; output.txt  Towards the end of the capture I am getting a huge number of bytes but no packets. | 2012-11-26 16:32:02 | 0 | 144032243667...'''
date = "2012-11-30T03:45:00Z"
lastmod = "2012-11-30T06:14:00Z"
weight = 16455
keywords = [ "graph", "tshark" ]
aliases = [ "/questions/16455" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error Graphing Using TShark](/questions/16455/error-graphing-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16455-score" class="post-score" title="current number of votes">0</div><span id="post-16455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting a strange error running the following Tshark command in Windows Command Prompt:</p><p>tshark -q -r capture.cap -t ad -z io,stat,10,ip.src==213.248.117.35 &gt; <a href="http://output.txt">output.txt</a></p><p>Towards the end of the capture I am getting a huge number of bytes but no packets.</p><pre><code>| 2012-11-26 16:32:02 |      0 | 14403224366743552 |
| 2012-11-26 16:32:12 |      0 | 14403224366743552 |
| 2012-11-26 16:32:22 |      0 | 14403224366743552 |
| 2012-11-26 16:32:32 |      0 | 14403224366743552 |
| 2012-11-26 16:32:42 |      0 | 14403224366743552 |</code></pre><p>When I run the same graph in Wireshark I do not have that problem.</p><p>Can anyone see my problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '12, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/95c900b24e31e3c7623eeaaca40cbed5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chazzquire&#39;s gravatar image" /><p><span>chazzquire</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chazzquire has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Nov '12, 04:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-16455" class="comments-container"><span id="16456"></span><div id="comment-16456" class="comment"><div id="post-16456-score" class="comment-score"></div><div class="comment-text"><p>what is your tshark version (tshark -v)?</p></div><div id="comment-16456-info" class="comment-info"><span class="comment-age">(30 Nov '12, 04:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16457"></span><div id="comment-16457" class="comment"><div id="post-16457-score" class="comment-score"></div><div class="comment-text"><p>1.8.3 Thanks,</p></div><div id="comment-16457-info" class="comment-info"><span class="comment-age">(30 Nov '12, 04:21)</span> <span class="comment-user userinfo">chazzquire</span></div></div><span id="16458"></span><div id="comment-16458" class="comment"><div id="post-16458-score" class="comment-score"></div><div class="comment-text"><p>O.k. at the first glance, it looks like a bug in thsark io stats.</p><ul><li>Is this a very large pcap file?</li><li>Is it possible to upload the file somewhere (think about privacy issues!)?</li><li>what is your OS version?</li></ul></div><div id="comment-16458-info" class="comment-info"><span class="comment-age">(30 Nov '12, 04:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16459"></span><div id="comment-16459" class="comment"><div id="post-16459-score" class="comment-score"></div><div class="comment-text"><p>I would prefer not to upload the capture. It is a large file size (almost 1GB) which was captured over 1 hour whilst streaming video. I'll try creating a smaller capture to see if that helps.</p></div><div id="comment-16459-info" class="comment-info"><span class="comment-age">(30 Nov '12, 04:55)</span> <span class="comment-user userinfo">chazzquire</span></div></div><span id="16460"></span><div id="comment-16460" class="comment"><div id="post-16460-score" class="comment-score"></div><div class="comment-text"><p>What is you OS version?</p></div><div id="comment-16460-info" class="comment-info"><span class="comment-age">(30 Nov '12, 05:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16461"></span><div id="comment-16461" class="comment not_top_scorer"><div id="post-16461-score" class="comment-score"></div><div class="comment-text"><p>I've no tried this with 200MB files and I'm having the same problem.</p></div><div id="comment-16461-info" class="comment-info"><span class="comment-age">(30 Nov '12, 05:08)</span> <span class="comment-user userinfo">chazzquire</span></div></div><span id="16462"></span><div id="comment-16462" class="comment not_top_scorer"><div id="post-16462-score" class="comment-score"></div><div class="comment-text"><p>Windows 7 Professional</p></div><div id="comment-16462-info" class="comment-info"><span class="comment-age">(30 Nov '12, 05:10)</span> <span class="comment-user userinfo">chazzquire</span></div></div><span id="16463"></span><div id="comment-16463" class="comment not_top_scorer"><div id="post-16463-score" class="comment-score"></div><div class="comment-text"><p>can you further reduce the file (half, half, half) to see, if there is any size related issue?</p></div><div id="comment-16463-info" class="comment-info"><span class="comment-age">(30 Nov '12, 05:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16464"></span><div id="comment-16464" class="comment not_top_scorer"><div id="post-16464-score" class="comment-score"></div><div class="comment-text"><p>I've downgraded to 1.6.x and this problem is no longer occurring.</p></div><div id="comment-16464-info" class="comment-info"><span class="comment-age">(30 Nov '12, 05:37)</span> <span class="comment-user userinfo">chazzquire</span></div></div></div><div id="comment-tools-16455" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-16455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16465"></span>

<div id="answer-container-16465" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16465-score" class="post-score" title="current number of votes">0</div><span id="post-16465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I've downgraded to 1.6.x and this problem is no longer occurring.</p></blockquote><p>O.K. so, it looks like a bug. Can you please:</p><ol><li>Try it with the latest 1.9 version ( <a href="http://www.wireshark.org/download/automated/win32/">http://www.wireshark.org/download/automated/win32/</a> )</li><li>If that does not work either, file a bug report at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a></li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '12, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Nov '12, 05:45</strong> </span></p></div></div><div id="comments-container-16465" class="comments-container"><span id="16466"></span><div id="comment-16466" class="comment"><div id="post-16466-score" class="comment-score"></div><div class="comment-text"><p>Ok, it's not working in 1.9 either so i'll report it.</p><p>The "-t ad" addition you gave me yesterday doesn't work in 1.6. Do you know any other way that I can show date and time?</p></div><div id="comment-16466-info" class="comment-info"><span class="comment-age">(30 Nov '12, 05:54)</span> <span class="comment-user userinfo">chazzquire</span></div></div><span id="16467"></span><div id="comment-16467" class="comment"><div id="post-16467-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The "-t ad" addition you gave me yesterday doesn't work in 1.6.</p></blockquote><p>Yes, I've seen that in the meantime. I believe that has been added after 1.6.</p><blockquote><p>Do you know any other way that I can show date and time?</p></blockquote><p>Only by rewriting the output of tshark with a script. Get the date/time of the first frame and then add the seconds of the tshark output to that date/time. Perl and Date::Calc may help.</p><p>UPDATE: Or, run the io stats with 1.6 <strong>and</strong> 1.8 and take the date/time stamps from the 1.8 output and the data from the 1.6 output.</p></div><div id="comment-16467-info" class="comment-info"><span class="comment-age">(30 Nov '12, 06:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16465" class="comment-tools"></div><div class="clear"></div><div id="comment-16465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

