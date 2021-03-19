+++
type = "question"
title = "Decoding GR-533/IN"
description = '''Can anyone help me with decoding a GR-533/IN trace? No matter what I fiddle with wireshark doesn&#x27;t want to decode the entire TCAP portion of the message. Thanks'''
date = "2014-06-04T10:30:00Z"
lastmod = "2014-06-05T05:55:00Z"
weight = 33396
keywords = [ "decode", "gr-533", "tcap" ]
aliases = [ "/questions/33396" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding GR-533/IN](/questions/33396/decoding-gr-533in)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33396-score" class="post-score" title="current number of votes">0</div><span id="post-33396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone help me with decoding a GR-533/IN trace? No matter what I fiddle with wireshark doesn't want to decode the entire TCAP portion of the message.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-gr-533" rel="tag" title="see questions tagged &#39;gr-533&#39;">gr-533</span> <span class="post-tag tag-link-tcap" rel="tag" title="see questions tagged &#39;tcap&#39;">tcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '14, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/c418c0b102a742cbe042d09671e7b571?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsh3650&#39;s gravatar image" /><p><span>jsh3650</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsh3650 has no accepted answers">0%</span></p></div></div><div id="comments-container-33396" class="comments-container"><span id="33403"></span><div id="comment-33403" class="comment"><div id="post-33403-score" class="comment-score"></div><div class="comment-text"><p>What is GR-533/IN? Are you saying that the TCAP portion does not translate into INAP or CAMEL or that part of the INAP message isn't decoded correctly? What subsyatemnumber(ssn) is used in the SCCP section? Have you tried changing the INAP/CAMEL prefernces to the ssn used?</p></div><div id="comment-33403-info" class="comment-info"><span class="comment-age">(04 Jun '14, 12:23)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="33405"></span><div id="comment-33405" class="comment"><div id="post-33405-score" class="comment-score"></div><div class="comment-text"><p>It's just IN, the older version of AIN. It's being used to query a LIDB to get the CIC associated with a toll free number. Wireshark decodes up to the opcode but then I get the "BER Error: This field lies beyond the end of the known sequence definition.". The payload/data for SCCP is this:</p><p>e2:3b:c7:04:00:01:00:37:e8:33:e9:31:cf:01:01:d0:02:83:01:f2:28:aa:0b:84:09:01:00:11:0a:78:47:75:00:88:84:09:02:00:11:0a:07:48:22:99:99:84:06:07:00:01:03:53:08:df:45:01:17:df:48:01:01</p><p>This is a querywithperm message.<br />
</p><p>Thanks</p></div><div id="comment-33405-info" class="comment-info"><span class="comment-age">(04 Jun '14, 13:52)</span> <span class="comment-user userinfo">jsh3650</span></div></div><span id="33412"></span><div id="comment-33412" class="comment"><div id="post-33412-score" class="comment-score"></div><div class="comment-text"><p>I forgot to answer your other part. Yes, I added in the SSNs, in this case 3 and 254, into the preferences so it would at least decode it to the point it is.</p></div><div id="comment-33412-info" class="comment-info"><span class="comment-age">(04 Jun '14, 16:29)</span> <span class="comment-user userinfo">jsh3650</span></div></div></div><div id="comment-tools-33396" class="comment-tools"></div><div class="clear"></div><div id="comment-33396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33415"></span>

<div id="answer-container-33415" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33415-score" class="post-score" title="current number of votes">0</div><span id="post-33415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately there is no dissector for AIN and the standard isn't free.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '14, 21:21</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span> </br></p></div></div><div id="comments-container-33415" class="comments-container"><span id="33417"></span><div id="comment-33417" class="comment"><div id="post-33417-score" class="comment-score"></div><div class="comment-text"><p>Where "not free" means <a href="http://telecom-info.telcordia.com/site-cgi/ido/docs.cgi?ID=SEARCH&amp;DOCUMENT=GR-533&amp;">USD 875</a>, which is very far indeed from "free". You're unlikely to see Wireshark enhanced to dissect IN/AIN unless either 1) there's a spec for it that costs less than USD 875 and somebody has time to implement it or 2) somebody with access to the spec has time to implement it.</p></div><div id="comment-33417-info" class="comment-info"><span class="comment-age">(04 Jun '14, 22:59)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="33441"></span><div id="comment-33441" class="comment"><div id="post-33441-score" class="comment-score"></div><div class="comment-text"><p>If it could be "loaned" I wonder if it would be possible to create one, or if there would be legal ramifications for doing so. As much as I hate to admit it these legacy Telcordia standards will be still be around for some time.</p></div><div id="comment-33441-info" class="comment-info"><span class="comment-age">(05 Jun '14, 05:55)</span> <span class="comment-user userinfo">jsh3650</span></div></div></div><div id="comment-tools-33415" class="comment-tools"></div><div class="clear"></div><div id="comment-33415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

