+++
type = "question"
title = "Diameter - dictionary.xml - is it possible to define a list of values for a proprietary AVP of type Unsigned16?"
description = '''From a Telco vendor I have some proprietary Diameter AVPs of type Unsigned16, with associated a list of possible values. When I try to define a list of possible values for this AVP in &quot;dictionary.xml&quot; in the following way I get the following error: &quot;Diameter Dictionary: AVP &#x27;CS-test&#x27; has a list of v...'''
date = "2017-08-10T03:45:00Z"
lastmod = "2017-08-18T05:59:00Z"
weight = 63461
keywords = [ "diameter", "list", "unsigned16", "dictionary" ]
aliases = [ "/questions/63461" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Diameter - dictionary.xml - is it possible to define a list of values for a proprietary AVP of type Unsigned16?](/questions/63461/diameter-dictionaryxml-is-it-possible-to-define-a-list-of-values-for-a-proprietary-avp-of-type-unsigned16)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63461-score" class="post-score" title="current number of votes">0</div><span id="post-63461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From a Telco vendor I have some proprietary Diameter AVPs of type Unsigned16, with associated a list of possible values. When I try to define a list of possible values for this AVP in "dictionary.xml" in the following way I get the following error:</p><pre><code>&quot;Diameter Dictionary: AVP &#39;CS-test&#39; has a list of values but isn&#39;t of a 32-bit or shorter integral type (FT-BYTES)&quot;</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/Example_NTmcr7j.PNG" alt="alt text" /></p><p>Note that if I try instead to define this proprietary AVP as type Enumerated, I have then an error in the decoding, as the the lenght of the AVP is 16 and not 32 as it is required by the type enumerated.</p><p>Do you know if there's a working syntax for Diameter to use in dictionary.xml to define a list of possible values for a type Unsigned16 AVP?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span> <span class="post-tag tag-link-unsigned16" rel="tag" title="see questions tagged &#39;unsigned16&#39;">unsigned16</span> <span class="post-tag tag-link-dictionary" rel="tag" title="see questions tagged &#39;dictionary&#39;">dictionary</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '17, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/b7f19633649e1cb3db81260497b64a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rpiccinini&#39;s gravatar image" /><p><span>rpiccinini</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rpiccinini has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63461" class="comments-container"></div><div id="comment-tools-63461" class="comment-tools"></div><div class="clear"></div><div id="comment-63461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63462"></span>

