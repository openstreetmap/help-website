+++
type = "question"
title = "Question on DNS Query Type"
description = ''' How many answers are there for Query Type= &quot;0x000b&quot;?  The given answer is (0,2). 0x000b is it a WKS?  From the attachment of the sample captured file, how should I obtain the answer? Thank you.  '''
date = "2014-04-06T13:27:00Z"
lastmod = "2014-04-07T11:58:00Z"
weight = 31573
keywords = [ "wireshark", "dns", "dnsquery" ]
aliases = [ "/questions/31573" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Question on DNS Query Type](/questions/31573/question-on-dns-query-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31573-score" class="post-score" title="current number of votes">0</div><span id="post-31573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><ol><li>How many answers are there for Query Type= "0x000b"?</li></ol><p>The given answer is <strong>(0,2)</strong>. 0x000b is it a WKS? From the attachment of the sample captured file, how should I obtain the answer? Thank you.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture3_1.JPG" alt="Query" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture3a.JPG" alt="Response" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-dnsquery" rel="tag" title="see questions tagged &#39;dnsquery&#39;">dnsquery</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '14, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/25eeb72bcc99164e433461c0dbeb5925?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HTHVampire&#39;s gravatar image" /><p><span>HTHVampire</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HTHVampire has no accepted answers">0%</span></p></img></div></div><div id="comments-container-31573" class="comments-container"></div><div id="comment-tools-31573" class="comment-tools"></div><div class="clear"></div><div id="comment-31573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31580"></span>

<div id="answer-container-31580" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31580-score" class="post-score" title="current number of votes">0</div><span id="post-31580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>WKS is an obsolete DNS record type and has a value of 11 (see RFC: 1035, 1123, 1127).</p><p>The hexadecimal notation of 11 is B.</p><p>Open the below sample capture and look at the first two packets:</p><pre><code>http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=dns.cap</code></pre><p>Compare the packets with the screenshots you posted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '14, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></img></div></div><div id="comments-container-31580" class="comments-container"><span id="31581"></span><div id="comment-31581" class="comment"><div id="post-31581-score" class="comment-score"></div><div class="comment-text"><p>Somehow, the question required me to find the answers for WKS,but there's no answer under the response packet, so I'm wondering, am I finding the right place as shown in my screen capture. Thank you.</p></div><div id="comment-31581-info" class="comment-info"><span class="comment-age">(06 Apr '14, 17:55)</span> <span class="comment-user userinfo">HTHVampire</span></div></div><span id="31599"></span><div id="comment-31599" class="comment"><div id="post-31599-score" class="comment-score"></div><div class="comment-text"><p>Yes you are looking in the right place.</p></div><div id="comment-31599-info" class="comment-info"><span class="comment-age">(07 Apr '14, 11:58)</span> <span class="comment-user userinfo">Roland</span></div></div></div><div id="comment-tools-31580" class="comment-tools"></div><div class="clear"></div><div id="comment-31580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

