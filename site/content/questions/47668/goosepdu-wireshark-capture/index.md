+++
type = "question"
title = "goosePDU wireshark capture"
description = '''Hello, I&#x27;m trying to build a GooseAPDU Packet with Scapy (Python Framework), and I don&#x27;t know exactly what is this CONTEXT and UNIVERSAL Class. Has anyone build a Goose Packet in any programming language?  This is the error: BER Error: Wrong field in SEQUENCE expected class:CONTEXT(2) tag:0 but foun...'''
date = "2015-11-17T08:12:00Z"
lastmod = "2015-11-17T09:42:00Z"
weight = 47668
keywords = [ "goose", "capture", "scapy", "ber", "apdu" ]
aliases = [ "/questions/47668" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [goosePDU wireshark capture](/questions/47668/goosepdu-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47668-score" class="post-score" title="current number of votes">0</div><span id="post-47668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm trying to build a GooseAPDU Packet with Scapy (Python Framework), and I don't know exactly what is this CONTEXT and UNIVERSAL Class. Has anyone build a Goose Packet in any programming language? This is the error: BER Error: Wrong field in SEQUENCE expected class:CONTEXT(2) tag:0 but found class:UNIVERSAL(0) tag:17</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-goose" rel="tag" title="see questions tagged &#39;goose&#39;">goose</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-scapy" rel="tag" title="see questions tagged &#39;scapy&#39;">scapy</span> <span class="post-tag tag-link-ber" rel="tag" title="see questions tagged &#39;ber&#39;">ber</span> <span class="post-tag tag-link-apdu" rel="tag" title="see questions tagged &#39;apdu&#39;">apdu</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '15, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/eee65d5449a31f0305f39bd040a24272?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daydreamingirl_&#39;s gravatar image" /><p><span>daydreamingirl_</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daydreamingirl_ has no accepted answers">0%</span></p></div></div><div id="comments-container-47668" class="comments-container"><span id="47672"></span><div id="comment-47672" class="comment"><div id="post-47672-score" class="comment-score"></div><div class="comment-text"><p>Are you 100% sure that this is a Wireshark-related question?</p><p>Are you 100% sure that the data you feed to the BER encoder conform to the ASN.1 description of the GOOSE PDU?</p><p><a href="https://en.wikipedia.org/wiki/X.690#BER_encoding">Here</a> you can find the meaning of the "class" in Type Identifier octet. It suggests that where you would use UNIVERSAL at higher levels, you need to use CONTEXT-SPECIFIC inside a SEQUENCE. Now the question is whether you specify the Type Identifier Octet "manually" or whether scapy does that for you (improperly in this case).</p></div><div id="comment-47672-info" class="comment-info"><span class="comment-age">(17 Nov '15, 09:42)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-47668" class="comment-tools"></div><div class="clear"></div><div id="comment-47668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

