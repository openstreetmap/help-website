+++
type = "question"
title = "Stop capture from commandline"
description = '''Is it possible to stop wireshark capture from console? I have a script which starts wireshark capture using command &quot;wireshark -i &amp;lt;interface&amp;gt; -k&quot; I want to stop it from console later. As there is no fixed time between start and stop I can&#x27;t use automatic stop options. tshark is not an option f...'''
date = "2014-06-04T07:06:00Z"
lastmod = "2014-06-05T13:31:00Z"
weight = 33377
keywords = [ "stopping", "command-line", "wireshark" ]
aliases = [ "/questions/33377" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Stop capture from commandline](/questions/33377/stop-capture-from-commandline)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33377-score" class="post-score" title="current number of votes">0</div><span id="post-33377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to stop wireshark capture from console? I have a script which starts wireshark capture using command "wireshark -i &lt;interface&gt; -k" I want to stop it from console later. As there is no fixed time between start and stop I can't use automatic stop options. tshark is not an option for me in this case and also starting wireshark capture with file save option isn't what I want.</p><p>So, if possible please tell me the steps needed or whether there is any workaround or not.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-stopping" rel="tag" title="see questions tagged &#39;stopping&#39;">stopping</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '14, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/5aae92c75bcf159f9da5092d5e7e99a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swap&#39;s gravatar image" /><p><span>swap</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swap has no accepted answers">0%</span></p></div></div><div id="comments-container-33377" class="comments-container"></div><div id="comment-tools-33377" class="comment-tools"></div><div class="clear"></div><div id="comment-33377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33472"></span>

<div id="answer-container-33472" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33472-score" class="post-score" title="current number of votes">0</div><span id="post-33472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>tshark is not an option for me in this case and also starting wireshark capture with file save option isn't what I want.</p></blockquote><p>well, then your options are 'limited', not to say non existent. ;-))</p><p>Reason: You cannot tell a running instance of Wireshark to stop the capturing process. There is no such functionality.</p><p>What I don't understand: Why do you need to start Wireshark in GUI mode (interactive mode) and then <strong>automatically</strong> tell it to stop capturing. Can't you just ask the person in front of the PC to click on the "STOP capture icon"? If no: Can you please add some details why you need to have it in exactly that way?</p><p>If you are 'flexible', my suggestion would be:</p><p>Do one of the following:</p><p>Either:</p><ul><li>start Wireshark as you did</li><li>then bring up a pop-up message (<strong>net send</strong> on windows or similar) and ask the user to click on the "STOP capture icon" in Wireshark</li></ul><p>Or:</p><ul><li>capture the traffic with <strong>dumpcap</strong> and write it to a file</li><li>If you want to stop the capturing process, <strong>kill</strong> the dumpcap process</li><li>start Wireshark with the saved capture file: <strong>wireshark -nr saved.pcap</strong></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '14, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33472" class="comments-container"></div><div id="comment-tools-33472" class="comment-tools"></div><div class="clear"></div><div id="comment-33472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

