+++
type = "question"
title = "Wireshark 2.0.1 diameter dictionary.xml"
description = '''I have Wireshark 2.0.1 64bit installed on a Windows 10 system (I know Windows 10?); when I attempt to update the diameter dictionary.xml file I get a list of errors. Any assistance would be appreciated. Examples: (And many, many more) Diameter Dictionary: AVP &#x27;CHAP-Algorithm&#x27; has a list of values bu...'''
date = "2016-01-11T09:03:00Z"
lastmod = "2016-01-22T18:50:00Z"
weight = 49096
keywords = [ "diameter", "dictionary" ]
aliases = [ "/questions/49096" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2.0.1 diameter dictionary.xml](/questions/49096/wireshark-201-diameter-dictionaryxml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49096-score" class="post-score" title="current number of votes">0</div><span id="post-49096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark 2.0.1 64bit installed on a Windows 10 system (I know Windows 10?); when I attempt to update the diameter dictionary.xml file I get a list of errors. Any assistance would be appreciated.</p><p>Examples: (And many, many more)</p><p>Diameter Dictionary: AVP 'CHAP-Algorithm' has a list of values but isn't of a 32-bit or shorter integral type (FT_BYTES)</p><p>Diameter Dictionary: AVP 'Accounting-Auth-Method' has a list of values but isn't of a 32-bit or shorter integral type (FT_BYTES)</p><p>Diameter Dictionary: AVP 'Origin-AAA-Protocol' has a list of values but isn't of a 32-bit or shorter integral type (FT_BYTES)</p><p>Diameter Dictionary: AVP 'MIP-Feature-Vector' has a list of values but isn't of a 32-bit or shorter integral type (FT_BYTES)</p><p>Diameter Dictionary: AVP 'MIP-Algorithm-Type' has a list of values but isn't of a 32-bit or shorter integral type (FT_BYTES)</p><p>Diameter Dictionary: AVP 'MIP-Replay-Mode' has a list of values but isn't of a 32-bit or shorter integral type (FT_BYTES)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-dictionary" rel="tag" title="see questions tagged &#39;dictionary&#39;">dictionary</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '16, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/ee772c86d70ee55a85c77cbf465fe042?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kh00le&#39;s gravatar image" /><p><span>kh00le</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kh00le has no accepted answers">0%</span></p></div></div><div id="comments-container-49096" class="comments-container"><span id="49097"></span><div id="comment-49097" class="comment"><div id="post-49097-score" class="comment-score"></div><div class="comment-text"><p>What is the "update" you're attempting to apply to dictionary.xml?</p></div><div id="comment-49097-info" class="comment-info"><span class="comment-age">(11 Jan '16, 09:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49183"></span><div id="comment-49183" class="comment"><div id="post-49183-score" class="comment-score"></div><div class="comment-text"><p>Thank you for taking the time to look at this question.</p><p>I am attempting to add additional AVP for Wireshark to decode. I was able to do this in the pervious versions. I did check the xml formatting and it checked fine.</p></div><div id="comment-49183-info" class="comment-info"><span class="comment-age">(13 Jan '16, 11:11)</span> <span class="comment-user userinfo">kh00le</span></div></div><span id="49186"></span><div id="comment-49186" class="comment"><div id="post-49186-score" class="comment-score"></div><div class="comment-text"><p>Can you give a specific example of what you're trying to add?</p><p>Note that the format of the XML has changed significantly in 2.0. In particular vendor IDs can no longer be inside applications (and applications must be in either base or a vendor). I don't think that's your problem but I just wanted to make sure you were aware...</p></div><div id="comment-49186-info" class="comment-info"><span class="comment-age">(13 Jan '16, 11:56)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-49096" class="comment-tools"></div><div class="clear"></div><div id="comment-49096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49473"></span>

<div id="answer-container-49473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49473-score" class="post-score" title="current number of votes">0</div><span id="post-49473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, so a quick check in the code suggests that the problem is the AVP you have added is listed as being of type OctetString (or grouped) but then it includes some 'enum' statements. If there are 'enum' statements, of course, the type should be Enumerated.</p><p>So, for example, I was able to get the same error by modifying this AVP to be of type OctetString (instead of Enumerated):</p><pre><code>&lt;avp name=&quot;SL-Request-Type&quot; code=&quot;2904&quot; mandatory=&quot;must&quot; vendor-bit=&quot;must&quot; vendor-id=&quot;TGPP&quot;&gt;
   &lt;type type-name=&quot;OctetString&quot;/&gt;
   &lt;enum name=&quot;INITIAL_REQUEST&quot;            code=&quot;0&quot;/&gt;
   &lt;enum name=&quot;INTERMEDIATE_REQUEST&quot;       code=&quot;1&quot;/&gt;
&lt;/avp&gt;</code></pre><p>(Hopefully this works; the Preview doesn't show the AVP definition...)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '16, 18:50</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-49473" class="comments-container"></div><div id="comment-tools-49473" class="comment-tools"></div><div class="clear"></div><div id="comment-49473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

