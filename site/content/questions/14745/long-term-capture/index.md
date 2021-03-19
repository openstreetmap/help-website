+++
type = "question"
title = "Long term capture"
description = '''I have a site with an intermittent issue that appears to be a client (probably a laptop) using all the bandwidth. It will be a while before I can be onsite and my remote options are limited. There is a monitor port configured for the internet connection and they have offered to put a laptop on it wi...'''
date = "2012-10-06T14:30:00Z"
lastmod = "2012-10-06T18:02:00Z"
weight = 14745
keywords = [ "capture-options", "capture-setup" ]
aliases = [ "/questions/14745" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Long term capture](/questions/14745/long-term-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14745-score" class="post-score" title="current number of votes">0</div><span id="post-14745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a site with an intermittent issue that appears to be a client (probably a laptop) using all the bandwidth. It will be a while before I can be onsite and my remote options are limited.</p><p>There is a monitor port configured for the internet connection and they have offered to put a laptop on it with any tool that they can install. It would need to be a Windows tool and easy for them to configure.</p><p>I was thinking about having them install Wireshark and start a multi-file capture. I'm concerned though that won't be able to stop the capture soon enough after the offending client appears.</p><p>It seems like I could get more useful information if I only capture headers. The instructions at <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureOptions.html">http://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureOptions.html</a> indicate that I can set "The maximum amount of data that will be captured for each packet," but I don't see that option.</p><p>Can you think of a better tool? I would love something that would trigger a new capture when bandwidth reaches a certain number. Otherwise I will just have them start a capture with ringbuffers and hope I get to it in time.</p><p>TIA.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-options" rel="tag" title="see questions tagged &#39;capture-options&#39;">capture-options</span> <span class="post-tag tag-link-capture-setup" rel="tag" title="see questions tagged &#39;capture-setup&#39;">capture-setup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '12, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/88f8545f500c22d07322212d1b4ef034?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ComputerX&#39;s gravatar image" /><p><span>ComputerX</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ComputerX has no accepted answers">0%</span></p></div></div><div id="comments-container-14745" class="comments-container"></div><div id="comment-tools-14745" class="comment-tools"></div><div class="clear"></div><div id="comment-14745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14746"></span>

<div id="answer-container-14746" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14746-score" class="post-score" title="current number of votes">3</div><span id="post-14746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ComputerX has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately Wireshark maintains state, even when used with multiple files, as it dissects the traffic so it's not the best tool for making a long term capture. <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a> (which is installed along with Wireshark) is the commandline version but this still maintains state as it also dissects the data. <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">Dumpcap</a> (also installed with Wireshark) is a pure capture utility so is best for long-term captures. The man page gives the options; the <code>-b</code> option is used for multiple files and the size of each file and the <code>-s</code> option controls how many bytes are captured from the front of each packet, I've used a value of 64 when doing similar traffic analysis.</p><p>Once you have gathered all your data you then need to analyse it. You can load each file into Wireshark and examine it, but to get a view over the whole capture period you could look at <a href="http://www.riverbed.com/us/products/cascade/wireshark_enhancements/cascade_pilot_personal_edition.php">Riverbed's Cascade Pilot</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '12, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-14746" class="comments-container"><span id="14748"></span><div id="comment-14748" class="comment"><div id="post-14748-score" class="comment-score"></div><div class="comment-text"><p>Perfect, and thank you. I had been looking at TShark and WinDump. I didn't know about Dumpcap. The -s option should let me trip the packets down to get the headers and truncate the payload.</p><p>I wonder if "capture [TCP|IP|MAC|etc.} headers only" would be a useful/practical feature request. It would require a certain amount of real-time analysis. I think. You guys are the experts :-)</p><p>Thank you again.</p></div><div id="comment-14748-info" class="comment-info"><span class="comment-age">(06 Oct '12, 15:19)</span> <span class="comment-user userinfo">ComputerX</span></div></div><span id="14749"></span><div id="comment-14749" class="comment"><div id="post-14749-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I wonder if "capture [TCP|IP|MAC|etc.} headers only" would be a useful/practical feature request. It would require a certain amount of real-time analysis.</p></blockquote><p>On *BSD and OS X and possibly AIX and Solaris 11, it'd require generating BPF code that looks at the relevant packet fields and calculates the packet length appropriate for the packet to include the relevant headers. I'm not sure what other platforms use the return value of a BPF program as the snapshot length (it might, on Linux and Windows-with-WinPcap; I suspect not in the others).</p></div><div id="comment-14749-info" class="comment-info"><span class="comment-age">(06 Oct '12, 18:02)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-14746" class="comment-tools"></div><div class="clear"></div><div id="comment-14746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14747"></span>

<div id="answer-container-14747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14747-score" class="post-score" title="current number of votes">0</div><span id="post-14747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>i posted this a while back which may help you "Wireshark - tshark Ring Buffer Example" http://www.lovemytool.com/blog/2011/03/wireshark-tshark-ring-buffer-example-by-tony-fortunato.html</p><p>and a bunch of others here <a href="http://thetechfirm.com/wireshark/wireshark.html">http://thetechfirm.com/wireshark/wireshark.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '12, 15:15</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p><span>thetechfirm</span><br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div></div><div id="comments-container-14747" class="comments-container"></div><div id="comment-tools-14747" class="comment-tools"></div><div class="clear"></div><div id="comment-14747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

