+++
type = "question"
title = "Float values in GOOSE Protocol"
description = '''Hello, I am working a product which supports IEC-61850 GOOSE protocol. I am using Wireshark for Packet analysis. According to similar question on forum: here http://ask.wireshark.org/questions/18597/goose-why-display-floating-point-in-hex I found that, Wireshark displays Float values as Hex becuase,...'''
date = "2013-05-15T23:11:00Z"
lastmod = "2013-05-17T04:23:00Z"
weight = 21169
keywords = [ "asn.1", "goose" ]
aliases = [ "/questions/21169" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Float values in GOOSE Protocol](/questions/21169/float-values-in-goose-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21169-score" class="post-score" title="current number of votes">0</div><span id="post-21169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am working a product which supports IEC-61850 GOOSE protocol. I am using Wireshark for Packet analysis.</p><p>According to similar question on forum: here <a href="http://"></a><a href="http://ask.wireshark.org/questions/18597/goose-why-display-floating-point-in-hex">http://ask.wireshark.org/questions/18597/goose-why-display-floating-point-in-hex</a></p><p>I found that, Wireshark displays Float values as Hex becuase, " <em>FloatingPoint ::= OCTET STRING as it's defined as OCTET STRING it will be displayed in hex.</em>". The authour has suggested to "<em>One could pssibly redifine the field in the .cnf file to FT_FLOAT but as there is no size constraint the OCTET STRING can be of arbitarry length</em>.".</p><p>I tried to figure how can I display Float value as floating value instread of HEX, but I could not find the solution for this. Please helm me.</p><p>Best Regards, Dhaval</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asn.1" rel="tag" title="see questions tagged &#39;asn.1&#39;">asn.1</span> <span class="post-tag tag-link-goose" rel="tag" title="see questions tagged &#39;goose&#39;">goose</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '13, 23:11</strong></p><img src="https://secure.gravatar.com/avatar/c21b470798033ecd236122627603f885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d2v0&#39;s gravatar image" /><p><span>d2v0</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="d2v0 has no accepted answers">0%</span></p></div></div><div id="comments-container-21169" class="comments-container"></div><div id="comment-tools-21169" class="comment-tools"></div><div class="clear"></div><div id="comment-21169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21185"></span>

<div id="answer-container-21185" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21185-score" class="post-score" title="current number of votes">0</div><span id="post-21185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If this is true: <a href="http://tissues.iec61850.com/tissue.mspx?issueid=817">http://tissues.iec61850.com/tissue.mspx?issueid=817</a> Final Proposal: Change Table A.2: Encoding allData in Fixed-length GOOSE Message. Basic Data Type Float 32 ASN.1 Tag 0x87 ASN.1 Len = 5 Comment: MMS Data Production: first byte=8, remaining 4 bytes represents the floating point number in IEEE 754 single precision format.</p><p>Add someting like this to the .cnf file</p><pre><code>#.FN_BODY FloatingPoint VAL_PTR= &amp;parameter_tvb
tvbuff_t    *parameter_tvb;
int length;

%(DEFAULT_BODY)s

 if (!parameter_tvb)
    return offset;

 length = tvb_length(parameter_tvb);
 if(length!=5)
    return offset;
 if(tvb_get_guint8(parameter_tvb,0) != 8)
    return offset;

 proto_tree_add_item(tree, hf_goose_foo, parameter_tvb, 1, 4, ENC_BIG_ENDIAN);</code></pre><p>and add the hf_ variable to the template file with FT_FLOAT or something along those lines. run make goose in the asn1 folder and then recompile Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '13, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '13, 03:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-21185" class="comments-container"><span id="21211"></span><div id="comment-21211" class="comment"><div id="post-21211-score" class="comment-score"></div><div class="comment-text"><p><span>@anders</span> Thanks. I will try your answer.</p></div><div id="comment-21211-info" class="comment-info"><span class="comment-age">(17 May '13, 02:39)</span> <span class="comment-user userinfo">d2v0</span></div></div><span id="21216"></span><div id="comment-21216" class="comment"><div id="post-21216-score" class="comment-score"></div><div class="comment-text"><p>Hi, If you get it to work please open a bug report and attach a sample pcap if possible and add your patch to the bug report for inclution into Wireshark. As of now we have no way of verifying the correctnes of any float data patch.</p></div><div id="comment-21216-info" class="comment-info"><span class="comment-age">(17 May '13, 03:37)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="21218"></span><div id="comment-21218" class="comment"><div id="post-21218-score" class="comment-score"></div><div class="comment-text"><p>Including one or more captures that contain the values in question with the patch would also be very helpful.</p></div><div id="comment-21218-info" class="comment-info"><span class="comment-age">(17 May '13, 04:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-21185" class="comment-tools"></div><div class="clear"></div><div id="comment-21185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

