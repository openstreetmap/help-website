+++
type = "question"
title = "Convert .pcap into .txt format"
description = '''Hello , I would like to know the procedure for converting a .pcap wireshark trace into .txt format and it should be in readable format. I have looked some procedures but it is still not clear to me. Do i need to install any other .exe other then wireshark to do so ? Thanks, Manoj '''
date = "2014-01-11T05:28:00Z"
lastmod = "2014-04-25T00:38:00Z"
weight = 28794
keywords = [ "conversion", "packet" ]
aliases = [ "/questions/28794" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Convert .pcap into .txt format](/questions/28794/convert-pcap-into-txt-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28794-score" class="post-score" title="current number of votes">1</div><span id="post-28794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello ,</p><p>I would like to know the procedure for converting a .pcap wireshark trace into .txt format and it should be in readable format. I have looked some procedures but it is still not clear to me. Do i need to install any other .exe other then wireshark to do so ?</p><p>Thanks, Manoj</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '14, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/556f3daa3ddd7037de091756989828b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manoj%20Singh&#39;s gravatar image" /><p><span>Manoj Singh</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manoj Singh has no accepted answers">0%</span></p></div></div><div id="comments-container-28794" class="comments-container"></div><div id="comment-tools-28794" class="comment-tools"></div><div class="clear"></div><div id="comment-28794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28796"></span>

<div id="answer-container-28796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28796-score" class="post-score" title="current number of votes">4</div><span id="post-28796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can just open the trace in the lastest stable build of Wireshark (1.10.5 at the moment) and then select "Menu" -&gt; "File" -&gt; "Export Packet Dissections" -&gt; "As Plain Text File". Select the packet range you want to see in your text file, e.g. packets 1-100 or so, and set the packet format to whatever you need. Most likely "Packet Details" or "Packet Summary line". Try both to see which one you need.</p><p>You should keep in mind that using "Packet Details" can result in a very long text file depending on the number ob packets you have in your trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '14, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28796" class="comments-container"></div><div id="comment-tools-28796" class="comment-tools"></div><div class="clear"></div><div id="comment-28796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32170"></span>

<div id="answer-container-32170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32170-score" class="post-score" title="current number of votes">0</div><span id="post-32170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I use the <code>tshark -x -r file.pcap</code> command line when hexdump like output is good for post processing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '14, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/22dd39dd38a838dd564ce33da0f35011?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nik&#39;s gravatar image" /><p><span>nik</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nik has no accepted answers">0%</span></p></div></div><div id="comments-container-32170" class="comments-container"></div><div id="comment-tools-32170" class="comment-tools"></div><div class="clear"></div><div id="comment-32170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

