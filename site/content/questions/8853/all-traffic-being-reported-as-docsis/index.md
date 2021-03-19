+++
type = "question"
title = "All Traffic Being Reported as Docsis"
description = '''Hello - I received a trace from an outside source. When I opened it up I used the Decode As feature. As a result all the traffic was interpreted as Docsis which was fine since it was coming off a cable modem infrastructure. However, my problem now is that no matter what I capture is now always inter...'''
date = "2012-02-06T09:24:00Z"
lastmod = "2017-06-28T15:17:00Z"
weight = 8853
keywords = [ "interpretation", "traffic" ]
aliases = [ "/questions/8853" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [All Traffic Being Reported as Docsis](/questions/8853/all-traffic-being-reported-as-docsis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8853-score" class="post-score" title="current number of votes">0</div><span id="post-8853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello - I received a trace from an outside source. When I opened it up I used the Decode As feature. As a result all the traffic was interpreted as Docsis which was fine since it was coming off a cable modem infrastructure. However, my problem now is that no matter what I capture is now always interpreted as Docsis which is nonsense. The question is how can I make my Wireshark installation revert back to normal?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interpretation" rel="tag" title="see questions tagged &#39;interpretation&#39;">interpretation</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '12, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/eca1bae1fbdee294c203074c46d15a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregwolf0797&#39;s gravatar image" /><p><span>gregwolf0797</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregwolf0797 has no accepted answers">0%</span></p></div></div><div id="comments-container-8853" class="comments-container"><span id="8860"></span><div id="comment-8860" class="comment"><div id="post-8860-score" class="comment-score"></div><div class="comment-text"><p>How was that trace captured? If it was captured from a Cisco device that puts DOCSIS frames onto an Ethernet as raw DOCSIS frames inside Ethernet framing, by a program that uses a sufficiently recent version of libpcap/WinPcap, they could have specified a link-layer header type of DOCSIS, so that Wireshark would <em>automatically</em> recognize it as DOCSIS traffic.</p></div><div id="comment-8860-info" class="comment-info"><span class="comment-age">(06 Feb '12, 11:09)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-8853" class="comment-tools"></div><div class="clear"></div><div id="comment-8853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8854"></span>

<div id="answer-container-8854" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8854-score" class="post-score" title="current number of votes">3</div><span id="post-8854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><h3 id="method-1">Method 1</h3><p>Using the same <strong>Decode As</strong> dialog that you originally used, click the <strong>Clear</strong> button.</p><h3 id="method-2">Method 2</h3><p>Using menu <strong>Analyze &gt; User Specified Decodes... &gt; Clear</strong>. This wipes out all <strong>Decode As</strong> settings.</p><p>(works as of Wireshark 1.7.0)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '12, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-8854" class="comments-container"></div><div id="comment-tools-8854" class="comment-tools"></div><div class="clear"></div><div id="comment-8854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15899"></span>

<div id="answer-container-15899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15899-score" class="post-score" title="current number of votes">0</div><span id="post-15899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Check the following settings:</strong> Preferences - Frame protocol - uncheck "treat all frames as docsis".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '12, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/4963b7fa0b6aa505b74d41ef6cfb2ffb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wslez&#39;s gravatar image" /><p><span>wslez</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wslez has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '12, 04:50</strong> </span></p></div></div><div id="comments-container-15899" class="comments-container"><span id="62378"></span><div id="comment-62378" class="comment"><div id="post-62378-score" class="comment-score"></div><div class="comment-text"><p>This saved me a lot of time. In Wireshark 2.2.7 on Mac, it is under <strong>Preferences-&gt;Advanced-&gt;frame.force_docsis_encap</strong></p></div><div id="comment-62378-info" class="comment-info"><span class="comment-age">(28 Jun '17, 15:17)</span> <span class="comment-user userinfo">IgorGanapolsky</span></div></div></div><div id="comment-tools-15899" class="comment-tools"></div><div class="clear"></div><div id="comment-15899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

