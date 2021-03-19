+++
type = "question"
title = "unable to send packet using tcpreplay"
description = '''Hi, We are finding difficult to replay a pcapng trace using tcp replay. Here is the error message we are seeing. Unable to send packet: Error with PF_PACKET send() : Message too long (errno =90)  Warning in send_packets.c:send_packets() line 180: Would like to know whether this is wireshark issue or...'''
date = "2014-05-28T09:29:00Z"
lastmod = "2016-05-04T04:09:00Z"
weight = 33137
keywords = [ "tcpreplay+wireshark" ]
aliases = [ "/questions/33137" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [unable to send packet using tcpreplay](/questions/33137/unable-to-send-packet-using-tcpreplay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33137-score" class="post-score" title="current number of votes">0</div><span id="post-33137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, We are finding difficult to replay a pcapng trace using tcp replay. Here is the error message we are seeing.</p><p>Unable to send packet: Error with PF_PACKET send() : Message too long (errno =90) Warning in send_packets.c:send_packets() line 180:</p><p>Would like to know whether this is wireshark issue or tcp replay issue.</p><p>Thanks for any help,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpreplay+wireshark" rel="tag" title="see questions tagged &#39;tcpreplay+wireshark&#39;">tcpreplay+wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '14, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-33137" class="comments-container"></div><div id="comment-tools-33137" class="comment-tools"></div><div class="clear"></div><div id="comment-33137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="33138"></span>

<div id="answer-container-33138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33138-score" class="post-score" title="current number of votes">0</div><span id="post-33138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Would like to know whether this is wireshark issue or tcp replay issue.</p></blockquote><p>could be one of the following</p><ul><li>libpacp on your system does not support pcpap-ng (please check libpcap version)</li><li>your pcap-ng file is somehow damaged (please check by opening the file with Wireshark)</li><li>If your OS is MAC OS X &lt; 1.5.0, you could have hit a known bug (see the tcprelay FAQ)</li></ul><p>So, please add some details about your system:</p><ul><li>OS and OS version</li><li>Wireshark version on that system</li><li>tcprelay version</li><li>libpcap version</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '14, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 May '14, 10:06</strong> </span></p></div></div><div id="comments-container-33138" class="comments-container"><span id="33139"></span><div id="comment-33139" class="comment"><div id="post-33139-score" class="comment-score"></div><div class="comment-text"><p>Easiest advice: convert your pcapng file to pcap and try again...</p></div><div id="comment-33139-info" class="comment-info"><span class="comment-age">(28 May '14, 10:13)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-33138" class="comment-tools"></div><div class="clear"></div><div id="comment-33138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33147"></span>

<div id="answer-container-33147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33147-score" class="post-score" title="current number of votes">0</div><span id="post-33147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>hi, i had the same issue, after setting the MTU of interface, i fix it. you could try it for using command ifconfig to set the MTU. "Unable to send packet: Error with PF_PACKET send() : Message too long (errno =90) Warning in send_packets.c:send_packets() line 180"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '14, 20:22</strong></p><img src="https://secure.gravatar.com/avatar/885666c057a323159826c414b83eae37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fred&#39;s gravatar image" /><p><span>fred</span><br />
<span class="score" title="26 reputation points">26</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fred has no accepted answers">0%</span></p></div></div><div id="comments-container-33147" class="comments-container"><span id="52215"></span><div id="comment-52215" class="comment"><div id="post-52215-score" class="comment-score"></div><div class="comment-text"><p>I have the same issue, recording on a windows 10 machine on an interface with 1500 MTU, JumboFrame disabled, trying to play on debian with 1500 mtu - and got this error: Message too long (errno = 90)</p></div><div id="comment-52215-info" class="comment-info"><span class="comment-age">(04 May '16, 01:09)</span> <span class="comment-user userinfo">kdani</span></div></div><span id="52218"></span><div id="comment-52218" class="comment"><div id="post-52218-score" class="comment-score"></div><div class="comment-text"><p>hi, you can make mtu larger to fix this issue. for example, set mtu 3000.</p></div><div id="comment-52218-info" class="comment-info"><span class="comment-age">(04 May '16, 02:32)</span> <span class="comment-user userinfo">fred</span></div></div><span id="52222"></span><div id="comment-52222" class="comment"><div id="post-52222-score" class="comment-score"></div><div class="comment-text"><p><span>@kdani</span>: Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-52222-info" class="comment-info"><span class="comment-age">(04 May '16, 04:09)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-33147" class="comment-tools"></div><div class="clear"></div><div id="comment-33147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33181"></span>

<div id="answer-container-33181" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33181-score" class="post-score" title="current number of votes">0</div><span id="post-33181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Opened a <a href="https://github.com/appneta/tcpreplay/issues/82">Tcpreplay issue</a> to track. Will investigate as part of 4.0.5 release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '14, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/bf31287cc10706fcd8ed7439e5738bc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fred%20Klassen&#39;s gravatar image" /><p><span>Fred Klassen</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fred Klassen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 May '14, 12:04</strong> </span></p></div></div><div id="comments-container-33181" class="comments-container"></div><div id="comment-tools-33181" class="comment-tools"></div><div class="clear"></div><div id="comment-33181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

