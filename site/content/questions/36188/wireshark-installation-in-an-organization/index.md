+++
type = "question"
title = "Wireshark installation in an organization"
description = '''I am joined a research organization and they told me to setup wireshark on their server. Here we are using three server first one is data server(debian), second one is router and third one is print server where we install all the software, printer etc. I don&#x27;t have any idea about wireshark setup for...'''
date = "2014-09-10T21:35:00Z"
lastmod = "2014-09-14T23:21:00Z"
weight = 36188
keywords = [ "setup", "installation" ]
aliases = [ "/questions/36188" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark installation in an organization](/questions/36188/wireshark-installation-in-an-organization)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36188-score" class="post-score" title="current number of votes">0</div><span id="post-36188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am joined a research organization and they told me to setup wireshark on their server. Here we are using three server first one is data server(debian), second one is router and third one is print server where we install all the software, printer etc. I don't have any idea about wireshark setup for an organization.</p><p>I need to know following information.</p><p>On which server i have to installed wireshark. How to install on that server. How to access wireshark. Can I access wireshark from my windows system and if yes the how.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '14, 21:35</strong></p><img src="https://secure.gravatar.com/avatar/115da44e16ba04b40d8e46aa3ba4d494?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amit%20sharma&#39;s gravatar image" /><p><span>amit sharma</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amit sharma has no accepted answers">0%</span></p></div></div><div id="comments-container-36188" class="comments-container"></div><div id="comment-tools-36188" class="comment-tools"></div><div class="clear"></div><div id="comment-36188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36309"></span>

<div id="answer-container-36309" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36309-score" class="post-score" title="current number of votes">0</div><span id="post-36309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You don't say what technology is used for the router or print servers. I'll assume they are Windows servers to give a mix.</p><ol><li>Install the Wireshark suite on all three servers and on your PC</li><li>On the Debian server create a script for each network interface to run dumpcap and use the -w option to specify where to write the data to - I recommend you also specify a ring buffer of multiple 200 MB files but be careful to create a ring buffer that doesn't fill the volume it writes to. Also don't write to a disk that is heavily used by the system to avoid performance impact.</li><li>On the the Windows servers create a batch (command) file for each network interface to run dumpcap and use the -w option to specify where to write the data to - again specify a ring buffer of multiple 200 MB files being careful to create a ring buffer that doesn't fill the volume it writes to. As with Debian, don't write to a volume that may impact performance e.g. the C: drive, database logging volumes, etc.</li><li>Use dumpcap to capture. Just run the scripts and batch files you have created to start and use Ctl-C to stop them.</li><li>Transfer the captured trace files from the server to your PC using FTP (make sure you use binary mode) or SMB (via a file share on the server)</li><li>Use Wireshark on your PC to do the analysis</li></ol><p>I hope that helps.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '14, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-36309" class="comments-container"><span id="36317"></span><div id="comment-36317" class="comment"><div id="post-36317-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer</p></div><div id="comment-36317-info" class="comment-info"><span class="comment-age">(14 Sep '14, 23:21)</span> <span class="comment-user userinfo">amit sharma</span></div></div></div><div id="comment-tools-36309" class="comment-tools"></div><div class="clear"></div><div id="comment-36309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