<div id="answer-container-63462" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63462-score" class="post-score" title="current number of votes">1</div><span id="post-63462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have zero knowledge of diameter, but looking at the dissector <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-diameter.c;h=da8901e5764e3e9f902108f0e35b113227a030a8;hb=HEAD">source code</a>, unsigned16 is not a supported type, only 32 and 64.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '17, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63462" class="comments-container"><span id="63463"></span><div id="comment-63463" class="comment"><div id="post-63463-score" class="comment-score"></div><div class="comment-text"><p>Actually if I do not try to define a list, the type Unsigned16 is correctly supported by dictionary.xml and all the proprietary AVPs are correctly decoded. But clearly without the list it is just shown the raw value.</p></div><div id="comment-63463-info" class="comment-info"><span class="comment-age">(10 Aug '17, 04:17)</span> <span class="comment-user userinfo">rpiccinini</span></div></div></div><div id="comment-tools-63462" class="comment-tools"></div><div class="clear"></div><div id="comment-63462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63473"></span>

<div id="answer-container-63473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63473-score" class="post-score" title="current number of votes">0</div><span id="post-63473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Actually if I do not try to define a list, the type Unsigned16 is correctly supported by dictionary.xml and all the proprietary AVPs are correctly decoded.</p></blockquote><p>There's nothing in the Wireshark Diameter dissector, Diameter dictionary reading code, or Diameter dictionary files that supports Unsigned16. Unknown types are treated as OctetString, so Wireshark only shows the raw octets of the value; it doesn't show it as a 16-bit big-endian integral value.</p><p>Neither <a href="https://tools.ietf.org/html/rfc3588">RFC 3588</a> nor <a href="https://tools.ietf.org/html/rfc6733">RFC 6733</a> list Unsigned16 as a "Basic AVP Data Format" - or as a "Derived AVP Data Format". Section 1.3.2 "Creating New AVPs" of RFC 6733 says</p><blockquote><p>A new AVP being defined MUST use one of the data types listed in Sections 4.2 or 4.3.</p></blockquote><p>However, <a href="https://tools.ietf.org/html/rfc6735">RFC 6735</a> repeatedly refers to an AVP data format "Unsigned16".</p><p>Any AVP data format Wireshark doesn't explicitly recognize is treated as OctetString, and the Internet-Draft <a href="https://tools.ietf.org/html/draft-frascone-xml-dictionary-00">draft-frascone-xml-dictionary-00</a>, "Diameter XML Dictionary", which is the specification for the XML format for a Diameter dictionary, says:</p><blockquote><p>The enum element defines a name to value mapping for use in encoding and decoding AVPs of type Unsigned32.</p></blockquote><p>with no mention of any other types - neither Unsigned16 nor OctetString.</p><p>So you can't currently use an enum element for your AVP with Wireshark.</p><p>We could add "Unsigned16" as a (quasi-)Basic AVP Data Format, and allow AVPs with that format to have an enum element. Given that at least one AVP mentioned in an RFC uses it, that <em>might</em> be a reasonable thing to do, although, on the other hand, a draft(?) of 3GPP TS 32.299 used Unsigned16 for SIP-Request-Timestamp-Fraction and SIP-Response-Timestamp-Fraction AVPs, but Alcatel-Lucent made a change request to make it Unsigned32 because Unsigned16 was "Not Diameter Compliant" as it was "not defined in RFC 3588 as diameter base format", and, in fact, the change was made.</p><p>So is the AVP length for that AVP 14? (I'm assuming from the presence of a vendor-id that the V flag is set and the Vendor-ID is present in the AVP.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '17, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-63473" class="comments-container"><span id="63483"></span><div id="comment-63483" class="comment"><div id="post-63483-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/79/guy-harris"></a><a href="https://ask.wireshark.org/users/79/guy-harris">@Guy Harris</a>,</p><blockquote>so is the AVP length for that AVP 14? (I'm assuming from the presence of a vendor-id that the V flag is set and the Vendor-ID is present in the AVP.)</blockquote><p>That's correct, the AVP length is 14. Also your other assumptions are correct. Below an example of how one of this AVPs is decoded using the Unsigned16 type in dictionary.xml. Clearly only the raw value is shown, as it is not possible to define a list.</p><p>Beside this specific AVP there are also some others from the same proprietary specification (references 3GPP TS 32.299, v8.4.0 and IETF RFC 4006) that are using an Unsigned16 type.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Example_Unsigned16.PNG" width="640" /></p></div><div id="comment-63483-info" class="comment-info"><span class="comment-age">(18 Aug '17, 03:33)</span> <span class="comment-user userinfo">rpiccinini</span></div></div><span id="63485"></span><div id="comment-63485" class="comment"><div id="post-63485-score" class="comment-score"></div><div class="comment-text"><p>Unsigned16 is derived from OctetString AVP base format. It holds 16 bit unsigned value, in network byte order. According to the 32-bit boundary alignment rules of RFC 3588 for values of type OctetString, the AVP value will be followed by 2 zero-valued bytes of padding to ensure that the next AVP will start in a 32-bit boundary.</p></div><div id="comment-63485-info" class="comment-info"><span class="comment-age">(18 Aug '17, 05:59)</span> <span class="comment-user userinfo">rpiccinini</span></div></div></div><div id="comment-tools-63473" class="comment-tools"></div><div class="clear"></div><div id="comment-63473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

