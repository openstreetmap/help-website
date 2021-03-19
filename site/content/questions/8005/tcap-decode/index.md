+++
type = "question"
title = "TCAP Decode"
description = '''Hi, I have a trace in which there is no SSN present. hence wireshark fails to decode the upper layers of the SCCP users (TCAP). Would it be possible to manually decode the TCAP portion? thanks'''
date = "2011-12-16T04:52:00Z"
lastmod = "2012-03-09T07:00:00Z"
weight = 8005
keywords = [ "wireshark" ]
aliases = [ "/questions/8005" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCAP Decode](/questions/8005/tcap-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8005-score" class="post-score" title="current number of votes">0</div><span id="post-8005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a trace in which there is no SSN present. hence wireshark fails to decode the upper layers of the SCCP users (TCAP). Would it be possible to manually decode the TCAP portion?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '11, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/a9fc1527b6be8c2d8f8b9d6b8899f2da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chathura&#39;s gravatar image" /><p><span>chathura</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chathura has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '11, 06:33</strong> </span></p></div></div><div id="comments-container-8005" class="comments-container"></div><div id="comment-tools-8005" class="comment-tools"></div><div class="clear"></div><div id="comment-8005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8009"></span>

<div id="answer-container-8009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8009-score" class="post-score" title="current number of votes">0</div><span id="post-8009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Modern (1.6.0 and later, IIRC) versions of Wireshark have a "default payload" SCCP preference. Just type "tcap" here and the SCCP dissector will hand the payload to TCAP even when there's no SSN.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '11, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-8009" class="comments-container"><span id="8010"></span><div id="comment-8010" class="comment"><div id="post-8010-score" class="comment-score"></div><div class="comment-text"><p>Hi I have already set the default payload to TCAP in 1.6.4 wireshark version and I still see the data portion not decoded. following is a sample bit stream i am trying to decode.</p><p>any help please? 17:19:51,183,649 ETHER |0 |00|a0|a5|68|08|9a|00|00|5e|00|01|03|08|00|45|00|00|b0|c0|9b|40|00|fc|84|1d|5d|cc|1c|ef|08|0c|47|d8|64|5a|64|0b|59|5a|bc|f5|bd|88|22|14|fe|00|03|00|90|00|00|04|bb|00|01|00|16|00|00|00|03|01|00|01|01|00|00|00|80|00|06|00|08|00|00|00|01|02|10|00|6e|00|ee|01|00|00|05|42|1b|03|02|01|ed|09|81|03|0c|15|09|c9|06|0a|91|02|07|87|00|06|09|89|95|0a|41|40|27|95|19|04|44|62|42|48|04|cd|13|02|01|6b|1e|28|1c|06|07|00|11|86|05|01|01|01|a0|11|60|0f|80|02|07|80|a1|09|06|07|04|00|00|01|00|0e|03|6c|1a|a1|18|02|01|01|02|01|38|30|10|80|08|13|60|04|01|51|86|66|f6|02|01|03|83|01|01|00|00|</p><p>thanks</p></div><div id="comment-8010-info" class="comment-info"><span class="comment-age">(16 Dec '11, 07:22)</span> <span class="comment-user userinfo">chathura</span></div></div><span id="8013"></span><div id="comment-8013" class="comment"><div id="post-8013-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" into a "comment".)</p><p>Can you paste a text2pcap-friendly version of that packet?</p><p>Can I assume that it IS decoding up to the SCCP layer, just not TCAP and higher?</p></div><div id="comment-8013-info" class="comment-info"><span class="comment-age">(16 Dec '11, 09:34)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="8036"></span><div id="comment-8036" class="comment"><div id="post-8036-score" class="comment-score"></div><div class="comment-text"><p>Hi, its working now. you need to type in using lower case (tcap) and then only it works. I typed TCAP in uppercase and couldnt see the upper layers getting decoded.</p><p>Thanks for the quick response appreciate it.</p></div><div id="comment-8036-info" class="comment-info"><span class="comment-age">(19 Dec '11, 03:18)</span> <span class="comment-user userinfo">chathura</span></div></div><span id="9456"></span><div id="comment-9456" class="comment"><div id="post-9456-score" class="comment-score"></div><div class="comment-text"><p>If the answer answered your question, don't forget to stop by and mark it as Accepted.</p></div><div id="comment-9456-info" class="comment-info"><span class="comment-age">(09 Mar '12, 07:00)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-8009" class="comment-tools"></div><div class="clear"></div><div id="comment-8009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

