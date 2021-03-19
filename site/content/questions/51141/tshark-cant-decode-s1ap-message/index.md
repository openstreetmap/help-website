+++
type = "question"
title = "tshark can&#x27;t decode s1ap message"
description = '''Hi, I have installed the latest nightly version of Wireshark in my linux box and some fields don&#x27;t show up correctly. To be more specific, I have tweaked dictionary.xml and some of the fields that were &#x27;unknown&#x27;, before are now shown correctly. These are some diameter messages.  Problem is that can&#x27;...'''
date = "2016-03-24T01:30:00Z"
lastmod = "2016-03-24T06:09:00Z"
weight = 51141
keywords = [ "decode", "unknown", "s1ap", "tshark", "wireshark" ]
aliases = [ "/questions/51141" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark can't decode s1ap message](/questions/51141/tshark-cant-decode-s1ap-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51141-score" class="post-score" title="current number of votes">0</div><span id="post-51141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have installed the latest nightly version of Wireshark in my linux box and some fields don't show up correctly. To be more specific, I have tweaked dictionary.xml and some of the fields that were 'unknown', before are now shown correctly. These are some diameter messages.</p><p>Problem is that can't find out how to do the same with s1ap messages. Any clue?</p><p>Thanks!</p><p>Br, Sotiris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-unknown" rel="tag" title="see questions tagged &#39;unknown&#39;">unknown</span> <span class="post-tag tag-link-s1ap" rel="tag" title="see questions tagged &#39;s1ap&#39;">s1ap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '16, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/286cb1a886d7fcc354e3898dac9be8d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SotirisAnt&#39;s gravatar image" /><p><span>SotirisAnt</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SotirisAnt has no accepted answers">0%</span></p></div></div><div id="comments-container-51141" class="comments-container"></div><div id="comment-tools-51141" class="comment-tools"></div><div class="clear"></div><div id="comment-51141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51142"></span>

<div id="answer-container-51142" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51142-score" class="post-score" title="current number of votes">1</div><span id="post-51142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>S1AP message decoding is written in C (compiled from the ASN.1 description) and not based on an external file content (like diameter.xml).</p><p>The current ASN.1 description being used for S1AP in master branch is v13.1.0 from 2015-12, so it's the latest available on 3GPP web site as of today.</p><p>What is you issue exactly? You have some raw value that does not get interpreted? The decoding is wrong? The best way to move forward is probably to fill a bug on our <a href="https://bugs.wireshark.org">Bugzilla tracking system</a> with a sample pcap attached and a description of your issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '16, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-51142" class="comments-container"><span id="51143"></span><div id="comment-51143" class="comment"><div id="post-51143-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thank you very much for your response. In a specific S1AP message, there is a new field added in the packet, which is not correctly decoded by Wireshark. This field is shown as "Item 7: unknown(195)", which is not the correct name. Of course subfields of that field are not displayed correctly either.</p><p>I had the same issue with some diameter fields, but did overcome it by modifying dictionary.xml file.</p></div><div id="comment-51143-info" class="comment-info"><span class="comment-age">(24 Mar '16, 01:59)</span> <span class="comment-user userinfo">SotirisAnt</span></div></div><span id="51144"></span><div id="comment-51144" class="comment"><div id="post-51144-score" class="comment-score"></div><div class="comment-text"><p>So could you share the pcap?</p></div><div id="comment-51144-info" class="comment-info"><span class="comment-age">(24 Mar '16, 02:33)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="51151"></span><div id="comment-51151" class="comment"><div id="post-51151-score" class="comment-score"></div><div class="comment-text"><p>The issue was further discussed in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12286">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12286</a> and the Wireshark version used was not using S1AP v13.1.0 but v12.2.0 that does not support ProSe IEs.</p><p>Wireshark 2.1.0 development tree decodes the message properly.</p></div><div id="comment-51151-info" class="comment-info"><span class="comment-age">(24 Mar '16, 06:09)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-51142" class="comment-tools"></div><div class="clear"></div><div id="comment-51142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

